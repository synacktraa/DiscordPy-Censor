#importing required modules

import discord
from discord.ext import commands
from censor import censor


TOKEN = "OTAxNDU4MTkyMDg3Nzc3MzIw.YXQKXQ.Bxbh6rViIAehJiTpL2mnYF6l-1A"

intents = discord.Intents().default()
intents.members = True #setting the discord intents for members to true

client = commands.Bot(command_prefix="$", intents=intents) #setting the command prefix to "$" and intents to intents

store = []

@client.event
async def on_ready(): #asynchronous function for discord bot to initialize
    activity = discord.Game(name="Zeroday.gg") #setting the activity variable to discord game 
    await client.change_presence(status=discord.Status.online, activity=activity) #when the bot is initialized the bot activity set to the activity provided
    print(f"Logged in as {client.user}.") 


@client.event
async def on_message(message): 
    
    """
        Checks for users messages.
    """
    if message.author == (client.user or message.author.client): 
        return

    channel = message.channel 
    author = message.author.name  
    msg = message.content
    
    try:

        await client.process_commands(message) 

        cen_msg = censor(msg)
        if message.content != cen_msg:
            await message.delete()
            await channel.send(f"{author}: {cen_msg}")
        else:
            pass
    
        """
            bot.process_commands processes the commands that have been registered to the bot and other groups. 
            Without this coroutine, none of the commands will be triggered.
        """

    except discord.errors.NotFound:
            return

    except discord.ext.commands.errors.CommandNotFound:
            return


client.run(TOKEN)
