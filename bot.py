import discord 
from discord.ext import commands 
import random
import json
import os 
import asyncio



intents = discord.Intents.default()

intents.members = True
client = commands.Bot(command_prefix='Prefix', intents = intents)








f = open("rules.txt","r")
rules = f.readlines()


filtered_words = ["fuck","nigga","FUCK","NIGGA","BITCH","bitch","semen","SEMEN","Fuck","Nigga","Bitch","Semen","COCK","cock","Cock"]

images = [ 
'https://i.redd.it/9h47cgnznja71.jpg',
'https://i.redd.it/1y87f4dx1ka71.png',
'https://i.redd.it/kmptok5s9na71.jpg',
'https://i.redd.it/7p05443qxja71.jpg',
'https://i.redd.it/29mm896cpla71.jpg',
'https://i.redd.it/ba0zmj6cuma71.jpg',
'https://i.redd.it/eiy1s0x3fma71.jpg',
'https://i.redd.it/f6skewuqqla71.png',
'https://i.redd.it/k1y2a23knna71.jpg',
'https://i.redd.it/j84k34qwmna71.jpg',
'https://i.redd.it/9b41zo1keia71.jpg',
'https://i.redd.it/76gbs21mika71.jpg',
'https://i.redd.it/qk1isrhrnna71.jpg',
'https://i.redd.it/nff04ufaaka71.png',
'https://i.redd.it/0g3639h68na71.jpg',
'https://tenor.com/view/coca-cola-coke-mentos-splash-explode-gif-16276207',
'https://i.redd.it/pvveth25jg271.png',
'https://i.redd.it/vpq1iwajni271.jpg',
'https://i.redd.it/2yybuj2alb071.jpg',
'https://i.redd.it/8eewgv2ub3071.gif',
'https://i.redd.it/9a7r9faxaqz61.gif',
'https://i.redd.it/zmygouf7vuz61.jpg',
'https://i.redd.it/253yuxxbunz61.png',
'https://i.redd.it/bqcq5arrdtz61.jpg',
'https://i.redd.it/p76w3lszviy61.jpg',
'https://i.redd.it/7fwkzp600my61.png',
'https://i.redd.it/4wj39f1xygy61.jpg',
'https://youtu.be/RcYDipyvNwE'
'https://cdn.discordapp.com/attachments/802073755455193089/839756699510505532/video1-6.mp4',
'https://cdn.discordapp.com/attachments/802073755455193089/819053632170229780/video0_-_2021-02-21T125822.998.mp4',
'https://cdn.discordapp.com/attachments/802073755455193089/819053570531262564/electrical_meme.mp4',
'https://cdn.discordapp.com/attachments/802073755455193089/819053546946953277/redditsave.com-shot_on_iphone-6boveuvdd9f61.mp4',
'https://i.redd.it/lfnu635s5gj61.jpg',
'https://i.redd.it/8l6pr7i6n1j61.png',
'https://i.redd.it/891akdjwc5j61.jpg',
'https://i.redd.it/e6kz1mnooui61.jpg',
'https://i.redd.it/o8w9b7o1svi61.jpg',
'https://i.redd.it/9d7xzu3ggxi61.png',
'https://i.redd.it/g7hcdie2tsj61.png',
'https://i.redd.it/yzxnkvyl8vi61.png',
'https://i.redd.it/r7d3qir1qxj61.png',
'https://i.redd.it/nh4viewniqj61.png',
'https://i.redd.it/stx4a9tb5ij61.jpg',
'https://i.imgur.com/IN8d11g.png',
'https://i.redd.it/5af05u0v7cj61.jpg'
'https://i.redd.it/t1klgfib0gj61.jpg',
'https://i.redd.it/5pd4nr5dwxi61.jpg',
'https://i.redd.it/pju57ktrlmj61.jpg',
'https://i.redd.it/6e10diwj28j61.jpg',
'https://i.redd.it/0ml7nkpdfqi61.jpg',
'https://i.redd.it/wn13meychwh61.jpg',
'https://i.redd.it/zg5zspeqihg61.jpg',
'https://i.redd.it/cmpwkxgn1fg61.gif',
'https://i.redd.it/1hfv565nzeg61.jpg',
'https://i.redd.it/ympkgtz9hfg61.jpg',
'https://i.redd.it/roet9wuiykg61.png',
'https://i.redd.it/kzinqpm3umg61.png',
'https://i.redd.it/dovk5umjcjg61.jpg',
'https://i.redd.it/1auwsq9rqlg61.jpg',
'https://i.redd.it/atzxr23nelg61.jpg',
'https://i.redd.it/v5bpvqi49ig61.jpg',
'https://cdn.discordapp.com/attachments/802073755455193089/808563735224123392/Screenshot_2021-01-13-11-00-45-1.png',
'https://i.redd.it/phgd5y29cnf61.jpg',
'https://i.imgur.com/Vazz4Oc.jpg',
'https://i.redd.it/b8s3lcy3rfe61.jpg',
'https://i.redd.it/mandjvv20ud61.jpg',
'https://i.redd.it/5l2u3hizssd61.jpg',
'https://i.redd.it/vlzchzhdvnd61.png',
'https://i.redd.it/zdkgx3nmxnd61.jpg',
'https://i.redd.it/yx20493kwhd61.jpg',
'https://i.redd.it/7492wmuq7sc61.jpg',
'https://i.redd.it/pm2xju7nulc61.jpg']


