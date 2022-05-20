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
link_firebase = "https://mikarpg-4d967-default-rtdb.firebaseio.com"

id_do_servidor = 900524034356285471 # id do servidor, caso queira comando global coloque None (mas os comandos podem demorar aparecer).


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
        super().__init__(intents=discord.Intents.all(), command_prefix=commands.when_mentioned_or(f"{prefix}")) # o bot vai responder tanto o prefixo especificado e menção como prefixo (ex: @seubot ping).

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

        await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name="Pica do debra e grossa", url='https://www.twitch.tv/directory/game/The%20Witcher%203%3A%20Wild%20Hunt'))
        bot.remove_command('help')

    async def setup_hook(self):

        # carregar cogs/extensões da pasta cogs
        if os.path.isdir(f'./cogs'):
            for filename in os.listdir(f'./cogs'):
                if filename.endswith('.py'):
                    try:
                        await self.load_extension(f'cogs.{filename[:-3]}')
                    except Exception:

                        traceback.print_exc()


        self.loop.create_task(self.setup_bot())

    

bot = MyBot()


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("Não tenho permissões suficientes!")

    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Você não tem permissões para usar este comando.')


# TESTE V2.0
# comando slash
@bot.tree.command(name="testslash")
@app_commands.guilds(900524034356285471) # registrar comando de barra apenas pra servidores especificos
async def testslash(interaction: discord.Interaction):
    # interaction.user = interaction.author
    await interaction.response.send_message("blablabla", ephemeral=True)

@bot.tree.command(name="a", description="a")
@app_commands.guilds()
async def a(interaction: discord.Interaction):
    await interaction.response.send_message('aaa')  

# hora class 
class Hora():
    def __init__(self):
        pass

    def hours(self):
        data = datetime.now()
        diferenca = timedelta(hours=-3)
        fuso_horario = timezone(diferenca)
        hora = data.astimezone(fuso_horario)
        hora_sp = hora.strftime('%H:%M')
        return hora_sp  





@bot.hybrid_command(name="avatar", description="(🔍) Veja o avatar de um usuário!")
@app_commands.guilds(900524034356285471)
async def avatar(ctx, membro: discord.Member = None):
    if not membro:
        membro = ctx.author

    view = buttons_all.button_avatar_user()
    view.add_item(discord.ui.Button(label="Download Avatar", style=discord.ButtonStyle.primary, url=f"{membro.display_avatar}", emoji="<:download:976292381324374016>"))

    embed = discord.Embed(description=f"**<:modopaisagem:966163112212447354> `Avatar de:` {membro.mention}**", color=0x6508ab)
    embed.set_image(url=f"{membro.display_avatar}")
    await ctx.send(ctx.author.mention, embed=embed, view=view)

@avatar.error
async def on_command_error(ctx, error):
    embed = discord.Embed(description=f"*Este usuário não foi encontrado! Por favor, verifique-se se o usuário esta no servidor!*", color=0x6508ab)
    await  ctx.send(ctx.author.mention, embed=embed, ephemeral=True)



# comando hibrido (slash e prefixed command)
@bot.hybrid_command(name="say", description="Mande mensagem através de mim.")
@app_commands.guilds(900524034356285471)
#@app_commands.describe(mensagem="") # descrever o argumento msg
async def say(ctx, *, mensagem: str):
    #await ctx.defer(ephemeral=True)
    # await asyncio.sleep(4) 
    #await ctx.send(content=msg)
    await ctx.send(f"{mensagem}\n\n\n*🤖 Mensagem enviada por: {ctx.author.mention}*")
    # await reaction.add_reaction('⚠️')


class buttonPing(discord.ui.View):
    @discord.ui.button(label="Atualizar Ping", style=discord.ButtonStyle.primary, emoji="<:antenna:963446876496101437>")
    async def button_ping(self, interaction: discord.Interaction, button: discord.ui.Button):
        # edit_message | send_message
        latency_bot = f"{round(bot.latency * 1000)}ms"
        embed = discord.Embed(description=f"<:antenna:963446876496101437> *Minha latência é de:* `{latency_bot}`", color=0x6508ab)

        await interaction.response.edit_message(embed=embed)

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