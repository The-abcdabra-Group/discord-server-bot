import discord
from utils.time import time
from typing import Union

class Punishments:
    """Represents a Punishment issuer
    This class is used to issue punishments to members and add those punishments to the database

    Attributes
    ------------
    client: :class:`discord.Client`
        Represents a client connection that connects to Discord. This class is used to interact with the Discord WebSocket and API.
    member: :class:`discord.Member`
        Represents a Discord member to a Guild.
    """

    def __init__(self, client: discord.Client, member: discord.Member):
        self.client = client
        self.member = member


    async def warn(self, reason: str, author: Union[str, discord.Member]):
        embed = discord.Embed(color=0xEF4444).set_author(name="Punishment Recieved").add_field(name="You have been warned", value=f"Reason: `{reason}` \n*Punishments are non-appealable*")
        
        try:
            await self.member.send(embed=embed)
        except:
            pass