@client.event
async def on_ready():
	# Setting `Playing ` status
	await client.change_presence(status=discord.Status.idle, activity=discord.Game(name=f"On {len(client.guilds)} Servers | $help"))


	print('Logged in as', client.user)



	
	
snipe_message_content = None
snipe_message_author = None
	
	
@client.event
async def on_message_delete(message):
	global snipe_message_content
	global snipe_message_author
	
	
	snipe_message_content = message.content
	snipe_message_author = message.author.name
	await asyncio.sleep(60)
	snipe_message_author = None
	snipe_message_content = None
	
	
	
	
	
	
	
@client.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete() 

    await client.process_commands(msg)

	





@client.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.MissingPermissions):
		await ctx.send("Hey! Sorry but you don't have the permission to perform that command!")
		await ctx.message.delete()
	elif isinstance(error,commands.MissingRequiredArgument):
		await ctx.send("Pls enter all the required Arguments!")
		await ctx.message.delete()



		
		
@client.command(aliases=['Snipe','esnipe','Esnipe'])
async def snipe(message):
	if snipe_message_content==None:
		await message.channel.send("**There is Nothing to snipe here!**")
	else:
		
		embed = discord.Embed(description=f"{snipe_message_content}")
		embed.set_footer(text=f"Requested By {message.author.name}#{message.author.discriminator}")
		embed.set_author(name = f"Sniped the message deleted by : {snipe_message_author}")
		await message.channel.send(embed=embed)
		return
		
		


@client.command(aliases=['hi','Hi','Hello'])
async def hello(ctx):
	await ctx.send("Hellow there! How are you!")

	

	

@client.command(aliases=['s','Say','S'])
async def say(ctx, *, say):
	await ctx.send(say)



	
	
	
	
	
	
	
@client.command(aliases=['Pong','Ping'])
async def ping(ctx):
    await ctx.send (f"Pong! My Current Ping is :-\n  {round(client.latency * 1000)}ms")
	
	


@client.command(aliases=['rules','Rules','Rule'])
async def rule(ctx,*,number):
	await ctx.send(rules[int(number)-1])

@client.command(aliases=['c','C','Clear'])
@commands.has_permissions(manage_messages = True)
async def clear (ctx,amount = 2):
	await ctx.channel.purge(limit = amount)


