import os
import discord
from discord import Member
from discord.utils import get
import random
import asyncio
import time
from discord.ext import commands, tasks
from random import choice
from webserver import keep_alive
import random
from random import randint


token = os.environ['token']
client = commands.Bot(command_prefix="£", intents=discord.Intents.all())
client.remove_command("help")




@client.event
async def on_ready():
	print("Bot is online and ready to serve!")
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f" £help"))



@client.command()
async def status(ctx):
    em = discord.Embed(title="Advertising & Community Bot is online!", colour=discord.Colour.purple())
    #em.set_footer(text=f"Time Occured: {curr_time}")
    await ctx.reply(embed=em, mention_author=False)
@client.command()
async def hello(ctx):
	bot = client.get_user(964509286699004007)
	dev = client.get_user(723569355710922802)
	member = ctx.author
	file = discord.File("happy-clap.gif")
	
	em = discord.Embed(title="👋",description=f"Hello there {member.mention}, I'm {bot.mention}, here to keep you safe in The Legion of Danks\nI was programmed by {dev.mention}", colour=discord.Colour.green())
    #em.set_footer(text=f"Time Occured: {curr_time}")
	em.set_image(url="attachment://happy-clap.gif")
	await ctx.reply(embed=em, file=file,mention_author=False)

@client.command()
async def help(ctx):
    em = discord.Embed(title="Help", description="Find the docs at <link-here>\nIf you find a bug with this bot, please create an error on the GitHub Repository (https://github.com/sam-march/Legion-Bot/issues)", colour=discord.Colour.green())
    #em.set_footer(text=f"Time Occured: {curr_time}")
    await ctx.reply(embed=em, mention_author=False)

@client.command()
async def docs(ctx):
    em = discord.Embed(title="Docs", description="Find the docs at <link-here>\nIf you find a bug with this bot, please create an error on the GitHub Repository (https://github.com/sam-march/Legion-Bot/issues)", colour=discord.Colour.green())
    #em.set_footer(text=f"Time Occured: {curr_time}")
    await ctx.reply(embed=em, mention_author=False)

@client.command()
async def ping(ctx):
	before = time.monotonic()
	em = discord.Embed(title="Latency Test", description=f"**Please Hold ... Working**", colour=discord.Colour.green())
	msg = await ctx.reply(embed=em, mention_author = False)
	ping = (time.monotonic() - before) * 1000
	em = discord.Embed(title="Ping", description=f"Latency: `{ping}ms`", colour=discord.Colour.green())
	await msg.edit(embed=em)

@client.command()
async def github(ctx):
	dev = client.get_user(723569355710922802)
	em = discord.Embed(title="Github Source Code", description=f"Find the source code for this bot, written by {dev.mention} at https://github.com/sam-march/Legion-Bot", colour=discord.Colour.green())
	await ctx.reply(embed=em, mention_author=False)


@client.command()
async def version(ctx):
	em = discord.Embed(title="Versions", description="Python:\n`3.8.12`\ndiscord.py:\n`Development Version`" , colour=discord.Colour.green())
	await ctx.reply(embed=em, mention_author=False)

@client.command()
async def dev(ctx):
	dev = client.get_user(723569355710922802)
	em = discord.Embed(title="About Developer", description=f"This bot was developed by {dev.mention}. If you wish to get in contact, do DM him", colour=discord.Colour.green())
	await ctx.reply(embed=em, mention_author=False)
@client.command()
async def about(ctx):
	dev = client.get_user(723569355710922802)
	em = discord.Embed(title="About Bot", description=f"I was developed by {dev.mention}, and I joined on the <t:1649429470:d>", colour=discord.Colour.green())
	await ctx.reply(embed=em, mention_author=False)
@client.command()
async def timestamp(ctx):
	dev = client.get_user(723569355710922802)
	em = discord.Embed(title="Timestamp Generator", description=f"We all know how hard discord timestamps are to write, so follow this handy link to quickly create them without the faff\nhttps://bchaing.github.io/discord-timestamp/", colour=discord.Colour.green())
	await ctx.reply(embed=em, mention_author=False)
@client.command()
async def invite(ctx):
	dev = client.get_user(723569355710922802)
	em = discord.Embed(title="Invite Bot", description=f"Unfortunately, you can't invite the bot, but if you want, DM {dev.mention}, as if he's free, he may make you a bot.", colour=discord.Colour.green())
	await ctx.reply(embed=em, mention_author=False)
@client.command()
async def rules(ctx):

	em = discord.Embed(title="Server Rules", description=f"Rules Coming Soon", colour=discord.Colour.green())
	await ctx.reply(embed=em, mention_author=False)

