import os
import subprocess
import discord
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
from discord.ext import commands


guild_id = your guild id here

# Create a Discord Intents object to enable certain events
intents = discord.Intents.default()

# Enable the events you need
intents.members = True
intents.guilds = True
intents.messages = True

# Create the bot with the intents parameter
#bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='/', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name='start', guild_ids=[guild_id],description="Starts the Valheim Server.")
async def start(ctx: SlashContext):
    # Change directory to the directory of the Python script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # Execute the command
    subprocess.call(['docker-compose', 'up', '-d'])


@slash.slash(name='stop', guild_ids=[guild_id],description="Stops the Valheim Server.")
async def stop(ctx: SlashContext):
    # Change directory to the directory of the Python script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # Execute the command
    subprocess.call(['docker-compose', 'down'])


@slash.slash(name='code', guild_ids=[guild_id],description="Gets the most recent join code.")
async def code(ctx: SlashContext):
    # Change directory to the directory of the Python script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # Execute the script
    subprocess.call(['python3', 'code.py'])


@slash.slash(name='status', guild_ids=[guild_id],description="Gets the server status boi.")
async def status(ctx: SlashContext):
    # Execute the script
    subprocess.call(['node', '/Users/krish/valheim-server/status.js'])



bot.run('your bot token here')

