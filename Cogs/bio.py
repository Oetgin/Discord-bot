# This program is the bio command for my discord bot, MARX
# Copyright (C) 2021  Oetgin

from discord.ext import commands


class BioCog(commands.Cog, name="bio command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "bio",
					usage="",
					description = "Give a short biography of Karl Marx.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def bio(self, ctx):
		message = await ctx.send("Karl Marx, né le 5 mai 1818 à Trèves dans le grand-duché du Bas-Rhin et mort le 14 mars 1883 à Londres,\
 est un philosophe, historien, sociologue, économiste, journaliste, théoricien de la révolution, socialiste et communiste prussien.\
 Il est connu pour sa conception matérialiste de l'histoire, son analyse des rouages du capitalisme et de la lutte des classes,\
 et pour son activité révolutionnaire au sein du mouvement ouvrier.\
 Il a notamment été un des membres dirigeants de l'Association internationale des travailleurs (Première Internationale).\
 Des courants de pensée se revendiquant principalement des travaux de Marx sont désignés sous le nom de marxisme.\
 Marx a eu une grande influence sur le développement ultérieur des sciences humaines et sociales.\
 Ses travaux ont marqué de façon considérable le xxe siècle,\
 au cours duquel de nombreux mouvements révolutionnaires et intellectuels se sont réclamés de sa pensée. (Source : https://fr.wikipedia.org/wiki/Karl_Marx)")

def setup(bot:commands.Bot):
	bot.add_cog(BioCog(bot))