import discord
from discord.ext import commands
import os
import datetime
from dotenv import load_dotenv
import pytz
from keep_alive import keep_alive
import requests

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
        await ctx.send("<a:9596wrong:1415369131301142548> Bu komut bulunamadı! Lütfen geçerli bir komut girin.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<a:9596wrong:1415369131301142548> Eksik argüman! Lütfen tüm gerekli argümanları sağlayın.")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("<a:9596wrong:1415369131301142548> Bu komutu kullanmak için gerekli izne sahip değilsiniz.")
    else:
        await ctx.send("<a:9596wrong:1415369131301142548> Bir hata oluştu. Lütfen daha sonra tekrar deneyin.")
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
            await message.channel.send(f"{user.name} şu anda <a:2290zzzsleepy:1415352435827802122> **afk!** Sebep: **{reason}**")

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    utc_time = datetime.datetime.utcnow()
    turkey_time = utc_time + datetime.timedelta(hours=3)

    embed = discord.Embed(
        title="Python Bot",
        description=f" **Latency**: {round(bot.latency * 1000)}ms <:6292goodconnection:1415371028657471601>",
        color=0x216bff,
        timestamp=turkey_time
    )
    embed.add_field(name="Founder", value="Loxy", inline=False,)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1413561809771692239/1413610825075261480/python-logo.png?ex=68bc8f2c&is=68bb3dac&hm=7e806c6f781e42a2fda97343ffc030b890d341c81b446ce091ee3541758fc5aa&")
    embed.add_field(name="Library", value="py-cord", inline=True)
    embed.add_field(name="Version", value="3.11.9", inline=True)
    embed.add_field(name="Language", value="<:64443python:1415364319109185689> Python", inline=True)
    embed.add_field(name="Hosted on", value="Render", inline=True)
    embed.add_field(name="My Prefix", value="**!**", inline=True)
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def deneme(ctx):
    await ctx.send("<:1000045006:1415428165752324370> __TEST AŞAMASINDA__. **MERAK ETTİĞİN BİR ŞEY VARSA <@950430488454127627> BU HESABA SORABİLİRSİN** <:8484hearts:1415374810497941574> ")


