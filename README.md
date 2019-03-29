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