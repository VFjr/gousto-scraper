from dataclasses import dataclass, asdict

@dataclass
class RecipeLink:
    name: str
    url: str
    prep_time: int
    image_url: str

    def to_dict(self):
        return asdict(self)

@dataclass
class RecipeInfo:
    ingredients: list[str]

    def to_dict(self):
        return asdict(self)