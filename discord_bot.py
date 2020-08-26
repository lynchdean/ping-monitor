# import discord
import yaml
from discord.ext import commands

from page_monitor import PageMonitor


def main():
    bot = commands.Bot(command_prefix='$')

    @bot.command()
    async def foot(ctx, arg):
        await ctx.send(arg)

    @bot.command()
    async def mon(ctx, url: str, wait: float):
        await ctx.send("Received.")
        pm = PageMonitor(url, int(wait))
        pm.wait_for_update()
        await ctx.send("Site Changed.")

    secrets = yaml.load(open('secrets.yaml'), Loader=yaml.FullLoader)
    bot.run(secrets["key"])


if __name__ == '__main__':
    main()
