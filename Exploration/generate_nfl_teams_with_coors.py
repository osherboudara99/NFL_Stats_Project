import pandas as pd

# NFL teams, cities, abbreviations, and coordinates
data = {
    "team_full_name": [
        "Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills",
        "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns",
        "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers",
        "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs",
        "Las Vegas Raiders", "Los Angeles Chargers", "Los Angeles Rams", "Miami Dolphins",
        "Minnesota Vikings", "New England Patriots", "New Orleans Saints", "New York Giants",
        "New York Jets", "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers",
        "Seattle Seahawks", "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Commanders"
    ],
    "city": [
        "Glendale, AZ", "Atlanta, GA", "Baltimore, MD", "Orchard Park, NY",
        "Charlotte, NC", "Chicago, IL", "Cincinnati, OH", "Cleveland, OH",
        "Arlington, TX", "Denver, CO", "Detroit, MI", "Green Bay, WI",
        "Houston, TX", "Indianapolis, IN", "Jacksonville, FL", "Kansas City, MO",
        "Paradise, NV", "Inglewood, CA", "Inglewood, CA", "Miami Gardens, FL",
        "Minneapolis, MN", "Foxborough, MA", "New Orleans, LA", "East Rutherford, NJ",
        "East Rutherford, NJ", "Philadelphia, PA", "Pittsburgh, PA", "Santa Clara, CA",
        "Seattle, WA", "Tampa, FL", "Nashville, TN", "Landover, MD"
    ],
    "team_abbrev": [
        "ARI", "ATL", "BAL", "BUF", "CAR", "CHI", "CIN", "CLE", "DAL", "DEN", "DET", "GB",
        "HOU", "IND", "JAX", "KC", "LV", "LAC", "LAR", "MIA", "MIN", "NE", "NO", "NYG",
        "NYJ", "PHI", "PIT", "SF", "SEA", "TB", "TEN", "WAS"
    ],
    "lat": [
        33.5270, 33.7550, 39.2904, 42.7738, 35.2271, 41.8623, 39.0957, 41.4993,
        32.7512, 39.7392, 42.3314, 44.5133, 29.7604, 39.7684, 30.3322, 39.0997,
        36.0940, 33.9581, 33.9581, 25.9580, 44.9778, 42.0654, 29.9511, 40.8136,
        40.8136, 39.9526, 40.4406, 37.4043, 47.6062, 27.9506, 36.1627, 38.9076
    ],
    "lon": [
        -112.2626, -84.3900, -76.6122, -78.7866, -80.8431, -87.6167, -84.5120, -81.6944,
        -97.0918, -104.9903, -83.0458, -88.0158, -95.3698, -86.1581, -81.6557, -94.5786,
        -115.1537, -118.3411, -118.3414, -80.2382, -93.2650, -71.2482, -90.0715, -74.0742,
        -74.0738, -75.1652, -79.9959, -121.9714, -122.3321, -82.4572, -86.7816, -76.8642
    ]
}

# Creating the dataframe
nfl_df = pd.DataFrame(data)

# Saving to a CSV file
file_path = "NFL_Teams_Coordinates.csv"
nfl_df.to_csv(file_path, index=False)