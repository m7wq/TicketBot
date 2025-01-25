import discord
import bot

tickets = []
category = None
ticket_support_role: discord.Role = bot.get_guild().get_role(int(bot.getenv("ROLE_ID")))

class Ticket:
    def __init__(self, channel: discord.TextChannel, creator: discord.User):
        self.channel = channel
        self.creator = creator
        pass




