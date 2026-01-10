import pandas as pd

def win_loss_by_game(schedules):
    win_loss_by_game_data = []
    
    for key in schedules:
        game = schedules[key]
        away_team = game['away_team']
        home_team = game['home_team']
        away_score = game['away_score']
        home_score = game['home_score']
        season = game['season']


        
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
            win_loss_by_game.append(win_row)
            win_loss_by_game.append(loss_row)
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
            win_loss_by_game.append(win_row)
            win_loss_by_game.append(loss_row)
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
            win_loss_by_game.append(first_tie_row)
            win_loss_by_game.append(second_tie_row)
    return win_loss_by_game.to_dict(orient="records")


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



        


    