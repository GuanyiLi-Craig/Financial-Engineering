# The Forward Equations

## Forward Equation

* $$P_{i,j}^e$$ denotes the time 0 price of a security that pays $1 at time i, state j and 0 at every other time and state. 
* Call such a security an elementary security and $$P_{i,j}^e$$ is its state price
* Can see that elementary security prices satisfy the forward equations

$$P_{k+1,s}^e = \cfrac{P_{k,s-1}^e}{2\cdot (1+r_{k,s-1})} + \cfrac{P_{k,s}^e}{2\cdot (1+r_{k,s})}, 0<s<k+1$$ 

* with $$P_{0,0}^e = 1$$  we have 

$$P_{k+1,0}^e = \cfrac{1}{2} \cdot \cfrac{P_{k,0}^e}{1+r_{k,0}}\\ \\ P_{k+1,k+1}^e = \cfrac{1}{2} \cdot \cfrac{P_{k,k}^e}{1+r_{k,k}}$$ 

* Consider the security that pays $1 only at $$t=3$$ and only in state 2
  * value of this security is $$P_{3,2}^e$$ by definition

![](../.gitbook/assets/image%20%2835%29.png)

* Work backwards in lattice to price it. Its value at node $$N_{2,2}$$ is

$$\cfrac{1}{1+r_{2,2}}\bigg[ \cfrac{1}{2}\cdot 0 + \cfrac{1}{2} \cdot 1 \bigg] = \cfrac{1}{2\cdot (1+r_{2,2})}$$ 

* its value at node $$N_{2,0}$$ is 0, and its value at node $$N_{2,1}$$ is

$$\cfrac{1}{1+r_{2,1}}\bigg[ \cfrac{1}{2}\cdot 1 + \cfrac{1}{2} \cdot 0 \bigg] = \cfrac{1}{2\cdot (1+r_{2,1})}$$ 

* therefore

$$P_{3,2}^e = \cfrac{1}{2 \cdot (1+r_{2,2})} \cdot P_{2,2}^e + \cfrac{1}{2 \cdot (1+r_{2,1})}\cdot P_{2,1}^e + 0 \cdot P_{2,0}^2$$ 

## Corresponding Elementary Prices

![](../.gitbook/assets/image%20%2834%29.png)

* Based on the above equation, we could have 

![](../.gitbook/assets/image%20%2836%29.png)

* Sample example

$$0.3079 = \cfrac{P^e_{k, s-1}}{2 \cdot (1+r_{k,s-1})} + \cfrac{P_{k,s}^e}{2\cdot(1+r_{k,s})} \\ = \cfrac{0.4432}{2\cdot(1+0.0675)} + \cfrac{0.2194}{2\cdot (1 + 0.0938)}$$ 

* Given the elementary prices the calculation of some security prices becomes very straightforward
  * i.e. 

$$Z_0^4 = 100 \cdot (0.0449 + 0.1868 + 0.2901 + 0.1992 + 0.0511) = 77.22$$ 

## Derivative Prices via Elementary Prices

* Consider a forward-start swap that begins at $$t = 1$$ and ends at $$t = 3$$ 
  * notional principal is $1M
  * fixed rate in the swap is 7%
  * payments at $$t=i \text{ for } i=2,3$$ are based as usual on fixed rate minus floating rate that prevailed at $$t = i-1$$ 
* The "forward" feature of the swap is that it begins at $$t = 1$$ 
  * first payment is then at $$t=2$$ since payments are made in arrears. 
* The value of the forward swap at $$t=0$$ is

$$V_0 = \displaystyle\sum_{i=2}^3 \bigg \{ \displaystyle\sum_{s} \cfrac{0.07 - r_{i-1,s}}{1+r_{i-1,s}} \cdot P^e_{i-1,s} \bigg\} \\ = \cfrac{0.07-0.0938}{1 + 0.0938} \cdot 0.2194 + \cfrac{0.07-0.0675}{1 + 0.0675} \cdot 0.4432 + \cfrac{0.07-0.0486}{1 + 0.0486} \cdot 0.2238+\\ \cfrac{0.07-0.075}{1 + 0.075} \cdot 0.4717+ \cfrac{0.07-0.054}{1 + 0.054} \cdot 0.4717 \\ = $5,800$$ 

