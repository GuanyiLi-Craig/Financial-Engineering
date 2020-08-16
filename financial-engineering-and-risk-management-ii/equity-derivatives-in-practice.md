# Equity Derivatives in Practice

## The Volatility Surface in Action and Skew

### Skew

Shape of the volatility surface is always changing but in general there is typically a skew in the case of stocks and stock indices

* that is more pronounced at shorter expirations.

As stated earlier, there was little or no skew before Wall street crash of 1987. There are at least two principal explanations for the skew:

* **Risk aversion**: This explanation can appear in many guises:
  * Security prices often jump and jumps to the downside tend to be larger and     more frequent than jumps to the upside.
  * As markets go down, fear sets in and volatility goes up.
  * Supply and demand. Investors like to protect their portfolio by purchasing     out-of-the-money puts and so there is more demand for options with lower     strikes.
* The **leverage effect**: The total value of company assets, i.e. debt + equity, is   a more natural candidate to follow GBM
  * in this case equity volatility should increase as the equity value     decreases.

### The Leverage Effect

Let $$V, E$$ and $$D$$ denote the total _value of a company_, the _company's equity_ and the _company's debt_, respectively. 

The fundamental accounting equation states that

$$V = D +E$$ 

Equations is the basis for classical **structural models**

* sometimes used to price **risky debt** and **credit default swaps**

