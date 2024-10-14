if [ "$(basename "$(pwd)")" = "src" ]; then
	pandoc --standalone --mathjax README.md  -o ../docs/index.html  --metadata title="Heizungsgesetz und Wärmepumpe im Altbau"
else
	echo "Change to src folder and run again!"
fi
