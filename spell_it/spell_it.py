class SpellIt:
    def __init__(self, bot):
        self.bot = bot

    async def message_recv(self, message):
        content = message.content
        if message.author.bot:
            return
        user = message.author
        if 'bb' in content:
            meme_ref = 'bb'
        elif 'pp' in content:
            meme_ref = 'pp'
        else:
            return
        await self.bot.send_message(message.channel, "{} you said {}".format(user.mention, meme_ref))


def setup(bot):
    n = SpellIt(bot)
    bot.add_listener(n.message_recv, "on_message")
    bot.add_cog(n)
