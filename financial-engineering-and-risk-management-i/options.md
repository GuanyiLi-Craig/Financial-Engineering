# Options

## Options

* **Definition. A European Call Option** gives the buyer the right but not the obligation to purchase 1 unit of the underlying at specified price K \(strike price\) at a specified time T \(expiration\). 
* **Definition. An American Call Option** gives the buyer the right but not the obligation to purchase 1 unit of the underlying at specified price K \(strike price\) at any time until a specified time T \(expiration\). 
* **Definition. A European Put Option** gives the buyer the right but not the obligation to sell 1 unit of the underlying at specified price K \(strike price\) at a speficied time T \(expiration\). 
* **Definition. An American Put Option** gives the buyer the right but not the obligation to sell 1 unit of the underlying at specified price K \(strike price\) at any time until a specified time T \(expiration\).

**Intrinsic value**: Intrinsic value refers to an investor's perception of the inherent value of an asset, such as a company, stock, option, or real estate

### Payoff and Intrinsic\* Value of a Call Option

Payoff of a European call option at expiration $$T$$ 

* price $$S_T < K$$ : do not exercise the option, payoff = 0
* price  $$S_T>K$$: exercise option and sell in the spot market, payoff =  $$S_T-K$$  

Payoff =  $$max(S_T - K, 0)$$ , which is non-linear in the price  $$S_T$$ .

_**Intrinsic value**_ of a call option at time  $$t< T = max(S_t - K, 0)$$ 

* In the money:  $$S_t > K$$ 
* At the money:  $$S_t = k$$ 
* Out of the money:  $$S_t < K$$ 

Everything works the other way for _**put**_ options. 

### Payoff and Intrinsic\* Value of a Put Option

Payoff of a European put option at expiration $$T$$ 

* price $$S_T > K$$ : do not exercise the option, payoff = 0
* price  $$S_T<K$$: exercise option and sell in the spot market, payoff =  $$S_T-K$$  

Payoff =  $$max(K-S_T, 0)$$ , which is non-linear in the price  $$S_T$$ .

_**Intrinsic value**_ of a put option at time  $$t< T = max(K-S_t , 0)$$ 

* In the money:  $$S_t < K$$ 
* At the money:  $$S_t = k$$ 
* Out of the money:  $$S_t > K$$ 

### Pricing Options

Pricing options is a model for this non-linear problem 

* European put/call with strike $$K$$ and expiration $$T: p_E(t; K, T), c_E(t; K, T)$$ 
* American put/call with strike $$K$$ and expiration $$T: p_A(t; K, T), c_A(t; K, T)$$ 

European put-call parity at time $$t$$ for non-dividend\* paying stock: 

$$p_E(t; K, T) + S_t = c_E(t; K, T) + K\cdot d(t, T) $$ 

Trading strategy

* At time $$t$$ buy European call with strike $$K$$ and expiration $$T$$ 
* At time $$t$$ sell European put with strike $$K$$ and expiration $$T$$ 
* At time $$t$$ \(short\) sell 1 unit of underlying and buy at time $$T$$ 
* Lend $$K\cdot d(t,T)$$ dollars up to time $$T$$ 

No-arbitrage argument

* Cash flow at time $$T: max(S_T - K, 0) - max(K-S_T, 0) - S_T + K = 0$$ 
* Cash flow at time $$t: -c_E(t; K, T) + p_E(t; K, T) + S_t - K\cdot d(t,T) = 0$$ 

### Bounds on Prices of European Options

Price of American option $$\geq$$ Price of European option

* $$c_A(t; K, T) \geq c_E(t;K, T),$$ and $$p_A(t; K, T) \geq p_E(t;K, T)$$ 

Lower bound on the European options as a function of stock price $$S_t$$ 

* $$c_E(t; K, T) = \max(S_t + p_E(t; K, T) - K\cdot d(t,T), 0) \geq \max(S_t - K\cdot d(t,T), 0)$$ 
  * $$p_E(t; K, T)$$ is cancelled because it greater or equal to 0
* $$p_E(t; K, T) = \max(K\cdot d(t,T) + c_E(t; K, T) - S_t, 0) \geq \max(K\cdot d(t,T) - S_t, 0)$$ 
  * $$c_E(t; K, T)$$ is cancelled because it greater or equal to 0

Upper bound on European options as a function of stock price $$S_t$$ 

* $$\max(S_t - K, 0) \leq S_T$$ implies $$c_E(t; K, T) \leq S_t$$ 
* $$\max(K-S_T, 0) \leq K$$ implies $$p_E(t; K, T) \leq K\cdot d(t,T)$$ 

