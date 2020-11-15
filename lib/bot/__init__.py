from datetime import datetime
from discord import Intents
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

PREFIX = "+"
OWNER_IDS = [534443142431375381]

class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler = AsyncIOScheduler()

		super().__init__(command_prefex = PREFIX,owner_ids = OWNER_IDS)

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

			embed = Embed(title = 'Now online!', 
			description = "Bot is now online!", 
			color = "0xFF0000",
			timespan)
			fields = [("Name", "Value", True),
					  ("Another field", "This field is next to the other one.")
					  ("A non-inline field", "This field will apear on it's own row.", False)]
			
			for name, value, inline in fields:
				embed.add.tield(name = name, value = value, inline = inline)
				embed.set_footer(text = "This is a footer!")
			await channel.send(embed = embed)
			
		else:
			print("bot recconected")

	async def on_message(self, message):
		pass

 bot = Bot()
	
