import discord, asyncio, sqlite3

from keys import tok
from discord.ext import commands
from dbcontrol import showrep, addrep, adm_addrep, adm_remrep, edit_bio, show_bio
from showimage import create_image

bot = commands.Bot(command_prefix="+")

@bot.command()
async def show(ctx, user : discord.Member = None):
    if user == None:
        rep = showrep(ctx.author.id)
        bio = show_bio(ctx.author.id)
        create_image(ctx.author.avatar_url, rep, ctx.author.display_name, bio)
        await ctx.send(file=discord.File('result.png'))
    else:
        rep = showrep(user.id)
        bio = show_bio(ctx.author.id)
        create_image(user.avatar_url, rep, user.display_name, bio)
        await ctx.send(file=discord.File('result.png'))

@bot.command()
async def rep(ctx, user: discord.Member=None):
    if user == None:
        rep = showrep(ctx.author.id)
        bio = show_bio(ctx.author.id)
        create_image(ctx.author.avatar_url, rep, ctx.author.display_name, bio)
        await ctx.send(file=discord.File('result.png'))   
    elif user.id == ctx.author.id:
        await ctx.send("You can't rep yourself!")
    else:
        await ctx.send(addrep(user.id, ctx.author.id))

@bot.command(pass_context=True)
@commands.has_any_role("r/chungus")
async def adrep(ctx, user: discord.Member=None, amount : int=0):
    if user == None or amount == 0:
        await ctx.send("Error!")
    else:
        await ctx.send(adm_addrep(user.id, amount))

@bot.command(pass_context=True)
@commands.has_any_role("r/chungus")
async def remrep(ctx, user: discord.Member=None, amount : int=0):
    if user == None or amount == 0:
        await ctx.send("Error!")
    else:
        await ctx.send(adm_remrep(user.id, amount))

@bot.command(pass_context=True)
async def bio(ctx, *bio):
    t = " ".join(bio)
    await ctx.send(edit_bio(ctx.author.id, t))

conn = sqlite3.connect('data.db')
global c
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS rep (userID int, reps int, repers text)")
c.execute("CREATE TABLE IF NOT EXISTS bios (userID int, bio text)")

bot.run(tok)