import re
import discord
from datetime import timedelta
from utils.punishments import Punishments


async def automod(client: discord.Client, config):
    link_regex = r"((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
    profanity_regex = r"pussy|cum|nude|nudes|nudities|fuck me|dick|cock|boobs|vagina|orgy|orgi|horny|horni|fuck|fuck you"
    ban_regex = r"nigger|nigga|retard|faggot"

    @client.event
    async def on_message(message: discord.Message):
        if not isinstance(message.channel, discord.TextChannel) or not config["automod"]["enabled"]:
            return

        if message.author.guild_permissions.administrator or message.guild.get_role(config["roles"]["staff_role"]) in message.author.roles:
            return

        if config["automod"]["filter_links"] and re.search(link_regex, message.content):
            punishment = Punishments(client, message.author, config)

            await message.channel.send(f"<a:deny:1033973641030946826> {message.author.mention} Please refrain from sending links on the server!")
            await message.delete()
            await punishment.warn("Sent unauthorized links in public chat` \nContents: `{message.content}", "Auto Moderator")
            return

        if config["automod"]["filter_profanity"] and re.search(profanity_regex, message.content, flags=re.IGNORECASE):
            punishment = Punishments(client, message.author, config)
            await message.channel.send(f"<a:deny:1033973641030946826> {message.author.mention} Please refrain from using profanity on the server!")
            await message.delete()
            await punishment.mute("Sent profanity on the server` \nContents: `{message.content}", "5m", "Auto Moderator")
            return

        if config["automod"]["filter_profanity"] and re.search(ban_regex, message.content, flags=re.IGNORECASE):
            punishment = Punishments(client, message.author, config)
            await message.delete()
            await punishment.ban(f"Used derogatory slurs and/or other blacklisted words` \nContents: `{message.content}", "Auto Moderator")
            return
        if config["automod"]["filter_everyone_ping"] and re.search(r"@everyone", message.content, flags=re.IGNORECASE):
            punishment = Punishments(client, message.author, config)
            await message.delete()
            await punishment.ban(f"Attempted to ping @everyone` \nContents: `{message.content}", "Auto Moderator")
            return