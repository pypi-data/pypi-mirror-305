import yahooFinanceWrapper_maddaxlallatin as YahooFinance

print(YahooFinance.getTrending())

appleStock = YahooFinance.Stock("AAPL")
print(appleStock.getFinancials())
