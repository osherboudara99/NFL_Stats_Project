import nfl_data_py as nfl
import datetime as dt

def get_team_data():
    teams_df = nfl.import_team_desc()
    teams = teams_df.to_dict(orient="records")
    return teams

def get_schedules_data():
    schedules_df = nfl.import_schedules(range(1999, dt.datetime.now().year + 1))
    schedules = schedules_df.to_dict(orient="records")
    return schedules