@client.command()
async def rps(ctx, choice=None):
	if choice==None:
		await ctx.reply("> You need to enter either `rock`, `paper` or `scissors` to play! Try again.", mention_author=False)
	else:
		bot_choice = random.randint(1,3)
		if bot_choice == 1:
			bot_choice = "rock"
		elif bot_choice == 2:
			bot_choice = "paper"
		elif bot_choice == 3:
			bot_choice = "scissors"
		else:
			await ctx.reply("> Oops, I messed up. Please try again", mention_author=False)
		choice = choice.lower()
		if choice == "rock":
			if bot_choice == "scissors":
				await ctx.reply("> You win, I chose scissors (✂️)", mention_author=False)
			elif bot_choice == "paper":
				await ctx.reply("> I win, I chose paper (📄)", mention_author=False)
			elif bot_choice == "rock":
				await ctx.reply("> Nobody won, we both chose rock (🪨)", mention_author=False)
		elif choice == "paper":
			if bot_choice == "scissors":
				await ctx.reply("> I win, I chose scissors (✂️)", mention_author=False)
			elif bot_choice == "paper":
				await ctx.reply("> Nobody won, we both chose paper (📄)", mention_author=False)
			elif bot_choice == "rock":
				await ctx.reply("> You win, I chose rock (🪨)", mention_author=False)
		elif choice == "scissors":
			if bot_choice == "scissors":
				await ctx.reply("> Nobody won, we both chose scissors (✂️)", mention_author=False)
			elif bot_choice == "paper":
				await ctx.reply("> You win, I chose paper (📄)", mention_author=False)
			elif bot_choice == "rock":
				await ctx.reply("> I win, I chose rock (🪨)", mention_author=False)
		else:
			await ctx.reply(f"> {choice}, really? You didn't enter `rock`, `paper` or `scissors`. Do you know how to play?", mention_author=False)


@client.command(aliases = ['gg', 'hl'])
async def guessing_game(ctx):
	bot_number= random.randint(1,100)
	bot_number2 = random.randint(1,100)
	if bot_number2 > bot_number:
		answer = "⬇️"
	elif bot_number2 < bot_number:
		answer = "⬆️"
	elif bot_number2 == bot_number:
		answer = "🤑"
	else:
		await ctx.reply(f">>> Oops, I messed up, please try again", mention_author=False)
	msg = await ctx.reply(f">>> Your hint is `{bot_number2}`. Do you think that the number is higher (⬆️), lower (⬇️), or the same as `{bot_number2}` (🤑)?", mention_author=False)
	await msg.add_reaction("⬆️")
	await msg.add_reaction("⬇️")
	await msg.add_reaction("🤑")
	def check(reaction, user):
		return user == ctx.message.author and str(reaction.emoji) in ['⬆️', '⬇️', '🤑']
	try:
		reaction, user = await client.wait_for('reaction_add', timeout=10, check=check)
		if reaction.emoji == '⬆️':
			if answer == '⬆️':
				await msg.edit(content=f"> Correct, how did you get that? The number I chose was {bot_number}")
			elif answer == '🤑':
				await msg.edit(content=f"> Wrong, good try. The number I chose was {bot_number}")
			elif answer == '⬇️':
				await msg.edit(content=f"> Wrong, good try. The number I chose was {bot_number}")
			else:
				await msg.edit(content="Oops, I messed up. Please try again")
		elif reaction.emoji == '⬇️':
			if answer == '⬆️':
				await msg.edit(content=f"> Wrong, good try. The number I chose was {bot_number}")
			elif answer == '🤑':
				await msg.edit(content=f"> Wrong, good try. The number I chose was {bot_number}")
			elif answer == '⬇️':
				await msg.edit(content=f"> Correct, how did you get that? The number I chose was {bot_number}")
			else:
				await msg.edit(content="Oops, I messed up. Please try again")
		elif reaction.emoji == '🤑':
			if answer == '⬆️':
				await msg.edit(content=f"> Wrong, good try. The number I chose was {bot_number}")
			elif answer == '🤑':
				await msg.edit(content=f"> Correct, how did you get that? The number I chose was {bot_number}")
			elif answer == '⬇️':
				await msg.edit(content=f"> Wrong, good try. The number I chose was {bot_number}")
			else:
				await msg.edit(content="Oops, I messed up. Please try again")
		else:
			await msg.edit(content="Oops, I messed up. Please try again")
	except asyncio.TimeoutError:
		await msg.edit(content="Timed out")

@client.command()
async def suggestion(ctx, *, suggestion=None):
	if suggestion==None:
		await ctx.reply("> You've got no ideas for me? To add a suggestion for a command to be added to the bot, type `£suggestion <suggestion>`. Now, I can get all your ideas", mention_author=False)
	else:
		await ctx.reply("> Thanks for your suggestion, we'll now add it to a staff poll to see if your command will be accepted.", mention_author=False)
		suggestions_channel = client.get_channel(965194070542667796)
		suggestions_channel2 = client.get_channel(965195879353049149)
		em = discord.Embed(title="Command Suggestion", description=f"{ctx.author.mention} just suggested a new command: ```{suggestion}```", colour=discord.Colour.green())
		msg1 = await suggestions_channel.send(embed=em)
		await suggestions_channel2.send(embed=em)
		await msg1.add_reaction('✅')
		await msg1.add_reaction('❌')

@




keep_alive()
client.run(token)