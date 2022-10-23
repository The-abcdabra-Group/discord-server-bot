import discord
from utils.time import convert_time
from discord import app_commands

async def economy(client: discord.Client, tree: app_commands.CommandTree, config):
    @tree.command(name="balance", description="Returns the user's economy balance", guild=discord.Object(id=config["commands"]["beta_guild"]))
    async def balance(interaction: discord.Interaction):
        await interaction.response.send_message("Your balance is `NULL` :coin:")