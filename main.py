import discord
import os
from utilities.dataparser import Bot
from utilities import default
config = default.config()
print("Logging in...")
bot = Bot(
    command_prefix=config["prefix"], prefix=config["prefix"],
    owner_ids=config["owners"], command_attrs=dict(hidden=True),
    intents=discord.Intents(  # kwargs found at https://discordpy.readthedocs.io/en/latest/api.html?highlight=intents#discord.Intents
        guilds=True, members=True, messages=True, reactions=True, presences=True, voice_states=True
    )
)
for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")


try:
    bot.run(config["token"])
except Exception as e:
    print(f"Error when logging in: {e}")