from fastapi import FastAPI
import nfl_data_py as nfl
from pydantic import BaseModel
from typing import List
from state import init_state
from models import Team_Records
from aggregations import team as team_agg

app = FastAPI(title="NFL Analytics API", version="1.0.0")

@app.on_event("startup")
async def start_up():
    init_state(app)


@app.get("/team/records/{season}", response_model=List[Team_Records])
def root(season: int):
    teams = [team for team in app.state.win_loss_by_game if team['season'] == season]
    response = team_agg.win_loss_by_season(teams)
    return response