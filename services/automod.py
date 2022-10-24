import re
import discord
from datetime import timedelta
from utils.punishments import Punishments

async def automod(client: discord.Client, config):
    link_regex = r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
    profanity_regex = r"pussy|cum|nude|nudes|nudities|fuck me|dick|cock|boobs|vagina|orgy|orgi|horny|horni|fuck|fuck you"
    
    @client.event
    async def on_message(message: discord.Message):
        staff_role = message.guild.get_role(config["roles"]["staff_role"])

        if message.author.guild_permissions.administrator == True:
            return

        if staff_role in message.author.roles:
            return

        if re.search(link_regex, message.content) and config["automod"]["filter_links"] == True:
            punishment = Punishments(client, message.author, config)

            await message.channel.send(f"<a:deny:1033973641030946826> {message.author.mention} Please refrain from sending links on the server!")
            await message.delete()
            await punishment.warn("Sent unauthorized links in public chat", "Auto Moderator")
            return

        if re.search(profanity_regex, message.content, flags=re.IGNORECASE) and config["automod"]["filter_profanity"] == True:
            await message.channel.send(f"<a:deny:1033973641030946826> {message.author.mention} Please refrain from using profanity on the server!")
            await message.delete()
            await message.author.timeout(timedelta(minutes=5))
            return