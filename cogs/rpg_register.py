import asyncio
from config.config_buttons import buttons_all
from config.config_rpg import class_config_rpg
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
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageOps



class Rpg(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@app_commands.command(name="raca", description="(RPG) Escolha uma raça para poder joga!")
	async def raca(self, interaction: discord.Interaction):
		login_user = class_config_rpg.verfy_player_mika(interaction.user.id)
		view = buttons_all.button_raca()

		if login_user.verify_player() == False:
			embed = discord.Embed(title="Raça's", description="Você só pode escolher 4 tipos de raças! Clique em uns dos bottons abiaxo para escolher a sua!", color=0x6508ab)

			await interaction.response.send_message(interaction.user.mention, embed=embed, ephemeral=True, view=view)
		else:
			embed = discord.Embed(description=f"✅ | *Olá! Você já escolheu raça `{login_user.player_raca()}`*\n",  color=0x6508ab)
			await interaction.response.send_message(interaction.user.mention, embed=embed, ephemeral=True)
			print()
	        	

async def setup(bot: commands.Bot):
	await bot.add_cog(Rpg(bot))