#AMDG
import requests, os
import pandas

class Klient:
    """
    Unofficial python wrapper for Kyber Network API.

    Kyber Network Developer Docs: https://developer.kyber.network/docs/

    NOTE: Much of the doc strings were taken directly from: https://developer.kyber.network/docs/API_ABI-RESTfulAPI/
    However, for more info follow the link, especially for response information.
    
    """
    
    #Endpoints:
    BUY_RATE="buy_rate"
    CHANGE_24H="change24h"
    CURRENCIES="currencies"
    GAS_LIM_CONF="gasLimitConfig"
    MARKET="market"
    QUOTE_AMOUNT="quote_amount"
    GAS_LIMIT="gas_limit"
    SELL_RATE="sell_rate"
    TRADE_DATA="trade_data"
    TRANSFER_DATA="transfer_data"
    USERS_STATUS="users/{}/currencies"
    USERS_DATA="users/{}/currencies/{}/enable_data"


    def __init__(self):
        self.baseurl = "https://api.kyber.network"
        self.kyberdocs="https://developer.kyber.network/docs/"
    
    def __str__(self):
        return "Python wrapper for Kyber Network API \n" \
        "Documentation can be found here: {}" \
        " \nVersion 1 ".format(self.kyberdocs)
    
    
    def _request_api_get(self,endpoint,params={}):
        """Used for HTML get requests.
        Arguments:
            endpoint {string}: The API endpoint
            params {dict}: URL Parameters
        Returns:
            HTML get request.
        """
        url= "{}/{}/".format(self.baseurl,endpoint)
        # if arg != "":
        #     url=url.format("{}/".format(args) )
        print(url)
        return requests.get(url,params)


    # def _request_api_post(self,endpoint,param={},arg=""):
    #     pass

        
    def get_id(self,symbol=""):
        """Returns the id associated with the symbol e.i. "ETH" or "Ethereum".
        Arguments:
            symbol {string}: The currencies symbol. Example: "ETH" or could also use "Ethereum".

        Returns:
            id {string}: The Kyber Network id for that symbol.
        """
        out=self._request_api_get( endpoint=self.CURRENCIES).json()["data"]
        for curr in out:
            if curr["symbol"]==symbol.upper():
                return curr["id"]

    def get_identity(self,id_num):
        """Returns the symbol e.i. "ETH" or "Ethereum" associated with a Kyber Network id.
        Arguments:
            id_num {string}: The Kyber Network id.
        Returns:
            name, symbol {string}:  Example: "ETH" and "Ethereum"
        """
        out=self._request_api_get( endpoint=self.CURRENCIES).json()["data"]
        for curr in out:
            if curr["id"]==id_num:
                name, symbol = curr["name"],curr["symbol"]
        
        return name, symbol


    def ping(self):
        """Test RESTful API connectivity. Reponse to the base url is 404.
        """
        out=requests.get("{}/currencies".format(self.baseurl)).ok
        if out is True:
            print("Connection Good.")
        else:
            print("Failed.")


    def buy_rate(self,symbol,qty,only_official_reserve=False):
        """Returns the latest BUY conversion rate in ETH. For example, 
        if you want to know how much ETH do you need to buy 1 DAI, 
        you can use this function.

        Parameters: [id, qty, only_official_reserve]

        Arguments:
            id {string}: The id represents the token you want to sell using ETH.
            qty {float}: A floating point number which will be rounded off to the decimals of the asset specified. 
                        The quantity is the amount of units of the asset you want to sell.
            only_official_reserve {boolean}: If no value is specified, 
                                            it will default to true. If true, the API will only return tokens 
                                            from the permissioned reserves. 
                                            If false, the API will return both permissioned reserve tokens and 
                                            also tokens that have been deployed permissionlessly.
        Returns:
            json response {dict}
        """
        params={"id":self.get_id(symbol=symbol),"qty":qty,"only_official_reserve":only_official_reserve}
        return self._request_api_get(self.BUY_RATE,params=params).json()

    def change_24hr(self,pair="",only_official_reserve=True):
        """Returns token to ETH and USD rates and percentage changes against the past day
            Arguments:
                pair {string}: Pair of currencies. Example: "ETH_MANA"
                only_official_reserve {boolean}: If no value is specified, it will default to true. If true, the API will only return tokens from the permissioned reserves. 
                If false, the API will return both permissioned reserve tokens and also tokens that have been deployed permissionlessly.
        
            Returns:
                json response {dict}
        """
        params={"only_official_reserve":only_official_reserve}
        data=self._request_api_get(self.CHANGE_24H,params).json()
        if pair =="":
            return data 
        elif pair !="":
            return data[pair]

    def currencies(self,**kwargs):
        """Returns a list of all possible tokens available for trade.

        Parameters: [only_official_reserve, include_delisted, page]

        Returns:
            json response {dict}
        """
        params={}
        if "params" in kwargs:
            params=kwargs["params"]

        return self._request_api_get( endpoint=self.CURRENCIES, params=params).json()["data"]

    def market(self,**kwargs):
        """General market json resonse. Its generally better to use the market class."""
        return  self._request_api_get(endpoint=self.MARKET)

    def qoute_amount(self,base_wallet="",qoute_wallet="",qty=0.0,side="BUY"):
        """Returns the amount of quote token needed to buy / received when selling qty amount of base token. 
            This endpoint will only work for official reserves.

        Arguments:
            base_wallet {string}:The base token contract address.
            qoute_wallet {string}: The quote token contract address.
            qty {float}: The amount of base tokens you would like to buy / sell.
            type {string}: BUY or SELL.
        Returns:
            json of response.
        """

        params={"base":base_wallet,"qoute":qoute_wallet,"qty":qty,"type":side}
        return self._request_api_get(endpoint=self.QUOTE_AMOUNT,params=params).json()["data"]
    
    def gas_limit(self,source_wallet="",dest_wallet="",amount=0.0):
        """Return the estimated Gas Limit used for a transaction based on source token amount.

        Arguments:
            source_wallet {string}: The source token contract address.
            dest_wallet {string}: The destination token contract address.
            amount {int}: The amount of source tokens.
        Returns:
            json of response.

        """
        params={"source": source_wallet, "dest": dest_wallet, "amount": amount}
        return self._request_api_get(endpoint=self.MARKET,params=params).json()["data"]


    def sell_rate(self,symbol,qty,only_official_reserve=False):
        """Returns the latest SELL conversion rate in ETH. 
            For example, if you want to know how much ETH you will get by SELLing 1 DAI, you can use this function.

        Arguments:
            id {string}: The id represents the token you want to sell using ETH.
            qty {float}: A floating point number which will be rounded off to the decimals of the asset specified. 
                        The quantity is the amount of units of the asset you want to sell.
            only_official_reserve {boolean}: If no value is specified, 
                                            it will default to true. If true, the API will only return tokens from the permissioned reserves. 
                                            If false, the API will return both permissioned reserve tokens and also tokens that have been deployed permissionlessly.
        Returns:
            json response {dict}
        """
        params={"id":self.get_id(symbol=symbol),"qty":qty,"only_official_reserve":only_official_reserve}
        return self._request_api_get(self.SELL_RATE,params=params).json()["data"]

    def trade_data(self,params={}):
        """Returns the transaction payload for the user to sign and broadcast in order to
            trade or convert an asset pair from token A to token B.

        Arguments:
            params {dict}: Because the large amount of parameters needed a single dict is recommended.
        Returns:
            json of response.

        """
        return self._request_api_get(self.TRADE_DATA,params=params).json()["data"]

    def trade_data(self,params={}):
        """Returns the transaction payload for the user to sign and broadcast in order to transfer an asset to a recipient.

        Arguments:
            params {dict}: Because the large amount of parameters needed a single dict is recommended.
        Returns:
            json of response.

        """
        return self._request_api_get(self.TRANSFER_DATA,params=params).json()["data"]

    
    def users_status(self,wallet="",enabled=True,**kwargs):
        """Returns a list of token enabled statuses of an Ethereum wallet. 
            It indicates if the wallet can sell a token or not. 
            If not, how many transactions he has to do in order to enable it.
        Arguments:
            wallet {str}: Wallet address.
        Returns:
            json of response.
        """
        params={}
        if "params" in kwargs:
            params=kwargs["params"]

        endpoint=self.USERS_STATUS
        endpoint=endpoint.format(wallet)
        print(endpoint)
        data=self._request_api_get( endpoint=endpoint,params=params).json()["data"]
        if enabled is False:
            return data
        seq=[]
        if enabled is True:
            for row in data:
                if row["enabled"] is True:
                    seq.append(row)
            return seq

    # def users_data(self,wallet="",enabled=True,**kwargs):
    #     """

    #     """
    #     params={}
    #     if "params" in kwargs:
    #         params=kwargs["params"]

    #     endpoint=self.USERS_STATUS
    #     endpoint=endpoint.format(wallet)
    #     print(endpoint)
    #     data=self._request_api_get( endpoint=endpoint,params=params).json()["data"]
    #     if enabled is False:
    #         return data
    #     seq=[]
    #     if enabled is True:
    #         for row in data:
    #             if row["enabled"] is True:
    #                 seq.append(row)
    #         return seq


class Market(Klient):
    """Class devoted to displaying responses to the market_data function 
        of the Klient class in a more effiecent manner.
    """
    def __init__(self):
        super().__init__()
        self.data=self._request_api_get( endpoint=self.MARKET).json()["data"]
        self.kyberdocs="https://developer.kyber.network/docs/"

    
    def per_token(self, symbol=""):
        for row in self.data:
            if row["quote_symbol"]==symbol.upper():
                return row
    
    def per_pair(self,pair=""):
        for row in self.data:
            if row["pair"]==pair.upper():
                return row
    



if __name__ == "__main__":

    k=Klient()
    print( k.change_24hr(pair="ETH_MANA") )


