import unicodedata
from LionAPI.services.database import create_connection
import requests
import pandas as pd
from mysql.connector import Error

def get_shots(home_team, away_team, match_date):
    """
    Fetches shot data for a soccer match from the SofaScore API.

    Parameters:
        home_team (str): Name of the home team.
        away_team (str): Name of the away team.
        match_date (str): Date of the match in 'YYYY-MM-DD' format.

    Returns:
        pd.DataFrame: DataFrame containing shot data, or None if there was an error.
    """
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor(dictionary=True)
        try:

            query = """
                SELECT event_id
                FROM events
                WHERE home_team = %s AND away_team = %s AND event_date = %s;
            """
            cursor.execute(query, (home_team, away_team, match_date))
            result = cursor.fetchone()

            if result is None:
                print("No game found for the given parameters.")
                return None
            
            event_id = result['event_id']
            url = f"https://sofascore.com/api/v1/event/{event_id}/shotmap"

            try:
                response = requests.get(url)
                response.raise_for_status()  

                shots = response.json()
                if 'shotmap' not in shots:
                    print("Invalid response structure.")
                    return None

                df = pd.json_normalize(shots['shotmap'])
                df = df[df['situation'] != 'shootout']

                selected_columns = [
                    'isHome', 'shotType', 'situation', 'bodyPart', 'goalMouthLocation',
                    'xg', 'id', 'time', 'addedTime', 'timeSeconds', 'reversedPeriodTime',
                    'reversedPeriodTimeSeconds', 'incidentType', 'player.name', 'player.position', 
                    'player.jerseyNumber', 'player.id', 'playerCoordinates.x', 'playerCoordinates.y', 
                    'playerCoordinates.z', 'goalMouthCoordinates.x', 'goalMouthCoordinates.y', 
                    'draw.start.x', 'draw.start.y', 'draw.end.x', 'draw.end.y', 'draw.goal.x', 'draw.goal.y', 
                    'goalType', 'xgot'
                ]

                result_df = df[selected_columns]

                result_df['team'] = result_df['isHome'].apply(lambda is_home: home_team if is_home else away_team)

                result_df = result_df.drop(columns=['home_team', 'away_team'], errors='ignore')

                return result_df

            except requests.exceptions.RequestException as e:
                print(f"Request error: {e}")
                return None

        except Error as e:
            print(f"Error querying data: {e}")
            return None

        finally:
            cursor.close()
            connection.close()
    else:
        print("Failed to create the database connection.")
        return None
    
