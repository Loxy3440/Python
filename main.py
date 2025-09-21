import discord
from discord.ext import commands
import os
import datetime
from dotenv import load_dotenv
import pytz
from keep_alive import keep_alive
import requests
import asyncio

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
    total_users = sum(len(g.members) for g in bot.guilds)
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, 
        name=f"Loxy's Dev | !help"
    ))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("<a:Wrong:1415383907049672794> Bu komut bulunamadı! Lütfen geçerli bir komut girin.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<a:Wrong:1415383907049672794> Eksik argüman! Lütfen tüm gerekli argümanları sağlayın.")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("<a:Wrong:1415383907049672794>> Bu komutu kullanmak için gerekli izne sahip değilsiniz.")
    else:
        await ctx.send("<a:Wrong:1415383907049672794> Bir hata oluştu. Lütfen daha sonra tekrar deneyin.")
        raise error

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return

    # AFK system
    if message.author.id in bot.afk_users:
        reason = bot.afk_users.pop(message.author.id)
        await message.channel.send(f"Hoşgeldin {message.author.mention}, **AFK** modundan çıktı! <a:1000045246:1415457313342357616> ")

    # Check if any mentioned users are AFK
    for user in message.mentions:
        if user.id in bot.afk_users:
            reason = bot.afk_users[user.id]
            await message.channel.send(f"{user.name} şu anda <:9225afk:1418323034971832521> **AFK!** Sebep: **{reason}**    <:Cat:1415447386632880139> ")

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    turkey_tz = pytz.timezone('Europe/Istanbul')
    turkey_time = datetime.datetime.now(turkey_tz)

    embed = discord.Embed(
        title="Python",
        description=f" <a:Wifi:1415437265915871295> **Latency**: {round(bot.latency * 1000)}ms <a:Wifi:1415437265915871295>",
        color=0x216bff,
        timestamp=turkey_time
    )
    embed.add_field(name=" <a:owner:1415434012419424458> Founder <a:owner:1415434012419424458>", value="**Loxy**", inline=False,)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1413561809771692239/1413610825075261480/python-logo.png?ex=68bc8f2c&is=68bb3dac&hm=7e806c6f781e42a2fda97343ffc030b890d341c81b446ce091ee3541758fc5aa&")
    embed.add_field(name="Library", value="py-cord", inline=True)
    embed.add_field(name="Version", value="**3.11.9**", inline=True)
    embed.add_field(name="Language", value="<:1000045010:1415431159130620024>", inline=True)
    embed.add_field(name="Hosted on", value="Render", inline=True)
    embed.add_field(name="My Prefix", value="**!**", inline=True)
    embed.add_field(name="<a:1000045251:1415465673995456653> Developer <a:1000045251:1415465673995456653> ", value=" **Loxy**", inline=False)
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def deneme(ctx):
    await ctx.send("<a:1000045039:1415459602656657429> __TEST AŞAMASINDA__. **MERAK ETTİĞİN BİR ŞEY VARSA <@950430488454127627> BU HESABA SORABİLİRSİN** <a:Hearts:1415383408208511158> <a:1000045256:1415471089290707094> ")

