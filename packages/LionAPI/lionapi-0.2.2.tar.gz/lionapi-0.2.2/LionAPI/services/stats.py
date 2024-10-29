from LionAPI.services.database import create_connection
from mysql.connector import Error
import pandas as pd
import requests
import re
from typing import Union
import warnings
import datetime

def get_stats(home_team, away_team, match_date):
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
            url = f"https://sofascore.com/api/v1/event/{event_id}/statistics"

            try:
                response = requests.get(url)
                response.raise_for_status()  
                
                match_data = response.json().get('statistics')[0].get('groups')
                match_overview = next((group for group in match_data if group.get('groupName') == "Match overview"), None)

                if match_overview is None:
                    print("No stats found in 'Match overview'.")
                    return None
                
                statistics_items = match_overview.get('statisticsItems')
                df = pd.DataFrame(statistics_items)

                return df
            
            except requests.exceptions.RequestException as e:
                print(f"Request error: {e}")
                return None
            
        except Error as e:
            print(f"Database query error: {e}")
            return None
        
        finally:
            cursor.close()
            connection.close()
    else:
        print("Failed to create database connection")
        return None
    

def load_standings(tournament_name, season_year):
    start_date = datetime.date(season_year, 8, 15)  # Mid-August
    end_date = datetime.date(season_year + 1, 5, 31)  # End of May next year
    
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor(dictionary=True)
        try:
            query = """
            SELECT tournament_id, season_id
            FROM events
            WHERE tournament_name = %s AND event_date BETWEEN %s AND %s
            LIMIT 1;
            """
            cursor.execute(query, (tournament_name, start_date, end_date))
            result = cursor.fetchone()

            if result is None:
                print("Invalid tournament name or season input")
                return None
            
            League = result['tournament_id']
            season_id = result['season_id']
            url = f"https://www.sofascore.com/api/v1/unique-tournament/{League}/season/{season_id}/standings/total"

            try:
                response = requests.get(url)
                response.raise_for_status()

                data = response.json()
                rows = [
                    {
                        'team': team['team']['name'],
                        'position': team['position'],
                        'matches': team['matches'],
                        'wins': team['wins'],
                        'scoresFor': team['scoresFor'],
                        'scoresAgainst': team['scoresAgainst'],
                        'id': team['id'],
                        'losses': team['losses'],
                        'draws': team['draws'],
                        'points': team['points'],
                        'scoreDiffFormatted': team['scoreDiffFormatted']
                    }
                    for standing in data['standings']
                    for team in standing['rows']
                ]
                df = pd.DataFrame(rows)
                return df
            
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

