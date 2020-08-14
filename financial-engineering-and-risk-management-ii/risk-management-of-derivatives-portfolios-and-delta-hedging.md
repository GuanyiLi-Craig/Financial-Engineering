# Risk Management of Derivatives Portfolios and Delta-Hedging

## Risk-Management of Derivatives Portfolios

The Black-Scholes formula for the price of a European call option with strike $$K$$ and expiration $$T$$ 

$$C_0 = S_0 \cdot e^{-cT} \cdot N(d_1) - K\cdot e^{-rT} \cdot N(d_2)$$ 

where 

$$d_1 = \cfrac{\log(S_0 / K) + (r - c + \sigma^2/2) \cdot T}{\sigma \cdot \sqrt{T}} \\ d_2 = d_1 - \sigma \cdot \sqrt{T}$$ 

and $$N(d)  = \mathbf{P} (N(0,1) \leq d)$$ 

Recall that $$r$$ is the risk-free interest rate, $$c$$ is the dividend yield and the stock price $$S_t$$ satisfies 

$$S_t = S_0 \cdot e^{(r - c - \sigma^2/2) t + \sigma W_t}$$ 

where $$W_t$$ is a Brownian motion under $$\mathbb{Q}$$ .

### Delta-Gamma-Vega Approximations to Option Prices

The option prices as a function of $$S$$ and $$\sigma$$ only. 

A simple application of Taylor's Theorem 

$$C(S+\Delta S, \sigma + \Delta \sigma) \approx C(S, \sigma) + \Delta S \cfrac{\partial C}{\partial S} + \cfrac{1}{2}(\Delta S)^2 \cfrac{\partial ^2C}{\partial S^2} + \Delta \sigma \cfrac{\partial C}{\partial \sigma} \\ \quad \quad \quad = C(S, \sigma) + \Delta S \delta + \cfrac{1}{2}(\Delta S)^2 \Gamma + \Delta \sigma \; \text{vega}$$ Then

$$\text{P&L} = \delta \; \Delta S + \cfrac{\Gamma}{2}(\Delta S)^2 + \text{vega} \; \Delta \sigma \\ \quad = \text{delta P&L} + \text{gamma P&L} + \text{vega P&L}$$ 

when $$\Delta \sigma = 0$$ , obtain the well-known **delta-gamma** approximation. Often used, for example, in historical **Value-at-Risk \(VaR\)** calculation.  It can also be written as 

$$\text{P&L} \approx \delta S \bigg(\cfrac{\Delta S}{S} \bigg) + \cfrac{\Gamma S^2}{2}\bigg(\cfrac{\Delta S}{S} \bigg)^2 + \text{vega} \; \Delta \sigma \\ \quad = \text{ESP} \times \text{Return} + $\text{ Gamma} \times \text{Return}^2 +  \text{vega }\Delta \sigma$$ 

where ESP denotes the equivalent stock position or "dollar" delta.

We could easily include a theta term in above equation and other “Greeks” if necessary.

Note that above equation also applies to portfolios of derivatives

* very useful for estimating P&L for relatively small moves in risk factors
* and market participants use such approximations all the time
* but for very large moves in S or σ breaks down
* scenario analysis comes to the rescue then.

### Scenario Analysis

![](../.gitbook/assets/image%20%2884%29.png)

The pivot table shows the P&L for an options portfolio in various scenarios

* could also report the Greeks in each scenario
* an easily adapt this to portfolios with multiple underlying securities.

It’s important to choose the risk factors and stress levels carefully

* can be very difficult for portfolios of complex derivatives

## Delta-Hedging

Recall that the delta of a European call and put option, respectively, are given by

$$\text{Call-Delta} = e^{-cT} \cdot \text{N}(d_1) \\ \text{Put-Delta} = e^{-cT} \cdot \text{N}(d_1) - e^{-cT}$$ 

where

$$d_1 = \cfrac{\log(S_0 / K) + (r - c + \sigma^2/2) \cdot T}{\sigma \cdot \sqrt{T}} $$ 

and $$\text{N}(d) = \text{P}(\text{N}(0,1) \leq d).$$ 

In the Black-Scholes model an option can be **replicated** exactly by following a **self-financing** trading strategy

* just as we did with the binomial model
* when we execute the s.f. trading strategy we say we are **delta-hedging** the   option.

But the Black-Scholes model assumes we can trade continuously

* of course this is not feasible in practice

So instead we “hedge” periodically

* feasible in practice but it means we can no longer exactly replicate the option payoff.

Let $$T$$ be the option expiration and let $$S_i$$ denote the value of the underlying security at time $$t_i$$ where

$$0=t_0 < t_1 < t_2 < \cdot \cdot \cdot < t_{n-1} < t_n = T$$ 

If $$V_0(S_0, \sigma_0)$$is the initial value of the option and $$\Delta t:= t_{i+1} -t_i$$ for all $$i$$ , then

