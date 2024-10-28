import discord
import os
from dotenv import load_dotenv
from discord import Interaction, app_commands

#make sure to have .env added too!
load.env()

token = os.getenv('DISCORD_TOKEN')

MOD_COMMAND_USE = ["admin", "mod", "staff"] #replace with your own roles. Watch our capital letter roles need to be given as a cappital letter


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='/', intents=intents)

bot.tree.command(name="hello", description="says hello back")
async def hello(interaction: Interaction)
  await interaction.response.send_message("hello!")

bot.tree.command(name="who-made", description="get info about who made the bot")
async def who-made(interaction: Interaction)
  await interaction.response.send_message("The one that has coded this nice bot is jnbeste12. Join our server too!!! https://discord.gg/63nvvVAARq")

@bot.tree.command(name="reload", description="reloads the bot")
async def reload_bot(interaction: Interaction):
    if not any(role.name in MOD_COMMAND_USE for role in interaction.user.roles):
        await interaction.response.send_message("no perms.", ephemeral=True)
        return
    
    try:
        await interaction.response.send_message("The bot will be reloaded...", ephemeral=True)

        # Sluit de bot af en herstart het script
        os.execv(sys.executable, ['python'] + sys.argv)

    except Exception as e:
        await interaction.response.send_message(f"something went wrong: {str(e)}", ephemeral=True)

@bot.tree.command(name="poll", description="Make a poll")
async def poll(interaction: Interaction, question: str, answer1: str, answer2: str):
        # Embed maken
        embed = discord.Embed(title="📊 Poll", description=f"{question}", color=discord.Color.blue())
        embed.add_field(name="1️⃣", value=answer1, inline=False)
        embed.add_field(name="2️⃣", value=answer2, inline=False)
        
        # Verzend het embed bericht
        message = await interaction.response.send_message(embed=embed)
        message = await interaction.original_response()
        
        # Voeg de reacties toe
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        

@bot.event
async def on_ready():
    await bot.tree.sync
    print(f'bot is ready as "{bot.user}')
    print(f'All commands are synced and ready')
    print(f'bot has been made by jnbeste12, TeamFun')
    print(f'join my server for support')
