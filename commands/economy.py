import discord
from discord import app_commands
from pymongo import MongoClient
from random import randrange

async def economy(client: discord.Client, tree: app_commands.CommandTree, mongodb: MongoClient, config):
    async def check_balance_exists(id: int):
        balance = mongodb["economy"]["balance"]

        if balance.find_one({"_id": id}) == None:
            balance.insert_one({"balance": 0, "bank_balance": 0, "_id": id})
        

    @tree.command(name="balance", description="Returns the user's economy balance", guild=discord.Object(id=config["commands"]["beta_guild"]))
    async def balance(interaction: discord.Interaction):
        await check_balance_exists(interaction.user.id)

        balance = mongodb["economy"]["balance"]
        
        data = balance.find_one({"_id": interaction.user.id})
        await interaction.response.send_message(f"Your balance is {data['balance']} :coin:")

    @tree.command(name="beg", description="Beg on the stone cold streets for coins", guild=discord.Object(id=config["commands"]["beta_guild"]))
    @app_commands.checks.cooldown(1, 30)
    async def beg(interaction: discord.Interaction):
        await check_balance_exists(interaction.user.id)

        balance = mongodb["economy"]["balance"]
        
        data = balance.find_one({"_id": interaction.user.id})
        money = randrange(150, 425)

        balance.update_one({"_id": interaction.user.id}, {"$set": {"balance": data["balance"] + money}})

        async def statement(number):
            if number == 1:
                await interaction.response.send_message(f"You begged on the streets and got {money} :coin:")
            if number == 2:
                await interaction.response.send_message(f"The old lady took pity and gave you {money} :coin:")
            if number == 3:
                await interaction.response.send_message(f"The abcdadbra gods grant you {money} :coin:")
            if number == 4:
                await interaction.response.send_message(f"While begging, you found {money} :coin: on the street!")
            if number == 5:
                await interaction.response.send_message(f"The Communist Party donated you {money} :coin:")
            if number == 6:
                await interaction.response.send_message(f"A bird was carrying {money} :coin: and dropped it in your hand")

        await statement(randrange(1,6))
    
    @beg.error
    async def beg_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)