$$V_{i+1} = V_i + \delta_i (S_{i+1} + S_i \cdot c \cdot \Delta t - S_i) + (V_i - \delta_i \cdot S_i) (e^{r\Delta t} - 1)$$ 

defines a **self-financing trading strategy** where $$\delta_i$$ units of the security are held at each time $$t_i$$ . 

If $$\Delta t \to 0$$ then this s.f. strategy will replicate the option payoff at time $$T$$ 

* otherwise it only replicates the payoff approximately so that
  * $$V_n \approx \text{Option Payoff at time } T$$ 
* assuming the $$\sigma$$ parameter that we used to price the option is "**correct**"
  * i.e. if $$\sigma_0 = \sigma$$ where $$\sigma$$ is the true volatility parameter in the pricing generating process so that
    * $$S_{i+1} = S_i \cdot e^{(\mu - \sigma^2/2) \Delta t + \sigma(W_{i+1} - W_i)}$$ 

If we assume the wrong $$\sigma_0$$ then $$V_0$$ and all the $$\delta_i$$'s will be "**wrong**"

* and the s.f. trading strategy may not come close to replicating the option payoff. 

Because we can’t know the true σ in advance and because security prices don’t even follow GBM’s, the concept of dynamic replication is therefore only a theoretical concept

* so at best can only hope to replicate options approximately.

## The Volatility Surface

### Problems with Black-Scholes

* Black-Scholes is an elegant model but for several reasons it does not   perform very well in practice:
  * security prices often jump
    * this is not possible with GBM
  * security price returns tend to have fatter tails than those implied by the log-normal distribution
  * and returns are clearly not IID in practice.
* Market participants are well aware that the Black-Scholes model is a very   poor approximation to reality
  * and have certainly known this since the Wall Street Crash of 1987.
* But the Black-Scholes model and the language of Black-Scholes model is   still pervasive in finance
  * most derivatives markets still use aspects of Black-Scholes to quote     prices and perform risk management.
* So even though Black-Scholes is clearly not a good approximation to market   dynamics, it is still necessary to understand it.

### The Volatility Surface

The incorrectness of Black-Scholes is most obviously manifested through the volatility surface

* a concept that is found throughout derivatives markets.

The volatility surface is constructed using market prices of European call and put options

* can also use American prices but it’s a little trickier.

**Definition.** The volatility surface, $$\sigma(K, T)$$ , is a function of the strike, $$K$$ , and expiration, $$T$$ . It is defined implicitly by

$$C_{mkt}(S, K, T) = C_{BS} (S, T, r, c, K, \sigma(K, T))$$ 

where $$C_{mkt}(S, K, T)$$ denotes the market price of the call option with expiration, $$T$$ , and strike, $$K$$, and $$C_{BS}(\cdot)$$ is the corresponding Black-Scholes formula for pricing this call option. 

![](../.gitbook/assets/image%20%2883%29.png)

If BS model where correct then should have a flat volatility surface with $$\sigma(K, T) = \sigma$$ for all $$K, T$$ , and it would be **constant** through time.

In practice, however, volatility surfaces are not flat and they move about randomly.

Options with lower strikes tend to have higher implied volatilities

* for a given maturity, $$T$$ , this feature is typically referred to as the **volatility skew** or **smile**.

For a given strike, $$K$$ , the implied volatility can be either increasing or decreasing with time-to-maturity

* in general $$\sigma(K,T)$$ converges to a constant as $$T \to \infty$$ 
* for $$T$$ small often observe an inverted volatility surface with short-term   options having much higher volatilities than longer-term options
  * this is particularly true in times of market stress.

Single-stock options are generally **American** and in this case, call and put options typically give rise to different surfaces.

The fact that the volatility surface is not constant emphasizes just how wrong Black-Scholes is

* but every equity and FX derivatives trading desk computes the   Black-Scholes implied volatility surface
* and the “Greeks” are computed \(and used\) using Black-Scholes
* use of the BS formula is often likened to “_using the wrong number in the   wrong formula to obtain the right price_”!

### Arbitrage Constraints on the Volatility Surface

The shape of the implied volatility surface is constrained by the absence of arbitrage. In particular:

1. Must have $$\sigma (K, T) ≥ 0$$ for all strikes $$K$$ and expirations $$T$$ .
2. At any given maturity, $$T$$ , the skew cannot be too steep
   1. otherwise arbitrage opportunities, e.g. put-spread arbitrage, will exist.
3. Likewise the term structure of implied volatility cannot be too inverted
   1. otherwise calendar spread arbitrages will exist.

In practice the implied volatility surface will not violate any of these restrictions

* otherwise there would be an arbitrage in the market.

These restrictions can be difficult to enforce, however, when we are stressing the volatility surface

* a task that is commonly performed for risk management purposes
* recall our earlier discussion on scenario analysis.

