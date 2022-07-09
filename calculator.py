import math
import sys
import pandas as pd
import yfinance as yf

''' The original equation for finding the intrinsic value of a stock (Benjamin Graham) '''
def intrinsic_value_equation_original(eps, growth_rate, current_corporate_bonds_yield):
	base_no_growth = 8.5
	average_corporate_bonds_yield = 4.4

	intrinsic_value = (eps*(base_no_growth + 2*growth_rate)*average_corporate_bonds_yield)/current_corporate_bonds_yield

	return intrinsic_value

''' The updated equation for finding the intrinsic value of a stock '''
def intrinsic_value_equation_updated(eps, growth_rate, current_corporate_bonds_yield):
	base_no_growth = 7
	average_corporate_bonds_yield = 4.4

	intrinsic_value = (eps*(base_no_growth + 1*growth_rate)*average_corporate_bonds_yield)/current_corporate_bonds_yield

	return intrinsic_value

def buy_or_sell_position(stock_current_price, stock_intrinsic_value):
	margin_of_safety = 35

	difference = (stock_current_price/stock_intrinsic_value) * 100

	acceptable_buy_price = (100 - margin_of_safety) / 100 * stock_intrinsic_value

	buy_or_sell = ""

	if stock_current_price < acceptable_buy_price:
		buy_or_sell ="BUY"
	else:
		buy_or_sell ="SELL"

	print("----------------------------------------------------------------")
	print("Intrinsic Value of Stock:\t{0:.2f}".format(stock_intrinsic_value))
	print("Current Stock Price:\t\t{0:.2f}".format(stock_current_price))
	print("Difference:\t\t\t{0:.2f}".format(difference))
	print("Margin of Safety:\t\t{0:.2f}".format(margin_of_safety))
	print("Acceptable Buy Price:\t\t{0:.2f}".format(acceptable_buy_price))
	print("Buy or Sell?:\t\t\t{0}".format(buy_or_sell))

	return 0

def single_stock():
	stock_name = input("Please enter a stock ID: ").upper()
	stock = yf.Ticker(stock_name).info
	eps = stock['trailingEps']
	growth_rate = stock['revenueGrowth'] * 100

	corporate_bond = yf.Ticker("VCIT").info
	current_corporate_bonds_yield = corporate_bond['bondRatings'][2]['aaa'] * 100

	original_intrinsic_value = intrinsic_value_equation_original(eps=eps, growth_rate=growth_rate, current_corporate_bonds_yield=current_corporate_bonds_yield)
	new_intrinsic_value = intrinsic_value_equation_updated(eps=eps, growth_rate=growth_rate, current_corporate_bonds_yield=current_corporate_bonds_yield)

	print("----------------------------------------------------------------")
	print("Stock:\t\t\t{0}".format(stock_name))
	print("Original equation:\t{0:.2f}".format(original_intrinsic_value))
	print("Updated equation:\t{0:.2f}".format(new_intrinsic_value))
	print("----------------------------------------------------------------")

	stock_current_price = stock['currentPrice']

	print("\n----------------------------------------------------------------")
	print("\t\tOriginal Equation")
	buy_or_sell_position(stock_current_price=stock_current_price, stock_intrinsic_value=original_intrinsic_value)

	print("\n----------------------------------------------------------------")
	print("\t\tNew Equation")
	buy_or_sell_position(stock_current_price=stock_current_price, stock_intrinsic_value=new_intrinsic_value)

	return 0

def multiple_stocks():
	stocks = []
	print("Please enter up to 10 stocks (if you want to stop type 'stop', 'STOP', or '')")
	print("----------------------------------------------------------------")

	for i in range(10):
		stock = input("Please enter a stock ID: ").upper()
		if stock == 'STOP' or stock == '':
			break
		else:
			stocks.append(stock)

	print("----------------------------------------------------------------")

	print(stocks)

	return 0

if __name__ == "__main__":
	single_stock()
	#multiple_stocks()