from dataclasses import dataclass

@dataclass
class RecipeLink:
    name: str
    url: str
    prep_time: int
    image_url: str

@dataclass
class RecipeInfo:
    ingredients: list[str]