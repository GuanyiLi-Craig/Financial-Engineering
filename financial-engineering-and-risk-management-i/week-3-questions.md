# Week 3 Questions

### 1._**Term structure of interest rates and swap valuation**_

Suppose the current term structure of interest rates, assuming annual compounding, is as follows:

| s1​ | s2​ | s3​ | s4​ | s5​ | s6​ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 7.0% | 7.3% | 7.7% | 8.1% | 8.4% | 8.8% |

What is the discount rate d\(0,4\)? \(Recall that interest rates are always quoted on an annual basis unless stated otherwise.\)

Please submit your answer rounded to three decimal places. So for example, if your answer is 0.4567 then you should submit an answer of 0.457.

#### Solution

Use discount rate formula

$$d(0, T) = \cfrac{1}{(1+R)^T}$$ 

where R is the fixed rate based on the contract. So, in this case

$$d(0, 4) = \cfrac{1}{(1+0.081)^4} \approx 0.732$$ 

### _**2. Swap Rates**_

Suppose a 6-year swap with a notional principal of $10 million is being configured. What is the fixed rate of interest that will make the value of the swap equal to zero. \(You should use the term structure of interest rates from Question 1.\)

#### Solution

Use swap rate formula

$$X = \cfrac{1-d(0,T)}{\displaystyle\sum_{t=1}^T d(0,t)}$$ 

Here we have the calculations

| equation | value |
| :--- | :--- |
| $$d(0, 1) = \cfrac{1}{1+0.07}$$  | 0.9346 |
| $$d(0, 2) = \cfrac{1}{(1+0.073)^2}$$  | 0.8686 |
| $$d(0, 3) = \cfrac{1}{(1+0.077)^3}$$  | 0.8005 |
| $$d(0, 4) = \cfrac{1}{(1+0.081)^4}$$  | 0.7323 |
| $$d(0, 5) = \cfrac{1}{(1+0.084)^5}$$  | 0.6681 |
| $$d(0, 6) = \cfrac{1}{(1+0.088)^6}$$  | 0.6029 |

so the answer is 8.62%

### 3 _**Hedging using futures**_

Suppose a farmer is expecting that her crop of oranges will be ready for harvest and sale as 150,000 pounds of orange juice in 3 months time. Suppose each orange juice futures contract is for 15,000 pounds of orange juice, and the current futures price is $$ F_0 = 118.65$$ cents-per-pound. Assuming that the farmer has enough cash liquidity to fund any margin calls, what is the risk-free price that she can guarantee herself. 

#### Solution:

118.65

She can go short 10 futures contracts each for 15,000 pounds. This way she can ensure that the payoff from the futures contract would remove all the uncertainty in the spot price of orange juice, and she can lock the price to **118.65** cents-per-pound.

### 4. _**Minimum variance hedge**_

Suppose a farmer is expecting that her crop of grapefruit will be ready for harvest and sale as 150,000 pounds of grapefruit juice in 3 months time. She would like to use futures to hedge her risk but unfortunately there are no futures contracts on grapefruit juice. Instead she will use orange juice futures. Suppose each orange juice futures contract is for 15,000 pounds of orange juice and the current futures price is $$ F_0 = 118.65$$ cents-per-pound. The volatility, i.e. the standard deviation, of the prices of orange juice and grapefruit juice is 20% and 25%, respectively, and the correlation coefficient is 0.7. What is the approximate number of contracts she should purchase to minimize the variance of her payoff?

#### Solution

Use minimum variance hedge formula

$$y^* = \cfrac{\mathbf{cov}(F_T, P_T)}{\mathbf{var}(F_T)}$$

where here we have 

$$\sigma_F = 20\% = 0.2 \\ \sigma_P = 25\% = 0.25\\   \mathbf{corr}(F, P) = 0.7$$ 

$$\mathbf{cov}(F_T, P_T) = \mathbf{corr}(F_T, P_T) \cdot \sigma_{F} \cdot \sigma_{P} = 0.035$$

$$\mathbf{var}(F_T) = \sigma_{F}^2 = 0.04$$

so that for one grapefruit contract, we should buy 0.875 orange contract. Here we need 10 grapefruit contracts, so the equivalent orange contracts number is $$0.875\times 10 =8.75 \approx 9$$ 

### 5._**Call Options**_

Consider a 1-period binomial model with $$R=1.02, S_0 = 100,u=1/d= 1.05$$ . Compute the value of a European call option on the stock with strike K=102. The stock does not pay dividends.

#### Solution

The arbitrage free call option equation is  

$$C_0 = \cfrac{1}{R} [\cfrac{R-d}{u-d}C_u + \cfrac{u-R}{u-d}C_d]  \approx 2.0373$$ 

Where $$C_u = 1.05 * S_0 - K = 3, C_d = 0$$ 

### 6. _**Call Options II**_

When you construct the replicating portfolio for the option in the previous question how many dollars do you need to invest in the cash account?

#### Solution

We can construct derivative security pricing function  

 $$\begin{cases}uS_0x + Ry = C_u \\ dS_0x + Ry = C_d \end{cases}$$

So that we have  

 $$\begin{cases}105x + 1.02y = 3 \\95.24x + 1.02y = 0 \end{cases}$$

by solving this linear equation we have 

 $$\begin{cases}x \approx 0.3073\\ y \approx -28.694 \end{cases}$$

