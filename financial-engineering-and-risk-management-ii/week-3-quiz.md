# Week 3 Quiz

## Instructions

Download the spreadsheet [EquityDerivsPractice\_PSet3.xlsx](https://d396qusza40orc.cloudfront.net/fe2/class_resources/EquityDerivsPractice_PSet3.xlsx) from the Course platform. The first worksheet, _"DemoSheet"_, displays the profit and loss from selling 100,000 European call options and then delta-hedging these options by following a self-financing trading strategy that attempts to replicate the payoff of these options. The details are given in the slides and one of the video modules. You can use the results in this worksheet to debug your Excel calculations for the questions below.

In the second worksheet, _"StockPricePaths"_, you will find four new price paths for the security. Your task in the questions below is to determine the performance of the delta-hedging strategy for each of these four price paths and relate the performance to the _realized volatility_ of each price path.

Once you have completed this quiz you should compare the realized volatilities with the implied volatility parameter \(30% in the spreadsheet\) that was used to price the options initially and construct the self-financing hedging strategies.

In particular, you should note what sort of price paths \(high volatility or low volatility\) tend to lead to an ultimate hedging profit and which types tend to lead to a loss. \(Note that once you have completed the quiz you can also start experimenting with this implied volatility parameter if you wish to do so. You may also want to try to generalize your Excel formulas to handle an arbitrary number of hedging periods \(currently 50\) as well as European put options.\)

### Tips

In this exercise we are selling \(i.e. shorting\) 100.000 EU call options written on the stock\(s\) we are given. The investor who buys \(i.e. goes long\) our options has the right to buy from us the underlying stock \(100.000 times\) at maturity at price K, and he does so if at maturity S&gt;K. Therefore, when S&gt;K we are making a loss. Now, we use a self-financing strategy \(aka delta-hedge the option\) to reduce the loss in case S&gt;K at maturity. The self-financing strategy involves going long \(i.e. buying\) delta\*100.000 number of shares of the underlying stock by borrowing money at the interest rate r \(usually called the risk-free rate in the Black-Scholes setup\).

More specifically to put that into the context using the example of the stock path in your assignment. We receive $310.815 from selling the options. At maturity the stock price turns out to be $54.41 which is greater than the agreed strike price of $50. The option holder will exercise the option, and therefore, we are obliged to sell to him 100.000 shares of the stock at the price of $50 each, which we need to buy from the stock market for the price of $54.41 per share. This implies that we make a loss equal to $440.787 \[=\(54.41-50.0\)\*100000\] from selling the option. Since we employed a delta hedging strategy though, the replicating portfolio we created at the beginning of the hedging period, has now reached a value of $496.181 in stocks and cash. We therefore end up with an overall profit of $55.394 \[= 496.181 - 440.787\].

\(A\) For the **Black-Scholes Call Option Price \(cell B10 and F2\)**, you need to use the 1st, 2nd and 3rd formulas found in the 2nd slide on the slides named 'The Greeks: Delta and Gamma'. The N\(d1\) function is the Standard Normal CDF and you can use Excel's built in function NORM.DIST\('d1',0,1,TRUE\). The same holds for N\(d2\).

\(B\) To understand how to compute **Δt**, as well as **annualized average returns** and **annualized standard deviation of returns**, please read this post: [https://www.coursera.org/learn/financial-engineering-2/discussions/weeks/3/threads/JF5aOAeEEee36g5uvZCkbA/replies/GyLV6QjaEee36g5uvZCkbA](https://www.coursera.org/learn/financial-engineering-2/discussions/weeks/3/threads/JF5aOAeEEee36g5uvZCkbA/replies/GyLV6QjaEee36g5uvZCkbA)

**\(C\) d1 \(column G\)** is computed using the 2nd formulas found in the 2nd slide on the slides named 'The Greeks: Delta and Gamma'. The only tricky part in the calculations of d1 is that in every period, you need to change S0 and T. More specifically, S0 will be the current period’s stock price, and T must be the remaining time until maturity \(i.e. for t=1 onwards, it must be the previous maturity minus Δt\). Finally, regarding d1, please make sure that you use the Excel’s function LN\(.\) for the calculations, not the LOG\(.\) one.

\(D\) For the calculation of **delta**, please use the 1st equation in slide 3 on the slides named 'The Greeks: Delta and Gamma'.

\(E\) From the above explanation \(see first paragraph\), it should be clear now that the **number of stocks held \(column H\)** at every period is delta times the number of options \(i.e. 100000 in our case\). So, to compute the number of stocks held, you basically only need to compute delta for every period.

\(F\) Regarding the **Cash Account $ Position \(column I\)**, we said that the self-financing strategy \(delta-hedge the option\) involves buying delta stocks for each one option we hold or sell. To buy these stocks we use the money from our portfolio \(i.e. S.F. Portfolio Value\) but if they exceed the money we have, we borrow the rest. Therefore, our cash account position at every period is:

-for one option: Vi – δi\*Si -for 100.000 options: Vi – δi\*100.000\*Si

Which is basically: ‘S.F. Portfolio Value’ – ‘Stock Position Value’ The ‘Cash Account $ Position’ \(i.e. the quantity invested in the cash account\) is discussed in the video corresponding to the ‘Delta-Hedging’ titled slides, slide number 3 \(see equation 11\). Note though that equation 11 holds for 1 option and therefore you need to adjust for the number of options you have in the exercise.

\(G\) Briefly, the formulas for calculating the **self-financing portfolio value \(column F\)** are:

- for i=0: V0\(S0, σ0\) = BS\(S0, r, c, K, σ0, T\) Note that the **self-financing portfolio value at time t=0** \(i.e. cell F2\) **is the same as the Black-Scholes option price \(i.e. cell B10\).** - for i&gt;=1: Vi+1 = Vi + δi\*\(Si+1 + SicΔt - Si\) + \(Vi - δiSi\)\*discount\_factor Since c=0, we have that: Vi+1 = Vi + δi\*\(Si+1 - Si\) + \(Vi - δiSi\)\*discount\_factor Note that the above equation is for holding 1 option. But here we have 100.000 options. Therefore, you must do the proper adjustments: Vi+1 = Vi + \(δi**\*100.000**\)\*\(Si+1 - Si\) + \(Vi – δi**\*100.000**\*Si\)\*discount\_factor Which basically is: Vi+1 = Vi + \(\# Stocks held\)\*\(Si+1 - Si\) + \(Cash Account $ Position\)\* discount\_factor

where discount\_factor = \(e^rΔt - 1\). Please also see the ‘Delta-Hedging’ titled slides, slide number 3 for the equations.

\(H\) Now, regarding the Option Payoff and the **Total Hedging P&L \(cell B11\)**:

In the exercise, the stock price at maturity turns out to be $54.41, which is higher than the strike price K=$50 agreed on the option. This means that the investor who bought the call option from us will exercise it. He will exercise it because by doing so he makes a profit from the option contract he paid for. On the other hand, we will make a loss. The loss we will make from selling the option contract is equal to the profit the investor will make \(excluding the money we received for selling the option, and similarly the money the investor paid for buying the option contract from us\). What do we need to pay to the option buyer \(i.e. what is his payoff\)? The option payoff for every call option is the difference between the option price at maturity and the strike price. Mathematically, the option payoff is:

Option Payoff = MAX\(0, S-K\)\*\(\#of shares embedded in the option\)

So we need to pay the Option Payoff to the option buyer, but we were smart enough to delta-hedge the option in case we had to incur this loss. The gains from delta-hedging the option are the gains of the S.F. Portfolio Value at time T \(i.e. the maturity of the option\), here $496,181. Therefore, the Total Hedging P&L is:

Total Hedging P&L = \(S.F. Portfolio Value at time T\) – Option Payoff Total Hedging P&L = \(S.F. Portfolio Value at time T\) – MAX\(0, S-K\)\*\(100.000\)

## Quiz 1

Compute the annualized realized volatility of the log-returns for price path \#1



