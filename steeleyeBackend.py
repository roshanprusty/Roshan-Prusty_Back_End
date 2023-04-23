from fastapi import FastAPI
import datetime as dt
from fastapi.encoders import jsonable_encoder
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()

class TradeDetails(BaseModel):
    buySellIndicator: str = Field(
        description="A value of BUY for buys, SELL for sells.")

    price: float = Field(description="The price of the Trade.")

    quantity: int = Field(description="The amount of units traded.")


class Trade(BaseModel):
    asset_class: Optional[str] = Field(
        alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")

    counterparty: Optional[str] = Field(
        default=None, description="The counterparty the trade was executed with. May not always be available")

    instrument_id: str = Field(
        alias="instrumentId", description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")

    instrument_name: str = Field(
        alias="instrumentName", description="The name of the instrument traded.")

    trade_date_time: dt.datetime = Field(
        alias="tradeDateTime", description="The date-time the Trade was executed")

    trade_details: TradeDetails = Field(
        alias="tradeDetails", description="The details of the trade, i.e. price, quantity")

    trade_id: str = Field(alias="tradeId", default=None,
                          description="The unique ID of the trade")

    trader: str = Field(description="The name of the Trader")


# `trade_inv` is a dictionary that stores the details of different trades. Each trade is identified by a unique integer key (1-15) and has three attributes: `buySellIndicator` (whether it is a buy or sell trade), `price` (the price of the trade), and `quantity` (the amount of units traded). This dictionary is used to populate the `trade_details` field of the `Trade` model.
trade_inv = {
    1: {
        "buySellIndicator": "Sell",
        "price": 29.99,
        "quantity": 10
    },
    2: {
        "buySellIndicator": "Buy",
        "price": 34.99,
        "quantity": 20
    },
    3: {
        "buySellIndicator": "Sell",
        "price": 67.99,
        "quantity": 30
    },
    4: {
        "buySellIndicator": "Buy",
        "price": 89.99,
        "quantity": 30
    },
    5: {
        "buySellIndicator": "Sell",
        "price": 119.99,
        "quantity": 30
    },
    6: {
        "buySellIndicator": "Buy",
        "price": 29.99,
        "quantity": 10
    },
    7: {
        "buySellIndicator": "Sell",
        "price": 20.43,
        "quantity": 77
    },
    8: {
        "buySellIndicator": "Buy",
        "price": 98.76,
        "quantity": 546
    },
    9: {
        "buySellIndicator": "Sell",
        "price": 150.99,
        "quantity": 789
    },
    10: {
        "buySellIndicator": "Buy",
        "price": 390.99,
        "quantity": 456
    },
    11: {
        "buySellIndicator": "Sell",
        "price": 26.45,
        "quantity": 123
    },
    12: {
        "buySellIndicator": "Buy",
        "price": 768.54,
        "quantity": 976
    },
    13: {
        "buySellIndicator": "Sell",
        "price": 566.98,
        "quantity": 675
    },
    14: {
        "buySellIndicator": "Buy",
        "price": 65.09,
        "quantity": 234
    },
    15: {
        "buySellIndicator": "Sell",
        "price": 76.69,
        "quantity": 67
    }
}


inventory = {
    1: {
        "asset_class": "Largecap",
        "counterparty": "buyer",
        "instrument_id": "AAPL",
        "instrument_name": "Apple",
        "trade_date_time": dt.datetime.now(),
        "trade_details": trade_inv[1],
        "trade_id": 1,
        "trader": "Arun"
    },
    2: {
        "asset_class": "Midcap",
        "counterparty": "seller",
        "instrument_id": "FTNT",
        "instrument_name": "Fortinet",
        "trade_date_time": dt.datetime.now(),
        "trade_details": trade_inv[2],
        "trade_id": 2,
        "trader": "Roshan"
    },
    3: {
        "asset_class": "Smallcap",
        "counterparty": "buyer",
        "instrument_id": "REXR",
        "instrument_name": "Rexford",
        "trade_date_time": dt.datetime.now(),
        "trade_details": trade_inv[3],
        "trade_id": 3,
        "trader": "Ayush"
    },
    4: {
        "asset_class": "Internationalequities",
        "counterparty": "seller",
        "instrument_id": "BABA",
        "instrument_name": "Alibaba",
        "trade_date_time": dt.datetime.now(),
        "trade_details": trade_inv[4],
        "trade_id": 4,
        "trader": "Divyansh"
    },
    5: {
        "asset_class": "Emergingmarket",
        "counterparty": "buyer",
        "instrument_id": "YNDX",
        "instrument_name": "Yandex",
        "trade_date_time": dt.datetime.now(),
        "trade_details": trade_inv[5],
        "trade_id": 5,
        "trader": "Mansi"
    },
    6: {
        "asset_class": "Investmentgrade",
        "counterparty": "seller",
        "instrument_id": "GOOG",
        "instrument_name": "AlphabetInc",
        "trade_date_time": dt.datetime.now(),
        "trade_details": trade_inv[6],
        "trade_id": 6,
        "trader": "simran"
    },
    7: {
        "asset_class": "Highyield",
        "counterparty": "buyer",
        "instrument_id": "HYG",
        "instrument_name": "iBoxx",
        "trade_date_time": dt.datetime.now(),
        "trade_details": trade_inv[7],
        "trade_id": 7,
        "trader": "rohit"
    },
    8: {
        "asset_class": "Governmentbonds",
        "counterparty": "seller",
        "instrument_id": "TLT",
        "instrument_name": "iShares",
        "trade_date_time": dt.datetime.now(),
        "trade_details": trade_inv[8],
        "trade_id": 8,
        "trader": "aman"
    },
    9: {
        "asset_class": "Treasurybonds",
        "counterparty": "buyer",
        "instrument_id": "30YR",
        "instrument_name": "30year",
        "trade_date_time": dt.datetime.now(),
        "trade_details": trade_inv[9],
        "trade_id": 9,
        "trader": "nilesh"
    },
    10: {
        "asset_class": "Municipalbonds",
        "counterparty": "seller",
        "instrument_id": "MUB",
        "instrument_name": "iShares",
        "trade_date_time": dt.datetime.now(),
        "trade_details": trade_inv[10],
        "trade_id": 10,
        "trader": "raghav"
    },
    11: {
        "asset_class": "Realestate",
        "counterparty": "buyer",
        "instrument_id": "SPG",
        "instrument_name": "SimonPropertyGroup",
        "trade_date_time": dt.datetime.now(),
        "trade_details": trade_inv[11],
        "trade_id": 11,
        "trader": "kuldeep"
    },
    12: {
        "asset_class": "Physicalrealestate",
        "counterparty": "seller",
        "instrument_id": "MLS",
        "instrument_name": "MLSlistings",
        "trade_date_time": dt.datetime.now(),
        "trade_details": trade_inv[12],
        "trade_id": 12,
        "trader": "aayush"
    },
    13: {
        "asset_class": "Commodities",
        "counterparty": "buyer",
        "instrument_id": "GC",
        "instrument_name": "COMEXGoldFutures",
        "trade_date_time": dt.datetime.now(),
        "trade_details": trade_inv[13],
        "trade_id": 13,
        "trader": "manoj"
    },
    14: {
        "asset_class": "currencies",
        "counterparty": "seller",
        "instrument_id": "usd",
        "instrument_name": "usdollar",
        "trade_date_time": dt.datetime.now(),
        "trade_details": trade_inv[14],
        "trade_id": 14,
        "trader": "om"
    },
    15: {
        "asset_class": "cryptocurrencies",
        "counterparty": "buyer",
        "instrument_id": "btc",
        "instrument_name": "bitcoin",
        "trade_date_time": dt.datetime.now(),
        "trade_details": trade_inv[15],
        "trade_id": 15,
        "trader": "nitish"
    }
}
# The above code is defining a dictionary named "inventory" which contains 15 key-value pairs. Each key represents a unique trade ID and the corresponding value is a dictionary containing details about the trade such as asset class, counterparty, instrument ID, instrument name, trade date and time, trade details, and trader.

"""
This is a Python function that returns a dictionary with a key "data" and value "success" when the
endpoint "/" is accessed using the GET method.
:return: A dictionary with a key "data" and a value "success" is being returned.
"""
@app.get("/")
def home():
    return {"data": "success"}


"""
This function retrieves a list of trades from an inventory with pagination options.
:param limit: The number of trades to be returned in a single page, defaults to 10
:type limit: int (optional)
:param offset: The starting index of the trades to be returned. It determines which trade to start
from in the list of trades, defaults to 0
:type offset: int (optional)
:return: A dictionary containing a list of trades and pagination information, including the total
number of pages, previous and next URLs based on the provided limit and offset parameters.
"""
@app.get("/get-trade/")
def get_trades(limit: int = 10, offset: int = 0):
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

"""
This function retrieves a trade item from the inventory based on its ID.   
:param item_id: This is a parameter for the endpoint "/get-trade/id/{item_id}". It is a required
integer parameter that represents the ID of the item that the user wants to retrieve from the
inventory. The function returns the item with the specified ID from the inventory dictionary
:type item_id: int
:return: The function `getbyid` returns the item in the `inventory` dictionary with the key `item_id`.
"""
@app.get("/get-trade/id/{item_id}")
def getbyid(item_id: int):
    return inventory[item_id]

"""
This function searches for trade data in an inventory based on a given name parameter and returns
the matching data.
:param name: The name parameter is a string that is used to search for trades in the inventory based
on the counterparty, instrument_id, instrument_name, or trader fields. The function returns a
dictionary of trades that match the search criteria
:type name: str
:return: The function `getbysearch` returns a dictionary containing all the trade items from the
`inventory` dictionary that match the search criteria specified by the `name` parameter. The search
criteria include matching the `counterparty`, `instrument_id`, `instrument_name`, or `trader` fields
of the trade items with the `name` parameter.
"""
@app.get("/get-trade/search")
def getbysearch(name: str):
    data = {}
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

"""
This function returns a dictionary of inventory items that belong to a specific asset class.    
:param name: The name parameter is a string that represents the asset class that the user wants to
retrieve trades for. The function filters the inventory dictionary to only include trades that
belong to the specified asset class and returns them in a dictionary format
:type name: str
:return: The function `asset` returns a dictionary containing all the items in the `inventory`
dictionary that have an `asset_class` attribute matching the `name` parameter passed to the
function.
"""
@app.get("/get-trade/assetclass")
def asset(name: str):
    data = {}
    for item_id in inventory:
        if inventory[item_id]["asset_class"] == name:
            data[item_id] = inventory[item_id]

    return data

"""
This function returns a dictionary of items from an inventory that have a trade price within a
specified range.
:param minprice: The minimum price of the item that the user is looking for in the inventory
:type minprice: float
:param maxprice: The maximum price of the trade item that the user is willing to pay for
:type maxprice: float
:return: a dictionary containing the items from the inventory whose trade_details price falls within
the specified range of minprice and maxprice.
"""
@app.get("/get-trade/price")
def price(minprice: float, maxprice: float):
    data = {}
    for item_id in inventory:
        if inventory[item_id]["trade_details"]["price"] >= minprice and inventory[item_id]["trade_details"]["price"] <= maxprice:
            data[item_id] = inventory[item_id]

    return data

"""
This function returns a dictionary of inventory items that have a specified trade type.   
:param name: The parameter "name" is a string that represents the trade type (buy or sell) that the
user wants to filter the inventory by. The function loops through the inventory dictionary and
returns a new dictionary containing only the items that have a trade type matching the input
parameter
:type name: str
:return: a dictionary containing the inventory items that have a trade type matching the input
parameter "name". The keys of the dictionary are the item IDs and the values are the corresponding
inventory items.
"""
@app.get("/get-trade/tradetype")
def tradetype(name: str):
    data = {}
    for item_id in inventory:
        if inventory[item_id]["trade_details"]["buySellIndicator"] == name:
            data[item_id] = inventory[item_id]

    return data

"""
This Python function creates a new item in an inventory dictionary if the item ID does not already
exist.    
:param item_id: An integer representing the unique identifier for the item being created
:type item_id: int
:param item: The parameter "item" is of type "Trade", which is likely a custom class or data model
that defines the properties and attributes of a trade item. It is used to pass in the details of the
item being created or added to the inventory
:type item: Trade
:return: the item that was just added to the inventory dictionary with the specified item_id. If the
item_id already exists in the inventory, an error message is returned instead.
"""
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Trade):
    if item_id in inventory:
        return{"Error": "Item already exists"}
    inventory[item_id] = item
    return inventory[item_id]

"""
:param item_id: an integer representing the unique identifier of the item to be deleted from the
inventory
:type item_id: int
:return: If the item with the given item_id is not found in the inventory, an error message is
returned. If the item is found and deleted successfully, a success message is returned.
"""
@app.delete("/delete-item")
def delete_item(item_id:int):
    if item_id not in inventory:
        return{"Error":"Item not Found"}
    del inventory[item_id]
    return{"Success":"Item Deleted"}