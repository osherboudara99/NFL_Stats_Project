from fastapi import FastAPI
import nfl_data_py as nfl
from pydantic import BaseModel
from typing import List
from state import init_state

app = FastAPI(title="NFL Analytics API", version="1.0.0")

@app.on_event("startup")
async def start_up():
    init_state(app)