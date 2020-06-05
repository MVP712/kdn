import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_message(message):
    if message.content.startswith("MVP 하이"):
        await message.channel.send("ㅎㅇ")
    if message.content.startswith("나 심심해"):
        await message.channel.send("소금줄까?")
    if message.content.startswith("나랑 놀자"):
        await message.channel.send("나 바빠")
    if message.content.startswith("너 누구임?"):
        await message.channel.send("mvp")
    if message.content.startswith("ㅋㅋㅋㅋㅋ"):
        await message.channel.send("왜 웃냐")
    if message.content.startswith("사랑해"):
        await message.channel.send("응~닥쳐")
    if message.content.startswith("오너"):
        await message.channel.send("왜 임마")
    if message.content.startswith("ㅇㅇ"):
        await message.channel.send("ㅋ")
    if message.content.startswith("야"):
        await message.channel.send("나 부르는겨?")
    if message.content.startswith("mvp 하이"):
        await message.channel.send("ㅎㅇ")
    if message.content.startswith("MVP"):
        await message.channel.send("왜")
    if message.content.startswith("교장"):
        await message.channel.send("네")
    if message.content.startswith("?"):
        await message.channel.send("ㅇ?")
    if message.content.startswith("왜"):
        await message.channel.send("ㅋ")

access_token = os.environ["BOT_TOKEN"]
        client.run(access_token)