@bot.command()
async def nah(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1415027311807299695/1418297339600306237/Screenshot_20250816-130442.jpg?ex=68cd9bd4&is=68cc4a54&hm=4771d8e64ff7b7461be75d50c6d8e4078a3d8268e2901cf74107fcae527c3675&")

@bot.command()
async def help(ctx):
    turkey_tz = pytz.timezone('Europe/Istanbul')
    turkey_time = datetime.datetime.now(turkey_tz)

    embed = discord.Embed(
        title="<:12895early:1418321924068606034> Help",
        description="Write **!helptr** or **!helpen**",
        timestamp=turkey_time,
        color=0xff0000
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1413561809771692239/1413992512917606514/python-logo.png?ex=68bfece5&is=68be9b65&hm=139dcd1ededf39864526676613c0b09ff3d71f4d418343a13d6575e62d420ea2&")
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def helptr(ctx):
    turkey_tz = pytz.timezone('Europe/Istanbul')
    turkey_time = datetime.datetime.now(turkey_tz)

    embed = discord.Embed(
        title="Help Menüsü",
        description=
        """ **Türkçe Komutlar Gösteriliyor. <a:8480peepoturkey:1418323342896664718>**
        
        ** <a:PartyZoom:1417218088897744936> ``Troll Komutlar``**
        > **!haddinibil** **---** __Haddini Bileceksin!__
        > **!nah** **---** __NAH!__
        > **!ahmetkaya** **---** __Ahmet Stone__
        > **!deneme** **---** __DENEME!__
        # -# <a:1384273237034401927:1415674228857897021> **DEVAMI YAKINDA**
        ** <a:1000045251:1415465673995456653> `Developer Komutları`**
        > **!dev `OR` !developer**
        > **!restart** **---** __Bota Restart Atar__
        > **!close** **---** __Botu Kapatır__
        # -# <a:1384273237034401927:1415674228857897021> **DEVAMI YAKINDA**
        ** <a:1347108314454167583:1415674138563186738> ``Yardımcı Komutlar``**
        > **!afk {Reason}** **---** __Seni Afk İlan Eder__
        > **!helptr** **--** <a:8480peepoturkey:1415710999910285413>
        > **!helpen** **--** <:99188flagusuk1:1419161283051261972>
        > **!pythontr** **--** __Python İle İlgili Kaynaklar Sunar__(<a:8480peepoturkey:1418323342896664718>)
        > **!pythonen** **--**__Python İle İlgili Kaynaklar Sunar__(<:99188flagusuk1:1419161283051261972>)
        # -# <a:1384273237034401927:1415674228857897021> **DEVAMI YAKINDA**
        """,
        timestamp=turkey_time,
        color=0xff0000
    )
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1413561809771692239/1419163052259151933/26210-owner.gif?ex=68d0c216&is=68cf7096&hm=8eb7e7456c6dab67c14ee242cef6f6b4a4c7b1b1f1a599e59e1e9e2732a78024&")
    await ctx.send(embed=embed)

@bot.command()
async def suicide(ctx):
    await ctx.send(f"{ctx.author.mention} <a:97128gun:1418321959078465597>")

@bot.command()
async def pythontr(ctx):
    turkey_tz = pytz.timezone('Europe/Istanbul')
    turkey_time = datetime.datetime.now(turkey_tz)

    embed = discord.Embed(
        title="<:1000045010:1415431159130620024> Python",
        description="Python öğrenmek için aşağıdaki butonları kullanabilirsiniz!",
        color=0xcc0000,
        timestamp=turkey_time
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1413561809771692239/1413992512917606514/python-logo.png?ex=68bfece5&is=68be9b65&hm=139dcd1ededf39864526676613c0b09ff3d71f4d418343a13d6575e62d420ea2&")
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Video#1", url="https://youtu.be/_wZUNiGtkcw?si=eL_ybYhg_v5w6TqA", emoji="<:1000045047:1415448594621796352>", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#2", url="https://youtu.be/CEr_UiR4Gvk?si=rzu8yYYvu5THBFEt", emoji="<:1000045047:1415448594621796352>", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#3", url="https://youtu.be/g4oIzj8fiCQ?si=i437FCMJqtVlff4Y", emoji="<:1000045047:1415448594621796352>", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#4", url="https://youtu.be/0KQp2v5vrV8?si=XpNLHmspKkTtInb8", emoji="<:1000045047:1415448594621796352>", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#5", url="https://youtu.be/g4oIzj8fiCQ?si=N4qzik7l1U_sYd8D", emoji="<:1000045047:1415448594621796352>", style=discord.ButtonStyle.red))
    await ctx.send(embed=embed, view=view)

@bot.command()
async def pythonen(ctx):
    turkey_tz = pytz.timezone('Europe/Istanbul')
    turkey_time = datetime.datetime.now(turkey_tz)
    
    embed = discord.Embed(
        title="<:1000045010:1415431159130620024> Python",
        description="To learn Python, you can use the buttons below!",
        color=0xcc0000,
        timestamp=turkey_time
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1413561809771692239/1413992512917606514/python-logo.png?ex=68bfece5&is=68be9b65&hm=139dcd1ededf39864526676613c0b09ff3d71f4d418343a13d6575e62d420ea2&")
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
    view = discord.ui.View()
    
    view.add_item(discord.ui.Button(label="Video#1", url="https://youtu.be/mB0EBW-vDSQ?si=hdIB3r6lO41mlrNb", emoji="<:1000045047:1415448594621796352>", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#2", url="https://youtu.be/St48epdRDZw?si=um7Q8epQ3SiaXlhL", emoji="<:1000045047:1415448594621796352>", style=discord.ButtonStyle.red))
    view.add_item(discord.ui.Button(label="Video#3", url="https://youtu.be/ix9cRaBkVe0?si=YI1XTQe7isDILW77", emoji="<:1000045047:1415448594621796352>", style=discord.ButtonStyle.red))
    await ctx.send(embed=embed, view=view)

@bot.command()
async def ahmetkaya(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1413561809771692239/1413623961190793347/Screenshot_20250816-170701.jpg?ex=68bc9b68&is=68bb49e8&hm=274cba55687980117d754d584566ee10db57fe59e92fb4c1b01a06b229a95837&")


# AFK System
@bot.command()
async def afk(ctx, *, reason=None):
    turkey_tz = pytz.timezone('Europe/Istanbul')
    turkey_time = datetime.datetime.now(turkey_tz)
    bot.afk_users[ctx.author.id] = reason or "AFK"
    embed = discord.Embed(
        title="<a:afk:1415383493613064303> AFK Mode",
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
    await ctx.send("<a:discordloading:1415383563154620436> Bot yeniden başlatılıyor...")
    await notify_owner(" <a:owner:1415434012419424458> Bot Başarıyla Yeniden Başlatıldı.")

@bot.command()
async def haddinibil(ctx):
    await ctx.send("https://tenor.com/view/rte-receptayyip-erdo%C4%9Fan-haddinibil-rtehaddinibil-gif-21346531")


@bot.command()
async def notify_owner(ctx, message):
    owner_id = int(os.getenv('OWNER'))
    owner = await bot.fetch_user(owner_id)
    if owner:
        await owner.send(f"<:xd:1415440381146955966>: {message}")


@bot.command()
async def dev(ctx):
    owner_id = int(os.getenv('OWNER'))
    owner = await bot.fetch_user(owner_id)
    if owner:
        await ctx.send(f"<a:1000045251:1415465673995456653> **Bot sahibi:** {owner.mention}")
    else:
        await ctx.send("<a:Wrong:1415383907049672794> Bot sahibi bulunamadı.")

@bot.command()
async def developer(ctx):
    owner_id = int(os.getenv('OWNER'))
    owner = await bot.fetch_user(owner_id)
    if owner:
        await ctx.send(f"<a:1000045251:1415465673995456653> **Bot sahibi:** {owner.mention}")
    else:
        await ctx.send("<a:Wrong:1415383907049672794> Bot sahibi bulunamadı.")

@bot.command()
async def close(ctx):
    turkey_tz = pytz.timezone('Europe/Istanbul')
    turkey_time = datetime.datetime.now(turkey_tz)
    owner_id = int(os.getenv('OWNER'))
    
    embed = discord.Embed(
        title="Bot Kapatılıyor <a:Verified22:1415383341586317433> ",
        description="<a:Mybest:1415383385735696596> Bot Kapatıldı!",
        timestamp=turkey_time,
        color=0xff0000
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1413561809771692239/1413992512917606514/python-logo.png?ex=68bfece5&is=68be9b65&hm=139dcd1ededf39864526676613c0b09ff3d71f4d418343a13d6575e62d420ea2&")
    embed.set_footer(text=f"{ctx.author.name}", icon_url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)
    if ctx.author.id == owner_id:
        await ctx.send(embed=embed)
        await notify_owner(ctx, "<a:owner:1415434012419424458> Başarıyla Bot Kapandı, **Lütfen Tekrar Renderdan Açmayı Unutma!**")
        await bot.close()

    else:
        await ctx.send("<a:Wrong:1415383907049672794> Bu komutu sadece bot sahibi kullanabilir.")
        await notify_owner(ctx, "<a:owner:1415434012419424458> Kapatma komutu yetkisiz bir kullanıcı tarafından denendi. <a:9596wrong:1415369131301142548>")

        
# .env dosyasından TOKEN değişkenini oku
token = os.getenv('TOKEN')
if not token:
    print("HATA: .env dosyasında TOKEN bulunamadı!")
    print("Lütfen .env dosyanızı kontrol edin:")
    print("TOKEN=bot_tokeniniz_buraya")
    print("owner=950430488454127627")
    exit(1)

bot.run(token)
