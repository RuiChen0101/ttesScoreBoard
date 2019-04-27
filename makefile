.PHONY: directories clean

all:

ui: src/ui/mainui.ui
	pyuic5 ./src/ui/mainui.ui -o ./src/ui/mainwindow.py

exe: ttesScoreBoard.py src/ui/mainwindow.py
	pyinstaller -F -w ./ttesScoreBoard.py

clean:
	rm -rf dist build __pycache__
stat:
	wc src/*
