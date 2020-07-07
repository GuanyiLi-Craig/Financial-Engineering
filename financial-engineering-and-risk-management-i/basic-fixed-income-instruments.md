# Basic Fixed Income Instruments

## Floating Rate Bonds and Term Structure of Interest Rates

### Linear Pricing

**Theorem**. \(**Linear Pricing**\) Suppose there is no arbitrage. Suppose also

* Price of cash flow $$c_A$$ is $$p_A$$
* Price of cash flow $$c_B$$ is $$p_B$$ 

Then the price of cash flow that pays $$c = c_A + c_B$$ must be $$p_A + p_B$$. 

Otherwise, it will create a arbitrage portfolio. 

#### Simple Example of Linear Pricing

Cash flow $$\vec{c} = (c_1, c_2, c_3, ..., c_T)$$is a portfolio of $$T$$separate cash flows , we define

* $$\vec{c^{(t)}}$$ pays $$c_t$$at time $$t$$and zero otherwise

Suppose the cash flows are annual and the annual interest rate is $$r$$. 

* Price of the cash flow $$\vec{c^{(t)}} = \cfrac{c_t}{(1+r)^t}$$
* Price of cash flow $$\vec{c} = \displaystyle\sum_{t=1}^{T} \cfrac{c_t}{(1+r)^t}$$

### Floating Interest Rates

Interest rate are random quantities. They fluctuate with time. Here is some assumptions

Let $$r_k$$denote the per period interest rate over period $$[k, k+1)$$

* The exact value of $$r_k$$becomes known only at time $$k$$
* 1-period loans issued in period $$k$$ to be repaid in period $$k+1$$ are charged $$r_k$$

**Cash flow** of floating rate bond

* coupon payment at time $$k$$ : $$r_{k-1} F$$
* face value at time $$n$$ : $$F$$

**Goal** : Compute the no-arbitrage price $$P_f$$ of the floating rate bond

#### **Solution**:

**Split up the cash flows** of floating rate bond into simpler cash flows

* $$p_k=$$ Price of contract paying $$r_{k-1}F$$ at time $$k$$
* $$P=$$ Price of principal $$F$$ at time $$n=\cfrac{F}{(1+r_0)^n}$$
  * where $$r_0$$ is the interest rate at time 0

**Price of floating rate bond** $$P_f = P + \displaystyle\sum_{k=1}^{n}p_k$$ 

Now we want to construct a portfolio that has a **deterministic** cash flow

* The price of a deterministic cash flow at time $$t=0$$ is given by the net present value \(NPV\)

So we can construct a strategy as following

|  | t=0 | t=k-1 | t=k |
| :--- | :--- | :--- | :--- |
| Buy contract  | $$-p_k$$ |   | $$r_{k-1}F$$ |
| Borrow $$\alpha$$ over $$[0, k-1]$$  | $$\alpha$$ | $$-\alpha(1+r_0)^{k-1}$$ |   |
| Borrow $$\alpha (1+r_0)^{k-1}$$ over $$[k-1, k]$$ |   | $$\alpha(1+r_0)^{k-1}$$ | $$-\alpha(1+r_0)^{k-1}(1+r_{k-1})$$ |
| Lent $$\alpha$$ from $$[0, k]$$ | $$-\alpha$$ |   | $$\alpha(1+r_0)^k$$ |

Cash flow at time $$k$$

* $$c_k = r_{k-1}F - \alpha(1+r_0)^{k-1}(1+r_{k-1}) + \alpha(1+r_0)^k $$
* $$c_k  =(F - \alpha(1+r_0)^{k-1})r_{k-1} + ar_0(1+r_0)^{k-1}$$
* Where random part is $$(F - \alpha(1+r_0)^{k-1})r_{k-1} $$
* and deterministic part it $$\alpha r_0(1+r_0)^{k-1}$$

In order to eliminate random part let's set 

* $$\alpha  =\cfrac{F}{(1+r_0)^{k-1}} $$

Then the net cash flow is now deterministic where

* $$c_k  =ar_0(1+r_0)^{k-1} = Fr_0 $$

Price of the portfolio \(at time 0\)

* $$p_k - \alpha + \alpha = p_k = \cfrac{c_k}{(1+r)^k} = \cfrac{Fr_0}{(1+r)^k}$$

Recall that 

$$P_f = P + \displaystyle\sum_{k=1}^{n}p_k \\ =\cfrac{F}{(1+r_0)^n} + \displaystyle\sum_{k=1}^{n}\cfrac{Fr_0}{(1+r_0)^k} \\ =\cfrac{F}{(1+r_0)^n} + Fr_0\displaystyle\sum_{k=1}^{n}\cfrac{1}{(1+r_0)^k} \\ = F$$ 

So the price $$P_f$$ ****of a floating rate bond is equal to its face value $$F$$

### Term Structure of Interest Rates

Interest rates depend on the term or duration of the loan.

