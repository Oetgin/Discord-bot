# This program is the status command for my discord bot, MARX
# Copyright (C) 2021  Oetgin

from discord.ext import commands
import json


class StatusCog(commands.Cog, name="status command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "status",
					usage="",
					description = "Show bot status.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def status(self, ctx):
		with open("Cogs/commands_config.json", "r") as config:
			data = json.load(config)
			quote_config = data["status"]
			if quote_config[0] == "0":	
				DeleteMessage = False
			else:
				DeleteMessage = True
		message = await ctx.send("The bot is currently in developpment. Many commands are not finished. Commands in developpment : ban - unban - invite_tracker.")
		if DeleteMessage:
			await ctx.message.delete()

def setup(bot:commands.Bot):
	bot.add_cog(StatusCog(bot))