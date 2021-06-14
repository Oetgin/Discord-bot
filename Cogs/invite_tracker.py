# This program is the invite_tracker command for my discord bot, MARX
# Copyright (C) 2021  Oetgin

from discord.ext import commands
import json


class InviteTrackerCog(commands.Cog, name="invite_tracker command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "invite_tracker",
					usage="",
					description = "Show how many people someone invited.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def invite_tracker(self, ctx, user = None):
		with open("Cogs/commands_config.json", "r") as config:
			data = json.load(config)
			quote_config = data["invite_tracker"]
			if quote_config[0] == "0":	
				DeleteMessage = False
			else:
				DeleteMessage = True
		if user == None:
			totalInvites = 0
			for i in await ctx.guild.invites():
				if i.inviter == ctx.author:
					totalInvites += i.uses
			await ctx.send(f"You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")
		# Part not working
		else:
			totalInvites = 0
			for i in await ctx.guild.invites():
				member = ctx.message.guild.get_member_named(user)
				if i.inviter == member:
					totalInvites += i.uses
			if member == None:
				await ctx.send("Invalid user, please make sure the member is not a bot and is in the server")
			else:
				await ctx.send(f"{member} has invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")
		if DeleteMessage:
			await ctx.message.delete()
		print(f"{ctx.author} used the invite_tracker command")

def setup(bot:commands.Bot):
	bot.add_cog(InviteTrackerCog(bot))