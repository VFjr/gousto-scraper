from gousto_scraper.constants import GET_RECIPES_PAGE_LIMIT

def page_to_offset(page: int) -> int:
    return page * GET_RECIPES_PAGE_LIMIT

def convert_recipes_to_recipe_in_url(url: str) -> str:
    """
    Converts the prefix "/recipes/" returned by API to "/recipe/" due to inconsistency in Gousto API
    """
    if not url.startswith("/recipes/"):
        raise ValueError("url must start with /recipes/")
    return url.replace("/recipes/", "/recipe/")
