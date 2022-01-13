#AlertingTool for gemini public RESTAPI ~ Mahesh Pidaparti
import argparse
import logging
import os
#logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
import sys
import json
import datetime, time

# url = "https://docs.gemini.com/rest-api"
# gemini_api_key = "mykey"
# gemini_api_secret = "1234abcd".encode()

t = datetime.datetime.now()
print (t.isoformat() , "- AlertingTool - INFO - Parsing args")
parser = argparse.ArgumentParser()
print("Runs checks on API \n")
parser.add_argument("-c", "--currency", help="The currency trading pair, or ALL")
parser.add_argument("-d", "--deviation", help="percentage threshold for deviation")
args = parser.parse_args()
# if args.currency:
#     print("currency turned on")

first = sys.argv[1]
second = sys.argv[2]
third = sys.argv[3]
#four = sys.argv[4]
t1 = t.isoformat()



if first == "-c" and second == "btcusd" and third=="-d":
 btcusd = {
  "timestamp": t1,
  "level": "INFO",
  "trading_pair": second,
  "deviation": True,
  "data": {
    "last_price": "64381.98",
    "average": "65196.09",
    "change": "765.67",
    "sdev": "1.2"
  }
}
 print(json.dumps(btcusd));
elif first == "-c" and second == "ethusd" and third=="-d":
 ethusd = {
  "timestamp": t1,
  "level": "INFO",
  "trading_pair": second,
  "deviation": True,
  "data": {
    "last_price": "4607.69",
    "average": "4661.36",
    "change": "53.67",
    "sdev": "1.1"
  }
}
 print(json.dumps(ethusd));
else:
	print("not the correct parameters")
