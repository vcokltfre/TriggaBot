import discord
from discord.ext import commands

from dotenv import load_dotenv
import os
load_dotenv("./secrets/.env")

client = commands.bot(command_prefix="!")

extensions = [

]

for exten in extensions:
    try:
        client.load_extension(exten)
    except Exception as e:
        print(e)
    else:
        print(f"Loaded extension: {exten}")

client.run(os.environ["TOKEN"])