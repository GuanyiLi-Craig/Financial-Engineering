# Implementation Difficulties

## Implement Details

Parameter estimation: mean return $$\bm{\mu}$$ and covariance $$\bm{V}$$ . There are some issues, such as

* Statistical errors in estimation
* Never have enough data: $$\bm{V}$$ has $$d\cdot (d+1)/2$$ independent parameters
* Portfolio is very sensitive to estimation errors. 

How does one get negative exposures in optimal mean-variance portfolios?

* Short the assets: unlimited downside! And often not feasible.
* leveraged Exchange Traded Funds \(ETFs\): Be very careful!

Is variance a good risk measure in practice?

* Works for Normal \(or elliptic\) random variables
* Need higher moments to capture deviation from Normality
* Tail risk measures

## Parameter Estimation

The true parameters $$(\bm{\mu}, \bm{V})$$ are never known. 

### Formula

Use Historical returns $$\bm{r}^{(1)}, \bm{r}^{(2)}, ..., \bm{r}^{(n)}$$ to compute estimates for

#### Mean

$$\mu^{(est)} = \cfrac{1}{N} \displaystyle\sum_{t=1}^N r^{(t)}$$ 

#### Covariance matrix

$$V^{(est)} = \cfrac{1}{N-1}\displaystyle\sum_{t=1}^N (r^{(t)} - \mu^{(est)}) \cdot (r^{(t)} - \mu^{(est)})^{\top}$$ 

### Example

* Each dot is an estimate for   the mean vector with $$N =  60$$ months of simulated data.
* Estimated mean can be quite “far” from the true mean.
* True mean lies in the 95% confidence ellipse with probability 0.95.

![](../.gitbook/assets/image%20%2861%29.png)

### Effective of Estimate Error

* Estimated mean and covariance from $$ N = 60$$ months of simulated data
* Estimated frontier = frontier for estimated parameters
* Realized frontier = true mean and volatility of the estimated frontier portfolios

![](../.gitbook/assets/image%20%2860%29.png)

Two identical assets with mean $$\mu$$ , variance $$\sigma^2$$ , and correlation $$\rho = 0$$ . Optimal investment $$\bm{x}^* = (0.5,0.5)$$ 

Suppose estimates

* $$\mu_1^{(est)} = \mu + \epsilon \quad  (\text{positive error})$$ 
* $$\mu_2^{(est)} = \mu - \epsilon \quad  (\text{negative error})$$ 

Average error in the estimates $$= 0 \; ...$$ estimator is good on average

Optimal investment: overweight asset 1. Precisely the wrong thing to do!

Realized performance is lower than expected for the overweighted asset and better than expected for the underweighted asset! Performance becomes worse as more shorting is allowed.

Ron Michaud: “Mean-variance results in error-maximizing investment-irrelevant portfolios.”

#### Efficient Frontier with No-Short Sales Constraint

The "corner" in the set $$\{ \bm{x} : \bm{x} \geq \bm{0} \}$$ makes solutions more sensitive to estimates

![](../.gitbook/assets/image%20%2864%29.png)

#### Efficient Frontier with Leverage Constraint

Leverage constraint: $$\displaystyle\sum_{i=1}^d | x_i | \leq 2$$ 

![](../.gitbook/assets/image%20%2866%29.png)

#### Efficient Frontier with Robust Constraints

Let $$S_m = $$ confidence region

Robust target return constraint: $$\min_{\bm{\mu}\in S_m} \{ \bm{\mu}^{\top} \bm{x} \} \geq r .$$ 

![](../.gitbook/assets/image%20%2862%29.png)

### Methods to Improve Parameter Estimates

Shrinkage methods: James and Stein \(1961\), Ledoit and Wolf

* "Shrink" to the global mean: $$\mu_i ^{(sh)} = \alpha \mu_i^{(est)} + (1-\alpha)(\cfrac{1}{d} \displaystyle\sum_{j=1}^{d} \mu_j)^{(est)}$$ 
* "Shrink" to identity matrix:  $$\mathbf{V} ^{(sh)} = \alpha \mathbf{V}^{(est)} + (1-\alpha)(\cfrac{1}{d} \displaystyle\sum_{j=1}^{d} \sigma^2_j)^{(est)} \mathbf{I}$$ 

Use subjective views to improve estimates: Black-Litterman method Non-parametric nearest neighbor-like methods

* Let $$r$$ denote the currently observed return
* Let $$S = \{ t: || r-r_t || \leq \beta \} =$$ times when historical returns where close to $$r$$ 
* Predict that future return belongs to the set $$\{ r_{t+1} : t \in S \}$$ 

