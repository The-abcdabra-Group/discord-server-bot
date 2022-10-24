import re
import discord

async def automod(client: discord.Client, config):
    link_regex = r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
    
    @client.event
    async def on_message(message: discord.Message):
        staff_role = message.guild.get_role(config["roles"]["staff_role"])

        if message.author.guild_permissions.administrator == True:
            return

        if staff_role in message.author.roles:
            return

        if re.search(link_regex, message.content):
            await message.delete()