import discord #discordでBOTを使うのにこれが必ずいる

TOKEN = 'NzM0Njg4NDYyODk2MzY1NjMy.XxVYAg.8O1ZAs7UlRrr5JYnGh_6ZolYuHU'

client = discord.Client()

@client.event #BOT起動時にCMDに表示される部分で無くてもよい
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message): #メッセージを受け取る関数なので必ず必要
    if message.content == "/おはよう":
    #:(コロン)を忘れずつけよう！Enterを押すと自動で改行されるよ！
        await message.channel.send('Hello world!!')

# この＊＊＊に自分のトークンを書き替える
client.run(TOKEN)
