import json
import os
import asyncio
import gousto_scraper
    
FILE_PATH = os.path.join(os.path.dirname(__file__), 'recipe_urls.json')

async def main():
    recipe_urls = await gousto_scraper.get_all_recipes(max_concurrent_requests=20)
    # Convert RecipeLink objects to dictionaries
    recipe_dicts = [recipe.to_dict() for recipe in recipe_urls]
    with open(FILE_PATH, 'w') as f:
        json.dump(recipe_dicts, f)
    print(f'Successfully saved {len(recipe_urls)} recipes to {FILE_PATH}')

if __name__ == '__main__':
    asyncio.run(main())
