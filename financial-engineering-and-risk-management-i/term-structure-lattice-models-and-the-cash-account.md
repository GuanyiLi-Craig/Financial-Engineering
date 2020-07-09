# Term Structure Lattice Models and the Cash Account

#### Some facts

* Fixed income markets are enormous and in fact bigger than equity markets.
* Fixed income derivatives markets are also enormous
  * includes interest-rate and bond derivatives, credit derivatives, MBS and ABS
  * will focus here on interest-rate and bond derivatives – using binomial lattice models.

## Binomial Models for the Short Rate

* Binomial model will be used to introduce
  * the mechanics of the most important fixed income derivative securities
    * bond futures \(and forwards\)
    * caplets and caps, floorlets and floors
    * swaps and swaptions
  * the “philosophy” behind fixed income derivatives pricing
* Fixed-income models are inherently more complex than security models
  * need to model evolution of **entire term-structure of interest rates.**
* The short-rate, $$r_t$$ , is the variable of interest in many fixed income models
  * including binomial lattice models
  * $$r_t$$ is the risk-free rate that applies between periods $$t$$ and $$t + 1$$ 
  * it is a random process but $$r_t$$ is known by time $$t$$ .

### The “Philosophy” of Fixed Income Derivatives Pricing

* We will simply specify **risk-neutral** probabilities for the short-rate, $$r_t$$
  * without any reference to the **true** probabilities of the short-rate
* This is in contrast to the binomial model for stocks where we specified $$p$$ and $$1 − p$$ 
  * and then used replication arguments to obtain $$q$$ and $$1 − q$$ 
* We will price securities in such a way that **guarantees no-arbitrage**
* Will match market prices of liquid securities via a **calibration** procedure
  * often the most challenging part.
* Will see that derivatives pricing in practice is really about **extrapolating\*** from liquid security prices to illiquid security prices.

### Zero-Coupon Bond \(zcb\)

![](../.gitbook/assets/image%20%2817%29.png)

* ZCB will be the basic securities
  * $$Z_{i,j}^k$$ for time $$i$$ , state $$j$$ price of a zcb that matures at time $$k$$ 
* Would specify binomial model by specifying all $$Z_{i,j}^k$$ 's at all nodes
  * possible but awkward if we want to ensure **no-arbitrage**
* Instead will specify the short-rate, $$r_{i,j}$$ at each node $$N_{i,j}$$ 
  * the risk-free rate that applies to the next period
* Let $$Z_{i,j}$$ be the date $$i$$, state $$j$$ price of a non-coupon paying security
* Use **risk-neutral** pricing to price every security so that 

$$Z_{i,j} = \cfrac{1}{1+r_{i,j}}[q_u \cdot Z_{i+1, j+1} + q_d \cdot Z_{i+1, j}]$$ 

where $$q_u \text{ and } q_d$$ are the risk-neutral probabilities of an up and down move, and $$q_u + q_d = 1$$ .

* There is no arbitrage when pricing using above equation
* If the security pays a "coupon", $$C_{i+1,j},$$ at date $$i+1$$ and state $$j$$ then

$$Z_{i,j} = \cfrac{1}{1+r_{i,j}}[q_u(Z_{i+1,j+1} + C_{i+1, j+1} + q_d(Z_{i+1, j} + C_{i+1, j}))]$$ 

where $$Z_{i+1,.}$$ is now the **ex-coupon** price at date $$i+1$$ 

* These is also a arbitrage free model

## The Cash Account and Pricing ZCBs

### The Cash Account

* The **cash-account** is a particular security that in each period earns interest at the short-rate
  * we use $$B_t$$ to denote its value at time $$t$$ and assume that $$B_0 = 1.$$ 
* The cash-account is **not risk-free** since $$B_{t+s}$$ is not known at time $$t$$ for any $$s > 1$$ 
  * it is locally risk-free since $$B_{t+1}$$ is known at time $$t$$ .
* Note that $$B_t$$ satisfies $$B_t = (1+r_{0,0})\cdot(1+r_1)...(1+r_{t-1})$$ 
  * so that $$\cfrac{B_t}{B_{t+1}} = \cfrac{1}{1+r_t}$$ 
* Risk-neutral pricing for a "non-coupon" paying security then rakes the form:

$$Z_{t,j} = \cfrac{1}{1+r_{t,j}}[q_u\cdot Z_{t+1, j+1} + q_d\cdot Z_{t+1, j}] \\ = E_t^Q\bigg[ \cfrac{Z_{t+1}}{1+r_{r,j}} \bigg] \\ = E_t^Q \bigg[ \cfrac{B_t}{B_{t+1}} Z_{t+1} \bigg]$$ 

* Therefore for a non-coupon paying security, above equation equivalent to 

$$\cfrac{Z_t}{B_t} = E_t^Q\bigg[ \cfrac{Z_{t+1}}{B_{t+1}} \bigg]$$ 

* We can iterate this equation to obtain

$$\cfrac{Z_t}{B_t} = E_t^Q \bigg[ \cfrac{Z_{t+s}}{B_{t+s}} \bigg]$$ 

for any non-coupon paying security and any $$s>0$$ 

### Risk-Neutral Pricing with the Cash-Account

* Risk-neutral pricing for a "coupon" paying security takes the form:

$$Z_{t,j} = \cfrac{1}{1 + r_{t,j}} [q_u(Z_{t+1, j+1} + C_{t+1, j+1}) + q_d(Z_{t+1,j} + C_{t+1,j})] \\ = E_t^Q \bigg[ \cfrac{Z_{t+1} + C_{t+1}}{1+r_{t,j}} \bigg]$$ where it can be reformed as 

$$\cfrac{Z_t}{B_t} = E_t^Q  \bigg[ \cfrac{C_{t+1}}{B_{t+1}} + \cfrac{Z_{t+1}}{B_{t+1}} \bigg]$$ 

more generally, iterate the equation and we can get 

$$\color{red}{\cfrac{Z_t}{B_t} = E_t^Q \bigg[ \displaystyle\sum_{j=t+1}^{t+s} \cfrac{C_j}{B_j} + \cfrac{Z_{t+s}}{B_{t+s}} \bigg]}$$ 

This also can ensure the no-arbitrage. 

### Example

#### A Short-Rate Lattice

![](../.gitbook/assets/image%20%2819%29.png)

* The short-rate, $$r$$ , grows by a factor of $$u=1.25$$ or $$d=0.9$$ in each period
* Suppose we have 100 at $$t=5$$ , we can compute the term-structure by pricing ZCB's of every maturity and then backing out the spot-rates for those maturities. 

![](../.gitbook/assets/image%20%2820%29.png)

$$\color{red}{83.08} = \cfrac{1}{1+\color{red}{0.0938}} \bigg[ 0.5 \cdot 89.51 + 0.5 \cdot 92.22 \bigg]$$ 

* So $$s_4 = 6.68\% \text{  where  } 77.22(1+s_4)^4 = 100$$ assuming per-period compounding.
* Therefore $$Z_0^1, Z_0^2, Z_0^3 \text{ and } Z_0^4$$ can be calculated. 
  * and then compute $$s_1, s_2, s_3 \text{ and } s_4$$ to obtain the term-structure of interest rates at time $$t=0$$ . 
* At $$t=1$$ we will compute new ZCB prices and obtain a new term-structure
  * model for the short-rate, $$r_t$$ , therefore defines a model for the term-structure. 

## Words

{% hint style="info" %}
* extrapolate
{% endhint %}

