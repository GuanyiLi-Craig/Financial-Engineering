# Statistical Biases and Potential Pitfalls

## Examples

### Recall Binomial Model

We say $$X$$ has a binomial distribution, or $$X \sim \text{Bin}(n, p)$$, if

$$\text{P}(X = r)  = \dbinom{n}{r} p^r (1-p)^{n-r}$$ 

The mean and variance of the binomial distribution satisfy

 $$\mathsf{E}[X] = n\cdot p \\ \mathsf{Var}(X) = n \cdot p \cdot (1-p)$$ 

So that

$$\mathsf{P} (X \geq r) = \displaystyle\sum_{i=r} ^n \dbinom{n}{i} p^i (1 - p)^{n-1}$$ . 

### M Fund Managers

Suppose instead there are M fund managers and that the manager who claims to have skill has the best track record of these managers. Assuming none of the managers have skill let:

* $$Z_i \equiv $$ event that $$i^{th}$$ manager out-performs in $$\geq r$$ years out of $$n$$ 
* $$V \equiv $$ event that the best manager out-performs in $$\geq r$$ years out of $$n$$ 

then

$$\mathsf{P}(V) \; = \; 1 - \mathsf{P}(\bar{Z}_1, \bar{Z}_2, ..., \bar{Z}_M)  \\ \quad \quad \quad = 1 - \big(\mathsf{P}(\bar{Z}_1) \big) ^ M \\ \quad \quad \quad = 1 - \big[ 1 - \mathsf{P}(Z_1) \big]^M$$ 

## Compute the Average Return

In financial markets expected returns often decrease as dollars invested increase.

This is because liquidity of a market or “capacity” of a trading strategy is not unbounded

* not always obvious to the small investor who only invests in liquid markets
* and therefore does not “move” the market.

Large investors often do “move” the market

* and the larger they are, the more they move it
* the more illiquid the market is, the more they move it
* so the cost per security increases with the number of securities they buy
* and the cost per security decreases with the number of securities they sell.

This implies that returns decrease as dollars invested increases.

* The question of how to compute average returns is important.
* Depending on how you answer it, certain types of investing can seem more   or \(much\) less attractive

e.g. the hedge fund industry

* in aggregate, they would prefer to report average returns over time
* and so they do.
* but for investors, the average \(net\) return per dollar invested is surely   more meaningful.

This has caused some controversy and debate

* there are good financial blogs that cover these topics and others
* see for example discussion at   [here](http://blogs.reuters.com/felix-salmon/2012/08/08/why-investors-should-avoid-hedge-funds/)

## Survivorship Bias and Data Snooping

### Survivorship Bias

Consider the following investment: purchase an equi-weighted portfolio of the top 20 stocks in the S&P 500.

* note that the stocks are chosen and fixed today.

In order to estimate the performance of this investment you decide to back-test it as follows:

* Get the last 20 years of daily return data for each of the 20 stocks
* On the first day, i.e. 20 years ago, set up the initial equi-weighted portfolio
  * if the stock, e.g. Google, did not yet exist then omit it from the portfolio     until it does exist.
* Every month rebalance the portfolio so that it remains equi-weighted
  * and take transactions costs into account.
* Plot the annual net returns, i.e. $$r_t$$ against $$t$$ where $$r_t$$ is the net return at   time $$t$$ realized over the previous year, of this back-test

### Data Snooping

A bank has 4 years worth of daily historical return data on USD-GBP exchange rate. It employs the following mechanism for generating a trading strategy:

* It first normalizes the entire return data so that it has mean 0 and variance 1 
  * \(normalizing data is a standard and well justified statistical technique\)
* 75% of the data, i.e. approx 750 returns, is kept for the training set
  * used for finding the trading strategy.
* Remaining 25%, i.e. approx 250 returns, is kept as a hold-out test set
  * used to evaluate whatever strategy is yielded by the training data.

The trading strategy appears to be a great success: on any given day it uses the returns of the previous 20 days to forecast the direction of the next day’s return.

But the trading strategy performs **poorly** in practice.

### Another Examples of Statistical Biases/Difficulties

* Good risk management always needs to be aware of statistical biases
  * survivorship bias and data snooping are everywhere!
* And how meaningful are statements such as:
  * “the stock market has never fallen over any 20-year period”?
* Just how likely is a 25 standard deviation move?
  * the size of the move as reported by some participants in August 2007
  * how likely is a 25 standard deviation move several days in a row \(!\)?
* The market for retail structured products
  * often structured as a note that pays a coupon tied to the performance of     another asset
  * often designed to look better than they are, i.e. they tend to
  * they invariably backtest very well
    * e.g. any structured product that is long Apple will presumably back-test very well       from 2000 onwards
  * investor often exposed to hidden risks, e.g. volatility risk and credit risk
  * often too expensive \(too many "middle men" and no price transparency\)
  * and no secondary market available in case you need to sell.

