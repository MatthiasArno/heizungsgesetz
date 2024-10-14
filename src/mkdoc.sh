if [ "$(basename "$(pwd)")" = "src" ]; then
	pandoc --standalone --mathjax README.md  -o ../docs/index.html \
	 --metadata title="Heizungsgesetz und Wärmepumpe im Altbau" \
	 --metadata description="SCOP (JAZ) Schätzung einer Wärmepumpe im Altbau (Fachwerk) mit Option Photovoltaik. Wirtschaftlichkeit und Förderbedingung nach Gebäudeenergiegesetz."
else
	echo "Change to src folder and run again!"
fi
