import discord
from discord import app_commands
import json

client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

config = json.load(open("config.json"))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=config["status"]))
    print("Connected to discord API! Initializing the client")
    await commands()    
    await services()


async def commands():
    from commands.moderation import moderation
    from commands.economy import economy


    await moderation(client, tree, config)
    await economy(client, tree, config)

    if config["commands"]["sync"] == False:
        print("Skipped syncing slash commands!")
        pass

    elif config["commands"]["sync"] == "ask":
        data = input("Would you like to sync slash commands with the discord API? (Y/N) ")
        if data == "Y" or data == "y":
            await tree.sync(guild=discord.Object(id=config["commands"]["guild"]))
            await tree.sync(guild=discord.Object(id=config["commands"]["beta_guild"]))
            print("Synced slash commands!")
        else:
            print("Skipped syncing slash commands!")
            pass

    elif config["commands"]["sync"] == True:
        await tree.sync(guild=discord.Object(id=config["commands"]["guild"]))
        await tree.sync(guild=discord.Object(id=config["commands"]["beta_guild"]))
        print("Synced slash commands!")



async def services():
    from services.verify import member_verification
    from services.antinuke import antinuke
    from services.automod import automod

    await member_verification(client, config)
    await antinuke(client, config)
    await automod(client, config)

client.run(config["token"])