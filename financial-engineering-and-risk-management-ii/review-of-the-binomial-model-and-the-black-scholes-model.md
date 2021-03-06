# Review of the Binomial Model and the Black-Scholes Model

## Binomial Model for Option Pricing

### Pricing a European Call Option

Assumptions:

* expiration at $$t = 3$$ 
* strick $$= $100$$ 
* $$R = 1.01$$ 

![](../.gitbook/assets/image%20%2872%29.png)

* Sample calculation:

$$15.48 = \cfrac{1}{1.01} [q_u \times 22.5 + q_d \times 7]$$ 

with $$q_u = \cfrac{R-d}{ u - d}, \; q_d = 1 -q_u$$ 

* We can also calculate the price as following
  * this is risk-neutral pricing in the binomial model
  * avoid having to calculate the price at every node

$$C_0 = \cfrac{1}{R^3} \mathbf{E}_0^{\mathbb{Q}} [\max(S_T - 100, 0)]$$ 

### Trading Strategies in the Binomial Model

* Let $$S_t$$ denote the stock price at time $$t$$ 
* Let $$\color{red}{B_t}$$ denote the value of the cash-account at time $$t$$ 
  * assume without any loss of generality that $$B_0 = 1, s.t. , B_t = R^t$$ 
  * so now explicitly viewing the cash account as a security
* Let $$x_t$$ denote number of shares held between times $$[t - 1, t], \text{ where } t = 1,2,...,n$$ 
* Let $$y_t$$ denote number of cash account held between times $$[t-1, t],\text{ where } t = 1, 2, ..., n $$ 
* Then $$\bm{\theta}_t := (x_t, y_t)$$ is the portfolio held:
  * immediately after trading at time $$t-1$$ so it is known at time $$t-1$$ 
  * immediately before trading at time $$t$$ 
* $$\bm{\theta}_t$$ is also a random process and in particular, a **trading strategy**

### Self-Financing Trading Strategies

**Definition.** The _value process_  , $$V_t(\bm{\theta})$$ , associated with a trading strategy, $$\bm{\theta}_t = (x_t, y_t),$$ is defined by

$$V_t = \begin{cases}  x_1 S_0 + y_1 B_0 \quad \text{ for } t =0 \\ x_t S_t + y_t B_t \quad \text{ for } t > 0 \end{cases}$$ 

**Definition.** A self-financing \(s.f.\) trading strategy is a trading strategy, $$\bm{\theta}_t = (x_t, y_t)$$, where changes in $$V_t$$ are due entirely to trading gains or losses, rather than the addition or withdrawal of cash funds. In particular, a s.f. strategy satisfies 

$$V_t = x_{t+1} S_t + y_{t+1} B_t, \quad t = 1, 2, ... , n-1$$ 

* The definition states that the value of a s.f. portfolio just before trading is equal   to the value of the portfolio just after trading
  * so no funds have been deposited or withdrawn

**Proposition.** If a trading strategy, $$\bm{\theta}_t$$ , is s.f. then the corresponding value process, $$V_t$$ , satisfies

$$V_{t+1} - V_t = x_{t+1} (S_{t+1} - S_t) + y_{t+1}(B_{t+1} - B_t)$$ 

so that changes in portfolio value can only be due to capital gains or losses and not the injection or withdrawal of funds.

* In the multi-period binomial model we can construct a s.f. trading strategy   that replicates the payoff of the option
  * this is called dynamic replication.
* The initial cost of this replicating strategy must equal the value of the   option
  * otherwise there’s an arbitrage opportunity.
* The dynamic replication price is of course equal to the price obtained from   using the risk-neutral probabilities and working backwards in the lattice.
* And at any node, the value of the option is equal to the value of the   replicating portfolio at that node.

### The Replication Strategy for European Option

![](../.gitbook/assets/image%20%2871%29.png)

* Sample calculation

$$0.802 \times 107 + (-74.84) \times 1.01 = 10.23$$ at upper node at time $$t=1$$ 

## The Black-Scholes Model

Black-Scholes assumes

* A continuously-compounded interest rate of $$r$$ 
* Geometric Brownian motion dynamics for the stock price, $$S_t, $$ so that 

$$S_t = S_0 \cdot e^{(\mu-\sigma^2/2)t + \sigma W_t}$$ 

where $$W_t $$ is a _standard Brownian motion_

* The stock pays a dividend yield of $$c$$ 
* Continuous trading with no transactions costs and short-selling allowed. 

If number of period $$n \to \infty$$ then binomial paths will looks like Brownian paths. 

### The Black-Scholes Formula

* In the binomial model the call option price is given by

$$C_0 = \mathbf{E}_0^{\mathbb{Q}} [e^{-rT} \max(S_T - K, 0)]$$ 

where $$q_u = \cfrac{R-d}{u-d}$$ and $$q_d = 1- q_u$$ 

* Assume $$n \to \infty$$ then the Black-Scholes GBM model is obtained s.t. 

$$S_t = S_0 \cdot e^{(r - c - \sigma^2/2) t + \sigma W_t}$$ 

and where $$W_t$$ is a Brownian motion under $$\mathbb{Q}$$ .

* Combine above two equations to obtain the Black-Scholes formula

$$C_0 = S_0 \cdot e^{-cT} \cdot N(d_1) - K\cdot e^{-rT} \cdot N(d_2)$$ 

