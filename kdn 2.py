import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_message(message):
    if message.content.startswith("사용법"):
        await message.channel.send("(kdn 수다봇 사용법입니다)  kdn 하이 , 심심해 , 나랑 놀자 , 너 누구임? , ㅋㅋㅋㅋㅋ , kdn 나랑 사귀자 , 야 kdn , ㅇㅇ , 야 임마 , 안녕하세요 , 야야야야 , ㅠㅠ , ? , 왜")
    if message.content.startswith("kdn 하이"):
        await message.channel.send("ㅎㅇ")
    if message.content.startswith("심심해"):
        await message.channel.send("소금줄까?")
    if message.content.startswith("ㅠㅠ"):
        await message.channel.send("맘껏 울어라")
    if message.content.startswith("너 누구임?"):
        await message.channel.send("kdn")
    if message.content.startswith("ㅋㅋㅋㅋㅋ"):
        await message.channel.send("왜 웃냐")
    if message.content.startswith("kdn 나랑 사귀자"):
        await message.channel.send("응~닥쳐")
    if message.content.startswith("야 kdn"):
        await message.channel.send("나를 왜 부르는 것이냐 애송이 녀석")
    if message.content.startswith("ㅇㅇ"):
        await message.channel.send("ㅋ")
    if message.content.startswith("야 임마"):
        await message.channel.send("나 부르는겨?")
    if message.content.startswith("안녕하세요"):
        await message.channel.send("ㅎㅇ")
    if message.content.startswith("야야야야"):
        await message.channel.send("왜")
    if message.content.startswith("나랑 놀자"):
        await message.channel.send("싫은뎁")
    if message.content.startswith("?"):
        await message.channel.send("ㅇ?")
    if message.content.startswith("왜"):
        await message.channel.send("ㅋ")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
