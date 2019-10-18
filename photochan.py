#!/usr/bin/python
#bot info
#clientid *
#clientkey *
#clientoken *
#permissions integer 511040
# *
#created by Anthony Skoury v2.0

#libraries

#for discord
import discord
from discord.ext import commands

#for image program
from PIL import Image
import os
import io
from io import BytesIO
import requests

#for exiting
import sys

#for games
import random


#bot token and initializations
TOKEN = 'NTI4NjUyMDAzMzcxNTE1OTA0.DwlxZg.TH5MVVmQCUWXZozkEtLdlKZOiZ4'
bot = commands.Bot(command_prefix='!')
client = discord.Client()
bot.remove_command('help')
pic_flag = 0 #no images have been edited
gif_flag = 0 #no gifs have been edited
convert_flag = 0 #no images have been converted


#login prompt
@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	#print(bot.user.id)
	print('------')
#End login prompt
	

#Misc commands

#Command saying hello to bot
@bot.command()
async def hello(ctx, arg=""):
    await ctx.send("Hi there "+str(ctx.author.mention)+"!")
#End of command hello
	
	
#Command to say how many servers bot is connected to (Should be 0 since bot is not public)	
@bot.command()
async def servers(ctx):
	servers = list(client.guilds)
	print("Connected on " + str(len(client.guilds))+" servers:")
	for x in range(len(servers)):
		print(' '+servers[x-1].name)
	await ctx.send(len(servers))
#End of command servers
	
	
#Command to turn off bot
@bot.command()
async def turnoff(ctx):
	if ctx.author.id == 176190181253054465: #set to id of bot owner
		await ctx.send("Turning off")
		await client.close()
		sys.exit()
	else:
		print(ctx.author)
		await ctx.send("You are not the bot owner")
		return	
#End of command turnoff
		

#Game Commands	
	
#Command to play Magic 8 Ball
@bot.command()
async def eb(ctx, arg):
	answers = random.randint(1,8)
	if answers == 1:
		await ctx.send("It is certain.")
	elif answers == 2:
		await ctx.send("Outlook good.")
	elif answers == 3:
		await ctx.send("You may rely on it.")
	elif answers == 4:
		await ctx.send("Ask me again later.")
	elif answers == 5:
		await ctx.send("Concentrate and ask again.")
	elif answers == 6:
		await ctx.send("Probably not.")
	elif answers == 7:
		await ctx.send("No.")
	elif answers == 8:
		await ctx.send("My sources say no.")
#End of command eb
		

#Command to play russian roulette
@bot.command()
async def rr(ctx):
	chamber = random.randint(1,6)
	name = ctx.author.name
	if chamber == 1:
		await ctx.send("The gun fires and "+name+" falls to the ground.")
	else:
		await ctx.send(name+" pulls the trigger and... nothing happens. Looks like "+name+" gets to live another day. Lucky you!")
#End of command rr
		

#Command to roll a die
@bot.command()
async def roll(ctx, arg, num=""):
	if arg == "d6":
		die = random.randint(1,6)
		if num != "":
			await ctx.send("You rolled a "+str(die)+" and predicted a "+str(num)+".")
		else:
			await ctx.send("You rolled a "+str(die)+".")
	elif arg == "d8":
		die = random.randint(1,8)
		if num != "":
			await ctx.send("You rolled a "+str(die)+" and predicted a "+str(num)+".")
		else:
			await ctx.send("You rolled a "+str(die)+".")
	elif arg == "d10":
		die = random.randint(1,10)
		if num != "":
			await ctx.send("You rolled a "+str(die)+" and predicted a "+str(num)+".")
		else:
			await ctx.send("You rolled a "+str(die)+".")
	elif arg == "d20":
		die = random.randint(1,10)
		if num != "":
			await ctx.send("You rolled a "+str(die)+" and predicted a "+str(num)+".")
		else:
			await ctx.send("You rolled a "+str(die)+".")
	else:
		await ctx.send("Please enter one of the four die on the list.")
#End of command roll		
		

#Command to play rock paper scissors
@bot.command()
async def rps(ctx, arg):
	if arg == "rock":
		input=1
	elif arg == "paper":
		input=2
	elif arg == "scissors":
		input=3
	else:
		await ctx.send("Please input a valid option")
		return
	out = random.randint(1,3)
	if out == 1:
		if input == 1:
			await ctx.send("We both picked rock, tie game!")
		elif input == 2:
			await ctx.send("You picked paper and I picked rock, you win!")
		elif input == 3:
			await ctx.send("You picked scissors and I picked rock, I win!")
	elif out == 2:
		if input == 1:
			await ctx.send("You picked rock and I picked paper, I win!")
		elif input == 2:
			await ctx.send("We both picked paper, tie game!")
		elif input == 3:
			await ctx.send("You picked scissors and I picked paper, you win!")
	elif out == 3:
		if input == 1:
			await ctx.send("You picked rock and I picked scissors, you win!")
		elif input == 2:
			await ctx.send("You picked paper and I picked scissors, I win!")
		elif input == 3:
			await ctx.send("We both picked scissors, tie game!")
