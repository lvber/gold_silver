import json
import os
import requests
import time
import datetime

while True:
    api_url = 'https://data-asg.goldprice.org/dbXRates/USD,USD,USD,USD,USD'
    response = requests.get(api_url)
    if response.status_code == 200:
        data_json = json.loads(response.content.decode('utf-8'))
    else:
        continue

    price_list = data_json['items']
    gold_price = price_list[0]['xauPrice']
    silver_price = price_list[0]['xagPrice']

    ratio = gold_price / silver_price
    ratio = round(ratio, 4)

    write_line = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").__str__() + ',' + str(ratio) + ',' + str(gold_price) + ',' + str(silver_price) + '\n'

    file_name = 'gold_silver.csv'
    if os.path.exists(file_name):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not

    ratio_file = open(file_name, append_write)
    ratio_file.write(write_line)
    ratio_file.close()

    print(write_line)
    time.sleep(30)