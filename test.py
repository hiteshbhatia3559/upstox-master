import csv

a= {'timestamp': 1553850656000, 'exchange': 'NSE_EQ', 'symbol': 'ACC', 'ltp': 1628.85, 'open': 1623, 'high': 1629, 'low': 1601.2, 'close': 1617.8, 'vtt': 716573, 'atp': 1613.37, 'oi': '', 'spot_price': 0, 'total_buy_qty': 101618, 'total_sell_qty': 89750, 'lower_circuit': 1456.05, 'upper_circuit': 1779.55, 'yearly_low': 1255.65, 'yearly_high': 1869.95, 'bids': [{'quantity': 144, 'price': 1627.9, 'orders': 4}, {'quantity': 30, 'price': 1627.85, 'orders': 1}, {'quantity': 55, 'price': 1627.8, 'orders': 1}, {'quantity': 1, 'price': 1627.55, 'orders': 1}, {'quantity': 23, 'price': 1627.5, 'orders': 1}], 'asks': [{'quantity': 135, 'price': 1628.9, 'orders': 2}, {'quantity': 1012, 'price': 1629, 'orders': 14}, {'quantity': 1, 'price': 1629.05, 'orders': 1}, {'quantity': 2, 'price': 1629.1, 'orders': 1}, {'quantity': 56, 'price': 1629.3, 'orders': 2}], 'ltt': 1553850655000}

f = open('new.csv','w+')

writer = csv.writer(f)

writer.writerow(a)
writer.writerow(a.values())