## Negative Exposures and Leveraged ETFs

### Short Position

Short positions can result in superior returns.

But short positions are very risky!

* Long positions have limited downside
  * The lowest price of an asset is zero.
  * The largest amount one can lose is the amount invested.
* Short positions have unlimited downside
  * Short positions are created by selling assets borrowed from a broker.
  * The asset has to be re-purchased and returned to the broker at a later date.
  * The price of the asset can become arbitrarily large.
  * Potential **loss from the short position can be arbitrarily large**

Need a product that has **negative exposure and limited liability**

### **Exchange Traded Funds \(ETFs\)**

ETFs are exchange traded products that track the returns on stock indices, bond indices, commodities, currencies, etc. 

![](../.gitbook/assets/image%20%2868%29.png)

### Leveraged ETFs

Produces daily returns that are a multiple of the daily returns 

* Bull ETFs: return $$\beta \times $$ the daily return on index. $$\beta=2,3$$ 
* Inverse ETFs: return $$-\beta \times $$ the daily return on index. $$\beta=1,2,3$$ 

![Source: Bloomberg.com](../.gitbook/assets/image%20%2863%29.png)

An inverse ETF is a product that gives **negative exposure to the index with limited liability** – all one stands to lose is the initial investment.

### Details on the Return on an ETF

The return on an ETF is the return on the underlying index **compounded daily.**

\*\*\*\*$$R_T^{(ETF)} = (1 + r_1) (1+r_2) ...(1+r_T)$$ 

where $$r_t$$ is the net daily return on the underlying index. 

The return on a leveraged ETF with leverage factor $$\beta$$ 

$$R_T^{(\beta-ETF)} = (1 + \beta r_1) (1+\beta r_2) ...(1+\beta r_T)$$ 

where $$r_t$$ is the net daily return on the underlying index. 

ETFs are constructed by investing in derivatives written on the index. 

The daily compounding has consequences that are not immediately obvious.

### Volatility and ETF Returns

The gross return from a static leveraged position in the underlying index is 

$$\cfrac{\beta S_T - (\beta - 1) \cdot S_0 \cdot (1+rT)}{S_0}$$ 

where $$r$$ is the **funding rate** and $$\beta$$ is the **leverage ratio.** 

The gross return from investing in the $$\beta-$$ Leverage ETF is approximately. 

$$\bigg(\cfrac{S_T}{S_0}\bigg)^{\beta} \cdot \exp\bigg((1-\beta)rT - fT - \cfrac{\beta^2 -\beta}{2} \displaystyle\sum_{i=1}^{n-1} \ln\bigg( \cfrac{S_{i+1}}{S_i} \bigg)^2\bigg)$$ 

where $$f$$ is the expense ratio of the fund and $$n$$ is the number of daily observations between times 0 and T. \(So $$S_n = S_T$$ \)

The term $$- \cfrac{\beta^2 -\beta}{2} \displaystyle\sum_{i=1}^{n-1} \ln\bigg( \cfrac{S_{i+1}}{S_i} \bigg)^2$$ is the loss due to short volatility. 

ETFs are generally designed for short-term plays on an index or sector, and should be used that way. Over long-periods **leveraged** ETFs do not work as one may expect, especially in **volatile market.**

## **Beyond Variance**

Problems with Variance

* Appropriate for Normal and other elliptic distributions
* Does not capture larger deviations from the mean
* Symmetric measure: equally penalizes the deviation above/below mean

### Value at Risk \(VaR\)

**Definition.**  The $$\text{VaR}_p(L)$$ of random loss $$L$$ at the confidence level $$p \in (0,1)$$ is defined as 

$$\text{VaR}_p(L) := p^{th} - \text{quantile* of } L \approx  F_L^{-1} (p)$$ 

where $$F_L$$ is the CDF of the random loss $$L.$$ 

$$\text{VaR}_p$$ is increasing in $$p$$ . 

### Conditional Value at Risk

**Definition.** The conditional value at risk $$\text{CVaR}_p(L)$$ of random variable $$L$$ at the confidence level $$p \in (0,1)$$ is defined as 

$$\text{CVaR}_p(L) = \mathbb{E} [L | L \geq \text{VaR}_p(L)] = \cfrac{\int_{\text{VaR}_p(L)}^{\infty} \; xf_L(x)\; dx}{\mathbb{P}(L \geq \text{VaR}_p(L))}$$ 

