import discord

async def member_verification(client: discord.Client, config):
    @client.event
    async def on_interaction(interaction: discord.Interaction):
        if interaction.channel_id != config["verification"]["channel"]:
            return

        elif interaction.data["custom_id"] != config["verification"]["interaction_id"]:
            return
            
        else:
            verification_roles = config["verification"]["verification_roles"]
            for data in verification_roles:
                role = interaction.guild.get_role(data)
                await interaction.user.add_roles(role)

            await interaction.response.defer()



# embed = discord.Embed(color=0xEF4444).set_author(name="Server Verification").add_field(name="Click the `Verify` button to gain access to the server", value="**By clicking the button** \n - You agree that you have read the Discord TOS and the server constitution \n - You agree to obey to any other rules in the <#1008869517587386548> \n - You agree to obey to any future rules that may be implemented \n - You agree to follow the Discord TOS \n** ** \n*Failure to follow the rules, even if you were hacked, is your responsibility. The staff of this server are not legally or ethically liabile for your actions against the server rules or the Discord TOS*")
# channel = await client.fetch_channel(1024017941580239030)
# view = discord.ui.View() # Establish an instance of the discord.ui.View class
# style = discord.ButtonStyle.gray  # The button will be gray in color
# item = discord.ui.Button(style=style, label="Verify")
# view.add_item(item=item)
# await channel.send(embed=embed, view=view)