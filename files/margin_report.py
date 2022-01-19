import os, sys, subprocess

bot = '/pycryptobot.py'
path = os.path.dirname(os.path.abspath(__file__))
bot = path + bot
# pairs is structured as : exchange, pair, buymaxsize

with open(path + '/pairs.txt', 'r') as f:
    txt = f.read()
    bots = [(x.split(",")[0].strip(),
             x.split(",")[1].strip(),
             x.split(",")[2].strip()) 
        for x in txt.split("\n")]
    pairs = [x[1] for x in bots]

    args = ["python", bot, "--exchange", "binance", "--stats", "--statgroup"]
    
    for b in pairs:
        args.append(str(b).strip())

    #print(args)  
    subprocess.call(args, cwd=path)