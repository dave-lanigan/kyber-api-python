#AMDG
import requests, os

class Klient:
    """
    Kyber Network Developer Docs: https://developer.kyber.network/docs/
    """
    
    
    #Endpoints:
    BUY_RATE="buy_rate"
    CHANGE_24H="change24h"
    CURRENCIES="currencies"
    GAS_LIM_CONF="gasLimitConfig"
    MARKET="market"
    #/quote_amount
    #/gas_limit
    SELL_RATE="sell_rate"
    #/trade_data
    #/transfer_data
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
        url= "{}/{}/".format(self.baseurl,endpoint)
        # if arg != "":
        #     url=url.format("{}/".format(args) )
        print(url)
        return requests.get(url,params)


    # def _request_api_post(self,endpoint,param={},arg=""):
    #     pass

        
    def get_id(self,symbol=""):
        """You can also use the name

        """
        out=self._request_api_get( endpoint=self.CURRENCIES).json()["data"]
        for curr in out:
            if curr["symbol"]==symbol.upper():
                return curr["id"]

    def get_identity(self,id_num):
        out=self._request_api_get( endpoint=self.CURRENCIES).json()["data"]
        for curr in out:
            if curr["id"]==id_num:
                name, symbol = curr["name"],curr["symbol"]
        
        return name, symbol


    def ping(self):
        """Test RESTful API connectivity. Reponse to the base url is 404 rn.
        """
        out=requests.get("{}/currencies".format(self.baseurl)).ok
        if out is True:
            print("Connection Good.")
        else:
            print("Failed.")

            
    def currencies(self,**kwargs):
        """Returns a list of all possible tokens available for trade.

        Parameters: only_official_reserve, include_delisted, page

        Returns:
            {json dict}:

            Example:

        """
        return self._request_api_get( endpoint=self.CURRENCIES, params=kwargs["params"]).json()["data"]


    def buy_rate(self,symbol,qty,only_official_reserve=False):
        """Returns the latest BUY conversion rate in ETH. For example, 
            if you want to know how much ETH do you need to buy 1 DAI, 
            you can use this function.

        Parameters: id, qty, only_official_reserve

        Returns:

        """
        params={"id":self.get_id(symbol=symbol),"qty":qty,"only_official_reserve":only_official_reserve}
        return self._request_api_get(self.BUY_RATE,params=params).json()
        

    def users_status(self,wallet="",enabled=True,**kwargs):
        """

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

    def change_24hr(self):
        """
        """
        return self._request_api_get(self.CHANGE_24H).json()

    



if __name__ == "__main__":

    kyber=Klient()
    kyber.ping()


    #print("here")
    #print(requests.get("https://api.kyber.network/buy_rate",params={"id": "0xdd974D5C2e2928deA5F71b9825b8b646686BD200" ,"qty":300}).json() )
    #print( kyber.buy_rate(symbol="KNC",qty=300) )

    mew="0xFE9b25750A078fe4B5BbbDFD7ce362Ed80Dc1272"
    cb="0x29160778AA6cC46dFa6fBa250Ce23D6456818ff7"
    
    # print(kyber.users_status(wallet=cb))

    # ID = kyber.users_status(wallet=cb)[0]["id"]
    # print( kyber.get_identity(ID) )