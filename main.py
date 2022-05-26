import asyncio
from config.config_buttons import buttons_all
import discord
from discord import app_commands
from discord.ext import commands
from discord.interactions import Interaction
from discord.ui import button, View, Button
import time
import random
from datetime import datetime, timezone, timedelta
import json
import os
import traceback
import colorama
from colorama import Fore 
from colorama import Style
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageOps
from googlesearch import search
colorama.init(autoreset=True)

# token security
if os.path.exists(os.getcwd() + "/config/config.json"):
    with open("./config/config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token": "", "Prefix": "m!"}
    
    with open(os.getcwd() + "/config/config.json", "w+") as f:
        json.dump(configTemplate, f)
        
token = configData["Token"]
prefix = configData["Prefix"]

#config firebase 
link_firebase = "" # Essa base ultiliza firebase como banco de dados, se você não usa firebase não tem problema

id_do_servidor = 900524034356285471 # coloca o id do seu servidor de teste do seu bot.


# CMD DESENHOS
print()
print()
print(f"""
    {Fore.GREEN}
    ███╗░░░███╗██╗██╗░░██╗░█████╗░  ██████╗░██████╗░░██████╗░  ██████╗░░█████╗░████████╗
    ████╗░████║██║██║░██╔╝██╔══██╗  ██╔══██╗██╔══██╗██╔════╝░  ██╔══██╗██╔══██╗╚══██╔══╝
    ██╔████╔██║██║█████═╝░███████║  ██████╔╝██████╔╝██║░░██╗░  ██████╦╝██║░░██║░░░██║░░░
    ██║╚██╔╝██║██║██╔═██╗░██╔══██║  ██╔══██╗██╔═══╝░██║░░╚██╗  ██╔══██╗██║░░██║░░░██║░░░
    ██║░╚═╝░██║██║██║░╚██╗██║░░██║  ██║░░██║██║░░░░░╚██████╔╝  ██████╦╝╚█████╔╝░░░██║░░░
    ╚═╝░░░░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░  ╚═════╝░░╚════╝░░░░╚═╝░░░""")
print()
print()

class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(intents=discord.Intents.all(), command_prefix=commands.when_mentioned_or(f"{prefix}"))

    async def setup_bot(self):
        await self.wait_until_ready()
        await self.tree.sync(guild=discord.Object(id=id_do_servidor) if id_do_servidor else None)

        data = datetime.now()
        diferenca = timedelta(hours=-3)
        fuso_horario = timezone(diferenca)
        hora = data.astimezone(fuso_horario)
        hora_sp = hora.strftime('%H:%M')

        # channel = bot.get_channel(954908161683382272)
        # embed = discord.Embed(title="📶 | __Status 𝑤𝘩𝑦 𝑚𝑖𝑘𝑎__", description=f"**Hello World!** I this online! 🟢", color=0xFF6464)
        # embed.set_thumbnail(url=f'{bot.user.avatar_url}')
        # embed.add_field(name="Status:", value=f"```ini\n[🟢 | {discord.Status.online}]```")
        # embed.add_field(name="Hora da inicialização:", value=f"```ini\n[⏰ | {hora_sp}]```")
        # embed.add_field(name="Repositório: <:heroku:954927920797851738>", value=f"```ini\n[Heroku: Cloud Application Platform]```")
        # embed.add_field(name="Latência: ", value=f"```ini\n[📡 | {round(bot.latency * 1000)}ms]```", inline=False)
        # embed.add_field(name="Status Atividade: ", value=f"```ini\n[🎮 | {activity}]```")
        # online = await channel.send("<@!904572362039631932>", embed=embed)
        # await online.add_reaction('✅')

        await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name="Discord.py [v2]", url='https://www.twitch.tv/directory/game/The%20Witcher%203%3A%20Wild%20Hunt'))
        bot.remove_command('help')

    async def setup_hook(self):

        # o cogs são como as pasta de " commands " do discord.js
        if os.path.isdir(f'./cogs'):
            for filename in os.listdir(f'./cogs'):
                if filename.endswith('.py'):
                    try:
                        await self.load_extension(f'cogs.{filename[:-3]}')
                    except Exception:

                        traceback.print_exc()


        self.loop.create_task(self.setup_bot())

    

bot = MyBot()

# configurações para não da erro quando alguém usa um comando que não exista!
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("Não tenho permissões suficientes!")

    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Você não tem permissões para usar este comando.')

# hora class 
class Hora():
    def __init__(self):
        pass
    # aqui e um função que pega a hora de são paulo! você pode muda o " timedelta " de acordo com a hora da sua cidade e estado
    def hours(self):
        data = datetime.now()
        diferenca = timedelta(hours=-3)
        fuso_horario = timezone(diferenca)
        hora = data.astimezone(fuso_horario)
        hora_sp = hora.strftime('%H:%M')
        return hora_sp  


# aqui são os buttons que e usado no command ping, para configura buttons você deve ir no "./config/config_buttons"
class buttonPing(discord.ui.View):
    @discord.ui.button(label="Atualizar Ping", style=discord.ButtonStyle.primary, emoji="<:antenna:963446876496101437>")
    async def button_ping(self, interaction: discord.Interaction, button: discord.ui.Button):
        # edit_message | send_message
        latency_bot = f"{round(bot.latency * 1000)}ms"
        embed = discord.Embed(description=f"<:antenna:963446876496101437> *Minha latência é de:* `{latency_bot}`", color=0x6508ab)

        await interaction.response.edit_message(embed=embed)

# aqui ele vai funciona tanto pra slash e prefix ao mesmo tempo!
@bot.hybrid_command(name="ping", description="(🏓) Veja meu ping.")
@app_commands.guilds(900524034356285471)
async def ping(ctx):
    view = buttonPing()
    latency_bot = f"{round(bot.latency * 1000)}ms"
    embed = discord.Embed(description="**Carregando...** <a:loading:974662727962337300>", color=0x6508ab)
    loading = await ctx.send(ctx.author.mention, embed=embed)

    await asyncio.sleep(4)

    embed = discord.Embed(description=f"<:antenna:963446876496101437> *Minha latência é de:* `{latency_bot}`", color=0x6508ab)
    await loading.edit(embed=embed, view=view)


bot.run(token)
