Problem Statement
```
1.Will be provide sample code there is need only websocket option which need to work always.
sample code link : https://gist.github.com/svishi/ba0ee4e08f1e2364addfe76c5b2ef7d7
references: https://github.com/upstox/upstox-python
2. need to save that live data in excel.

required api key: sW8QnFzjKO3tmY2LTehyg5sztKCTPmN6fzymZKVh
api secret: 97h1eqpunb
authantication code: 80a243368dfdc90579ad0bcef9bc8705b5fca013 (if this code not work then call me on +919175019097 will be genrate new one)

Important point: the live websocket data recive only in market hours 9.15am to 3.30 pm so u need to test or work to base on this time of schedule.
```

Note
```
1. If you need to track say 10 instruments, you must have 10 CPU cores available
2. The API will time out after 3:30
3. Data received is in the form of <name of stock>.csv, and all data received through websocket is printed to the sheet.
```

Instructions
```
-1. Install Notepad++ (will be needed to add instruments)
0. Download the Program as a zip file from Github, then extract at any location, say /Project/
1. Download Python 3.5 from : https://www.python.org/ftp/python/3.5.0/python-3.5.0-amd64-webinstall.exe
2. Install Python 3.5 at C:/Python35, and make sure Python is configured in PATH (Google this if you did not understand)
3. Install Chrome
4. Open command prompt, then type the following (if there are errors, contact me):
a. 'pip install upstox-api' without quotes, press enter and let it complete the install
b. 'pip install selenium' without quotes, press enter and let it complete the install
c. 'pip install webdriver-manager' without quotes, press enter and let it complete the install
d. 'python main.py' will run the script (if there is an error, contact me)
e. The output will be <name_of_instrument>.csv which you can open in Excel
5. If you want to add instruments/stocks to track, open main.py in notepad or notepad++, then edit line 58.
6. You need to add the ticker of the stock, not the name (for eg, Tata Chemicals is not valid but TATACHEM is)
7. All done. Read the Note above if you haven't read.
```