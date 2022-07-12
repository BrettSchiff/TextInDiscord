import discord
from discord.ext import commands
import keys

client = discord.Client();
client = commands.Bot(command_prefix="!");
is_client_running = False;

@client.event
async def on_ready():
    global is_client_running

    if not is_client_running:
        is_client_running = True
        print(f"Bot {client.user.name} initialising...")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!"):
        await message.channel.trigger_typing()
    
    await client.process_commands(message)


@client.command()
async def peepee(ctx):
<<<<<<< HEAD
    await ctx.send("poopoo from the cloud")
=======
    await ctx.send("poopoo")
>>>>>>> b275a04f536c88eeb839251f2d2f7690ec9ed838


@client.command()
async def terminate(ctx):
    await ctx.send("Terminating...")
    await client.logout()


client.run(keys.TOKEN)