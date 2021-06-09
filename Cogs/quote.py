# This program is the quote command for my discord bot, MARX
# Copyright (C) 2021  Oetgin

from asyncio import DefaultEventLoopPolicy
from discord.ext import commands
from random import choice
import json


class QuoteCog(commands.Cog, name="quote command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "quote",
					usage="",
					description = "Give a random quote of Karl Marx.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def quote(self, ctx):
		with open("Cogs/commands_config.json", "r") as config:
			data = json.load(config)
			quote_config = data["quote"]
		if quote_config[0] == "0":
			DeleteMessage = False
		else:
			DeleteMessage = True
		IsQuote = False
		while not IsQuote:
			quote = choice(open("Cogs/quote_list.txt", encoding='utf-8').readlines())
			if quote[0] in "0123456789":
				IsQuote = True
		count = 0
		Done = False
		for a in quote:
			if a == "." and not Done:
				quote = quote[:(count+1)] + "__" + quote[(count+1):]
				Done = True
			count += 1
		quote = "__" + quote
		message = await ctx.send("> " + quote)
		if DeleteMessage:
			await ctx.message.delete()


def setup(bot:commands.Bot):
	bot.add_cog(QuoteCog(bot))