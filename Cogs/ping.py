# This program is the ping command for my discord bot, MARX
# Copyright (C) 2021  Oetgin

from discord.ext import commands
import time
import json


class PingCog(commands.Cog, name="ping command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "ping",
					usage="",
					description = "Display the bot's ping.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def ping(self, ctx):
		with open("Cogs/commands_config.json", "r") as config:
			data = json.load(config)
			quote_config = data["ping"]
			if quote_config[0] == "0":
				DeleteMessage = False
			else:
				DeleteMessage = True
		before = time.monotonic()
		message = await ctx.send("🏓 Pong !")
		ping = (time.monotonic() - before) * 1000
		await message.edit(content=f"🏓 Pong !  `{int(ping)} ms`")
		if DeleteMessage:
			await ctx.message.delete()
		print(f"{ctx.author} used the ping command (ping : {int(ping)} ms)")

def setup(bot:commands.Bot):
	bot.add_cog(PingCog(bot))