from asyncio import sleep
from glob import glob
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from discord import Embed , File
from datetime import datetime
from discord.ext.commands import (CommandNotFound, BadArgument, MissingRequiredArgument,CommandOnCooldown)
from apscheduler.triggers.cron import CronTrigger
from discord.errors import HTTPException, Forbidden


PREFIX = "+"
OWNER_IDS = [534443142431375381]

class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler = AsyncIOScheduler()

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

	async def on_ready(self):
		if not self.ready:
			self.ready = True

			print("bot ready")

			channel = self.get_channel(776501954054193223)
			await channel.send("Now online!")

			embed = Embed(title="Im here", description="Bot is online",colour=0xFF0000, timestamp=datetime.utcnow())
			fields=[("Vladyslav Petriuk , Alona Kovtun , Vladyslava Tokar","Authors",True),("     w60083                     w60065                 w60092","Indexs",False),("Commands","----------------------------------------------------------------------------------",False),("Hello","Say +hi",True),("echo","+echo message",True),("punch","+punch member reason",True)]
			for name ,value,inline in fields:
				embed.add_field(name=name,value=value,inline=inline)
			await channel.send(embed=embed)
		else:
			print("bot recconected")

	async def on_message(self, message):
		pass

bot=Bot()