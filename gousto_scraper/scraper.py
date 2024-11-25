from gousto_scraper.types import RecipeLink, RecipeInfo
from gousto_scraper.constants import GET_RECIPES_ENDPOINT, GET_RECIPES_PAGE_LIMIT, IMAGE_WIDTH
from gousto_scraper.errors import NoMoreRecipesError
from gousto_scraper.utils import page_to_offset
import aiohttp
import asyncio
import json
import logging

async def get_recipe_links_from_page(page: int) -> list[RecipeLink]:
    """
    Takes a page number and returns a list of recipe links

    Raises:
        aiohttp.ClientResponseError: If the response status code is not 200.
        NoMoreRecipesError: If there are no more recipes to scrape.
    """
    logging.debug(f"Scraping page {page}")

    offset = page_to_offset(page)
    
    api_url = f"{GET_RECIPES_ENDPOINT}&limit={GET_RECIPES_PAGE_LIMIT}&offset={offset}"
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status != 200:
                raise aiohttp.ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message=f"HTTP error occurred: {response.status}"
                )
            
            data = await response.json()
            entries = data["data"]["entries"]
            recipe_list = []

            # check if there are any more recipes to scrape
            if len(entries) == 0:
                raise NoMoreRecipesError

            for entry in entries:
                # Get the image with the correct width
                image_url = None
                images = entry["media"]["images"]
                for image in images:
                    if image["width"] == IMAGE_WIDTH:
                        image_url = image["image"]
                        break

                if image_url is None:
                    logging.error(f"No image found for {entry['title']} (url: {entry['url']}) with width {IMAGE_WIDTH}. Skipping recipe as this is likely a broken recipe")
                    continue
                recipe_link = RecipeLink(
                    name=entry["title"],
                    url=entry["url"],
                    prep_time=entry["prep_times"]["for_2"],
                    image_url=image_url
                )
                recipe_list.append(recipe_link)
            
            return recipe_list

async def get_all_recipes(max_concurrent_requests=5):
    page = 0
    all_recipes = []

    while True:
        try:
            # Create a set of tasks, respecting the max concurrency limit
            tasks = [
                get_recipe_links_from_page(page + i)
                for i in range(max_concurrent_requests)
            ]

            # Execute tasks concurrently
            results = await asyncio.gather(*tasks, return_exceptions=True)

            page_completed = False
            for result in results:
                if isinstance(result, NoMoreRecipesError):
                    # Stop further processing if we encounter a `NoMoreRecipesError`
                    page_completed = True
                    continue
                elif isinstance(result, Exception):
                    # Handle other exceptions if necessary
                    print(f"Error occurs: {result}")
                else:
                    all_recipes.extend(result)

            if page_completed:
                break

            page += max_concurrent_requests
        except NoMoreRecipesError:
            break

    return all_recipes