Merton \(1970's\) recognized that equity could be viewed as a **call option** on $$V$$ with strike equal to $$D$$ 

* valid since debt-holders get paid before equity holders. 

Let $$\Delta V, \Delta E$$ and $$\Delta D$$ be the change in values of  $$V, E$$ and $$D$$, respectively.  Then $$V + \Delta V = (E + \Delta E) + (D + \Delta D)$$ so that

$$\cfrac{V + \Delta V}{V} = \cfrac{E + \Delta E}{V} + \cfrac{D + \Delta D}{V} \\ \quad = \cfrac{E}{V}\bigg( \cfrac{E + \Delta E}{E} \bigg) + \cfrac{D}{V}\bigg( \cfrac{D+\Delta D}{D} \bigg)$$ 

If equity component is substantial so that it absorbs almost all losses and the debt is not very risky, then $$\Delta D$$ will be very small and implies

$$\sigma_V \approx \cfrac{E}{V} \sigma_E$$ 

where $$\sigma_V$$ and $$\sigma_E$$ are the firm value and equity volatilities, respectively. Therefore

$$\sigma_E \approx \cfrac{V}{E} \sigma_V = \bigg( 1 + \cfrac{D}{E} \bigg) \sigma_V$$ 

**If** $$\sigma_V$$ **a constant, then** $$\sigma_E$$ **will increase as** $$E$$ **decreases.** 

### The Meaning of the Volatility Surface

Assume volatility surface has been constructed from European option prices.

Consider a butterfly strategy centered at $$K$$ where 

* long a call option with strike $$K - \Delta K$$ 
* long a call with strike $$K + \Delta K$$ 
* short 2 call options with strike $$K.$$ 

Value of butterfly, $$B_0$$ , at time $$t = 0$$ , satisfies

$$B_0 = C(K-\Delta K, T) - 2 \cdot C(K, T) + C(K + \Delta K, T)$$ 

But we also have

$$B_0 \approx e^{-rT} \cdot \mathbb{Q}(K - \Delta K \leq S_T \leq K+\Delta K) \cdot \cfrac{\Delta K }{2} \\ \quad = e^{-rT} \cdot f_T(K) \cdot 2 \cdot \Delta K \cdot \cfrac{\Delta K}{2} \\ \quad = e^{-rT} \cdot f_T(K) \cdot (\Delta K)^2$$ 

where $$f_T(K)$$ is the **risk-neutral** PDF of $$S_T$$ evaluated at $$K$$ . Above two equations yields

$$f_T(K) \approx e^{rT} \cdot \cfrac{C(K-\Delta K, T) - 2\cdot C(K, T) + C(K+\Delta K, T)}{(\Delta K)^2}$$ 

and letting $$\Delta K \to 0$$ then

$$f_T(K) = e^{rT} \cdot \cfrac{\partial^2 C}{\partial K^2}$$ 

Volatility surface therefore gives the marginal risk-neutral distribution of the stock price, $$S_T$$ , for any fixed time $$T$$ . 

This means that given the implied volatility surface, $$\sigma(K, T)$$ , we can compute the price,

$$P_0 = \text{E}_0^{\mathbb{Q}}\big[ e^{-rT} \cdot f(S_T) \big] $$ 

of any derivative security whose payoff, $$f(\cdot)$$ , only depends on the underlying stock price at a single and fixed time $$T$$ . 

It tells us **nothing** about the **joint distribution** of the stock price at multiple times, $$T_1, ..., T_n$$ 

* not surprising since the volatility surface is constructed from European option prices
* and European option prices only depend on marginal distribution of $$S_T$$ 

**Example**. Suppose we wish to compute the price of a **knockout** put option with time $$T$$ payoff

$$\max(K - S_T, 0)  \; 1_{\{\min_{\; 0\leq t \leq T} S_t \geq B \} }$$ 

We cannot compute the price of this option given only the volatility surface.

## The Volatility Surface and Pricing Derivatives

### Pricing a Digital Option

Wish to price a digital option which pays $$$1$$if the time $$T$$ stock price, $$S_T$$ , is greater than $$K$$ and $$0$$ otherwise

* we know that we can price this security given the implied volatility surface. 

Easy to see that the digital price, $$D(K, T)$$ , is given by

$$D(K, T) = \displaystyle\lim_{\Delta K \to 0} \cfrac{C_{\text{mkt}}(K, T) - C_{\text{mkt}} (K + \Delta K, T)}{ \Delta K} \\ \quad \quad = - \displaystyle\lim_{\Delta K \to 0} \cfrac{C_{\text{mkt}}(K + \Delta K, T) - C_{\text{mkt}}(K, T)}{\Delta K} \\ \quad \quad = - \cfrac{\partial C_{\text{mkt}}(K, T)}{\partial K}$$ 

Recall that $$C_{\text{mkt}}(K, T) = C_{\text{BS}}(K, T, \sigma(K, T)).$$ 

Imply chain rule 

$$D(K, T) = - \cfrac{\partial C_{\text{BS}}(K, T, \sigma(K, T))}{\partial K} \\ \quad \quad = - \cfrac{\partial C_{\text{BS}}}{\partial K} - \cfrac{\partial C_{\text{BS}}}{\partial \sigma} \cdot \cfrac{\partial\sigma}{\partial K} \\ \quad \quad = \cfrac{\partial C_{\text{BS}}}{\partial K} - \text{vega} \times \text{skew}$$ 

The $$\cfrac{\partial C_{\text{BS}}}{\partial K}$$ and $$\cfrac{\partial C_{\text{BS}}}{ \partial \sigma}$$ using the Black-Scholes formula. And the skew, $$\cfrac{\partial \sigma}{\partial K}$$ , can be estimated from the implied volatility surface. 

This is an example of how the Black-Scholes “technology” is used in practice

* even though the Black-Scholes model is known to be wrong.

### An Example from Gatheral’s “The Volatility Surface”

Suppose $$r = c = 0, T= 1$$ year, $$S_0 = 100$$ and $$K = 100$$ so the digital is at-the-money.

Suppose also that the skew is $$2.5\%$$ per $$10\%$$ change in strike and $$\sigma_{atm} = 25\%$$ .

Letting $$\phi(\cdot)$$ be the PDF of a standard normal random variable we then have

$$D(100, 1) = \text{N}\bigg( -\cfrac{\sigma_{atm}}{2} \bigg) - S_0 \cdot \phi\bigg( \cfrac{\sigma_{atm}}{2}  \bigg) \cdot \cfrac{- 0.025}{0.1 \cdot S_0} \\ \quad \quad = \text{N}\bigg( -\cfrac{\sigma_{atm}}{2}  \bigg) + 0.25 \phi \bigg( \cfrac{\sigma_{atm}}{2}  \bigg) \\ \quad \quad \approx 0.45 + 0.25 \times 0.4 \\ \quad \quad = 0.55$$ 

Therefore the digital price = 55% of notional when priced correctly.

If we ignored the skew and just computed the Black-Scholes digital price using the ATM implied volatility, the price would have been 45% of notional

* which is significantly less than the correct price.

### Pricing a Range Accrual

Consider a 3-month range accrual on the S&P 500 index with range 1, 500 to 1, 550.

After 3 months the product pays X% of notional where 

$$X = \%$$ of days over the 3 months that index is inside the range. 

For example, if the notional is $10M and the index is inside the range 70% of the time, then the payoff is $7M.

**Question:** Is it possible to calculate the price of this range accrual using the volatility surface?

**Answer:** Yes. Consider a portfolio consisting of a pair of digitals for each date between now and the expiration.

## Beyond the Volatility Surface and Black-Scholes

### Same Marginals But Different Joint Distributions

### Derivatives Pricing in Practice



