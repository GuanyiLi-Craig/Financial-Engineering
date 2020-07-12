# Fixed Income Derivatives

## Options on Bonds

### Short-Rate Lattice

* Short-rate lattice

![](../.gitbook/assets/image%20%2824%29.png)

* Pricing a ZCB that matures at time $$t = 4$$ 

![](../.gitbook/assets/image%20%2822%29.png)

### Pricing a European call option on the ZCB

* Strick $$K=$84$$ 
* Option expiration at time $$T=2$$ 
* Option payoff $$= \max(0, Z_{2,.}^4 - 84)$$ 
* Underlying ZCB maturates at $$t=4$$ 

![](../.gitbook/assets/image%20%2825%29.png)

for example, 1.56 is calculated by 

$$1.56 = \cfrac{1}{1+0.075} \bigg[ \cfrac{1}{2} \cdot 0 + \cfrac{1}{2} \cdot 3.35 \bigg]$$ 

### Pricing a American put option on the ZCB

* Strick $$K=$88$$ 
* Option expiration at time $$T=3$$ 
* Option payoff at  $$t=3 \text{ is } \max(0, 88-Z_{3,.}^4)$$ 
* Underlying ZCB maturates at $$t=4$$ 

![](../.gitbook/assets/image%20%2823%29.png)

* For example, value 4.92 and value 8.73 is calculated by

$$4.92 = \max\bigg( 88-83.08, \cfrac{1}{1+0.0938} \bigg[ \cfrac{1}{2}\cdot 0 + \cfrac{1}{2} \cdot 0 \bigg]  \bigg) \\ 8.73 = \max\bigg( 88-79.27, \cfrac{1}{1+0.075} \bigg[ \cfrac{1}{2}\cdot 4.92 + \cfrac{1}{2} \cdot 0.65 \bigg]  \bigg)$$ 

* Turns out it's optimal early-exercise everywhere

## Bond Forward

### Pricing a Forward on a Coupon-Bearing Bond

* Delivery at $$t=4$$ for a 2-year $$10\%$$ coupon-bearing bond
* We assume delivery takes place just after a coupon has been paid
* In the pricing lattice we use backwards induction to compute the $$t=4$$ ex-coupon price of the bond
* Let $$G_0$$ be the forward price at $$t=0$$ and let $$Z_4^6$$ be the ex-coupon bond price at $$t=4$$ . Then risk-neutral pricing implies 

$$0 = E_0^Q \bigg[ \cfrac{Z_4^6 - G_0}{B_4} \bigg]$$ 

where $$B_4$$ is the value of the cash-account at $$t=4$$ 

* Rearranging terms and using the fact that $$G_0$$ is known at date $$t=0$$ we obtain

$$\color{red}{G_0 = \cfrac{E_0^Q[Z_4^6/B_4]}{E_0^Q[1/B_4]}}$$ 

* Recall that $$E_0^Q[1/B_4]$$ is time $$t=0$$ price of a ZCB maturing at $$t=4$$ but with a face value $1. 
  * has already calculated this to be 0.7722 \( $$77.22/100$$ \)
* Find ex-coupon price, $$Z_4^6$$ , of the bond at time $$t=4.$$ 

![](../.gitbook/assets/image%20%2826%29.png)

For example

$$98.44 = \cfrac{1}{1+0.1055} \bigg[ \cfrac{1}{2} \cdot 107.19 + \cfrac{1}{2} \cdot 110.46 \bigg] \\ 116.24 = \cfrac{1}{1+0.0354} \bigg[ \cfrac{1}{2}\cdot 110 + \cfrac{1}{2} \cdot 110 \bigg] + 10$$ 

* Backwards in lattice to compute $$E_0^Q[\cfrac{Z_4^6}{B_4}] = 79.83$$ 
  * Then we can apply the equation $$G_0 = \cfrac{E_0^Q[Z_4^6/B_4]}{E_0^Q[1/B_4]} = \cfrac{79.83}{0.7722} = 103.38$$ 

![](../.gitbook/assets/image%20%2828%29.png)

## Bond Futures

### Pricing Futures Contracts