#End of command rps
		
		
#Help Commands
		
#Command that lists commands
@bot.command()
async def help(ctx):
    await ctx.send(
'''
Hello there! Here are a list of supported commands.
```prolog
Photo/GIF Editor Commands
Note <> After A Filter Name Means Required Input Value
!pic <img url | uploaded img> <filter> [value] :: Edit A Picture
!gif <gif url | uploaded gif> <filter> [value] :: Edit A GIF
!filters                                       :: List Of Filters
!convert <img url | uploaded img> <type>       :: Convert To Type
!types                                         :: List Of Filetypes
!avatar 									   :: Get A User Avatar


Game Commands
!roll <d6 | d8 | d10 | d20> [#]         :: Roll A Die
!rr                                     :: Play Russian Roulette
!eb <question>                          :: Play Magic Eight Ball
!rps <rock | paper | scissors>          :: Play Rock Paper Scissors


Miscellaneous Commands
!help                                   :: Lists This Command
!hello                                  :: Say Hello To Photo-Chan
```
'''
)
#End of command help


#Command that lists filters for photolab exec
@bot.command()
async def filters(ctx):
	await ctx.send(
'''
Here are a list of supported filters/operations.
```prolog
Note <> After A Filter Name Means Required Input Value
brightness <integer>      ::  Increase The Brightness
contrast <integer>        ::  Change The Contrast
saturate <float percent>  ::  Adjust Saturation Of An Image
hue <angle>               ::  Rotate Hue (Angle In Radians)
gamma <float>             ::  Gamma Correction
red <integer>             ::  Set R In Image RGB Values
green <integer>           ::  Set G In Image RGB Values
blue <integer>            ::  Set B In Image RGB Values
hflip                     ::  Horizontally Flip An Image
vflip                     ::  Vertically Flip An Image
rotateright               ::  Rotate An Image Right
rotateleft                ::  Rotate An Image Left
resize <integer percent>  ::  Resize An Image
meddenoise                ::  Apply Median Method Denoise
avgdenoise                ::  Apply Average Method Denoise
shuffle                   ::  Shuffle An Image
hmirror                   ::  Horizontally Mirror An Image
bnw                       ::  Make An Image Black And White
edge                      ::  Edge Detection
coloredge <#hex code>     ::  Custom RGB Color Edge Detection
sketch                    ::  Pencil On Paper Sketch
negative                  ::  Invert The Colors Of An Image
solarise <integer>        ::  Limited Color Inversion
desolarise <integer>      ::  Different Version Of Solarise
bug                       ::  Apply Buggy Filter (Random)
```
'''
)    
#End of command filters