Effect to dividends $$p_E(t; K, T) + S_t - D  = c_E(t; K, T) + K\cdot d(t, T)$$ 

* where $$D=$$ present value of all dividends until maturity

### Bounds on Prices of American Options

Price of American call as function of stock price $$S_t$$ :

* $$c_A(t; K, T) \geq c_E(t; K, T) \geq \max(S_t - K\cdot d(t, T), 0) > \max(S_t - K, 0)$$ 
  * $$d(t,T) < 1$$ in real life

Thus, the price of an American call is always strictly greater than the exercise value of the call option. 

**Never** optimal to exercise an American call on a non-dividend paying stock early!

$$c_A(t;K, T) = c_E(t; K, T)$$ 

Price of American put as function of stock price $$S_t$$ 

* Bound $$p_A(t;K, T) \geq p_E(t;K, T) \geq \max(K\cdot d(t,T) - S_t, 0)$$ 
* But the exercise value of a American put option is $$\max(K-S_t, 0)$$ 

Bound didn't worth well here. 

![](../.gitbook/assets/image%20%283%29.png)

* If price greater than like 50, then should hold
* If price less than around 50, then should exercise. 

## Option Pricing and the Binomial Model 

#### Binomial Model [&lt;-- link --&gt;](https://www.investopedia.com/terms/b/binomialoptionpricing.asp#:~:text=The%20binomial%20option%20pricing%20model%20is%20an%20options%20valuation%20method,and%20the%20option's%20expiration%20date.)

![](../.gitbook/assets/image%20%2815%29.png)

where 

* $$S_u = S\cdot u$$ with probability $$p$$ 
* $$S_d = S\cdot d$$ where $$d = \cfrac{1}{u}$$ with probability $$1-p$$ 

#### St Petersburg Paradox [&lt;-- link --&gt;](https://plato.stanford.edu/entries/paradox-stpetersburg/)

* Daniel Bernoulli resolved this by introducing a utility function $$u(\cdot)$$ 
  * $$u(x)$$ measures how much utility or benefit you obtains from x units of wealth
  * different people have different utility functions
  * $$u(\cdot)$$ should be _increasing_ and _concave_

### The 1-Period Binomial Model

![](../.gitbook/assets/image%20%2810%29.png)

* Can borrow or lend at gross **risk-free rate, R**
  * so that $1 in cash account at t =0 is worth $R at t = 1
  * Same to the borrow, like if borrow $1 at t=0 then has to pay $R at t=1
* Also assume that **short-sales** are allowed
  * where the short sales is _the sale of an asset or stock the seller does not own._
* Assume **no transactions fee** 

### Type A and Type B Arbitrage

Earlier definitions of weak and strong arbitrage applied in a deterministic world. Need more general definitions when we introduce **randomness**. 

**Definition.  Type A arbitrage** is a security or portfolio that produces immediate positive reward at $$t=0$$ and has non-negative value at $$t=1$$. i.e. a security with initial cost, $$V_0 < 0$$, and time $$t=1$$ value $$V_1 \geq 0$$ .

**Definition.  Type B arbitrage** is a security or portfolio that has a non-positive initial cost, has positive probability of yielding a positive payoff at t = 1 and zero probability of producing a negative payoff then. i.e. a security with initial cost, $$V_0 \leq 0$$, and time $$t=1$$ value $$V_1 \geq 0$$ but $$V_1 \neq 0$$ 

### Arbitrage in the 1-Period Binomial Model

![](../.gitbook/assets/image%20%2811%29.png)

* Recall we can borrow or lend at gross risk-free rate, R, per period. 
* And short-sales are allowed. 

**Theorem.** There is no arbitrage if and only if $$d<R<u$$  

**Proof**: 

* \(i\) Suppose $$R<d$$ . Then borrow $$S_0$$ and invest in stock. 
* \(ii\) Suppose $$u< R$$ . Then short-sell one share of stock and invest proceeds in cash-account. 
* Both case give a type B arbitrage. 

Will soon see other direction, i.e. if  $$d<R<u$$  , then there can be no-arbitrage.



## Words

{% hint style="info" %}
* _intrinsic_
  * belonging to a thing by its very nature

    _"form was treated as something intrinsic, as the very essence of the thing"_

  * situated within or belonging solely to the organ or body part on which it acts

    _"intrinsic muscles"_
* _dividend_
  * that part of the earnings of a corporation that is distributed to its shareholders; usually paid quarterly
  * a number to be divided by another number
  * a bonus; something extra \(especially a share of a surplus\)
{% endhint %}

