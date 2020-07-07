# Introduction to Derivative Security

## Swaps Contract

### Basics

#### **Definition**. 

* Swaps are contracts that transform **one kind of cash flow into another**. 

#### Example

* Plain vanilla swap: fixed interest rate vs floating interest rates 
* Commodity swaps: exchange floating price for a fixed price. e.g. gold swaps, oil swaps. 
* Currency swaps 

#### Why swaps? 

* Change the nature of cash flows 
* Leverage strengths in different markets

### Examples

#### Leverage Strength

![](../.gitbook/assets/image%20%281%29.png)

* Where the 3.95% is depends on supply and demand

Cons:

* These two companies bust be continues. 
* If one of them was default, the other one will be in great risk. 
* So here we need to introduce the intermediaires 

#### Financial Intermediaries

![](../.gitbook/assets/image%20%285%29.png)

### Pricing Interest Rate Swaps

$$r_t = $$ floating \(unknown\) interest rate at time $$t$$. 

$$N$$ is the notional principal amount. In an interest rate swap, $$N$$is the predetermined dollar amounts, or principal, on which the exchanged interest payments are based. 

Cash flows at time $$t = 1, ..., T$$ and the notional principal $$N$$, fixed rate $$X$$

* Company A \(long position in swap\): receives $$Nr_{t-1}$$ and pays $$NX$$
* Company B \(short position in swap\): receives $$NX$$ and pays $$Nr_{t-1}$$

#### Value of the _swap_ to company A

It receives the cash flow, the principle, $$N$$ times $$r_0, r_1, ..., r_{T-1}$$  at times 1, 2, 3, 4 up to capital T-1. This is precisely the cash flow associated with the floating weight bond, minus the face value. So in a floating weight bond, at the expiration capital T, in addition to the coupon payment, you have received the notional principal back. This time you do not get the notional principal

* $$N\cdot(r_0, ..., r_{T-1}) =$$ \(Cash flow of floating rate bond\) - \(Face value\). Therefore value of swap to company A

$$V_A = N\cdot(1-d(0,T)) - NX\displaystyle\sum_{t=1}^{T}d(0,t)$$

Where $$ N\cdot(1-d(0,T))$$ is the value of the floating rate payment received, and  $$NX\displaystyle\sum_{t=1}^{T}d(0,t)$$ is the value of fixed rate payments

Where 

* Set $$X$$ so that $$V_A = 0$$, we have 

$$X = \cfrac{1-d(0, T)}{\sum_{t=1}^{T}d(0,t)}$$

## Futures Contract

### Problems with Forward Contracts

* Not organized through an exchange. 
* Consequently, _**no price transparency**_! 
* Double-coincidence-of-wants: need someone to take the opposite side! 
* Default risk of the counterparty.

### Future Contract

* Solves the problem of a multitude\* of prices for the same maturity by marking-to-market 
  * disbursing\* profits/losses at the end of each day 
* Now contracts can be organized through an exchange. 
* Can be written on any underlying security with a settlement price 
  * Commodities 
  * Broad based indicies, e.g. S & P 500, Russel 2000, etc. 
  * Volatility\* of the market, e.g. VIX futures

### Mechanics of a Futures Contract

* Individuals open a margin account with a broker 
* Enter into N futures contracts with price $$F_0$$
* Deposit initial margin into the account ≈ 5 − 10% of contract value 
* All profit/loss settled using margin account 
* Margin call if balance is low

### Pros & Cons of Future

* Pros: 
  * High leverage: high profit 
  * Very liquid 
  * Can be written on a wide variety of underlying assets 
* Cons: 
  * High leverage: high risk 
  * Futures prices are approximately linear function of the underlying – only linear payoffs can be hedged 
  * May not be flexible enough; back to Forwards!

### Price Futures

* Need martingale\* pricing formalism
* Deterministic interest rate: forward price = futures price
* At maturity futures price $$F_T =$$ price of underlying $$S_T$$ 

### Hedging Using Futures: Long Hedge

Today is Sept. 1st. A baker needs 500, 000 bushels of wheat on December 1st. So, the baker faces the risk of an uncertain price on Dec. 1st. 

