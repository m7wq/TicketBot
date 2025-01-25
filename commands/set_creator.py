from bot import *
from storage import *
import ticket_handler

@tree.command("setCreator", "Set ticket creating embed")
async def creator_handle(action: discord.Interaction):
    client.add
    if category == None:
        action.response.send_message("There's an issue in system initializing, Please wait for fixing", ephemeral=True)
        return
    
    embed = discord.Embed(
        color=discord.Color.colour.blue,
        title="**Create a Ticket!**",
        description="If you need any support or you need to report something you can open ticket by clicking on Create",
        url="https://th.bing.com/th/id/OIP.QGClI7MjESuq3jRer34aYQAAAA?rs=1&pid=ImgDetMain"
    )

    
        

    button = Button(label="Create",emoji="🎫")

    button.callback = ticket_handler.handle

    view = View().add_item(button)

    action.channel.send(embed=embed,view=view)