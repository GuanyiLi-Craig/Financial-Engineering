# Basics of Fixed Income

**Fixed income** refers to any type of investment under which the **borrower or issuer** is obliged to make payments of a **fixed amount** on a **fixed schedule**. For example,

* the borrower may have to pay interest at a fixed rate once a year, and to repay the principal amount on maturity. 

**Fixed-income securities** can be contrasted with equity securities – often referred to as stocks and shares – that create no obligation to pay dividends or any other form of income.

In order for a company to grow its business, it often must raise money – for example, to  finance an acquisition; to buy equipment or land; or to invest in new product development. The terms on which investors will finance the company will depend on the risk profile of the company. The company can give up equity by issuing stock, or can promise to pay regular interest and repay the principal on the loan \(bonds or bank loans\). Fixed-income securities also trade differently than equities. Whereas equities, such as common stock, trade on exchanges or other established trading venues, many fixed-income securities trade over-the-counter on a principal basis.

The term "fixed" in "fixed income" refers to **both the schedule of obligatory payments** and the **amount**. "Fixed income securities" can be distinguished from inflation-indexed bonds, variable-interest rate notes, and the like. If an issuer misses a payment on a fixed income security, the issuer is in default, and depending on the relevant law and the structure of the security, the payees may be able to force the issuer into bankruptcy. In contrast, if a company misses a quarterly dividend to stock \(non-fixed-income\) shareholders, there is no violation of any payment covenant, and no default.

## Introduction to No-Arbitrage\*

No-arbitrage, or arbitrage free condition is a situation in which 

* all relevant assets are priced appropriately and 
* there is no way for one's gains to outpace market gains without taking on more risk. 

Assuming an arbitrage-free condition is important in financial models, thought its existence is mainly theoretical.

### Contracts, Prices and No-Arbitrage

Consider the following contract

* Pay price _p_ at time _t = 0_
* Receive $$c_k$$ at time _t=k, k=1,...,T_

Note that cash flow$$c_k$$could be negative.

The no-arbitrage condition bounds the price p for this contract

* Weak No-Arbitrage: $$c_k$$_&gt;= 0_ for _all k&gt;=1_  then the price for this contract  _**p&gt;=0**_
* Strong No-Arbitrage: $$c_k$$_&gt;=0_ for all _k&gt;=1_ and $$c_l$$_**&gt;**0_ for some _l_  then the price for this contract _**p&gt;0**_

Essentially eliminate the possibility of a free-lunch. 

Implicit assumptions underlying the no-arbitrage condition

* Market are **liquid**
  * Sufficient number of buyers and sellers
* **Price** information is **available** to all buyers and sellers
* **Competition** in supply and demand will **correct** any **deviation** from no-arbitrage prices

## Interest Rates and Fixed Income Instruments

### Simple and Compound Interest

**Definition**. An amount $$A$$invested for n periods at a _**simple interest**_ rate of $$r$$ per period is worth $$A\cdot(1 + n\cdot r)$$ at maturity\*.

**Definition**. An amount $$A$$invested for n periods at a _**compound interest**_ rate of $$r$$ per period is worth $$A\cdot(1 + n)^r$$ at maturity.

Interest rates are typically quoted on annual basis, even if the compounding period is less than 1 year. 

*  $$n$$ compounding period in each year
* rate of interest $$r$$ 
* $$A$$ invested for $$y$$ years yields $$A\cdot(1+\cfrac{r}{n})^{y\cdot n}$$ 

Definition. _**Continuous compounding**_ corresponds to the situation where the length of the compounding period goes to zero. Therefore, an amount $$A$$ invested for y years is worth $$\lim\limits_{n\to \infty}A\cdot(1-\cfrac{r}{n})^{y\cdot n} = A\cdot e^{r\cdot y}$$ at maturity.

### Present Value

Present value \(PV\) is the current value of a future sum of money or stream of cash flows given a specified rate of return.

Price $$p$$ of a contract that pays $$c = (c_0, c_1, c_2, ... c_N)$$

* $$c_k > 0 \equiv$$cash inflow, and $$c_k < 0 \equiv$$cash outflow

Present Value \(PV\) at fixed rate r per period 

$$PV(\vec{c}, r) = c_0 + \cfrac{c_1}{1+r} + \cfrac{c_2}{(1+r)^2} + ... +\cfrac{c_N}{(1+r)^N} = \displaystyle\sum_{k=0}^N \cfrac{c_k}{(1+r)^k}$$

No-arbitrage argument, suppose one can borrow and lend at rate r for unlimited amount,

* Portfolio cash flows = 0
* Price of portfolio $$p - \displaystyle\sum_{k=0}^{T} \cfrac{c_k}{(1+r)^k} \geq 0 \to p \geq \displaystyle\sum_{k=0}^{T} \cfrac{c_k}{(1+r)^k}$$