where $$f_L$$ is the density of the random loss $$L.$$ The features are

* $$\text{CVaR}$$ is also a “tail” risk measure 
* $$\text{CVaR}_p(L) ≥ \text{VaR}_p(L) $$ 
* $$\text{CVaR}_p$$ is increasing in $$p$$ 
* Other names: _Tail conditional expectation_ and _Expected Shortfall_

### VaR and CVaR for Normal Distribution

Suppose $$L \sim N(\mu, \sigma^2)$$ . 

$$\text{VaR}_p (L) = \mu + \sigma \Phi^{-1} (p)$$ 

where $$\Phi$$ is the cumulative distribution function \(CDF\) of a standard Normal with mean 0 and volatility 1. 

$$\text{CVaR}_p(L) = \mu + \sigma\bigg( \cfrac{1}{1-p} \displaystyle\int_p^1 \Phi^{-1} (\beta) \; d\beta \bigg)$$ 

where $$\Phi$$ is the cumulative distribution function \(CDF\) of a standard Normal with mean 0 and volatility 1.

$$\text{VaR}_p$$ and $$\text{CVaR}_p$$ for a Normal random variable **completely** defined by mean $$\mu$$ and volatility $$\sigma$$ .

### VaR and CVaR from samples

Suppose $$L_1, L_2, ..., L_N$$ are $$N$$ independently and identically distributed \(**IID**\) samples from the $$\text{Loss } L$$ . 

 Let $$L_{(1)}, L_{(2)}, ..., L_{(N)}$$ denote the order-statistics \(**ascending** order\) of the $$N$$ samples. 

Let $$K_p = \lceil pN \rceil.$$ 

* $$\text{VaR}_p(L) \approx L_{(K_p)} = K_p$$-th term in the sorted samples
* $$\text{CVaR}_p(L) \approx \cfrac{1}{(1-p)N} \displaystyle\sum_{k=K_p}^N L_{(k)} \\ \quad \quad \quad \quad \; \; =\text{sum of the largest } N - K_p +1 \text{ samples divided by  } (1-p)N$$ 

### Impact of Return Distribution

**Experiment setup:**

* Computed the Sharpe optimal portfolio for the data in the spreadsheet
* Generate $$N = 10,000$$ samples of loss $$-r_x$$ for three different distributions
  * Multivariate Normal with mean $$\bm{\mu}$$ and covariance $$\bm{V}$$ 
  * Multivariate $$t$$ with $$\nu = 12$$ degree of freedom, mean $$\bm{\mu}$$ , covariance $$\bigg(\cfrac{\nu -2}{\nu} \bigg) \mathbf{V}$$ 
  * Mixture of Normals $$0.75 \cdot N(\bm{\mu}, (0.76)^2 \cdot \bm{V}) + 0.25 \cdot N(\bm{\mu}, (1.5)^2 \cdot \bm{V})$$ 
* Used samples to estimate VaR and CVaR

The Students’s t distribution has fatter tails than Normal particularly when the degrees of freedom are small. Expect VaR and CVaR to be larger. 

The Normal distribution with covariance matrix $$(1.5)^2V$$ has all volatilities 50% higher. The mixture models a situation where there is 25% chance of very high volatility. Expect VaR and CVaR to be large. 

* **Loss histogram for Normal returns**

![](../.gitbook/assets/image%20%2869%29.png)

* **Loss histogram for t returns**

![](../.gitbook/assets/image%20%2867%29.png)

* **Loss histogram for mixture of Normals**

![](../.gitbook/assets/image%20%2865%29.png)

### Pros and Cons of VaR

#### Pros

* Captures the tail behaviour of portfolio losses
* Can be robustly estimated from data: not very susceptible to outliers
* Captures the tail behaviour of portfolio losses beyond the p-th quantile
* Sub-additive: diversification reduces CVaR
* Mean-CVaR portfolio selection problems can be solve very efficiently

#### Cons:

* Only sensitive to the p-th quantile and not the distribution beyond
* Incentive for “tail stuffing”
* VaR is not sub-additive: diversification can increase VaR
* CVaR is defined by an expectation: can be sensitive to outliers
* We will return to the topic of VaR and CVaR in the risk management module

## Words

{% hint style="info" %}
* quantile 
  * Quantiles are points taken at regular intervals from the cumulative distribution function \(CDF\) of a random variable. Dividing ordered data into q essentially equal-sized data subsets is the motivation for q-quantiles; the quantiles are the data values marking the boundaries between consecutive subsets.
{% endhint %}

