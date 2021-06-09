# This program is the invite command for my discord bot, MARX
# Copyright (C) 2021  Oetgin

from discord.ext import commands
import json


class InviteCog(commands.Cog, name="invite command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "invite",
					usage="",
					description = "Create an invite link for the current server.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def invite(self, ctx):
		with open("Cogs/commands_config.json", "r") as config:
			data = json.load(config)
			quote_config = data["invite"]
			if quote_config[0] == "0":
				DeleteMessage = False
			else:
				DeleteMessage = True
		# Creating invite link
		invitelink = await ctx.channel.create_invite()
		# Dming it to the person 
		await ctx.send("Do you want to invite comrades to your server ? Use this link : " + str(invitelink))
		if DeleteMessage:
			await ctx.message.delete()

def setup(bot:commands.Bot):
	bot.add_cog(InviteCog(bot))
