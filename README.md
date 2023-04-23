
# FastAPI 
The code uses FastAPI to create an inventory management system for trades with Pydantic models to validate requests and responses, and dictionaries to store trade details.


## Installation

You must install the following modules in order to use this rest API.

```bash
  pip install fastapi
```
```bash
  pip install uvicorn
```
Create the App component
```bash
app = FastAPI()
add_pagination(app)
```
Run the program:
```bash
uvicorn main:app --reload
```
This will start the program on http://localhost:8000/.

    
## Models
This API uses two Pydantic models - TradeDetails and Trade. TradeDetails model contains the details of the trade, such as the buy/sell indicator, price, and quantity. The Trade model contains the overall details of the trade, such as asset class, counterparty, instrument ID and name, trade date-time, trade details, trade ID, and trader.
```bash
class TradeDetails(BaseModel):
    buy_sell_indicator: str
    price: float
    quantity: float

class Trade(BaseModel):
    asset_class: str
    counterparty: str
    instrument_id: str
    name: str
    trade_datetime: str
    trade_details: TradeDetails
    trade_id: str
    trader: str
```
# Features

When you launch the server, it will return: A dictionary containing the key "data" and the value "success"
```bash
@app.get("/")
def home():
    return {"data":"success"}
```
### Get All Trades by Pagination
This endpoint retrieves a list of trades from an inventory with pagination options.
```bash
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
```
Output: 
```bash
"pagination": {
    "total_pages": 3,
    "previous": null,
    "next": "/get-trade/?limit=5&offset=0"
  }
```
### Get By Id
This function that retrieves a trade item from an inventory based on its ID.

The function is associated with the endpoint "/get-trade/id/{item_id}". It takes a required integer parameter item_id, which represents the ID of the item that the user wants to retrieve from the inventory. The function then returns the item with the specified ID from the inventory dictionary.
```bash
@app.get("/get-trade/id/{item_id}")
def getbyid(item_id: int):
    return inventory[item_id]
```
URL:
```bash
localhost/get-trade/id/1
```
Output: The data which have id 1 will be shown the value of id can be changed by user.
```bash
{
  "asset_class": "Largecap",
  "counterparty": "buyer",
  "instrument_id": "AAPL",
  "instrument_name": "Apple",
  "trade_date_time": "2023-04-23T15:53:48.856525",
  "trade_details": {
    "buySellIndicator": "Sell",
    "price": 29.99,
    "quantity": 10
  },
  "trade_id": 1,
  "trader": "Arun"
}
```

### API Endpoint for Searching Trade Data
This FastAPI function is used to search for trade data in the inventory based on a given name parameter and returns the matching data. The name parameter is a string that is used to search for trades in the inventory based on the counterparty, instrument_id, instrument_name, or trader fields. The function returns a dictionary of trades that match the search criteria.
```bash
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
```
URL: localhost:8000/get-trade/search?name=Roshan

Output:
```bash
{
  "2": {
    "asset_class": "Midcap",
    "counterparty": "seller",
    "instrument_id": "FTNT",
    "instrument_name": "Fortinet",
    "trade_date_time": "2023-04-23T15:53:48.856525",
    "trade_details": {
      "buySellIndicator": "Buy",
      "price": 34.99,
      "quantity": 20
    },
    "trade_id": 2,
    "trader": "Roshan"
  }
}
```



### API for Filtering Inventory Trades
TThis code implements a simple API that allows a user to filter an inventory of trades using various criteria. The inventory is stored as a dictionary, where each key represents a unique item ID and the corresponding value is a dictionary of the item's attributes, including its trade details.

The API provides three endpoints, each of which accepts specific parameters to filter the inventory:

#### /get-trade/assetclass
This endpoint accepts a name parameter, which is a string representing the asset class the user wants to retrieve trades for. The function filters the inventory dictionary to only include trades that belong to the specified asset class and returns them in a dictionary format.
```bash
@app.get("/get-trade/assetclass")
def asset(name:str):
    data = {}
    for item_id in inventory:
        if inventory[item_id]["asset_class"] == name:
            data[item_id]=inventory[item_id]

    return data
```
URL: 
```bash
loaclhost:8000/get-trade/assetclass?name=Largecap
```
Output:
```bash
{
  "1": {
    "asset_class": "Largecap",
    "counterparty": "buyer",
    "instrument_id": "AAPL",
    "instrument_name": "Apple",
    "trade_date_time": "2023-04-23T16:08:13.734061",
    "trade_details": {
      "buySellIndicator": "Sell",
      "price": 29.99,
      "quantity": 10
    },
    "trade_id": 1,
    "trader": "Arun"
  }
}
```
#### /get-trade/price
This endpoint accepts minprice and maxprice parameters, which are floats representing the minimum and maximum trade price the user is interested in. The function filters the inventory dictionary to only include trades whose price falls within the specified range and returns them in a dictionary format.

URL
```bash
loaclhost:8000/get-trade/price?minprice=20.00&maxprice=80.00
```
Output: This will return all the data which has price range of 20.00 <= data <= 80.00

#### /get-trade/tradetype

URL :
```bash
/get-trade/tradetype?name=Sell
```
Output: This will return all the data which tradetype value of sell like this

#### Post item
Based on the pydantic class concept, this API allows users to build and publish their own data. It will determine whether or not the data at item id is there, and if not, it will create the item.
```bash
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Trade):
    if item_id in inventory:
        return{"Error": "Item already exists"}
    inventory[item_id] = item
    return inventory[item_id]
```
To Create item

First go to docs 
```bash
http://127.0.0.1:8000/docs
```
Then choose Post item, and from there you may create an item by providing an item add and all other options.

#### Delete item

This function deletes an item from the inventory dictionary based on the provided item ID. 

```bash
@app.delete("/delete-item")
def delete_item(item_id:int):
    if item_id not in inventory:
        return{"Error":"Item not Found"}
    del inventory[item_id]
    return{"Success":"Item Deleted"}
```

To delete item
First go to docs 
```bash
http://127.0.0.1:8000/docs
```
Then choose Delete item, and from there you can delete item.