import pandas as pd

def win_loss_by_game(schedules):
    """Compute per-game win/loss/tie rows from a list of schedule dicts.

    Expects `schedules` to be a list of dicts where each dict has keys:
    'away_team', 'home_team', 'away_score', 'home_score', 'season'.
    """
    win_loss_by_game_data = []

    for game in schedules:
        away_team = game['away_team']
        home_team = game['home_team']
        away_score = game['away_score']
        home_score = game['home_score']
        season = game['season']

        # Skip games without scores (e.g., future / unplayed games)
        if pd.isna(away_score) or pd.isna(home_score):
            continue

        if home_score > away_score:
            win_row = {
                'team': home_team,
                'opponent': away_team,
                'win': 1,
                'loss': 0,
                'tie': 0,
                'season': season,
                'points_for': home_score,
                'points_against': away_score,
            }
            loss_row = {
                'team': away_team,
                'opponent': home_team,
                'win': 0,
                'loss': 1,
                'tie': 0,
                'season': season,
                'points_for': away_score,
                'points_against': home_score,
            }
            win_loss_by_game_data.append(win_row)
            win_loss_by_game_data.append(loss_row)
        elif away_score > home_score:
            win_row = {
                'team': away_team,
                'opponent': home_team,
                'win': 1,
                'loss': 0,
                'tie': 0,
                'season': season,
                'points_for': away_score,
                'points_against': home_score,
            }
            loss_row = {
                'team': home_team,
                'opponent': away_team,
                'win': 0,
                'loss': 1,
                'tie': 0,
                'season': season,
                'points_for': home_score,
                'points_against': away_score,
            }
            win_loss_by_game_data.append(win_row)
            win_loss_by_game_data.append(loss_row)
        else:
            first_tie_row = {
                'team': away_team,
                'opponent': home_team,
                'win': 0,
                'loss': 0,
                'tie': 1,
                'season': season,
                'points_for': away_score,
                'points_against': home_score,
            }
            second_tie_row = {
                'team': home_team,
                'opponent': away_team,
                'win': 0,
                'loss': 0,
                'tie': 1,
                'season': season,
                'points_for': home_score,
                'points_against': away_score,
            }
            win_loss_by_game_data.append(first_tie_row)
            win_loss_by_game_data.append(second_tie_row)

    return win_loss_by_game_data


def win_loss_by_season(win_loss_by_game_data):
    df = pd.DataFrame(win_loss_by_game_data)
    agg_df = df.groupby(['team', 'season']).agg({
        'win': 'sum',
        'loss': 'sum',
        'tie': 'sum',
        'points_for': 'sum',
        'points_against': 'sum'
    }).reset_index()
    return agg_df.to_dict(orient="records")



        


    