import pydantic
from typing import List

class Team_Records(pydantic.BaseModel):
    team: str
    season: int
    win: int
    loss: int
    tie: int
    points_for: int
    points_against: int

