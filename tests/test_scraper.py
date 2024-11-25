import pytest
import gousto_scraper
import asyncio

@pytest.mark.asyncio
async def test_get_recipe_links_from_page():
    recipe_links = await gousto_scraper.get_recipe_links_from_page(0)
    assert isinstance(recipe_links, list)
    assert len(recipe_links) == gousto_scraper.constants.GET_RECIPES_PAGE_LIMIT
    assert all(isinstance(link, gousto_scraper.types.RecipeLink) for link in recipe_links)

    recipe_links = await gousto_scraper.get_recipe_links_from_page(20)
    assert isinstance(recipe_links, list)
    assert len(recipe_links) == gousto_scraper.constants.GET_RECIPES_PAGE_LIMIT
    assert all(isinstance(link, gousto_scraper.types.RecipeLink) for link in recipe_links)

@pytest.mark.asyncio
async def test_no_more_recipes():
    with pytest.raises(gousto_scraper.errors.NoMoreRecipesError):
        await gousto_scraper.get_recipe_links_from_page(10000)
