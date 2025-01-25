import discord
from discord import app_commands
from discord.ui import Button, View
from discord.utils import get
from discord.ext import commands
from dotenv import load_dotenv, dotenv_values
from os import getenv

load_dotenv()


intents = discord.Intents.default()


client = discord.Client(intents=intents)


guilds_id = getenv("GUILD_ID")

tree = app_commands.CommandTree(client=client)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    try:
        synced = await tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


    

def get_guild()-> discord.Guild:
    client.get_guild(guilds_id)


    


client.run(getenv("TOKEN"))


    