@bot.command()
async def pythontr(ctx):
    utc_time = datetime.datetime.utcnow()
    turkey_time = utc_time + datetime.timedelta(hours=3)

    embed = discord.Embed(
        title="<:64443python:1415364319109185689> Python",
        description="Python öğrenmek için aşağıdaki butonları kullanabilirsiniz!",
        color=0xcc0000,
        timestamp=turkey_time
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1413561809771692239/1413992512917606514/python-logo.png?ex=68bfece5&is=68be9b65&hm=139dcd1ededf39864526676613c0b09ff3d71f4d418343a13d6575e62d420ea2&")
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Video#1", url="https://youtu.be/_wZUNiGtkcw?si=eL_ybYhg_v5w6TqA", emoji="<:youtube:1414975498467016764>", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#2", url="https://youtu.be/CEr_UiR4Gvk?si=rzu8yYYvu5THBFEt", emoji="<:youtube:1414975498467016764>", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#3", url="https://youtu.be/g4oIzj8fiCQ?si=i437FCMJqtVlff4Y", emoji="<:youtube:1414975498467016764>", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#4", url="https://youtu.be/0KQp2v5vrV8?si=XpNLHmspKkTtInb8", emoji="<:youtube:1414975498467016764>", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#5", url="https://youtu.be/g4oIzj8fiCQ?si=N4qzik7l1U_sYd8D", emoji="<:youtube:1414975498467016764>", style=discord.ButtonStyle.red))
    await ctx.send(embed=embed, view=view)

@bot.command()
async def pythonen(ctx):
    utc_time = datetime.datetime.utcnow()
    turkey_time = utc_time + datetime.timedelta(hours=3)
    
    embed = discord.Embed(
        title="<:64443python:1415364319109185689> Python",
        description="To learn Python, you can use the buttons below!",
        color=0xcc0000,
        timestamp=turkey_time
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1413561809771692239/1413992512917606514/python-logo.png?ex=68bfece5&is=68be9b65&hm=139dcd1ededf39864526676613c0b09ff3d71f4d418343a13d6575e62d420ea2&")
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
    view = discord.ui.View()
    
    view.add_item(discord.ui.Button(label="Video#1", url="https://youtu.be/mB0EBW-vDSQ?si=hdIB3r6lO41mlrNb", emoji="<:youtube:1414975498467016764>", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#2", url="https://youtu.be/St48epdRDZw?si=um7Q8epQ3SiaXlhL", emoji="<:youtube:1414975498467016764>", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#3", url="https://youtu.be/ix9cRaBkVe0?si=YI1XTQe7isDILW77", emoji="<:youtube:1414975498467016764>", style=discord.ButtonStyle.red))
    await ctx.send(embed=embed, view=view)

@bot.command()
async def ahmetkaya(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1413561809771692239/1413623961190793347/Screenshot_20250816-170701.jpg?ex=68bc9b68&is=68bb49e8&hm=274cba55687980117d754d584566ee10db57fe59e92fb4c1b01a06b229a95837&")





# AFK System
@bot.command()
async def afk(ctx, *, reason=None):
    utc_time = datetime.datetime.utcnow()
    turkey_time = utc_time + datetime.timedelta(hours=3)
    bot.afk_users[ctx.author.id] = reason or "AFK"
    embed = discord.Embed(
        title="<a:2290zzzsleepy:1415352435827802122> AFK Mode",
        description=f"{ctx.author.mention}, artık **AFK** modundasın!\n**Sebep:** {reason or 'Sebep belirtilmedi'}",
        color=0x216bff,
        timestamp=turkey_time
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1413561809771692239/1413992512917606514/python-logo.png?ex=68bfece5&is=68be9b65&hm=139dcd1ededf39864526676613c0b09ff3d71f4d418343a13d6575e62d420ea2&")
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
    await ctx.send(embed=embed)


import os
import requests
from discord.ext import commands

@bot.command()
@commands.is_owner()
async def restart(ctx):
    deploy_hook = os.getenv('RENDER_DEPLOY_HOOK')
    requests.post(deploy_hook)
    await ctx.send("<a:5985discordloading:1415364278524838021> Bot yeniden başlatılıyor...")

@bot.command()
async def haddinibil(ctx):
    await ctx.send("https://tenor.com/view/rte-receptayyip-erdo%C4%9Fan-haddinibil-rtehaddinibil-gif-21346531")


@bot.command()
async def notify_owner(ctx, message):
    owner_id = int(os.getenv('OWNER'))
    owner = await bot.fetch_user(owner_id)
    if owner:
        await owner.send(f"<:2633notification:1415379621402251426>: {message}")


@bot.command()
async def owner(ctx):
    owner_id = int(os.getenv('OWNER'))
    owner = await bot.fetch_user(owner_id)
    if owner:
        await ctx.send(f"<a:owner:1415352659552243833> Bot sahibi: {owner.mention}")
    else:
        await ctx.send("<a:9596wrong:1415369131301142548> Bot sahibi bulunamadı.")


@bot.command()
async def close(ctx):
    utc_time = datetime.datetime.utcnow()
    turkey_time = utc_time + datetime.timedelta(hours=3)
    owner_id = int(os.getenv('OWNER'))
    
    embed = discord.Embed(
        title="Bot Kapatılıyor",
        description="<a:3983_My_best_verified:1415374950763855953> Bot Kapatıldı!",
        timestamp=turkey_time,
        color=0xff0000
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1413561809771692239/1413992512917606514/python-logo.png?ex=68bfece5&is=68be9b65&hm=139dcd1ededf39864526676613c0b09ff3d71f4d418343a13d6575e62d420ea2&")
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
    if ctx.author.id == owner_id:
        await ctx.send(embed=embed)
        await bot.close()

    else:
        await ctx.send("<a:9596wrong:1415369131301142548> Bu komutu sadece bot sahibi kullanabilir.")
        await notify_owner(ctx, "<a:owner:1415352659552243833> Kapatma komutu yetkisiz bir kullanıcı tarafından denendi. <a:9596wrong:1415369131301142548>")

        
# .env dosyasından TOKEN değişkenini oku
token = os.getenv('TOKEN')
if not token:
    print("HATA: .env dosyasında TOKEN bulunamadı!")
    print("Lütfen .env dosyanızı kontrol edin:")
    print("TOKEN=bot_tokeniniz_buraya")
    print("owner=950430488454127627")
    exit(1)

bot.run(token)
