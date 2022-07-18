import requests

def current_price(amt,curr):
    # making get request on endpoint: 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

    coins =  {
        "eth":"ethereum",
        "btc":"bitcoin",
        "xrp":"ripple"
    }


    curr = curr.lower()

    if curr not in coins:
        return 0 , False
    
    coin = coins[curr]

    data = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd").json()
    #{'bitcoin': {'usd': 22185}}
    print(data,"#######")
    amt = round(float(amt) * data[coin]['usd'])
    print(amt)
    
    return amt , True







