import wxpy as pp

# 实例化，并登录微信

bot = pp.Bot(cache_path=True)

# 调用图灵机器人API

tuling = pp.Tuling(api_key='4a0488cdce684468b95591a641f0971d')

@bot.register()

def auto_reply(msg):

    tuling.do_reply(msg)

pp.embed()