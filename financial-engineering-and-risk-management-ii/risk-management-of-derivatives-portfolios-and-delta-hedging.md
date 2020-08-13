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

