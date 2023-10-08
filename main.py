import nextcord as discord
from owo import owoify
from tools import meth, get_settings
from nextcord.ext import commands
from nextcord import Interaction
from oni import Onih

#never ever post the token

bot=get_settings("settings.json")

intents = discord.Intents.all()
intents.message_content = True

class MegaBot(commands.Bot):
    async def is_owner(self, user):
        if user.id in bot.owners:
            return True
        else:
            return False

client = MegaBot(command_prefix=bot.pfx,case_insensitive=True,intents=intents,help_command=None)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(status=bot.status.value,activity=discord.Game(bot.status.text))

@client.slash_command(name="h", description='Responds with "h"', guild_ids=bot.guilds)
async def h(interaction):
    await interaction.response.send_message("h")

@client.slash_command(name="ping", description='Responds with "Pong!"', guild_ids=bot.guilds)
async def ping(interaction):
    await interaction.response.send_message("Pong!")

@client.slash_command(name="pong", description='Responds with "Ping!"', guild_ids=bot.guilds)
async def pong(interaction):
    await interaction.response.send_message("Ping!")

@client.slash_command(name= "calc", description= "This command runs math!", guild_ids= bot.guilds)
async def calc(interaction, math):
    try:
        await interaction.response.send_message(meth(math))
    except:
        await interaction.response.send_message(f"Could not evaluate `{math}` :(")

@client.slash_command(name= "owo", description= "This command owoifies text!", guild_ids= bot.guilds)
async def owo(interaction, text):
    await interaction.response.send_message(owoify(text))

@client.slash_command(name= "help", description= "This command displays the help message for this bot!", guild_ids= bot.guilds)
async def help(interaction):
    e=discord.Embed(title=f"{bot.name} Help", color=bot.color, description="This is a list of all my commands and how to use them :)")
    e.set_footer(text="Made By Kev And H")
    e.add_field(name="H",value="This command responds with h and is used like `/h`")
    e.add_field(name="Calc",value="This command calculates math and is used like `/calc 1+1`")
    e.add_field(name="Ping",value="This command responds with pong and is used like `/ping`")
    e.add_field(name="Pong",value="This command responds with ping and is used like `/pong`")
    e.add_field(name="owo",value=owoify("This command owoifies the text you give it")+" and is used like `/owo Hello, World!!`")
    e.add_field(name="Help",value="this command displays this message and is used like `/help`")
    await interaction.response.send_message(embed=e)

@client.slash_command(name="confess", description="Sends an anonymous confession!", guild_ids=bot.guilds)
async def confess(interaction, text):
    channel = client.get_channel(bot.anon_channel)
    if bot.anon_log:
        log=client.get_channel(bot.anon_log_channel)
    try:
        e=discord.Embed(description=text, color=bot.color)
        e.set_footer(text=f"Anonymous confession by {bot.name}")
        msg= await channel.send(embed=e)
        if bot.anon_log:
            try:
                le=discord.Embed(title=f"Anonymous confession sent by {interaction.user.name}", description=f'{interaction.user.mention} said "{text}"', color=bot.color)
                le.set_footer(text=f"{interaction.user.name.capitalize()}'s id is {interaction.user.id}")
                await log.send(embed=le)
            except:
                le=discord.Embed(title=f"Anonymous confession sent by {interaction.user.name}", description=f"{interaction.user.mention}'s confession is {msg.jump_url}", color=bot.color)
                le.set_footer(text=f"{interaction.user.name.capitalize()}'s id is {interaction.user.id}")
                await log.send(embed=le)
        await interaction.response.send_message(f"Sent in {channel.mention}!", ephemeral= True)
    except:
        await interaction.response.send_message("Message was too long :(", ephemeral= True)
        if bot.anon_log:
            le=discord.Embed(title=f"Anonymous confession attempted by {interaction.user.name}", description= f"But {interaction.user.mention}'s confession was too long :(", color=bot.color)
            le.set_footer(text=f"{interaction.user.name.capitalize()}'s id is {interaction.user.id}")
            await log.send(embed=le)
            try:
                await log.send(f"{interaction.user.name.capitalize()}'s confession was: ```\n{text}\n```")
            except:
                pass

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f"You did something wrong.\n```\n{error}\n```")

client.add_cog(Onih(bot=client))
client.run(bot.token)