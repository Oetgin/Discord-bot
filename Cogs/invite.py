# This program is the invite command for my discord bot, MARX
# Copyright (C) 2021  Oetgin

from discord.ext import commands


class InviteCog(commands.Cog, name="invite command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "invite",
					usage="",
					description = "Create an invite link for the current server.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def invite(self, ctx):
        # Creating invite link
         invitelink = await ctx.channel.create_invite()
        # Dming it to the person 
         await ctx.send(invitelink)

def setup(bot:commands.Bot):
	bot.add_cog(InviteCog(bot))