@client.command(aliases=['k','K','Kick'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No reason provided"):
	try:
	    await member.send("You Have Been kicked because: "+reason)
	except:
		await ctx.send("The Member Has Their DMs Closed!")

	await member.kick(reason=reason)


@client.command(aliases=['b','B','Ban'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No reason provided"):
	await ctx.send(member.name + " has been banned because: "+reason)
	await member.ban(reason=reason)

	
@client.command(aliases=['ub','Ub','UB','Unban'])
@commands.has_permissions(ban_members= True)
async def unban(ctx,*,member):
	banned_users = await ctx.guild.bans()
	member_name, member_disc = member.split ('#')
	for banned_entry in banned_users:
		user = banned_entry.banned_user
		if(user.name, user.discriminator)==(member_name,member_disc):
			await ctx.guild.unban(user)
			await ctx.send(member_name +" has been unbanned!")
			return

	await ctx.send(member+" was not found!")

	
@client.command(case_insensitive=True, aliases=['Mute'])
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    if reason == None:
        await ctx.send('Please write a reason!')
        return
    guild = ctx.guild
    muteRole = discord.utils.get(guild.roles, name = "Muted")
 
    if not muteRole:
        await ctx.send("No Mute Role found! Creating one now...")
        muteRole = await guild.create_role(name = "Muted")
 
        for channel in guild.channels:
            await channel.set_permissions(muteRole, speak=False, send_messages=False, read_messages=True, read_message_history=True)
        await member.add_roles(muteRole, reason=reason)
        await ctx.send(f"{member.mention} has been muted in {ctx.guild} | Reason: {reason}")
        await member.send(f"You have been muted in {ctx.guild} | Reason: {reason}")

	
	
@client.command(case_insensitive=True, aliases=['Unmute'])
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member, *, reason=None):
 
    guild = ctx.guild
    muteRole = discord.utils.get(guild.roles, name = "Muted")
 
    if not muteRole:
        await ctx.send("The Mute role can\'t be found! Please check if there is a mute role or if the user already has it!")
        return
    await member.remove_roles(muteRole, reason=reason)
    await ctx.send(f"{member.mention} has been unmuted in {ctx.guild}")
    await member.send(f"You have been unmuted in {ctx.guild}")

	
	
@client.command(aliases=['Warn'])
@commands.has_permissions(kick_members=True)
async def warn(ctx,member : discord.Member,*,reason="Not specified"):
    if member == ctx.author:
        await ctx.send("You cannot warn yourself.")
    else:
        em = discord.Embed(title="**Warned**", description=f"{member} was warned because: {reason}", color=discord.Color.red())
        em2 = discord.Embed(title="**Warned**", description=f"You have been warned because: {reason}", color=discord.Color.red())
        await member.send(embed=em2)
        await ctx.send(embed=em)


@client.command(aliases=['user','info','Whois','User','Info'])
async def whois(ctx , member: discord.Member = None):
    member= ctx.author if not member else member
    roles = [role for role in member.roles]



    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Guild name:", value=member.display_name)

    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top role:", value=member.top_role.mention)

    embed.add_field(name="Bot?", value=member.bot)

    await ctx.send(embed=embed)


	
@client.command(aliases=['Server'])
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)
	
	
	

@client.command(aliases=['Meme'])
async def meme(ctx):
	embed = discord.Embed(color = discord.Colour.green())

	random_link = random.choice(images)

	embed.set_image(url = random_link)

	await ctx.send(embed = embed) 

	
	
@client.command(aliases = ['pl','Pl','Poll'])
async def poll(ctx,*, msg):
    channel = ctx.channel
    try:
        op1 , op2 = msg.split("or")
    except:
        await channel.send("Correct Syntax: [Choice1] or [Choice2]")
        return



        embed = discord.Embed(title="Poll", description = txt,colour = discord.Colour.black())
        message_ = await channel.send(embed=embed)
        await message__.add_reaction("<a:tick:828860946788253696>")
        await message__.add_reaction("<a:cross:828860995769466970>")
        await ctx.message.delete()
	
	
	


	
def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2


    return val * time_dict[unit]

	




	
	
	
	
	
	
	
	
@client.command(aliases=['gw','Gw','Giveaway'])
@commands.has_permissions(kick_members = True)
async def giveaway(ctx):
    await ctx.send("Let's start this giveaway! Please answer these questions within 15 seconds!")

    questions = ["Which channel should the giveaway be hosted in?", 
                "What should be the duration of the giveaway? (s|m|h|d)",
                "What will be the prize of the giveaway?"]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel 

    for i in questions:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You didn\'t answer in time, please be quicker next time!')
            return
        else:
            answers.append(msg.content)
    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"You didn't mention a channel properly. Pls do it like this {ctx.channel.mention} next time!")
        return

    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"You didn't answer the time with a proper unit. Pls use (s|m|h|d) next time!")
        return
    elif time == -2:
        await ctx.send(f"The time must be an integer. Pls enter an integer next time")
        return            

    prize = answers[2]

    await ctx.send(f"The Giveaway will be in {channel.mention} and will last {answers[1]}!")


    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    embed.add_field(name = "Hosted by:", value = ctx.author.mention)

    embed.set_footer(text = f"Ends {answers[1]} from now!")

    my_msg = await channel.send(embed = embed)


    await my_msg.add_reaction(":tada:")


    await asyncio.sleep(time)


    new_msg = await channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! {winner.mention} has won {prize}!")
	
	
	
	
	
	
@client.command()
@commands.has_permissions(kick_members = True)
async def reroll(ctx, channel : discord.TextChannel, id_ : int):
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        await ctx.send("The id was entered incorrectly.")
        return
    
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! The new winner is {winner.mention}.!")    
	
	
	
	
	
	
	
	
	



	
	


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	









client.run("Token")
