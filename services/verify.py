import discord


async def member_verification(client: discord.Client, config):
    @client.event
    async def on_interaction(interaction: discord.Interaction):
        if interaction.channel_id != config["verification"]["channel"]:
            return
        elif interaction.data["custom_id"] != config["verification"]["interaction_id"]:
            return
        else:
            for data in config["verification"]["verification_roles"]:
                await interaction.user.add_roles(interaction.guild.get_role(data))
            await interaction.response.defer()
