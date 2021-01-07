from discord import Forbidden
from discord.ext.commands import Cog
from discord.ext.commands import command


class Welcome(Cog):
	def __init__(self, bot):
		self.bot = bot

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("welcome")

	@Cog.listener()
	async def on_member_join(self, member):
		db.execute("INSERT INTO exp(UserID) VALUES (?)", member.id)
		await self.bot.get_channel(789501683624706080).send(f"Welcome to **{member.guild.name}** {member.menthion}! Head over to <#776501954054193225> to say hi!")

		try:
			await member.send(f"Welcome to **{member.fuild.name}**! Enjoy your stay!")

		except Forbidden:
			pass

		await member.add_roles(*(member.guild.get_role(id_) for id_ in (534443142431375381)))


	@Cog.listener()
	async def on_member_leave(self, member):
		pass

def setup(bot):
	bot.add_cog(Welcome(bot))


