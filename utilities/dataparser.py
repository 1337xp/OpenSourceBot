import discord
from discord.ext.commands import AutoShardedBot
class Bot(AutoShardedBot):
    def __init__(self, *args, db, prefix=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = prefix
        self.db = db

    async def on_message(self, msg):
        if not self.is_ready() or msg.author.bot or not discord.permissions.Permissions.can_handle(msg, "send_messages"):
            return

        await self.process_commands(msg)