#Command that lists file formats for converting
@bot.command()
async def types(ctx):
	await ctx.send(
'''
Here are a list of supported file formats.
```prolog
jpg                   ::  Joint Photographic Experts Group
png                   ::  Portable Network Graphics
bmp                   ::  Bitmap
gif                   ::  Graphic Interchange Format
ppm                   ::  Portable Pixel Map
```
'''
) 
#End of command types

	
#Command to conduct photo editing
@bot.command()
async def pic(ctx, img_url, arg="", opt=""):
	global pic_flag
	global gif_flag
	global convert_flag
	if pic_flag == 1 or gif_flag == 1 or convert_flag == 1:
		await ctx.send("Still working on the previous command, please wait for the result then resend!")
		return
	pic_flag = 1
	listOfFilters = ['shuffle' , 'bnw' , 'edge' , 'coloredge', 'brightness' , 'hmirror' , 'hue' , 'hflip' , 'vflip' , 'rotateright' , 'rotateleft' , 'resize' , 'saturate' , 'bug' , 'meddenoise' , 'avgdenoise' , 'contrast' , 'gamma' , 'negative' , 'solarise' , 'desolarise' , 'sketch' , 'red' , 'green' , 'blue']
	if ctx.message.attachments: #shifting args if image is uploaded
		opt = arg
		arg = img_url
		img_url = ctx.message.attachments[0].url
	if arg not in listOfFilters:
		await ctx.send("Sorry I don't recognize the filter you asked for! Please input a valid filter from '!filters'.")
		pic_flag = 0
		return
	if arg == "coloredge": #converting hex color into RGB for executable
		if opt:
			hex = opt.lstrip('#')
			rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))
			opt = str("r="+str(rgb[0])+"g="+str(rgb[1])+"b="+str(rgb[2]))
	response = requests.head(img_url)
	if 'content-length' in response.headers and int(response.headers['content-length']) < 5242880: #limit on file to 5MB to keep computations faster
		response = requests.get(img_url)	
		i = Image.open(BytesIO(response.content)) #downloading image
	if 'content-length' not in response.headers or int(response.headers['content-length']) >= 5242880:
		await ctx.send("Sorry, I only work on images with a size less than 5MB!")
		pic_flag = 0
		return
	await ctx.send("Ok let me work on that picture for you, please give me a moment!")	
	i.save("image.ppm") #converting image to ppm format for executable
	os.system(r"./PhotoLabCL -i image -"+arg+" "+opt) #running executable with inputs
	newim = Image.open("editedpic.ppm")
	newim.save("photochan_pic_edit.jpg") #converting edited image to jpg
	if os.stat('photochan_pic_edit.jpg').st_size > 8388000: #discord has a limit on uploads to be 8MB
		await ctx.send("This edited picture is too big, let me make it smaller so I can send it!")
		while os.stat('photochan_pic_edit.jpg').st_size > 8388000:
			os.system(r"./PhotoLabCL -i editedpic -resize 85") #compressing image by resizing until under 8MB
			newim = Image.open("editedpic.ppm")
			newim.save("photochan_pic_edit.jpg")
		await ctx.send("Compressing complete. Sending image.")	
	await ctx.send("Here's your edited image!", file=discord.File("photochan_pic_edit.jpg"))
	os.remove("image.ppm") #cleanup
	os.remove("editedpic.ppm")
	os.remove("photochan_pic_edit.jpg")
	print("Done removing files and executing command pic.")
	pic_flag = 0
