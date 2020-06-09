 # kyber-api-python
 An unoffical Python wrapper for the [Kyber Network RESTful API](https://developer.kyber.network/docs/API_ABI-RESTfulAPI/).
 
 ### Installation:
 ```
 host:~$ pip3 install kybernet
 ```
 
 ### Usage:
 
 #### buy_rate() and sell_rate() functions
 Both these functions only return the buy rate in ether. The token andd the quantity are required.
 
 buy_rate() gives the amount of ETH needed to buy "qty" of "symbol".
 sell_rate() gives the amountn of ETH you will get if you sell "qty" of "symbol".
 
  ```
 >> from kyber import Klient
 >> k=Klient()
 >> k.buy_rate("USDT",5) 
[{'src_id': '0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', 'dst_id': '0xdac17f958d2ee523a2206206994597c13d831ec7', 'src_qty': [0.020763930243451224], 'dst_qty': [5]}]

>>k.sell_rate("USDT",5)
[{'src_id': '0xdac17f958d2ee523a2206206994597c13d831ec7', 'dst_id': '0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', 'src_qty': [5], 'dst_qty': [0.020614951950264353]}]
 
 ```
 
 #### change_24hr function
 ```
 >> from kybernet.client import Klient
 >> k=Klient()
 >> k.change_24hr(pair="ETH_MANA") 
 {'timestamp': 1590713022873, 'token_symbol': 'MANA', 'token_name': 'Mana', 'token_address': '0x0f5d2fb29fb7d3cfee444a200298f468908cc942', 'token_decimal': 18, 'rate_eth_now': 0.00017415435941736, 'change_eth_24h': -7.89, 'rate_usd_now': 0.03872940716483917, 'change_usd_24h': -2.96}
 ```
 
 
 
 ### API Endpoints:
 
* /buy_rate
* /change24h
* /currencies
* /gasLimitConfig
* /market
* /quote_amount
* /gas_limit
* /sell_rate
* /trade_data
* /transfer_data
* /users/:user_address/currencies
* /users/:user_address/currencies/:currency_id/enable_data

 ### Notes:
Please read the Kyber Network Developer docs for more information about the calls.

