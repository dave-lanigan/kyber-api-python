 # kyber-api-python
 An unoffical Python wrapper for the [Kyber Network RESTful API]. (https://developer.kyber.network/docs/API_ABI-RESTfulAPI/)
 
 ### Installation:
 ```
 host:~$ pip3 install kyber
 ```
 
 ### Usage:
 ```
 >> from kyber import Klient
 >> k=Klient()
 >> k.change_24hr(pair="ETH_MANA") 
 {'timestamp': 1590713022873, 'token_symbol': 'MANA', 'token_name': 'Mana', 'token_address': '0x0f5d2fb29fb7d3cfee444a200298f468908cc942', 'token_decimal': 18, 'rate_eth_now': 0.00017415435941736, 'change_eth_24h': -7.89, 'rate_usd_now': 0.03872940716483917, 'change_usd_24h': -2.96}
 ```
 
 ### API Endpoints:
 
/buy_rate
/change24h
/currencies
/gasLimitConfig
/market
/quote_amount
/gas_limit
/sell_rate
/trade_data
/transfer_data
/users/:user_address/currencies
/users/:user_address/currencies/:currency_id/enable_data
 
