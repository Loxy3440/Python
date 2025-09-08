import discord
from discord.ext import commands
import os
import datetime
from dotenv import load_dotenv
import pytz
from keep_alive import keep_alive

keep_alive()

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

# Initialize afk_users as a bot attribute to ensure it persists
bot.afk_users = {}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Game(name="!help"))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Bu komut bulunamadı! Lütfen geçerli bir komut girin.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Eksik argüman! Lütfen tüm gerekli argümanları sağlayın.")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("Bu komutu kullanmak için gerekli izne sahip değilsiniz.")
    else:
        await ctx.send("Bir hata oluştu. Lütfen daha sonra tekrar deneyin.")
        raise error

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return

    # AFK system
    if message.author.id in bot.afk_users:
        reason = bot.afk_users.pop(message.author.id)
        await message.channel.send(f"Hoşgeldin {message.author.mention}, **AFK** modundan çıktı!")

    # Check if any mentioned users are AFK
    for user in message.mentions:
        if user.id in bot.afk_users:
            reason = bot.afk_users[user.id]
            await message.channel.send(f"{user.name} şu anda AFK! Sebep: {reason}")

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    utc_time = datetime.datetime.utcnow()
    turkey_time = utc_time + datetime.timedelta(hours=3)

    embed = discord.Embed(
        title="Python Bot",
        description=f"**Latency**: {round(bot.latency * 1000)}ms",
        color=0x216bff,
        timestamp=turkey_time
    )
    embed.add_field(name="Founder", value="Loxy", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1413561809771692239/1413610825075261480/python-logo.png?ex=68bc8f2c&is=68bb3dac&hm=7e806c6f781e42a2fda97343ffc030b890d341c81b446ce091ee3541758fc5aa&")
    embed.add_field(name="Library", value="py-cord", inline=True)
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def deneme(ctx):
    await ctx.send("__TEST AŞAMASINDA__. **MERAK ETTİĞİN BİR ŞEY VARSA <@950430488454127627> BU HESABA SORABİLİRSİN**")

@bot.command()
async def pythontr(ctx):
    embed = discord.Embed(
        title="Python",
        description="Python öğrenmek için aşağıdaki butonları kullanabilirsiniz!",
        color=0xcc0000,
        timestamp=datetime.datetime.utcnow() + datetime.timedelta(hours=3)
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1413561809771692239/1413992512917606514/python-logo.png?ex=68bfece5&is=68be9b65&hm=139dcd1ededf39864526676613c0b09ff3d71f4d418343a13d6575e62d420ea2&")
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Video#1", url="https://youtu.be/_wZUNiGtkcw?si=eL_ybYhg_v5w6TqA", emoji="📹", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#2", url="https://youtu.be/CEr_UiR4Gvk?si=rzu8yYYvu5THBFEt", emoji="📹", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#3", url="https://youtu.be/g4oIzj8fiCQ?si=i437FCMJqtVlff4Y", emoji="📹", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#4", url="https://youtu.be/0KQp2v5vrV8?si=XpNLHmspKkTtInb8", emoji="📹", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#5", url="https://youtu.be/g4oIzj8fiCQ?si=N4qzik7l1U_sYd8D", emoji="📹", style=discord.ButtonStyle.red))
    await ctx.send(embed=embed, view=view)

@bot.command()
async def pythonen(ctx):
    embed = discord.Embed(
        title="Python",
        description="To learn Python, you can use the buttons below!",
        color=0xcc0000,
        timestamp=datetime.datetime.utcnow() + datetime.timedelta(hours=3)
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1413561809771692239/1413992512917606514/python-logo.png?ex=68bfece5&is=68be9b65&hm=139dcd1ededf39864526676613c0b09ff3d71f4d418343a13d6575e62d420ea2&")
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Video#1", url="https://youtu.be/mB0EBW-vDSQ?si=hdIB3r6lO41mlrNb", emoji="📹", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#2", url="https://youtu.be/St48epdRDZw?si=um7Q8epQ3SiaXlhL", emoji="📹", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#3", url="https://youtu.be/ix9cRaBkVe0?si=YI1XTQe7isDILW77", emoji="📹", style=discord.ButtonStyle.red))
    await ctx.send(embed=embed, view=view)

@bot.command()
async def ahmetkaya(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1413561809771692239/1413623961190793347/Screenshot_20250816-170701.jpg?ex=68bc9b68&is=68bb49e8&hm=274cba55687980117d754d584566ee10db57fe59e92fb4c1b01a06b229a95837&")

# AFK System
@bot.command()
async def afk(ctx, *, reason=None):
    bot.afk_users[ctx.author.id] = reason or "AFK"
    embed = discord.Embed(
        title="AFK Mode",
        description=f"{ctx.author.mention}, artık **AFK** modundasın!\n**Sebep:** {reason or 'Sebep belirtilmedi'}",
        color=0x216bff
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1413561809771692239/1413992512917606514/python-logo.png?ex=68bfece5&is=68be9b65&hm=139dcd1ededf39864526676613c0b09ff3d71f4d418343a13d6575e62d420ea2&")
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def haddinibil(ctx):
    await ctx.send("https://tenor.com/view/rte-receptayyip-erdo%C4%9Fan-haddinibil-rtehaddinibil-gif-21346531")

@bot.command()
async def close(ctx):
    # .env'deki owner değişkenini kullan
    owner_id = int(os.getenv('owner'))  # .env'deki owner değişkenini oku
    if ctx.author.id == owner_id:
        embed = discord.Embed(
            title="Bot Kapatılıyor",
            description="Bot Kapatıldı",
            color=0xff0000
        )
        await ctx.send(embed=embed)
        await bot.close()
    else:
        await ctx.send("Bu komutu sadece bot sahibi kullanabilir!")

# .env dosyasından TOKEN değişkenini oku
token = os.getenv('TOKEN')
if not token:
    print("HATA: .env dosyasında TOKEN bulunamadı!")
    print("Lütfen .env dosyanızı kontrol edin:")
    print("TOKEN=bot_tokeniniz_buraya")
    print("owner=950430488454127627")
    exit(1)

bot.run(token)
