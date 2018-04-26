import discord
import asyncio
import random

client = discord.Client()

primo_text = ['Through the gates of hell As we make our way to heaven','Through the Nazi lines Primo victoria', """We've been training for years Now we're ready to strike As the great operation begins""", "We're the first wave on the shore We're the first ones to fall", 'Yet soldiers have fallen before In the dawn they will pay', "With their lives as the priceHistory's written today", 'In this burning inferno Know that nothing remains', 'As our forces advance on the beach',  'Aiming for heaven though serving in hell', 'Victory is ours their forces will fall',  'Through the gates of hell As we make our way to heaven', 'Through the Nazi lines Primo victoria',  'On the 6th of June On the shores of western Europe 1944', 'D-day upon us',  "We've been here before Used to this kind of war", 'Crossfire grind through the sand Our orders were easy', "It's kill or be killed Blood on both sides will be spilled",  'In the dawn they will pay With their lives as the price', "History's written today Now that we are at war", 'With the axis again This time we know what will come', 'Aiming for heaven though serving in hell Victory is ours their forces will fall', 'Through the gates of hell As we make our way to heaven', 'Through the Nazi lines Primo victoria',  'On the 6th of June On the shores of western Europe 1944', 'D-day upon us',  '6th of June 1944 Allies are turning the war', 'Normandy state of anarchy Overlord',  'Aiming for heaven though serving in hell Victory is ours their forces will fall',  'Through the gates of hell As we make our way to heaven', 'Through the Nazi lines Primo victoria', 'On the 6th of June On the shores of western Europe 1944 D-day upon us',  'Through the gates of hell As we make our way to heaven', 'Through the Nazi lines Primo victoria',  'On the 6th of June On the shores of western Europe 1944', 'Primo victoria' ]

def role_random(text):
    roles = ['Carry', 'Mider', 'Hardline', 'Support', 'Roamer']
    people = text.split()
    dict = {}
    text = ''
    for i in people:
        role = random.choice(roles)
        roles.remove(role)
        dict[i] = role
    for i in dict:
        text += i + '-' + dict[i] + '\n'
    return text

channels = {}

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    for ch in client.get_all_channels():
        channels[ch.name] = ch
    print('aб'*70)
@client.event
async def on_message(message):

    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        print(log.author)

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!roles'):
        await client.send_message(message.channel, role_random(message.content[6:]))
    elif message.content.startswith('!primovictoria'):
        for i in primo_text:
            await client.send_message(message.channel, i, tts=True)
@client.event
async def on_voice_state_update(before,after):
    if(before.voice.voice_channel!=None and after.voice.voice_channel!=before.voice.voice_channel):
        await client.send_message(channels['polovnik'], before.nick + ' вышел из ' + before.voice.voice_channel.name, tts = True)
    if(after.voice.voice_channel!=None and after.voice.voice_channel!=before.voice.voice_channel):
        await client.send_message(channels['polovnik'], after.nick + ' зашел в ' + after.voice.voice_channel.name, tts = True)
    if(before.voice.self_mute==False and after.voice.self_mute==True):
        await client.send_message(channels['polovnik'], after.nick + ' выключил микрофон', tts=True)
    if (before.voice.self_mute == True and after.voice.self_mute == False):
        await client.send_message(channels['polovnik'], after.nick + ' включил микрофон', tts=True)
client.run('MzQ0OTIzNDQ5MTgzMTc0Njc4.DXFsJg.hDbHZiHn9_KYI-oWyHD8OU72LOw')
