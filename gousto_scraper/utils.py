from gousto_scraper.constants import GET_RECIPES_PAGE_LIMIT

def page_to_offset(page: int) -> int:
    return page * GET_RECIPES_PAGE_LIMIT
