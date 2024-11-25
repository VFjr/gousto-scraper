import gousto_scraper
import asyncio

async def main():
    #recipe_links = await gousto_scraper.get_all_recipes(max_concurrent_requests=20)
    #recipe_links = await gousto_scraper.get_recipe_links_from_page(180)
    #print(recipe_links)
    recipe_info = await gousto_scraper.get_recipe_info("/recipes/copy-of-homemade-chicken-goujons-cheesy-beans")
    print(recipe_info)

asyncio.run(main())

