import os, sys, subprocess

bot = '/pycryptobot.py'

path = os.path.dirname(os.path.abspath(__file__))
bot = path + bot

with open(path + '/pairs.txt', 'r') as f:
    txt = f.read()
    bots = [(x.split(",")[0].strip(),
             x.split(",")[1].strip(),
             x.split(",")[2].strip()) 
        for x in txt.split("\n")]
    
    for i,b in enumerate(bots):
        exchange, pair,size = b
        args = ["python", bot, "--exchange", exchange, "--market", pair, "--maxbuysize", size]
        #print(args)  
        subprocess.call(args, cwd=path)