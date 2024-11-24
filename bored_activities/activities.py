import requests
import discord

API_URL = 'http://panel2.mcboss.top:25569/bored'

def fetch_bored_activity():
    """
    Fetches a random activity from the API.

    Returns:
        str: A random activity or an error message.
    """
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            return data.get('activity', 'No activity found.')
        else:
            return "Sorry, I couldn't fetch an activity right now."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def create_activity_embed():
    """
    Creates a Discord embed with a random activity.

    Returns:
        discord.Embed: A Discord embed containing the activity.
    """
    activity = fetch_bored_activity()
    embed = discord.Embed(
        title="Feeling Bored? 🤔",
        description=activity,
        color=discord.Color.blue()
    )
    return embed