* Let $$F_k$$ be the date $$k$$ price of a futures contract that expires after $$n$$ periods
* Let $$S_k$$ denote the time $$k$$ price of the security underlying the futures contract. 
* Then $$F_n = S_n$$ , i.e., at expiration the futures price and the underlying security price must coincide.
* Can compute the future price at $$t=n-1$$ by recalling that anytime we enter a futures contract, the initial value of the contract is 0. 
* Therefore the future price, $$F_{n-1}$$ , at date $$t=n-1$$ must satisfy

$$\cfrac{1}{B_{n-1}} = E_{n-1}^Q\bigg[ \cfrac{F_n-F_{n-1}}{B_n} \bigg]$$ 

* Since $$B_n \text{ and } F_{n-1}$$ are both known at date $$t=n-1$$ , we therefore have 

$$F_{n-1} = E^Q_{n-1}[F_n]$$ 

* By the same argument, we obtain 

$$F_k = E_k^Q[F_{k+1}] \text{  for  } 0\leq k < n$$ 

* Same as pricing future, use the law of iterated expectations to obtain

$$F_0 = E^Q_0[F_n]$$ 

* Since $$F_n = S_n$$ we have 
  * holds regardless of whether or not underlying security pays coupons etc. 

$$\color{red}{F_0 = E_0^Q[S_n]}$$ 

* In contrast corresponding forward price, $$G_0$$ , satisfies

$$\color{red}{G_0 = \cfrac{E_0^Q[S_n/B_n]}{E_0^Q[1/B_n]}}$$ 

### A Futures Contract on a Coupon-Bearing Bond

* Consider that futures contract written on same coupon bond as earlier forward contract Underlying coupon bond matures at time t = 6 Futures expiration at t = 4
* Backward to calculate the lattice simply by $$F_{n-1} = E^Q_{n-1}[F_n]$$ and we can get

![](../.gitbook/assets/image%20%2829%29.png)

For example

$$101.14 = \cfrac{1}{2} \cdot 98.44 + \cfrac{1}{2} \cdot 103.83$$ 

* Note that the forward price, **103.38**, and futures price, **103.22**, are close but not equal. 

## Caplets and Floorlets

### Pricing a Caplet

* A caplet is similar to a European call option on the interest rate, $$r_t$$ .
  * Usually settled in arrears but they may also be settled in advance. 
  * If maturity is $$\tau$$ and strike is $$c$$ , then payoff of a caplet \(settled in arrears\) at time $$\tau$$ is 

$$(r_{\tau-1} - c) ^{+}$$ 

So the caplet is a call option on the short rate prevailing\* at time $$\tau - 1$$ , settled at time $$\tau$$ . 

* A floorlet is the same as a caplet except the payoff is $$(c-r_{\tau-1})^+$$ 
* A **cap** consists of a sequence of caplets all of which have the same strike
* A **floor** consists of a sequence of floorlets all of which have the same strike
* Recall the short-rate lattice

![](../.gitbook/assets/image%20%2827%29.png)

* Suppose the expiration at t=6 and strike = 2%
* Note that it is easier to record the time t = 6 cash flows at their time 5 predecessor nodes, and then discount them appropriately
* So $$(r_5 - c)^+$$  at time t = 6 is worth

$$\cfrac{(r_5 - c)^+}{1+r_5} \text{  at } t=5$$ 

![](../.gitbook/assets/image%20%2830%29.png)

* A simple calculation:

$$0.015 = \cfrac{\max(0, 0.0345 - 0.02)}{1+0.0345}$$ 

* Now we can work backwards in the lattice to find the price at t = 0, for example

$$0.021 = \cfrac{1}{1 + 0.0394} \bigg[ \cfrac{1}{2} \cdot 0.028 + \cfrac{1}{2} \cdot 0.015 \bigg]$$ 

## Swaps and Swaptions

### Pricing Swaps

* Suppose the fixed rate is 5% that expires at $$t=6$$ , and 
  * first payment at $$t=1$$ and final payment at $$t=6$$ 
  * payment of $$\pm (r_{i,j} - K)$$ made at time $$t = i + 1$$ if in state $$j$$ at time $$i$$ .
* 
## Words

{% hint style="info" %}
* prevail
  * be larger in number, quantity, power, status or importance
  * be valid, applicable, or true
  * continue to exist
  * prove superior

    _"The champion prevailed, though it was a hard fight"_

  * use persuasion successfully

    _"He prevailed upon her to visit his parents"_
{% endhint %}

