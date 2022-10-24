import discord
from typing import Union
from utils.time import convert_time


class Punishments:
    """Represents a Punishment issuer
    This class is used to issue punishments to members and add those punishments to the database

    Attributes
    ------------
    client: :class:`discord.Client`
        Represents a client connection that connects to Discord. This class is used to interact with the Discord WebSocket and API.
    member: :class:`discord.Member`
        Represents a Discord member to a Guild.
    config: :json:
        Represents the application configuration
    """

    def __init__(self, client: discord.Client, member: discord.Member, config):
        self.client = client
        self.member = member
        self.config = config


    async def warn(self, reason: str, author: Union[str, discord.Member]):
        staff_logs = await self.client.fetch_channel(self.config["channels"]["staff_logs"])

        embed = discord.Embed(color=0xEF4444).set_author(name="Punishment Recieved").add_field(name="You have been warned", value=f"Reason: `{reason}` \n*Punishments are non-appealable*")
        logs_embed = discord.Embed(color=0xEF4444).set_author(name="Punishment Logs").add_field(name=f"Member was warned", value=f"{self.member.mention} **was warned** \nReason: `{reason}` \nPunished By: `{author}`")

        await staff_logs.send(embed=logs_embed)
        try:
            await self.member.send(embed=embed)
        except:
            await staff_logs.send(f"<a:deny:1033973641030946826> Unable to notify {self.member.mention} of punishment")
        

    async def mute(self, reason: str, time: str, author: Union[str, discord.Member]):
        pytime = Time()
        data = await pytime.convert_time(time)

        await self.member.timeout(data, reason=reason)

        staff_logs = await self.client.fetch_channel(self.config["channels"]["staff_logs"])

        embed = discord.Embed(color=0xEF4444).set_author(name="Punishment Recieved").add_field(name="You have been muted", value=f"Reason: `{reason}` \nTime: `{time}` \n*Punishments are non-appealable*")
        logs_embed = discord.Embed(color=0xEF4444).set_author(name="Punishment Logs").add_field(name=f"Member was muted", value=f"{self.member.mention} **was muted** \nReason: `{reason}` \nTime: `{time}` \nPunished By: `{author}`")

        await staff_logs.send(embed=logs_embed)
        try:
            await self.member.send(embed=embed)
        except:
            await staff_logs.send(f"<a:deny:1033973641030946826> Unable to notify {self.member.mention} of punishment")