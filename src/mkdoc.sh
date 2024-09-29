if [ "$(basename "$(pwd)")" = "src" ]; then
	pandoc --standalone --mathjax README.md  >../docs/index.html
else
	echo "Change to src folder and run again!"
fi
