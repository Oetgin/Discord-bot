# This program is the main program for my discord bot, MARX
# Copyright (C) 2021  Oetgin

print("main.py  Copyright (C) 2021  Oetgin")

import discord
from discord.ext import commands
import json
import os


# Get configuration.json
with open("configuration.json", "r") as config: 
	data = json.load(config)
	token = data["token"]
	prefix = data["prefix"]


class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

# Intents
intents = discord.Intents.default()
# The bot
bot = commands.Bot(prefix, intents = intents)


# Get the absolute path of a file
def getabsolute(file):
	script_dir = os.path.dirname(__file__) # <-- absolute dir the script is in
	rel_path = file
	abs_file_path = os.path.join(script_dir, rel_path)
	return abs_file_path

# Load cogs
if __name__ == '__main__':
	for filename in os.listdir(getabsolute("Cogs")):
		if filename.endswith(".py"):
			bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
	print(f"We have logged in as {bot.user}")
	print("Discord version : " + discord.__version__)
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help"))

bot.run(token)