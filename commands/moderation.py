import discord
from utils.time import convert_time
from discord import app_commands


async def moderation(client: discord.Client, tree: app_commands.CommandTree, config):
    @tree.command(name="mute", description="Silences a user for the specified amount of time", guild=discord.Object(id=config["commands"]["guild"]))
    # @app_commands.checks.has_any_role(1024016676162900040, 1024016899702526045)
    async def mute(interaction: discord.Interaction, user: discord.Member, time: str, reason: str):
        # Assert values for type checking
        assert isinstance(interaction.user, discord.Member)
        assert isinstance(client.user, discord.ClientUser)

        
        pytime = await convert_time(time)

        if user.id == interaction.user.id:
            embed = discord.Embed(color=0xEF4444).set_author(name="Mute Command").add_field(name="Failed to execute command", value=f"You cannot mute yourself, unless...")
        
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        elif user.top_role > interaction.user.top_role:
            embed = discord.Embed(color=0xEF4444).set_author(name="Mute Command").add_field(name="Failed to execute command", value=f"{user.mention} has a higher role than you")
        
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        elif user.id == client.user.id:
            embed = discord.Embed(color=0xEF4444).set_author(name="Mute Command").add_field(name="Failed to execute command", value=f"You cannot punish {client.user.mention}")
        
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        elif user.guild_permissions.administrator == True:
            embed = discord.Embed(color=0xEF4444).set_author(name="Mute Command").add_field(name="Failed to execute command", value="You cannot punish an `ADMINISTRATOR`")
        
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        else:
            await user.timeout(pytime, reason=reason)
            embed = discord.Embed(color=0x22C55E).set_author(name="Mute Command").add_field(name="Command Successful", value=f"{user.mention} has been muted for `{time}` \nReason: `{reason}`").set_footer(text="Abuse of Power is Prohibited")
        
            await interaction.response.send_message(embed=embed, ephemeral=True)


    @tree.command(name="ban", description="Bans a user permanently", guild=discord.Object(id=config["commands"]["guild"]))
    async def ban(interaction: discord.Interaction, user: discord.Member, reason: str):
        # Assert values for type checking
        assert isinstance(interaction.user, discord.Member)
        assert isinstance(client.user, discord.ClientUser)


        if user.id == interaction.user.id:
            embed = discord.Embed(color=0xEF4444).set_author(name="Ban Command").add_field(name="Failed to execute command", value=f"You cannot ban yourself, unless...")
        
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        elif user.top_role > interaction.user.top_role:
            embed = discord.Embed(color=0xEF4444).set_author(name="Ban Command").add_field(name="Failed to execute command", value=f"{user.mention} has a higher role than you")
        
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        elif user.id == client.user.id:
            embed = discord.Embed(color=0xEF4444).set_author(name="Ban Command").add_field(name="Failed to execute command", value=f"You cannot punish {client.user.mention}")
        
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        elif user.guild_permissions.administrator == True:
            embed = discord.Embed(color=0xEF4444).set_author(name="Ban Command").add_field(name="Failed to execute command", value="You cannot punish an `ADMINISTRATOR`")
        
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        else:
            await user.ban(reason=reason)
            embed = discord.Embed(color=0x22C55E).set_author(name="Ban Command").add_field(name="Command Successful", value=f"{user.mention} has been permanently banned from the server \nReason: `{reason}`").set_footer(text="Abuse of Power is Prohibited")

            await interaction.response.send_message(embed=embed, ephemeral=True)