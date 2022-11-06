import discord
from discord import app_commands
from pymongo import MongoClient
from random import randrange

async def economy(client: discord.Client, tree: app_commands.CommandTree, mongodb: MongoClient, config):

    @tree.command(name="balance", description="Returns the user's economy balance", guild=discord.Object(id=config["commands"]["beta_guild"]))
    async def balance(interaction: discord.Interaction):
        balance = mongodb["economy"]["balance"]

        if balance.find_one({"_id": interaction.user.id}) == None:
            balance.insert_one({"balance": 0, "_id": interaction.user.id})
        
        data = balance.find_one({"_id": interaction.user.id})
        await interaction.response.send_message(f"Your balance is {data['balance']} :coin:")

    
