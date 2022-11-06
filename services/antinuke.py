import discord


async def antinuke(client: discord.Client, config):
    if not config["antinuke"]["enabled"]:
        return

    # Reject all discord bots from joining the server
    @client.event
    async def on_member_join(member):
        if member.bot:
            await member.ban(reason = "abcdabra Anti Nuke Defense")
            channel = await client.fetch_channel(config["channels"]["staff_logs"])
            await channel.send(f"The server anti-nuke prevented `{member}` from joining")