where 

$$d_1 = \cfrac{\log(S_0 / K) + (r - c + \sigma^2/2) \cdot T}{\sigma \cdot \sqrt{T}} \\ d_2 = d_1 - \sigma \cdot \sqrt{T}$$ 

and $$N(d)  = \mathbf{P} (N(0,1) \leq d)$$ 

* Note that $$\mu$$ does not appear in the Black-Scholes formula
  * just as $$p$$ is not used in option pricing calculations for the binomial model
* Black-Scholes obtained their formula using a similar replicating strategy argument to the one we used for binomial model
* European put option price, $$P_0$$ , can be calculated from put-call parity

$$P_0 + S_0 \cdot e^{-cT} = C_0 + K\cdot e^{-rT}$$ 

* The Black-Scholes formula is arguably the most important and famous formula in all of finance and economics 
  * it is used extensively in the financial industry
  * it has also let to an enormous amount of academic work since it's publication
* We will see how it is used in practice
  * but will emphasize now that the GBM model is not a good     approximation to security prices
  * and everybody knows this!

## The Greeks: Delta and Gamma

### Review Black-Scholes Formula

The Black-Scholes formula for the price of a European call option with strike $$K$$ and expiration $$T$$ 

$$C_0 = S_0 \cdot e^{-cT} \cdot N(d_1) - K\cdot e^{-rT} \cdot N(d_2)$$ 

where 

$$d_1 = \cfrac{\log(S_0 / K) + (r - c + \sigma^2/2) \cdot T}{\sigma \cdot \sqrt{T}} \\ d_2 = d_1 - \sigma \cdot \sqrt{T}$$ 

and $$N(d)  = \mathbf{P} (N(0,1) \leq d)$$ 

Recall that $$r$$ is the risk-free interest rate, $$c$$ is the dividend yield and the stock price $$S_t$$ satisfies 

$$S_t = S_0 \cdot e^{(r - c - \sigma^2/2) t + \sigma W_t}$$ 

where $$W_t$$ is a Brownian motion under $$\mathbb{Q}$$ .

The “**Greeks**” refer to the partial \(mathematical\) derivatives of a \(financial\) derivative security price with respect to the model parameters. 

### Delta $$\delta$$ 

**Definition.** The delta of an option is the partial derivative of the option price with respect to the price of the underlying security.

The delta measures the **sensitivity** of the option price to the price of the underlying security.

The delta of a European call option satisfies

$$\text{delta} = \cfrac{\partial C}{\partial S} = e^{-cT} \cdot \text{N}(d_1)$$ 

* follows from $$C_0 = S_0 \cdot e^{-cT} \cdot N(d_1) - K\cdot e^{-rT} \cdot N(d_2)$$ 
* although more tedious to calculate than it may appear to be. 

The delta of a European put option is also easily calculated. 

![](../.gitbook/assets/image%20%2880%29.png)

![](../.gitbook/assets/image%20%2874%29.png)

![](../.gitbook/assets/image%20%2876%29.png)

### Gamma $$\gamma$$ 

**Definition.** The **gamma** of an option is the partial derivative of the option’s delta with respect to the price of the underlying security.

Gamma measures the **sensitivity** of the option delta to the price of the underlying security.

The gamma of a call option satisfies

$$\text{gamma} = \cfrac{\partial ^2 C}{\partial S^2} = e^{-cT} \cfrac{\phi (d_1)}{\sigma S\cdot \sqrt{T}}$$ 

where $$\phi(\cdot)$$ is the standard normal PDF

The gamma of a European put option is easily calculated from put-call parity

$$e^{-rT} K + C = e^{-cT} S + P$$ 

Gamma for European options is always positive due to option convexity. 

![](../.gitbook/assets/image%20%2875%29.png)

![](../.gitbook/assets/image%20%2882%29.png)

### Vega  

**Definition.** The vega of an option is the partial derivative of the option price with respect to the volatility parameter, $$\sigma$$ .

Vega therefore measures the sensitivity of the option price to $$\sigma$$ .

The vega of a call option satisfies

$$\text{vega} = \cfrac{\partial C}{ \partial \sigma} = e^{-cT} S \cdot \sqrt{T} \cdot \phi(d_1)$$ 

where $$\phi(\cdot)$$ is the PDF standard normal random variable.

The vega of a European put option is easily calculated from put-call parity

$$e^{-rT} K + C = e^{-cT} S + P$$ 

![](../.gitbook/assets/image%20%2877%29.png)

![](../.gitbook/assets/image%20%2881%29.png)

### Theta $$\theta$$ 

**Definition.** The theta of an option is the **negative** of the partial derivative of the option price with respect to time-to-maturity. 

The theta of an option is therefore the sensitivity of the option price to a negative change in time-to-maturity. It satisfies

$$\text{theta} = -\cfrac{\partial C}{\partial T} = -e^{-cT} S \cdot \phi(d_1) \cfrac{\sigma}{2\sqrt{T}} + c\cdot e^{-cT} S \text{N}(d_1) - r\cdot K \cdot e^{-rT} \text{N}(d_2)$$ 

where $$\phi(\cdot)$$ is the standard normal PDF.

![](../.gitbook/assets/image%20%2878%29.png)

![](../.gitbook/assets/image%20%2873%29.png)

