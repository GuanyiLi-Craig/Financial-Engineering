---
description: >-
  https://www.coursera.org/learn/financial-engineering-1/exam/gTDDd/introduction-to-basic-fixed-income-securities
---

# Week 2 Questions

### 1. _**Lottery payments**_

A major lottery advertises that it pays the winner $10 million. However this prize money is paid at the rate of $500,000 each year \(with the first payment being immediate\) for a total of 20 payments. What is the present value of this prize at 10% interest compounded annually?

#### Solution: 

apply the present value equation

$$PV(\vec{c},r) = \displaystyle\sum_{k=0}^N \cfrac{c_k}{(1+r)^k} = \displaystyle\sum_{k=0}^{19} \cfrac{0.5M}{(1+0.1)^k} = 4.6825M$$ 

### _**2. Sunk Costs \(Exercise 2.6 in Luenberger\)**_

A young couple has made a deposit of the first month's rent \(equal to $1,000\) on a 6-month apartment lease. The deposit is refundable at the end of six months if they stay until the end of the lease. The next day they find a different apartment that they like just as well, but its monthly rent is only $900. And they would again have to put a deposit of $900 refundable at the end of 6 months. They plan to be in the apartment only 6 months. Should they switch to the new apartment? Assume an \(admittedly unrealistic!\) interest rate of 12% per month compounded monthly.

#### Solution: 

use net present value \(NPV\). 

if stay, they pay 1000 per month at the first day of a month and get 1000 back after 6 months. So the cash flow should be 

$$C_1 = -\displaystyle\sum_{k=0}^5 \cfrac{1000}{1.12^k} + \cfrac{1000}{1.12^6} \approx -4222$$ 

If moved to 900, then they have to pay 900 right now and get it back 6 months later. The cash flow will be 

$$C_2 = -900 -\displaystyle\sum_{k=0}^{5}\cfrac{900}{1.12^k} + \cfrac{900}{1.12^6} \approx -4700$$ 

So they should stay

### _**3. Relation between spot and discount rates**_

Suppose the spot rates for 1 and 2 years are $$s_1 = 6.3\%$$ and $$s_2 = 6.9\%$$ with annual compounding. Recall that in this course interest rates are always quoted on an annual basis unless otherwise specified. What is the discount rate $$d(0,2)$$?

#### Solution

Discount rate considers the total years. Here only $$s_2$$ will be used. 

$$d(0, 2) = \cfrac{1}{(1+s_2)^2} = \cfrac{1}{1.069^2} \approx 0.8751$$ 

### _**4. Relation between spot and forward rates**_

Suppose the spot rates for 1 and 2 years are $$s_1 = 6.3\%$$ and $$s_2 = 6.9\%$$ with annual compounding. Recall that in this course interest rates are always quoted on an annual basis unless otherwise specified. What is the forward rate,  $$f_{1,2}$$ assuming annual compounding?

#### Solution

Directly apply forward rate equation

$$f_{uv} = (\cfrac{(1+s_v)^v}{(1+s_u)^u})^{\cfrac{1}{v-u}} - 1 = (\cfrac{(1+s_2)^2}{1+s_1})^{\cfrac{1}{2-1}} - 1 \approx 0.075 = 7.5\%$$

### _**5. Forward contract on a stock**_

The current price of a stock is $400 per share and it pays no dividends. Assuming a constant interest rate of 8% per year compounded quarterly, what is the stock's theoretical forward price for delivery in 9 months?

#### Solution

Directly apply forward price

$$F = \cfrac{S_0}{d(0, T)} = \cfrac{400}{\cfrac{1}{(1+0.08/4)^3}} \approx 424.4832$$ 

### _**6. Bounds using different lending and borrowing rate**_

Suppose the borrowing rate $$r_B = 10\%$$ compounded annually. However, the lending rate \(or equivalently, the interest rate on deposits\) is only 8% compounded annually. Compute the difference between the upper and lower bounds on the price of a perpetuity that pays A = 10,000$ per year.

#### Solution

Here we need to consider perpetuity situation, the corresponding present value for lending and borrowing are

$$PV_B(A, r_B) = \cfrac{A}{r_B} = 125,000, \\ PV_L(A, r_L) = \cfrac{A}{r_L} = 100,000$$ 

So that the difference is 25,000.

### _**7. Value of a Forward contract at an intermediate time**_

Suppose we hold a forward contract on a stock with expiration 6 months from now. We entered into this contract 6 months ago so that when we entered into the contract, the expiration was T=1 year. The stock price at 6 months ago was $$S_0 = 100,$$ the current stock price is 125 and the current interest rate is r=10% compounded semi-annually. \(This is the same rate that prevailed 6 months ago.\) What is the current value of our forward contract?

#### Solution

Apply forward value equation

$$f_t = (F_t - F_0) \cdot d(t,T)$$ where

$$F_t = \cfrac{S_t}{d(t, T)}$$ 

So we have 

$$f_t = (\cfrac{S_t}{d(t, T)} - \cfrac{S_0}{d(0, T)})\cdot d(t, T) \\ = (\cfrac{125}{\cfrac{1}{1+0.1/2}} - \cfrac{100}{\cfrac{1}{(1+0.1/2)^2}})*\cfrac{1}{1+0.1/2} \\ = 125 - \cfrac{100}{1/1.05} \\ = 20$$ 

