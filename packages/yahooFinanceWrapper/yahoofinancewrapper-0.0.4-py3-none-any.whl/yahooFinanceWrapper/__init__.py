import requests

base_url = "https://api.maddaxlallatin.com/stock/v1/"


def getEndpoint(url):
    response = requests.request("GET", url, headers={}, data={})
    return response.json()

def getTrending():
    url = base_url + "trending"
    return getEndpoint(url)
def getGainers():
    url = base_url + "gainers"
    return getEndpoint(url)
def getLosers():
    url = base_url + "losers"
    return getEndpoint(url)
def getSectors():
    url = base_url + "sectors"
    return getEndpoint(url)

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.url = base_url + ticker
    def getPrice(self):
        return getEndpoint(self.url+"/price")
    def getHistory(self, start_date=None, end_date=None):
        if start_date and end_date:
            return getEndpoint(self.url+"/history?start_date="+start_date+"&end_date="+end_date)
        else:
            return getEndpoint(self.url+"/history")
    def getProfile(self):
        return getEndpoint(self.url+"/profile")
    def getNews(self, number=10):
        return getEndpoint(self.url+"/news?number="+str(number))
    def getAnalystRecommendations(self):
        return getEndpoint(self.url+"/analyst-recommendations")
    def getEarnings(self):
        return getEndpoint(self.url+"/earnings")
    def getDividends(self, number=15):
        return getEndpoint(self.url+"/dividends?number_dividends="+str(number))
    def getFinancials(self, income_statement=True, balance_sheet=True, cash_flow=True):
        return getEndpoint(self.url+"/financials?income_statement="+str(income_statement)+"&balance_sheet="+str(balance_sheet)+"&cash_flow="+str(cash_flow))

appleStock = Stock("AAPL")
print(appleStock.getFinancials())
