import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

ADMIN_RATE = 1443123217790144623
SUGGESTIONS = 1443913955910094848
TICKET_RATE = 1443159868881244295

@bot.event
async def on_ready():
    print(f"{bot.user} شغال!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    channel = message.channel.id
    content = message.content
    author = message.author

    if channel == ADMIN_RATE:
        await message.delete()
        embed = discord.Embed(
            title="📌 تقييم إداري",
            description=f"**{content}**",
            color=discord.Color.dark_purple()
        )
        embed.set_footer(text="NawafSystem")

        msg = await message.channel.send(
            content=f"📝 | تقييم جديد من {author.mention}",
            embed=embed
        )
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
        return

    if channel == SUGGESTIONS:
        await message.delete()
        embed = discord.Embed(
            title="💡 اقتراح جديد",
            description=f"**{content}**",
            color=discord.Color.dark_theme()
        )
        embed.set_footer(text="NawafSystem")

        msg = await message.channel.send(
            content=f"✨ | اقتراح مقدم من {author.mention}",
            embed=embed
        )
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
        return

    if channel == TICKET_RATE:
        await message.delete()
        embed = discord.Embed(
            title="🎟️ تقييم تذكرة",
            description=f"**{content}**",
            color=discord.Color.purple()
        )
        embed.set_footer(text="NawafSystem")

        msg = await message.channel.send(
            content=f"📨 | تقييم من {author.mention}",
            embed=embed
        )
        await msg.add_reaction("⭐")
        await msg.add_reaction("💜")
        return

    await bot.process_commands(message)

bot.run(os.getenv("TOKEN"))
