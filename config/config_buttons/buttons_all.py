import asyncio
import discord
from discord import app_commands
from discord.ext import commands
from discord.interactions import Interaction
from discord.ui import button, View, Button
import random
import json
import os
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageOps

class button_raca(discord.ui.View):
    @discord.ui.button(label="Tiefling", style=discord.ButtonStyle.primary, emoji="<:antenna:963446876496101437>")
    async def button_tiefling(self, interaction: discord.Interaction, button: discord.ui.Button):
        # edit_message | send_message
       
        embed = discord.Embed(description=f"você escolheu a raça Tiefling!", color=0x6508ab)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="humano", style=discord.ButtonStyle.primary, emoji="<:antenna:963446876496101437>")
    async def button_humano(self, interaction: discord.Interaction, button: discord.ui.Button):
        # edit_message | send_message
       
        embed = discord.Embed(description=f"você escolheu a raça humano!", color=0x6508ab)
        await interaction.response.edit_message(embed=embed)

        
class button_avatar_user(discord.ui.View):
    pass