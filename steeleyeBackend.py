from fastapi import FastAPI
import datetime as dt
from fastapi.encoders import jsonable_encoder
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()
#

class TradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")

    price: float = Field(description="The price of the Trade.")

    quantity: int = Field(description="The amount of units traded.")


class Trade(BaseModel):
    asset_class: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")

    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with. May not always be available")

    instrument_id: str = Field(alias="instrumentId", description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")

    instrument_name: str = Field(alias="instrumentName", description="The name of the instrument traded.")

    trade_date_time: dt.datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")

    trade_details: TradeDetails = Field(alias="tradeDetails", description="The details of the trade, i.e. price, quantity")

    trade_id: str = Field(alias="tradeId", default=None, description="The unique ID of the trade")

    trader: str = Field(description="The name of the Trader")

trade_inv = {
    1:{
    "buySellIndicator" : "Sell",
    "price" : 29.99,
    "quantity" : 10
    },
    2:{
    "buySellIndicator" : "Buy",
    "price" : 34.99,
    "quantity" : 20
    },
    3:{
    "buySellIndicator" : "Sell",
    "price" : 67.99,
    "quantity" : 30
    },
    4:{
    "buySellIndicator" : "Buy",
    "price" : 89.99,
    "quantity" : 30
    },
    5:{
    "buySellIndicator" : "Sell",
    "price" : 119.99,
    "quantity" : 30
    },
    6:{
    "buySellIndicator" : "Buy",
    "price" : 29.99,
    "quantity" : 10
    },
    7:{
    "buySellIndicator" : "Sell",
    "price" : 20.43,
    "quantity" : 77
    },
    8:{
    "buySellIndicator" : "Buy",
    "price" : 98.76,
    "quantity" : 546
    },
    9:{
    "buySellIndicator" : "Sell",
    "price" : 150.99,
    "quantity" : 789
    },
    10:{
    "buySellIndicator" : "Buy",
    "price" : 390.99,
    "quantity" : 456
    },
    11:{
    "buySellIndicator" : "Sell",
    "price" : 26.45,
    "quantity" : 123
    },
    12:{
    "buySellIndicator" : "Buy",
    "price" : 768.54,
    "quantity" : 976
    },
    13:{
    "buySellIndicator" : "Sell",
    "price" : 566.98,
    "quantity" : 675
    },
    14:{
    "buySellIndicator" : "Buy",
    "price" : 65.09,
    "quantity" : 234
    },
    15:{
    "buySellIndicator" : "Sell",
    "price" : 76.69,
    "quantity" : 67
    }
}

inventory = {
    1:{
    "asset_class" : "Largecap",
    "counterparty" : "buyer",
    "instrument_id" : "AAPL",
    "instrument_name" : "Apple",
    "trade_date_time" : dt.datetime.now(),
    "trade_details" : trade_inv[1],
    "trade_id" : 1,
    "trader"  : "Arun"
    },
    2:{
    "asset_class" : "Midcap",
    "counterparty" : "seller",
    "instrument_id" : "FTNT",
    "instrument_name" : "Fortinet",
    "trade_date_time" : dt.datetime.now(),
    "trade_details" : trade_inv[2],
    "trade_id" : 2,
    "trader"  : "Roshan"
    },
    3:{
    "asset_class" : "Smallcap",
    "counterparty" : "buyer",
    "instrument_id" : "REXR",
    "instrument_name" : "Rexford",
    "trade_date_time" : dt.datetime.now(),
    "trade_details" : trade_inv[3],
    "trade_id" : 3,
    "trader"  : "Ayush"
    },
    4:{
    "asset_class" : "Internationalequities",
    "counterparty" : "seller",
    "instrument_id" : "BABA",
    "instrument_name" : "Alibaba",
    "trade_date_time" : dt.datetime.now(),
    "trade_details" : trade_inv[4],
    "trade_id" : 4,
    "trader"  : "Divyansh"
    },
    5:{
    "asset_class" : "Emergingmarket",
    "counterparty" : "buyer",
    "instrument_id" : "YNDX",
    "instrument_name" : "Yandex",
    "trade_date_time" : dt.datetime.now(),
    "trade_details" : trade_inv[5],
    "trade_id" : 5,
    "trader"  : "Mansi"
    },
    6:{
    "asset_class" : "Investmentgrade",
    "counterparty" : "seller",
    "instrument_id" : "GOOG",
    "instrument_name" : "AlphabetInc",
    "trade_date_time" : dt.datetime.now(),
    "trade_details" : trade_inv[6],
    "trade_id" : 6,
    "trader"  : "simran"
    },
    7:{
    "asset_class" : "Highyield",
    "counterparty" : "buyer",
    "instrument_id" : "HYG",
    "instrument_name" : "iBoxx",
    "trade_date_time" : dt.datetime.now(),
    "trade_details" : trade_inv[7],
    "trade_id" : 7,
    "trader"  : "rohit"
    },
    8:{
    "asset_class" : "Governmentbonds",
    "counterparty" : "seller",
    "instrument_id" : "TLT",
    "instrument_name" : "iShares",
    "trade_date_time" : dt.datetime.now(),
    "trade_details" : trade_inv[8],
    "trade_id" : 8,
    "trader"  : "aman"
    },
    9:{
    "asset_class" : "Treasurybonds",
    "counterparty" : "buyer",
    "instrument_id" : "30YR",
    "instrument_name" : "30year",
    "trade_date_time" : dt.datetime.now(),
    "trade_details" : trade_inv[9],
    "trade_id" : 9,
    "trader"  : "nilesh"
    },
    10:{
    "asset_class" : "Municipalbonds",
    "counterparty" : "seller",
    "instrument_id" : "MUB",
    "instrument_name" : "iShares",
    "trade_date_time" : dt.datetime.now(),
    "trade_details" : trade_inv[10],
    "trade_id" : 10,
    "trader"  : "raghav"
    },
    11:{
    "asset_class" : "Realestate",
    "counterparty" : "buyer",
    "instrument_id" : "SPG",
    "instrument_name" : "SimonPropertyGroup",
    "trade_date_time" : dt.datetime.now(),
    "trade_details" : trade_inv[11],
    "trade_id" : 11,
    "trader"  : "kuldeep"
    },
    12:{
    "asset_class" : "Physicalrealestate",
    "counterparty" : "seller",
    "instrument_id" : "MLS",
    "instrument_name" : "MLSlistings",
    "trade_date_time" : dt.datetime.now(),
    "trade_details" : trade_inv[12],
    "trade_id" : 12,
    "trader"  : "aayush"
    },
    13:{
    "asset_class" : "Commodities",
    "counterparty" : "buyer",
    "instrument_id" : "GC",
    "instrument_name" : "COMEXGoldFutures",
    "trade_date_time" : dt.datetime.now(),
    "trade_details" : trade_inv[13],
    "trade_id" : 13,
    "trader"  : "manoj"
    },
    14:{
    "asset_class" : "currencies",
    "counterparty" : "seller",
    "instrument_id" : "usd",
    "instrument_name" : "usdollar",
    "trade_date_time" : dt.datetime.now(),
    "trade_details" : trade_inv[14],
    "trade_id" : 14,
    "trader"  : "om"
    },
    15:{
    "asset_class" : "cryptocurrencies",
    "counterparty" : "buyer",
    "instrument_id" : "btc",
    "instrument_name" : "bitcoin",
    "trade_date_time" : dt.datetime.now(),
    "trade_details" : trade_inv[15],
    "trade_id" : 15,
    "trader"  : "nitish"
    }
}



@app.get("/")
def home():
    return {"data":"success"}

@app.get("/get-trade/")
def get_trades(limit: int=10, offset: int = 0):
    end_index = offset + limit
    trades = list(inventory.values())[offset:end_index]
    total_pages = len(inventory) // limit + (len(inventory) % limit != 0)
    previous_url = None
    if offset > 0:
        previous_offset = max(offset - limit, 0)
        previous_url = f"/get-trade/?limit={limit}&offset={previous_offset}"
    next_url = None
    if end_index < len(inventory):
        next_offset = end_index
        next_url = f"/get-trade/?limit={limit}&offset={next_offset}"
    result = {
        "trades": trades,
        "pagination": {
            "total_pages": total_pages,
            "previous": previous_url,
            "next": next_url
        }
    }
    
    return result

@app.get("/get-trade/id/{item_id}")
def getbyid(item_id:int):
    return inventory[item_id]

@app.get("/get-trade/search")
def getbysearch(name:str):
    data ={}
    for item_id in inventory:
        if inventory[item_id]["counterparty"] == name:
            data[item_id] = inventory[item_id]
        if inventory[item_id]["instrument_id"] == name:
            data[item_id] = inventory[item_id]
        if inventory[item_id]["instrument_name"] == name:
            data[item_id] = inventory[item_id]
        if inventory[item_id]["trader"] == name:
            data[item_id] = inventory[item_id]

    return data


@app.get("/get-trade/assetclass")
def asset(name:str):
    data = {}
    for item_id in inventory:
        if inventory[item_id]["asset_class"] == name:
            data[item_id]=inventory[item_id]

    return data


@app.get("/get-trade/price")
def price(minprice:float,maxprice:float):
    data = {}
    for item_id in inventory:
        if inventory[item_id]["trade_details"]["price"] >= minprice and inventory[item_id]["trade_details"]["price"] <= maxprice:
            data[item_id] = inventory[item_id]

    return data


@app.get("/get-trade/tradetype")
def tradetype(name:str):
    data = {}
    for item_id in inventory:
        if inventory[item_id]["trade_details"]["buySellIndicator"] == name:
            data[item_id]=inventory[item_id]

    return data



@app.post("/create-item/{item_id}")
def create_item(item_id:int,item:Trade):
    if item_id in inventory:
        return{"Error":"Item already exists"}
    inventory[item_id]=item
    return inventory[item_id]