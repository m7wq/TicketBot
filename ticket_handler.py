from bot import *
import storage

async def handle(interaction: discord.Interaction):
    
    for ticket in storage.tickets:
        if interaction.user.name == ticket.creator.name: 
            interaction.response.send_message("You have been already in ticket",ephemeral=True)
            return
        


    try:

        
        channel: discord.TextChannel =storage.category.guild.create_text_channel(
            name= "ticket-"+interaction.user.name,
            category= storage.category,
            
            
        )

        
        
        channel.members.clear()
        channel.members.append(interaction.user)

        ticket = storage.Ticket(channel,interaction.user)

        storage.tickets.append(ticket)

        channel.guild.role

        for user in channel.guild.members:
            for role in user.roles:
                if role == storage.ticket_support_role:
                    channel.members.append(user)

       

        interaction.response.send_message("Successfully created ticket " + f"{channel.mention}", ephemeral=True)
        
    except:
        interaction.response.send_message("Error | couldn't create the ticket", ephemeral=True)

    color = discord.colour.Color.brand_red

    embed = discord.Embed(
        title=f"@everyone **{interaction.user.mention} has created a ticket**",
        description=f"Sir, {interaction.user.mention} Please wait for staff to wake up\nPlease do not mention any staff.\nThanks for your patient",
        color=color
    )

    button = Button(
        style=discord.ButtonStyle.danger,
        label="Close"
    )

    async def close_ticket(close_interaction: discord.Interaction):
       interaction.response.send_message("Ticket closed successfully") 
       await channel.name = channel.name+"-closed"
       await channel.members.remove(interaction.user)

    
       storage.tickets.remove(ticket)
       await client.create_dm(interaction.user).send(f"Your ticket in **{discord.guild.__name__}** Server has been closed by {close_interaction.user.name}")

    button.callback = close_ticket
    view = View().add_item(button)

    channel.send(embed=embed,view=view)