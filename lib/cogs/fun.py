from random import choice, randint
from typing import Optinal

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import commands

class Fun(Cog):
	def __init__(self, bot):
		self.bot = bot
	#new
	@command(name="hello", aliases=["hi"])
	async def say_hello(self, ctx):
		await ctx.send(f"{choice(('Hello', 'Hi', 'Hey', 'Hiya'))} {ctx.author.mention}!")


	@command(name="dice", aliases=["roll"])
	async def rool_dice(self, ctx, die_string: str):
		dice, value = (int(term) for term in die_string.split("d"))
		rolls = [randit(1, value) for i in range(dice)]

		await ctx.send(" + ".join([str(r) for r in rolls]) + f" = {sum(rolls)}")

	@command(name="slap", aliases=["hit"])
	async def slap_member(self, ctx, member: Member, *, reason: Optional[str] = "no reason"):
		await ctx.send(f"{ctx.author.nick} slapped {member.mention} for {reason}!")

	
	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("fun")


def setup(bot):
	bot.add_cog(Fun(bot))
