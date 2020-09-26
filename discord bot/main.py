import asyncio
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from itertools import cycle
import json
import os
import time

def get_prefix(client, message): #this json file is loaded and unloaded after everytime leaving or joining a server
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix = get_prefix)
client.remove_command("help")
status = cycle(["Our life is what our thoughts make it.",
        "The soul becomes dyed with the colour of its thoughts.",
        "If it is not right do not do it; if it is not true do not say it.",
        "The best revenge is not to be like your enemy.",
        "Reject your sense of injury and the injury itself disappears.",
        ])
#------------------------------------------------EVENTS-----------------------------------------------------------------------

@client.event
async def on_ready():
    change_status.start()
    print("Bot is online!")
    
@client.event#Creates the json file of prefixes on join
async def on_guild_join(guild):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = "!"#adds the prefix ! with the guild id

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent = 4)

@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

    prefixes.pop(str(guild.id))#Removes the guild id and prefix from the prefixes.json file

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent = 4)

#---------------------------------------------TASKS-------------------------------------------------------------------------------

@tasks.loop(seconds=60)#cycles the bot status from all the statuses in the first statuses list
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))

#----------------------------------------------COMMANDS----------------------------------------------------------------------------

@client.command()#changes prefix for the specified guild id and saves it into prefixes.json
async def changeprefix(ctx, prefix):
    with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix#specifies the new prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent = 4)

    await ctx.send(f"Prefix changed to: {prefix}")#confirms

@client.command()#clears the amount of given text natural value=5
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit = amount)

@client.command()#displays all projects
async def projects(ctx):
    if os.stat("projects.txt").st_size == 0:#checks if the projects.text file is full or not
        await ctx.send("Please wait untill a project is added or add a project!")
    else:
        projects = open("projects.txt")

    lines = projects.readlines()
    for line in lines:
        await ctx.send(line)

@client.command()
async def addproject(ctx):
    if os.stat("projects.txt").st_size == 0:#if the text file is filled
        await ctx.send("No project has been created yet!\nCreate The first and shine like Sirius A!\nUse the command: !createproject to create your own")
    else:
        projects = open("projects.txt")

        lines = projects.readlines()
        for line in lines:
            await ctx.send(line)
        await ctx.send("These are the Projects available to join please check if we already have similar project before creating yours\nUse the command: !createproject to send yourself and others to and endless stackoverflow quest!")

@client.command()
async def createproject(ctx):

    def check(m):#cheks the sender of the message if the author is not the same as the one giving the command !createproject their message is ignored
        return m.author == ctx.message.author
    
    await ctx.send("Thanks for adding your project to our database!\nPlease enter the project name:")
    msg = await client.wait_for("message", check = check, timeout = 30)
    name = str(msg.content)#converts project name to str

    await ctx.send(f"Confirm name:{name}?\nPlease respond with yes or no")
    confirmation = await client.wait_for("message", check = check, timeout = 30)
    if confirmation.clean_content.lower() == "yes":
        project_name = name#saves the name as project_name for later usage on the projects.txt
        await ctx.send(f"Project name confirmed as:{name}")
    elif confirmation.clean_content.lower() == "no":
        await ctx.send(f"Your project hasn't been saved\n Please run the !createproject command again.\n Your project name was{name}")
    else:
        await ctx.send(f"Invalid response your project hasn't been saved\nPlease run the !createproject command again\n Your project name was{name}")
    
    time.sleep(1)
    await ctx.send("Enter project description:")
    msg = await client.wait_for("message", check = check, timeout = 30)
    desc = str(msg.content)

    await ctx.send(f"Confirm description:{desc}?\nPlease respond with yes or no")
    confirmation = await client.wait_for("message", check = check, timeout = 30)
    if confirmation.clean_content.lower() == "yes":
        project_desc = desc#saves the desc as project_desc for later usage on the projects.txt
        await ctx.send(f"Project description confirmed as:{desc}")
    elif confirmation.clean_content.lower() == "no":
        await ctx.send(f"Your project hasn't been saved\n Please run the !createproject command again.\n Your project description was{desc}")
    else:
        await ctx.send(f"Invalid response your project hasn't been saved\nPlease run the !createproject command again\n Your project description was{desc}")

    time.sleep(1)
    await ctx.send("Enter the languages planned to be used in the project:")
    msg = await client.wait_for("message", check = check, timeout = 30)
    languages = str(msg.content)

    await ctx.send(f"Confirm languages:{languages}?\nPlease respond with yes or no")
    confirmation = await client.wait_for("message", check = check, timeout = 30)
    if confirmation.clean_content.lower() == "yes":
        project_languages = languages#saves the languages as project_languages for later usage on the projects.txt
        await ctx.send(f"Project languages confirmed as:{languages}")
    elif confirmation.clean_content.lower() == "no":
        await ctx.send(f"Your project hasn't been saved\n Please run the !createproject command again.\n Your project languages were{languages}")
    else:
        await ctx.send(f"Invalid response your project hasn't been saved\nPlease run the !createproject command again\n Your project description was{languages}")

    await ctx.send("Project name: " + project_name + "\nProject description: " + project_desc + "\nProject Language(s):" + project_languages + "\nOwner:" + ctx.message.author.name + "\nContributers: None yet" )

    new_project_adding = open("projects.txt", "a")
    new_project_adding.write("Project name: " + project_name)
    new_project_adding.write("\nProject description: " + project_desc)
    new_project_adding.write("\nProject languages: " + project_languages)
    new_project_adding.write("\nProject Owner: " + ctx.message.author.name)
    new_project_adding.close()

@client.command(pass_context=True)
async def help(cxt):

    embed = discord.Embed(
        color = discord.Colour.orange()
    )

    embed.set_author(name="Help")
    embed.add_field(name = "!changeprefix", value = "Put anything after that and it will be the new prefix", inline = False)
    embed.add_field(name = "!clear", value = "Put any integer after clear with a space and that amoun of messages will be cleared. The deafult amount is 5", inline = False)
    embed.add_field(name = "!projects", value = "Displays current projects", inline = False)
    embed.add_field(name = "!addproject", value = "Gives you instructions about how a new project can be added", inline = False)
    embed.add_field(name= "!createproject", value = "Starts the process of adding a new open source project and makes you it's owner", inline = False)
    
    await cxt.send(embed = embed)
client.run("YOUR DISCORD TOKEN HERE")