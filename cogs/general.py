import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(name="TriggaBot"))

    @commands.group(name="help")
    async def help(self, ctx):
        if ctx.invoked_subcommand == None:
            embed = discord.Embed(title="Help", description="Help Commands")
            embed.add_field(name="Help", value="Displays this help section.")
            await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(General(bot))