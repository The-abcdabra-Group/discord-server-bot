import discord
from discord import app_commands
import json
from services.verify import member_verification
from commands.moderation import moderation
from commands.economy import economy
from services.antinuke import antinuke

client = discord.Client(intents=discord.Intents.all())
client.tree = app_commands.CommandTree(client)

config = json.load(open("config.json"))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=config["status"]))
    print("Connected to discord API! Initializing the client")
    await commands()    
    await services()


async def commands():
    await moderation(client, client.tree, config)
    await economy(client, client.tree, config)

    if config["commands"]["sync"] == False:
        print("Skipped syncing slash commands!")
        pass

    elif config["commands"]["sync"] == "ask":
        data = input("Would you like to sync slash commands with the discord API? (Y/N) ")
        if data == "Y" or data == "y":
            await client.tree.sync(guild=discord.Object(id=config["commands"]["guild"]))
            await client.tree.sync(guild=discord.Object(id=config["commands"]["beta_guild"]))
            print("Synced slash commands!")
        else:
            print("Skipped syncing slash commands!")
            pass

    elif config["commands"]["sync"] == True:
        await client.tree.sync(guild=discord.Object(id=config["commands"]["guild"]))
        await client.tree.sync(guild=discord.Object(id=config["commands"]["beta_guild"]))
        print("Synced slash commands!")



async def services():
    await member_verification(client, config)
    await antinuke(client, config)


client.run(config["token"])