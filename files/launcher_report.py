import os, sys, subprocess

bot = '/pycryptobot.py'

path = os.path.dirname(os.path.abspath(__file__))
bot = path + bot

with open(path + '/pairs_report.txt', 'r') as f:
    txt = f.read()
    bots = txt.split("\n")
    
    args = ["python", bot, "--exchange", "binance", "--stats", "--statgroup"]
    
    for b in bots:
        args.append(str(b).strip())

    #print(args)  
    subprocess.call(args, cwd=path)