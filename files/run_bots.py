import subprocess, json, sys, time, os

restart_interval = 7200 # restart traders every x number of seconds to account for config changes, here 2h

def read_markets():
    with open('markets-binance.json', 'r+') as infile: 
        j = json.load(infile)
        return j['markets']

def start_process(market):
    global processes
    run_command = f'python3 pycryptobot.py --exchange binance --market {market} --smartswitch 1 --buymaxsize 50'
    list_command = run_command.split(sep=' ')

    process = subprocess.Popen(list_command,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True,
                        )

    processes.append(process)


def kill_processes():
    global processes
    for i in processes:
        print(f'Killing {i.args}')
        i.kill()

def live_check():
    global processes

    for i in processes:
        if i.poll() != None:
            print(f'Application failure: {i.args}')

def main():
    global processes
    
    while True:
        processes = []
        start_time = time.time()
        market_list = read_markets()
        print(f"Markets starting: {market_list}")
        for i in market_list:
            start_process(i)
            time.sleep(60)


        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time < restart_interval:
                time.sleep(10)
                live_check()
            else:
                kill_processes()
                break
    
main()
