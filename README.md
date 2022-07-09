# Intrinsic Value of a Stock Calculator
This project uses Benjamin Graham's equation for calculating the intrinsic value of a stock. The program utilizes the original equation, as well as an updated version of the equation.

## Equation
$V = \frac{EPS \times (8.5 + 2g) \times 4.4}{Y}$ \
$V$ = intrinsic value \
$EPS$ = earnings per share \
8.5 = base for a no-growth company (7 in the updated version) \
$g$ = grwoth rate for the next five years (estimation) \
4.4 = average yield of AAA corporate bonds \
$Y$ = current yield of AAA corporate bonds

## API
This project uses the yahoofinance API (yfinance) to pull stock prices, corporate bond yields, etc.