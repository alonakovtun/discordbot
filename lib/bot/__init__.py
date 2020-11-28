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

class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler = AsyncIOScheduler()

		#db.autosave(self.scheduler)
		super().__init__(command_prefix=PREFIX,owner_ids=OWNER_IDS)

	def run(self, version):
		self.VERSION = version

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
		
		channel = self.get_channel(776501954054193223)  
		await channel.send("An error occured!")
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
			self.ready = True
			self.guild = self.get_guild(776501953593212950)
			self.scheduler.start()


			channel = self.get_channel(776501954054193223)  
			await channel.send("Now online!")

			embed = Embed(title="Im here", description="Bot is online",colour=0xFF0000, timestamp=datetime.utcnow())
			fields=[("Vladyslav Petriuk , Alona Kovtun , Vladyslava Tokar","Authors",True),("     w60083                     w60065                 w60092","Indexs",False),("Commands","----------------------------------------------------------------------------------",False),("Hello","Say +hi",True),("echo","+echo message",True),("punch","+punch member reason",True)]
			for name ,value,inline in fields:
				embed.add_field(name=name,value=value,inline=inline)
			embed.set_author(name="Bot", icon_url=self.guild.icon_url)
			await channel.send(embed=embed)

			print("bot ready")
		else:
			print("bot recconected")

	async def on_message(self, message):
		pass

bot=Bot()