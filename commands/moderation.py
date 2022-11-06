import discord
from discord import app_commands
from utils.punishments import Punishments


async def moderation(client: discord.Client, tree: app_commands.CommandTree, config):
    @tree.command(name="mute", description="Silences a user for the specified amount of time", guild=discord.Object(id=config["commands"]["guild"]))
    # @app_commands.checks.has_any_role(1024016676162900040, 1024016899702526045)
    async def mute(interaction: discord.Interaction, user: discord.Member, time: str, reason: str):
        if user.top_role > interaction.user.top_role or user.id in [interaction.user.id, client.user.id] or user.guild_permissions.administrator:
            embed = discord.Embed(color=0xEF4444).set_author(name="Mute Command").add_field(name="Failed to execute command", value="You cannot mute this user!")

            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        else:
            punishment = Punishments(client, user, config)
            await punishment.mute(reason, time, interaction.user)
            embed = discord.Embed(color=0x22C55E).set_author(name="Mute Command").add_field(name="Command Successful", value=f"{user.mention} has been muted for `{time}` \nReason: `{reason}`").set_footer(text="Abuse of Power is Prohibited")
        
            await interaction.response.send_message(embed=embed, ephemeral=True)

    @tree.command(name="ban", description="Bans a user permanently", guild=discord.Object(id=config["commands"]["guild"]))
    async def ban(interaction: discord.Interaction, user: discord.Member, reason: str):
        if user.top_role > interaction.user.top_role or user.id in [interaction.user.id, client.user.id] or user.guild_permissions.administrator:
            embed = discord.Embed(color=0xEF4444).set_author(name="Ban Command").add_field(name="Failed to execute command", value="You cannot ban this user!")
        
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        else:
            punishment = Punishments(client, user, config)
            await punishment.ban(reason, interaction.user)
            embed = discord.Embed(color=0x22C55E).set_author(name="Ban Command").add_field(name="Command Successful", value=f"{user.mention} has been permanently banned from the server \nReason: `{reason}`").set_footer(text="Abuse of Power is Prohibited")

            await interaction.response.send_message(embed=embed, ephemeral=True)

    @tree.command(name="kick", description="Kicks a user permanently", guild=discord.Object(id=config["commands"]["guild"]))
    async def kick(interaction: discord.Interaction, user: discord.Member, reason: str):
        if user.top_role > interaction.user.top_role or user.id in [interaction.user.id, client.user.id] or user.guild_permissions.administrator:
            embed = discord.Embed(color=0xEF4444).set_author(name="Kick Command").add_field(name="Failed to execute command", value="You cannot kick this user!")
        
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        else:
            punishment = Punishments(client, user, config)
            await punishment.kick(reason, interaction.user)
            embed = discord.Embed(color=0x22C55E).set_author(name="Kick Command").add_field(name="Command Successful", value=f"{user.mention} has been kicked from the server \nReason: `{reason}`").set_footer(text="Abuse of Power is Prohibited")

            await interaction.response.send_message(embed=embed, ephemeral=True)

    @tree.command(name="warn", description="Warns a user for infractions of server rules", guild=discord.Object(id=config["commands"]["guild"]))
    async def warn(interaction: discord.Interaction, user: discord.Member, reason: str):
        if user.top_role > interaction.user.top_role or user.id in [interaction.user.id, client.user.id] or user.guild_permissions.administrator:
            embed = discord.Embed(color=0xEF4444).set_author(name="Warn Command").add_field(name="Failed to execute command", value="You cannot warn this user!")
        
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        else:
            punishment = Punishments(client, user, config)
            await punishment.warn(reason, interaction.user)
            embed = discord.Embed(color=0x22C55E).set_author(name="Warn Command").add_field(name="Command Successful", value=f"{user.mention} has been warned! \nReason: `{reason}`").set_footer(text="Abuse of Power is Prohibited")

            await interaction.response.send_message(embed=embed, ephemeral=True)