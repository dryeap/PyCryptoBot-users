options=()

for d in ./*/; do
options+=(--tab -t ${d:2} -e "bash -c 'cd $d && python3 pycryptobot.py; bash' ")
done

gnome-terminal "${options[@]}"