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
  * has already calculated this to be 0.7722

## Bond Future