#End of command pic

	
#Command to edit gif
@bot.command()
async def gif(ctx, gif_url, arg="", opt=""):
	global gif_flag
	global pic_flag
	global convert_flag
	if pic_flag == 1 or gif_flag == 1 or convert_flag == 1:
		await ctx.send("Still working on the previous command, please wait for the result then resend!")
		return
	gif_flag = 1
	listOfFilters = ['shuffle' , 'bnw' , 'edge' , 'coloredge', 'brightness' , 'hmirror' , 'hue' , 'hflip' , 'vflip' , 'rotateright' , 'rotateleft' , 'resize' , 'saturate' , 'bug' , 'meddenoise' , 'avgdenoise' , 'contrast' , 'gamma' , 'negative' , 'solarise' , 'desolarise' , 'sketch' , 'red' , 'green' , 'blue']
	if ctx.message.attachments:
		opt = arg
		arg = gif_url
		gif_url = ctx.message.attachments[0].url
	if arg not in listOfFilters:
		await ctx.send("Sorry I don't recognize the filter you asked for! Please input a valid filter from '!filters'.")
		gif_flag = 0
		return
	if arg == "coloredge":
		if opt:
			hex = opt.lstrip('#')
			rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))
			opt = str("r="+str(rgb[0])+"g="+str(rgb[1])+"b="+str(rgb[2]))
	if gif_url.startswith("https://tenor.com/view/"):
		gif_url = gif_url+".gif"
	response = requests.head(gif_url)
	if 'content-length' not in response.headers or int(response.headers['content-length']) >= 5242880:
		await ctx.send("Sorry, I only work on gifs with a size less than 5MB!")
		gif_flag = 0
		return
	if 'content-length' in response.headers and int(response.headers['content-length']) < 5242880:
		response = requests.get(gif_url)	
		with open('/home/pi/Discord/PhotoChan/tmp.gif', 'wb') as f:
			f.write(response.content) #downloading gif
		await ctx.send("Since this is a gif this will take a bit longer, please wait a up to a minute!")
		ig = Image.open("tmp.gif")
		imagelist = [] #list for each frame of edited gif
		count = 0
		try: #iterating through entire gif to count frames
			while 1:
				ig.seek(ig.tell()+1)
				count = count+1
		except EOFError:
			pass
		fps = 1000 / ig.info['duration']	
		num_key_frames = count
		print(num_key_frames)
		with Image.open('tmp.gif') as im: #creating an image for each frame
			for i in range(num_key_frames):
				im.seek(im.n_frames // num_key_frames * i)
				im.save('{}.png'.format(i))
		for x in range(count): #looping through each frame to edit
			newim = Image.open(str(x)+".png").convert('RGB').save(str(x)+'.ppm')
			os.remove(str(x)+".png")
			os.system(r"./PhotoLabCL -i "+str(x)+" -"+arg+" "+opt)
			gifim = Image.open("editedpic.ppm")
			gifim.save(str(x)+".gif")
			os.remove("editedpic.ppm")
			imagelist.append(gifim) #appending each edited gif frame to imagelist
		imagelist[0].save('photochan_gif_edit.gif', #saving the imagelist as an animated gif
               save_all=True,
               append_images=imagelist[1:],
               duration=fps,
               loop=0)
		await ctx.send("Almost done with your gif!")
		if os.stat('photochan_gif_edit.gif').st_size > 8388000: #too complex and time consuming to resize to aborting if over 8MB
			await ctx.send("The edited gif is too large for me to send, sorry!")
			os.remove("photochan_gif_edit.gif")
			os.remove("tmp.gif")
			for x in range(count): #cleanup
				os.remove(str(x)+".ppm")
				os.remove(str(x)+".gif")
			print("Done removing files and executing command.")
			gif_flag = 0
			return
		await ctx.send("Here's your edited gif, enjoy!!", file=discord.File("photochan_gif_edit.gif"))
		os.remove("photochan_gif_edit.gif")
		os.remove("tmp.gif")
		for x in range(count): #cleanup after upload
			os.remove(str(x)+".ppm")
			os.remove(str(x)+".gif")
		print("Done removing files and executing command gif.")
		gif_flag = 0
#End of command gif


#Command to convert pic format
@bot.command()
async def convert(ctx, img_url="", arg=""):
	global convert_flag
	global gif_flag
	global pic_flag
	if pic_flag == 1 or gif_flag == 1 or convert_flag == 1:
		await ctx.send("Still working on the previous command, please wait for the result then resend!")
		return
	convert_flag = 1
	listOfTypes = ['jpg' , 'png' , 'bmp' , 'gif' , 'ppm']
	if ctx.message.attachments:
		arg = img_url
		img_url = ctx.message.attachments[0].url
	if arg not in listOfTypes:
		await ctx.send("Sorry I don't recognize the filter you asked for! Please input a valid file type from '!types'.")
		convert_flag = 0
		return
	response = requests.head(img_url)
	if 'content-length' in response.headers and int(response.headers['content-length']) < 5242880:
		response = requests.get(img_url)	
		i = Image.open(BytesIO(response.content))
	if 'content-length' not in response.headers or int(response.headers['content-length']) >= 5242880:
		await ctx.send("Sorry, I only work on images with a size less than 5MB!")
		convert_flag = 0
		return
	await ctx.send("Ok let me convert that picture for you, please give me a moment!")		
	i.save("convertedimage."+str(arg))
	if os.stat('convertedimage.'+str(arg)).st_size > 8388000:
		temp_im = Image.open("convertedimage."+str(arg))
		temp_im.save("editedpic.ppm")
		await ctx.send("This converted picture is too big, let me make it smaller so I can send it!")
		while os.stat('convertedimage.'+str(arg)).st_size > 8388000:
			os.system(r"./PhotoLabCL -i editedpic -resize 85")
			i = Image.open("editedpic.ppm")
			i.save("convertedimage."+str(arg))
		os.remove("editedpic.ppm")
	await ctx.send("Here's your converted picture!", file=discord.File("convertedimage."+str(arg)))
	os.remove("convertedimage."+str(arg))
	print("Done removing files and executing command convert.")
	convert_flag = 0
#End of command convert

@bot.command()
async def avatar(ctx, arg):
	response = requests.head(ctx.author.avatar_url)
	if 'content-length' in response.headers and int(response.headers['content-length']) < 5242880: #limit on file to 5MB to keep computations faster
		response = requests.get(ctx.author.avatar_url)	
		i = Image.open(BytesIO(response.content)) #downloading image
	if 'content-length' not in response.headers or int(response.headers['content-length']) >= 5242880:
		await ctx.send("Sorry, I only work on images with a size less than 5MB!")
		pic_flag = 0
		return
	#await ctx.send("Ok let me work on that picture for you, please give me a moment!")	
	i.save("image.ppm") #converting image to ppm format for executable
	newim = Image.open("image.ppm")
	newim.save("photochan_pic_edit.jpg") #converting edited image to jpg
	await ctx.send("Here's your avatar!", file=discord.File("photochan_pic_edit.jpg"))
	os.remove("image.ppm") #cleanup	

bot.run(TOKEN)
#EOF