Hedging strategy: buy 100 futures contracts maturing on Dec. 1st – each for 5000 bushels, which equals the baker demands. 

Cash flow on Dec. 1st

* Futures position at maturity: $$F_T- F_0 = S_T - F_0$$
* Buy in the spot market: $$S_T$$
* Effective cash flow: $$S_T - F_0 - S_T = -F_0$$

The risk is that in reality in order for all of this to workout, you had to put money into a margin account. And you have to keep adding money to the margin account in case there are margin costs. If at any point during the time from 0 to T, from September 1st to December 1st, there is a margin call and you're not able to provide the money necessary to keep your position going. The broker is going to cancel your position and all the benefits that you were thinking about getting from the future position are no longer available.

### Perfect Hedges are not always possible

* The date $$T$$ may not be a futures expiration date. 
* $$P_T$$ may not correspond to an integer number of futures contracts 
* A futures contract on the underlying may not be available 
* The futures contract might not be liquid 
* The payoff $$P_T$$ may be nonlinear in the underlying

Basis = Spot price of underlying - futures price

* Perfect hedge: $$Basis = 0$$ at time $$T$$
* Basis risk: $$Basis \neq 0$$ at time $$T$$
* Basis risk arises because the futures contract is on a related but different asset, or expires at a different time.

### Minimum Variance Hedge

#### Example 

Today is Sept. 1st. A taco company needs 500, 000 bushels of kidney beans on December 1st. So, the taco company faces the risk of an uncertain price. 

**Problem**: No kidney bean futures available. Basis risk inevitable. 

**Hedge**: Go long  $$y$$ soybean futures each for 5000 bushels of soybeans 

Cash Flow in 90 days

* Future position at maturity:  $$(F_T - F_0 ) y$$
* Buy kidney beans in the spot markt:  $$P_T$$
* Effective cash flow  $$C_T = y\cdot(F_T - F_0) +P_T$$

$$P_T \neq y\cdot F_T$$ for any  $$y$$means _perfect hedge impossible_!

In order to minimize the variance, we firstly need to find the variance equation. Here we firstly denote

* $$\mathbf{var}(x)$$ : variance of x, which is the average of the squared differences from the Mean.
  * [&lt;-- wiki --&gt;](https://en.wikipedia.org/wiki/Variance)
* $$\mathbf{cov}(x, y)$$: covariation\* of x and y which is a measure of the joint variability of two random variables
  * [&lt;-- wiki --&gt;](https://en.wikipedia.org/wiki/Covariance)

$$\mathbf{var}(C_T) = \mathbf{var}(P_T) + \mathbf{var}(y\cdot(F_T - F_0)) + 2\cdot \mathbf{cov}(y\cdot(F_T - F_0), P_T) \\ = \mathbf{var}(P_T) + y^2\mathbf{var}(F_T) + 2y\cdot \mathbf{cov}(F_T, P_T)$$

where $$F_0$$ is a constant so it can be cancelled. 

Set the derivative with respect to $$y$$ to zero:

$$\cfrac{\partial \mathbf{var}(C_T(y))}{\partial y} = 2y \mathbf{var}(F_T) + 2 \mathbf{cov}(F_T, P_T) = 0$$

Optimal number of future contracts:

$$y^* = \cfrac{\mathbf{cov}(F_T, P_T)}{\mathbf{var}(F_T)}$$

## Words

{% hint style="info" %}
* _multitude_
  * a large indefinite number

    _"a multitude of TV antennas_

  * a large gathering of people
  * the common people generally
* _disburse_
  * pay out
* _volatility_
  * the property of changing readily from a solid or liquid to a vapor
  * the trait of being unpredictably irresolute

    _"the volatility of the market drove many investors away"_

  * being easily excited
* _martingale_
  * a harness strap that connects the nose piece to the girth; prevents the horse from throwing back its head
  * spar under the bowsprit of a sailboat
* _formalism_
  * the doctrine that formal structure rather than content is what should be represented
  * \(philosophy\) the philosophical theory that formal \(logical or mathematical\) statements have no meaning but that its symbols \(regarded as physical entities\) exhibit a form that has useful applications
  * the practice of scrupulous adherence to prescribed or external forms
* _covariation_ 
  * \(statistics\) correlated variation
{% endhint %}

