import os, sys, subprocess

bot = '/pycryptobot.py'

path = os.path.dirname(os.path.abspath(__file__))
bot = path + bot
exchanges = []
pairs = []

with open(path + '/pairs_test.txt', 'r') as f:
    txt = f.read()
    bots = [(x.split(",")[0].strip(),
             x.split(",")[1].strip()) 
        for x in txt.split("\n")]
    
    for i, b in enumerate(bots):
        exchanges.append(b[0])
        pairs.append(b[1])
   
    statgroup = f'{" ".join(str(x) for x in pairs)}'
    args = ["python", bot, "--exchange", exchanges[0],"--stats", "--statgroup", statgroup]
    #print(args)  
    subprocess.call(args, cwd=path)