* Investors prefer their funds to be liquid rather than tied up
* Investors have to be offered a higher rate to lock in funds for a longer period
* Other explanations
  * Expectation of future rates
  * market segmentation

#### Terms

* **Spot rate** $$s_t =$$ interest rate for a loan maturing in  $$t$$ years
  *  $$A$$ in year  $$t \to PV = \cfrac{A}{(1+s_t)^t}$$
* **Discount rate**  $$d(0, t) = \cfrac{1}{(1+s_t)^t}$$
  * Can infer the spot rates from bond prices
* **Forward rate**  $$f_{uv}$$ : interest rate quoted _today_ for lending from year  $$u$$ to  $$v$$
  * From no-arbitrage , at time  $$v$$ the income should be the same. So that
  *  $$(1+s_v)^v = (1+s_u)^u(1+f_{uv})^{v-u}  \to  f_{uv} = (\cfrac{(1+s_v)^v}{(1+s_u)^u})^{\cfrac{1}{v-u}} - 1$$
* Relation between spot and forward rates is
  *  $$(1+s_t)^t = \displaystyle\prod_{k=0}^{t-1}(1+f_{k,k+1})$$

## Forward Contracts

**Definition**. A **forward contract** gives the buyer the right, and also the obligation, to purchase 

* a specified amount of an asset 
* at a specified time $$T$$ 
* at a specified price$$F$$ \(called the **forward price**\) set at time $$t=0$$ 

**Example**. 

* Forward contract for delivery of a stock with maturity 6 months 
* Forward contract for sale of gold with maturity 1 year 
* Forward contract to buy 10m $ worth of Euros with maturity 3 months 
* Forward contract for delivery of 9-month T-Bill with maturity 3 months.

### Setting the Forward Price

Goal: set the forward price $$F$$ for a forward contract at time $$t=0$$ for 1 unit of an asset with

* asset price $$S_t$$ at time $$t$$ 
* and maturity $$T$$ 

$$f_t=$$ value or price at time $$t$$ of a long position in the forward contract. 

Value of the forward contract at time $$T$$ is $$f_T = (S_T - F)$$

* long position in forward: must purchase the asset at price $$F$$
* spot price of asset $$S_T$$

Forward price $$F$$ is set so that at time $$t=0$$ value or price $$f_0 =0$$. Then we could use no-arbitrage principle to set $$F$$.

#### Short Selling an Asset

Short selling is the selling of shares in a stock that the seller doesn’t own 

* The seller borrows the shares from the broker 
* The shares comes from the brokerage’s own inventory 
* The shares are sold and the proceeds are credited to the seller’s account 

However, sooner or later the seller must “close” the short by buying back the shares \(called covering\).

Profit/loss associated with a short sale 

* Results in a profit when the price drops 
* Results in a loss when the price increases 

Short positions can be very risky 

* Price can only drop to zero 
  * potential profit is bounded 
* Price can increase to arbitrarily large values
  * potential loss is unbounded

#### No-arbitrage Argument to Set $$F$$

Assume asset has no intermediate cash flow, e.g. dividends, or storage costs. We design the following portfolio:

Buy contract, short sell the underlying and lend $$S_0$$ up to time $$T$$.

| Cash flow | $$t=0$$ | $$t=T$$ |
| :--- | :--- | :--- |
| Buy contract | $$f_0 = 0$$ | $$f_T = S_T-F$$ |
| Short sell asset and buy back at time $$T$$ | $$+S_0$$ | $$-S_T$$ |
| Lend $$S_0$$ up to $$T$$ | $$-S_0$$ | $$\cfrac{S_0}{d(0,T)}$$ |
| Net cash flow | 0 | $$\cfrac{S_0}{d(0, T)} - F $$ |

The portfolio has a deterministic cash flow at time $$T$$ and the cost = 0. Therefore

$$0 = (\cfrac{S_0}{d(0, T)} - F) \cdot d(0,T) \to \\ F = \cfrac{S_0}{d(0, T)}$$

$$F$$ if strictly greater than the spot price $$S_0$$ because of the **cost of carry.**

### Construct Forward Value $$f_t, t>0$$

Recall the value of a long forward position

* at time 0, $$f_0 = 0$$
* at time $$T$$, $$f_T = S_T - F$$

Here we denote 

* $$F_0$$ : Forward price at time 0 for delivery at time $$T$$
* $$F_t$$ : Forward price at time $$t$$ for delivery at time $$T$$

Pricing via the no-arbitrage arguments

| Cash flow | $$t=t$$ | $$t=T$$ |
| :--- | :--- | :--- |
| Short $$F_t$$ contract | 0 | $$F_t - S_T$$ \(reverse because short position\) |
| Long $$F_0$$ contract | $$-f_t$$ | $$S_T - F_0$$ |
| Net cash flow | $$-f_t$$ | $$F_t - F_0$$ |

The portfolio has a deterministic cash flow, therefore,

$$f_t = (F_t - F_0) \cdot d(t,T)$$

