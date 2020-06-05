import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("하이")
    if message.content.startswith("!규칙"):
        await message.channel.send("음 아직 규칙을 못정했어 정하고 알려줄게")

    if message.content.startswith("!사진"):
        


client.run("NzE2OTI1MjgzMzg2Nzg1ODgy.XtcHNQ.kEIUbKxf8tjvQPUBx8MY3JEOxTc")
