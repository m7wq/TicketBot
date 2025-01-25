from bot import *

@tree.command(name="setCategory",description="set tickets creating location",)
@app_commands.describe(category="Your tickets catagory")
async def append_ticket_channel(interaction: discord.Interaction, category: discord.CategoryChannel):



    try:
        category = category
    except:
        await interaction.response.send_message("Error while setting the category.", ephemeral=True)

    await interaction.response.send_message("Successfully set your category")