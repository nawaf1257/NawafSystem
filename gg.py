import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# روماتك عدلها
ROOM_RATE_PEOPLE = 1443123217790144623
ROOM_SUGGESTIONS = 1443913955910094848
ROOM_TICKET_RATE = 1443159868881244295


@bot.event
async def on_ready():
    print(f"Bot logged as {bot.user}")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content
    author = message.author

    # -------------------------------------------------------------
    # 1️⃣ روم تقييم الأشخاص — Embed أزرق
    # -------------------------------------------------------------
    if message.channel.id == ROOM_RATE_PEOPLE:

        if message.mentions:
            target = message.mentions[0]
            text = content.replace(target.mention, "").strip()
        else:
            await message.delete()
            await message.channel.send("⚠️ لازم تكتب منشن الشخص + رأيك فيه.")
            return

        await message.delete()

        embed = discord.Embed(
            title="📌 تقييم جديد",
            description=f"💬 **{text}**",
            color=0x3498db
        )

        embed.add_field(name="👤 المقيّم", value=author.mention, inline=True)
        embed.add_field(name="🎯 المقيّم له", value=target.mention, inline=True)
        embed.set_footer(text="Nawaf")

        sent = await message.channel.send(embed=embed)
        await sent.add_reaction("👍")
        await sent.add_reaction("👎")
        return

    # -------------------------------------------------------------
    # 2️⃣ روم الاقتراحات — Embed أصفر
    # -------------------------------------------------------------
    if message.channel.id == ROOM_SUGGESTIONS:

        await message.delete()

        embed = discord.Embed(
            title="💡 اقتراح جديد",
            description=f"**{content}**",
            color=0xf1c40f
        )

        embed.add_field(name="👤 المرسل", value=author.mention, inline=False)
        embed.set_footer(text="Nawaf")

        sent = await message.channel.send(embed=embed)
        await sent.add_reaction("👍")
        await sent.add_reaction("👎")
        return

    # -------------------------------------------------------------
    # 3️⃣ روم تقييم التذكرة — Embed أخضر
    # -------------------------------------------------------------
    if message.channel.id == ROOM_TICKET_RATE:

        await message.delete()

        embed = discord.Embed(
            title="🎟️ تقييم تذكرة",
            description=f"**{content}**",
            color=0x2ecc71
        )

        embed.add_field(name="👤 المستخدم", value=author.mention, inline=False)
        embed.set_footer(text="Nawaf")

        sent = await message.channel.send(embed=embed)
        await sent.add_reaction("👍")
        await sent.add_reaction("👎")
        return

    await bot.process_commands(message)


bot.run(TOKEN)
