from app.api import team_data

def init_state(app):
    app.state.teams = team_data.get_team_data()
    app.state.schedules = team_data.get_schedules_data()