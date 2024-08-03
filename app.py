import os
import re
from discord.ext import commands
from discord import app_commands
from discord import Intents, Interaction
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

@bot.tree.command(name='kongify')
async def kongify(interaction: Interaction, message: str):
    modified_message = re.sub(r'con', 'kong', message, flags=re.IGNORECASE)
    await interaction.response.send_message(modified_message)

bot.run(DISCORD_BOT_TOKEN)
