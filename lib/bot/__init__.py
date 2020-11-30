from asyncio import sleep
from glob import glob
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

from discord import Embed , File
from datetime import datetime
from discord.ext.commands import (CommandNotFound, BadArgument, MissingRequiredArgument,CommandOnCooldown)
from apscheduler.triggers.cron import CronTrigger
from discord.errors import HTTPException, Forbidden

#from ..db import db


PREFIX = "+"
OWNER_IDS = [534443142431375381]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]


class Ready(object):
	def __init__(self):
		for cog in COGS:
			setattr(self, cog, False)

	def ready_up(self, cog):
		setattr(self, cog, True)
		print(f"{cog} cog ready")

	def all_ready(self):
		return all([getattr(self, cog) for cog in COGS])




class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.cogs_ready = Ready()
		self.guild = None
		self.scheduler = AsyncIOScheduler()

		#db.autosave(self.scheduler)
		super().__init__(command_prefix=PREFIX,owner_ids=OWNER_IDS)


	def setup(self):
		for cog in COGS:
			self.load_extension(f"lib.cogs.{cog}")
			print(f"{cog} cog loaded")

		print("setup complete")


	def run(self, version):
		self.VERSION = version

		print("running setup...")
		self.setup()

		with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
			self.TOKEN = tf.read()

		print("running bot...")
		super().run(self.TOKEN, reconnect = True)

	async def on_connect(self):
		print("bot connected")

	async def on_disconnect(self):
		print("bot disconnected")

	async def on_error(self, err, *args, **kwargs):
		if err == "on_command_error":
			await args[0].send("Something went wrong!")
		
		await self.stdout.send("An error occured!")
		raise

	async def on_command_error(self, ctx, exc):
		if isinstanse(exc, CommandNotFound):
			pass

		elif hasattr(exc, "original"):
			raise exc.original
		else:
			raise exc

	async def on_ready(self):
		if not self.ready:
			self.guild = self.get_guild(776501953593212950)
			self.stdout = self.get_channel(776501954054193223)
			self.scheduler.start()


			channel = self.get_channel(776501954054193223)  
			
			embed = Embed(title="Im here", description="Bot is online",colour=0xFF0000, timestamp=datetime.utcnow())
			fields=[("Vladyslav Petriuk , Alona Kovtun , Vladyslava Tokar","Authors",True),("     w60083                     w60065                 w60092","Indexs",False),("Commands","----------------------------------------------------------------------------------",False),("Hello","Say +hi",True),("echo","+echo message",True),("punch","+punch member reason",True)]
			for name ,value,inline in fields:
				embed.add_field(name=name,value=value,inline=inline)
			embed.set_author(name="Bot", icon_url=self.guild.icon_url)
			await channel.send(embed=embed)


			while not self.cogs_ready.all_ready():
				await sleep(0.5)

			await self.stdout.send("Now online!")

			self.ready = True
			print("bot ready")
		else:
			print("bot recconected")

	async def on_message(self, message):
		pass

bot=Bot()