In order to get the upper bound of the PV, we can reverse above process, and we can get the following conclusion if we could both lend and borrow unlimited amount at fixed rate r.

$$p = PV(\vec{c}, r)$$

### Different Lending and Borrowing Rates

Lend \(deposit money to bank\) at rate $$r_L$$and borrow rate at rate $$r_B$$, and we know $$r_L < r_B$$

* Buy contract and borrow $$\cfrac{c_k}{(1+r_B)^k}$$ for $$k$$years where $$k = 1, 2, 3, ..., N$$
  * No-arbitrage argument: price $$p - \displaystyle\sum_{k=0}^N \cfrac{c_k}{(1+r_B)^k} \geq 0$$
  * So we can get the **lower bound** $$p \geq PV(\vec{c}, r_B)$$
* Sell contract and lend \(deposit to bank\)$$\cfrac{c_k}{(1+r_L)^k}$$for $$k$$years where $$k = 1, 2, 3, ..., N$$
  * Similar as above, we get the **upper bound** $$p \leq PV(\vec{c}, r_L)$$

So that we can get the bounded price  $$PV(\vec{c}, r_B) \leq p \leq PV(\vec{c}, r_L)$$from no-arbitrage argument. Then the supply and demand set the final price $$p$$

### Fixed Income Securities

Fixed income securities "guarantee" a fixed cash flow. The risks are 

* Default risk
* Inflation\* risk
* Market risk

Perpetuity\*: $$c_k = A$$for all $$k \geq 1$$:

* $$p=\displaystyle\sum_{k=1}^{\infty} \cfrac{A}{(1+r)^k} = \cfrac{A}{r}$$

Annuity\*: $$c_k=A$$ for all $$k = 1, 2, 3, ..., N$$

* Annuity = Perpetuity - Perpetuity starting in year N+1
* Price $$p= \cfrac{A}{r} - \cfrac{1}{(1+r)^N}\cdot \cfrac{A}{r} = \cfrac{A}{r} (1-\cfrac{1}{(1+r)^N})$$

### Bond

#### Feature of Bonds

* **Face value** $$F$$: usually 100 or 1000
  * amount paid to a bondholder at the maturity date
* **Coupon rate** $$\alpha$$: pays $$c = \alpha F /2$$every half a year
  * is the rate of interest paid by bond issuers on the bond's face value.
* **Maturity** $$T$$**:** Date of the payment of the face value and the last coupon
* **Price** $$P$$: price that this bond going to be selling
* **Quality rating**: S&P Ratings _AAA, AA, BBB, BB, CCC, CC_

Bonds differ in many dimensions, and it is hard to compre bonds. ****In order to be able to compare bonds, on quantity has to be introduced

**Yield to maturity** $$\lambda$$

* YTM indicates how much an **investor will earn** if the bond is held until it matures, including the value of the remaining coupon payments as well as the return \(the capital gain, or loss\) of the principal sum upon maturity.
* Annual interest rate at which price $$P$$equals **present value** of coupon payments plus face value.$$P = \cfrac{F}{(1+\lambda/2)^{2T}} + \displaystyle\sum_{k=1}^{2T} \cfrac{c}{(1+\lambda/2)^k}$$
* Why do think in terms of yield
  * Summarizes **face value**, **coupon**, **maturity** and **quality**
  * Relates to quality: lower quality $$\to$$lower price $$\to$$higher yield to maturity
  * Relates to interest rate movements

## Words

{% hint style="info" %}
* _arbitrage_
  * n. a kind of hedged investment meant to capture slight differences in price; when there is a difference in the price of something on two different markets the arbitrageur simultaneously buys at the lower price and sells at the higher price
  * v. practice arbitrage, as in the stock market
* _rationale_
  *  n. \(law\) an explanation of the fundamental reasons \(especially an explanation of the working of some device in terms of laws of nature\)

    _"the rationale for capital punishment"_
* _maturity_
  * the period of time in your life after your physical growth has stopped and you are fully developed
  * state of being mature; full development
  * the date on which a financial obligation must be repaid
* _inflation_
  * a general and progressive increase in prices

    _"in inflation everything gets more valuable except money"_

  * \(cosmology\) a brief exponential expansion of the universe \(faster than the speed of light\) postulated to have occurred shortly after the big bang
  * lack of elegance as a consequence of being pompous and puffed up with vanity
  * the act of filling something with air
* _perpetuity_
  * the property of being perpetual \(seemingly ceaseless\)
* _annuity_
  *  income from capital investment paid in a series of regular payments

    _"his retirement fund was set up to be paid as an annuity"_
{% endhint %}



