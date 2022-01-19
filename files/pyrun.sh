echo "stopping all bots..."
kill $(ps aux | grep pycryptobot.py | grep -v grep | awk '{print $2}')
echo "updating bot..."
git pull
while read p;
do
  echo "launching $p bot..."
  lxterminal -t $p -e "while true; do git pull; python3 pycryptobot.py --config config/$p.json; done"
  echo "$p Done!"
  sleep 1
done < pairs.txt
echo "All bots launched, to the moon!!!!"
sleep 5