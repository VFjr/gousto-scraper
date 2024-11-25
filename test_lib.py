import gousto_scraper
import asyncio

async def main():
    recipe_links = await gousto_scraper.get_all_recipes(max_concurrent_requests=20)
    #recipe_links = await gousto_scraper.get_recipe_links_from_page(180)
    #print(recipe_links)

asyncio.run(main())

