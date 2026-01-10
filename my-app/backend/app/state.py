from data import team as team_data
from aggregations import team as team_agg

def init_state(app):
    app.state.teams = team_data.get_team_data()
    app.state.schedules = team_data.get_schedules_data()
    app.state.win_loss_by_game = team_agg.win_loss_by_game(app.state.schedules)