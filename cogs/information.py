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


class information(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@app_commands.command(name="introu", description="adf")
	async def introu(self, interaction: discord.Interaction, name: str):
		await interaction.response.send_message(f"a {name}")

	@app_commands.command(name="ab", description="adf")
	@app_commands.guilds(900524034356285471)
	async def ab(self, interaction: discord.Interaction, membro: discord.Member = None):
	    if not membro:
	        membro = interaction.user

	    view = buttons_all.button_avatar_user()
	    view.add_item(discord.ui.Button(label="Download Avatar", style=discord.ButtonStyle.primary, url=f"{membro.display_avatar}", emoji="<:download:976292381324374016>"))

	    embed = discord.Embed(description=f"**<:modopaisagem:966163112212447354> `Avatar de:` {membro.mention}**", color=0x6508ab)
	    embed.set_image(url=f"{membro.display_avatar}")
	    await interaction.response.send_message(interaction.user.mention, embed=embed, view=view)

async def setup(bot: commands.Bot):
	await bot.add_cog(information(bot))