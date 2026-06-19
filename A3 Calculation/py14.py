cost_price,sell_price=map(int,input("Enter the cost price and sell price").split())
profit_percent=(sell_price-cost_price)/cost_price*100
print("Cost Price:",cost_price)
print("Sell Price:",sell_price)
print("Profit Percent:",profit_percent)