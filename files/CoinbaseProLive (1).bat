@echo off
ECHO Starting Coinbase Pro Bots...
cd C:\PyCryptoBot
git pull

SETLOCAL
SET "var1="
SET "var2="
FOR /f "tokens=*" %%a IN (C:\PyCryptoBot\CoinbaseProLive.txt) DO (
 CALL SET "var1=%%var2%%"
 SET "var2=%%a"
 IF DEFINED var1 (
  CALL ECHO %%var1%%
  CALL ECHO %%var2%%
  CALL start powershell -Command "python pycryptobot.py --exchange coinbasepro --market %%var1%% %%var2%% --buymaxsize 145 --logfile %%var1%%_CoinbasePro.log"
  SET "var1="
  SET "var2="
  TIMEOUT 5
  )
)