import requests

def get_crypto_price(crypto_id):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[crypto_id]['usd']
    else:
        print('Error fetching data')
        return None

crypto_name = input("Enter name of crypto: ")
print()
price = get_crypto_price(crypto_name)
if price:
    print(f"The current price of {crypto_name} is ${price}")