# This program is the bio command for my discord bot, MARX
# Copyright (C) 2021  Oetgin

from discord.ext import commands
import json


class BioCog(commands.Cog, name="bio command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "bio",
					usage="",
					description = "Give a short biography of Karl Marx.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def bio(self, ctx):
		with open("Cogs/commands_config.json", "r") as config:
			data = json.load(config)
			quote_config = data["bio"]
			if quote_config[0] == "0":	
				DeleteMessage = False
			else:
				DeleteMessage = True
		message = await ctx.send("**Karl Heinrich Marx** (5 May 1818 – 14 March 1883) was a German philosopher, economist, historian, sociologist, political theorist,\
 journalist and socialist revolutionary. Born in Trier, Germany, Marx studied law and philosophy at university. He married Jenny von Westphalen in 1843.\
 Due to his political publications, Marx became stateless and lived in exile with his wife and children in London for decades,\
 where he continued to develop his thought in collaboration with German thinker Friedrich Engels and publish his writings, researching in the British Museum Reading Room.\
 His best-known titles are the 1848 pamphlet The Communist Manifesto and the three-volume Das Kapital (1867–1883).\
 Marx's political and philosophical thought had enormous influence on subsequent intellectual, economic and political history.\
 His name has been used as an adjective, a noun, and a school of social theory. (Source : https://en.wikipedia.org/wiki/Karl_Marx)")
		if DeleteMessage:
			await ctx.message.delete()
		print(f"{ctx.author} used the bio command")

def setup(bot:commands.Bot):
	bot.add_cog(BioCog(bot))