import discord
from threading import Thread
intents = discord.Intents.default()
intents.message_content = True
messageAuthor1 = "amongus"
guildname = "amogu"
client = discord.Client(intents=intents)
input1 = input
list_input = []
channel_dict = {}
alreadySent = False


@client.event
async def on_message(message):
    global messageAuthor1
    print(message.author , 'in channel' , message.channel)
    print(message.content)
    messageAuthor1 = message.author 
    


@client.event
async def on_ready():               
    #checks if login was successful and if the user is correct
    print(f'We have logged in as {client.user}')

    #fetches the names of the channels in your server and numbers them 
    #make sure not to make any typos in ENTER SERVER NAME HERE
    guild = discord.utils.get(client.guilds, name="Euuuphrates River")
    print(f'Fetching channels in server: {guild.name}')
    channels = guild.channels
    i = 1
    for channel in channels:
        print(f'Channel {i}: {channel.name}  {channel.id}')
        globals()[f'{i}'] = channel.id
        i += 1
    while True:
        global alreadySent
        if alreadySent == False:
            try:
                i = int(input("Enter the number of the channel you want to type in:"))
                channel_id = globals()[str(i)]
                channel_dict[i] = channel.id
                alreadySent = True
            except KeyError:
                print("Invalid input. Please enter a valid number.")
        else:
            while True:
                y = input("What would you like to send? ")
                selected_channel = client.get_channel(channel_id)
                if y == "exitChannel":
                    alreadySent = False
                    await amongus()
                else:
                    await selected_channel.send(y)
                    alreadySent = True
                break

async def amongus():
    guild = discord.utils.get(client.guilds, name="Euuuphrates River")
    print(f'Fetching channels in server: {guild.name}')
    channels = guild.channels
    i = 1
    for channel in channels:
        print(f'Channel {i}: {channel.name}  {channel.id}')
        globals()[f'{i}'] = channel.id
        i += 1


    '''print('Which channel would you like to pick (put in the number for it)')
    i = input("Enter the number of the channel you want to type in:")
    channel_id = globals()['channel{i}']
    selected_channel = client.get_channel(globals()[str(channel_id)])
    selected_channel.send("amogus")
    print (i)
    channelID = i'''

input_thread = Thread(target=on_message)
input_thread.start

'''@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    global messageAuthor1
    if messageAuthor1 == message.author:
        print(message.content)
    else:
        print(message.author , 'in channel' , message.channel)
        print(message.content)
        messageAuthor1 = message.author 

    
'''

'''@client.event
async def on_ready():
    global serverobj 
    for guild in client.guilds:
        for channel in guild.channels:
            print(f' - Channel: {channel.name}, ID: {channel.id}')
            while True:
             text = input("What message do you want to send? ")
        await client.send_message(channelobj, text)'''






client.run('MTA2OTM3MDI0ODY3MjgzNzcyNQ.GtmUgb.6jIbqHlr18a8KKHM-x8Mc-TttccQ9BXWBdN584')


#client.run('MTA2OTM3MDI0ODY3MjgzNzcyNQ.GtmUgb.6jIbqHlr18a8KKHM-x8Mc-TttccQ9BXWBdN584')