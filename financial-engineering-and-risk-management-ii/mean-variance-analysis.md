# Mean Variance Analysis

## Overview

* Assets and portfolios
* Quantifying random asset and portfolio returns: mean and variance
* Mean-variance optimal portfolios
* Efficient frontier
* Sharpe ratio and Sharpe optimal portfolios
* Market portfolio
* Capital Asset Pricing Model

## Mean Variance Optimisation

### Assets and portfolios

Asset is anything we can purchase

* Random price: $$P(t)$$ 
* Random gross return: $$R(t) = \cfrac{P(t+1)}{P(t)}$$ 
* Random net return: $$r(t) = R(t) - 1 = \cfrac{P(t+1) - P(t)}{P(t)}$$ 

Total wealth $$W>0$$ distributed over $$d$$ assets

* $$w_i=$$ $ amount in asset $$i : w_i > 0 \equiv \text{long}, w_i < 0 \equiv \text{short}$$ 
* Net return on a position $$\bm{w}$$ 

$$r_w(t) = \cfrac{\displaystyle\sum_{i=1}^{d} R_i(t)w_i - \displaystyle\sum_{i=1}^{d} w_i}{W} = \cfrac{\displaystyle\sum_{i=1}^{d} r_i(t) w_i}{\displaystyle\sum_{i=1}^{d} w_i} = \displaystyle\sum_{i=1}^{d} r_i(t) \cdot \cfrac{w_i}{W}$$ 

* portfolio vector $$\bm{x} = (x_1, ..., x_d) : $$ each component can be $$+ve/-ve$$ 
  * $$x_i = $$ fraction invested in asset $$i \to \displaystyle\sum_{i=1}^{d} x_i = 1$$ 

Random net return on the portfolio $$r_x = \displaystyle\sum_{i=1}^{d} r_i x_i$$ 

### Random Returns on Assets and Portfolios

Parameters defining asset returns

* Mean of asset returns: $$\mu_i = \mathbb{E}[r_i(t)]$$ 
* Variance of asset returns: $$\sigma_i^2 = \mathbf{var}(r_i(t))$$ 
* Covariance of asset returns: $$\sigma_{ij} = \mathbf{cov}(r_i(t), r_j(t)) = \rho_{ij}\sigma_i \sigma_j$$ 
* Correlation of asset returns:  $$\rho_{ij} = \mathbf{cor}(r_i(t), r_j(t))$$ 

All parameters assumed to be constant over time. 

Parameters defining portfolio returns 

* Expected return on a portfolio $$\bm{x} = (x_1, ..., x_d)^{\intercal}$$ 

$$\mu_x = \mathbb{E}[r_x(t)] = \displaystyle\sum_{i=1}^d \mathbb{E}[r_i(t)]x_i = \displaystyle\sum_{i=1}^d \mu_i x_i$$ 

* Variance of the return on portfolio $$\bm{x} :$$ 

$$\sigma_x^2 = \mathbf{var}(r_x(t)) = \mathbf{var}\bigg( \displaystyle\sum_{i=1}^d r_i x_i \bigg) = \displaystyle\sum_{i=1}^d \displaystyle\sum _{j=1}^d \mathbf{cov}(r_i(t), r_j(t)) x_i x_j$$ 

### Diversification Reduces Uncertainty

$$d$$ assets each with $$\mu_i \equiv \mu, \sigma_i \equiv \sigma, \rho_{ij} = 0, \forall i \neq j$$ 

Two different portfolios

* $$\bm{x} = (1, 0,...,0)^{\top}$$ : everything invested in asset 1. 
* $$\bm{y} = \cfrac{1}{d} (1,1,...,1)^{\top}$$ : equal investment in all assets. 

Expected returns of the two portfolios

* $$\mu_x = \mathbb{E} \bigg[ \displaystyle\sum_{i=1}^d \mu_i x_i\bigg] = \mu_1 = \mu$$ 
* $$\mu_y = \mathbb{E} \bigg[ \displaystyle\sum_{i=1}^d \mu_i y_i\bigg] = \cfrac{1}{d} \displaystyle\sum_{i=1}^{d} \mu_i = \mu$$ 

Both have the same expected return!

Variance of returns of the two portfolios

* $$\sigma_x^2 = \mathbf{var}\bigg(\displaystyle\sum_{i=1}^d r_i x_i\bigg) = \sigma^2$$ 
* $$\sigma_y^2 = \mathbf{var}\bigg(\displaystyle\sum_{i=1}^d r_i y_i\bigg) = \displaystyle\sum_{i=1}^d \sigma^2\big(\cfrac{1}{d}\big)^2 = \cfrac{\sigma^2}{d}$$ 

Diversified portfolio has a much lower variance!

### Markowitz Mean-Variance Portfolio Selection

Markowitz \(1954\) proposed that 

* "Return" of a portfolio $$\equiv$$ Expected return $$\mu_x$$ 
* "Risk" of a portfolio$$\equiv$$ volatility $$\sigma_x$$ 

Efficient frontier

* Efficient frontier $$\equiv$$ max return for a given risk
* characterize the efficient frontier
* compute efficient/optimal portfolios 

![](../.gitbook/assets/image%20%2849%29.png)

### Mean Variance Formulations

* Minimize risk ensuring return $$\geq$$ target return

$$\min_x \sigma_x^2 \; \text{ s.t. } \; \mu_x \geq r \equiv \min_x \displaystyle\sum_{i=1}^d \displaystyle\sum_{j=1}^d \sigma_{ij}x_i x_j \;\text{ s.t. }\; \displaystyle\sum_{i=1}^d \mu_i x_i \geq r \; ,\; \displaystyle\sum_{i=1}^d x_i = 1$$ 

* Maximum return ensuring risk $$\leq$$ risk budget

$$\max_x \mu_x \; \text{ s.t. }  \; \sigma_x^2 \leq \bar{\sigma} ^2 \equiv \max_x \displaystyle\sum_{i=1}^d\mu_i x_i \; \text{ s.t. } \; \displaystyle\sum_{i=1}^d \displaystyle\sum_{j=1}^d \sigma_{ij} x_i x_j \leq \bar{\sigma}^2 \;, \; \displaystyle\sum_{i=1}^d x_i = 1.$$ 

* Maximum a risk-adjusted return 

$$\max_x (\mu_x - \tau\sigma_x^2) \equiv \max_x \bigg( \displaystyle\sum_{i=1}^d \mu_i x_i - \tau \bigg(   \displaystyle\sum_{i=1}^d \displaystyle\sum_{j=1}^d \sigma_{ij} x_i x_j \bigg) \bigg) \; \text{ s.t. } \; \displaystyle\sum_{i=1}^d x_i = 1$$ 

 $$\tau \equiv$$ risk-aversion\* parameter

## Efficient Frontier

### Mean-Variance for 2-Asset Market

$$d = 2$$ asserts

* Assert 1: mean return $$\mu_1$$ and variance $$\sigma_1^2$$ 
* Assert 2: mean return $$\mu_2$$ and variance $$\sigma_2^2$$ 
* Correlation between asset returns $$\rho$$ 

Portfolio: $$(x, 1-x)$$ 

$$\mu_x = \displaystyle\sum_{i=1} ^d \mu_i x_i  = \mu_1 x + \mu_2(1-x)$$ 

$$\sigma_x^2 = \displaystyle\sum_{i,j = 1}^d \sigma_{ij}x_i x_j = \displaystyle\sum_{i=1}^d \sigma_i^2x_i^2 + 2 \displaystyle\sum_{j > i} \sigma_{ij} x_i x_j \\ \quad \; \, = \sigma_1^2 x^2 + \sigma_2^2(1-x)^2 + 2 \rho\sigma_1\sigma_2 x(1-x)$$ 

Minimize risk formulation for the mean-variance portfolio selection problem

$$\min_x \big(\sigma_1^2 x^2 + \sigma^2_2 (1-x)^2 + 2\rho \sigma_1 \sigma_2 x (1+x)\big) \; \text{ s.t. } \; \mu_1 x + \mu_2 (1-x) = r$$ 

Expected return constraint $$x = \cfrac{r-\mu_2}{\mu_1 - \mu_2}$$ 

Variance:

$$\sigma_{r}^2 = \sigma_1^2 \bigg( \cfrac{r-\mu_2}{\mu_1 - \mu_2} \bigg) +  \sigma_2^2 \bigg( \cfrac{\mu_1 - r}{\mu_1 - \mu_2} \bigg) + 2 \rho \sigma_1 \sigma-2 \bigg( \cfrac{r-\mu_2}{\mu_1 - \mu_2} \bigg) \bigg( \cfrac{\mu_1 - r}{\mu_1 - \mu_2} \bigg) \\ \quad = a r^2 + br + c$$ 

Explicit expression for the variance as a function of target return $$r$$ . 

![](../.gitbook/assets/image%20%2848%29.png)

Only the top half is efficient.

### Computing the Optimal Portfolio

Mean-variance portfolio selection problem

$$\sigma^2(r) = \min_x(\displaystyle\sum_{i=1}^d \displaystyle\sum_{j=1}^d \sigma_{ij} x_i x_j) \; \text{ s.t. } \; \displaystyle\sum_{i=1}^d\mu_i x_i = r \; , \; \displaystyle\sum_{i=1}^d x_i = 1$$ 

From the **Lagrangian** with [**Lagrange multiplier**](https://en.wikipedia.org/wiki/Lagrange_multiplier) **** $$u, v$$ 

$$L = \displaystyle\sum_{i=1}^d \displaystyle\sum_{j=1}^d \sigma_{ij} x_i x_j v - v\bigg( \displaystyle\sum_{i=1}^d \mu_i x_i -r \bigg) - u \bigg( \displaystyle\sum_{i=1}^d x_i - 1\bigg)$$ 

Set $$\cfrac{\partial L}{\partial x_i} = 0 \text{ for } i=1,...,d$$ gives $$d$$equations

$$2 \displaystyle\sum_{i=1}^d \sigma_{ij} x_j - v\mu_i - u = 0, \text{ for all } i=1,...,d$$ 

Can solve the $$d+2$$ equations in $$d + 2$$ variables: $$x_1, ..., x_d, u \text{ and } v$$ .

**Theorem.** A portfolio $$\bm{x}$$ is mean-variance optimal if, and only if, it is feasible\* and there exists $$u, v$$ satisfy above equation. 

Matrix formulation

![](../.gitbook/assets/image%20%2850%29.png)

Therefore

![](../.gitbook/assets/image%20%2851%29.png)

### Two Fund Theorem

Fix two different target returns: $$r_1 \neq r_2$$ 

Suppose

* $$\bm{x}^{(1)} = \big( x_1^{(1)}, x_2^{(1)}, ..., x_d^{(1)} \big)^{\top}$$ optimal for $$r_1: $$ Lagrange multiplier $$(v_1, u_1)$$ 
* $$\bm{x}^{(2)} = \big( x_1^{(2)}, x_2^{(2)}, ..., x_d^{(2)} \big)^{\top}$$ optimal for $$r_2: $$ Lagrange multiplier $$(v_2, u_2)$$ 

Consider any other return $$r$$ 

* Choose $$\beta = \cfrac{r - r_1}{r_2 - r_1}$$ 
* Consider the position: $$\bm{y} = (1-\beta) \bm{x}^{(1)} + \beta \bm{x}^{(2)}$$ 

$$\bm{y}$$ is a portfolio

$$\displaystyle\sum_{i=1}^d y_i= (1-\beta) \displaystyle\sum_{i=1}^d x_i^{(1)} + \beta \displaystyle\sum_{i=1}^d x_i^{(2)} = (1- \beta) + \beta = 1$$ 

$$\bm{y}$$ is feasible for target return $$r$$ 

$$\displaystyle\sum_{i=1}^d y_i\mu_i= (1-\beta) \displaystyle\sum_{i=1}^d \mu_i x_i^{(1)} + \beta \displaystyle\sum_{i=1}^d \mu_i x_i^{(2)} = (1- \beta)r_1 + \beta r_2 = r$$ 

Set $$v = (1-\beta ) v_1 + \beta v_2 \text{ and } u = (1 + \beta) u_1 + \beta u_2$$ 

$$2  \displaystyle\sum_{j=1}^d \sigma_{ij} y_j - v \mu_i - u \\ \quad \quad = \displaystyle\sum_{j=1}^d 2 \sigma_{ij} \big( (1-\beta) x^{(1)}_j  + \beta x_j^{(2)}\big) - \mu_i \big( (1-\beta)v_1+ \beta v_2 -  \big) - \big( (1-\beta)u_1+ \beta u_2 \big) \\ \quad \quad =  (1 - \beta) \bigg( 2 \displaystyle\sum_{j=1}^d \sigma_{ij} x_j^{(1)} - v_1 \mu_i - u_1  \bigg) + \beta \bigg( 2  \displaystyle\sum_{j=1}^d \sigma_{ij} x_j^{(2)} - v_2 \mu_i - u_2 \bigg) = 0$$ 

$$\bm{y}$$ is optimal for target return $$r$$ .

**Theorem.** All efficient portfolios can be constructed by diversifying between any two efficient portfolios with different expected returns. 

The optimal portfolio for target return $$r$$ 

$$\mathbf{y}^{*} = \bigg( \cfrac{r_2 - r}{r_2 - r_1} \bigg) \mathbf{x}^{(1)} +  \bigg( \cfrac{r - r_1}{r_2 - r_1} \bigg) \mathbf{x}^{(2)} \\ \quad = \underbrace{r\bigg( \cfrac{\mathbf{x}^{(2)} - \mathbf{x}^{(1)}}{r_2 - r_1} \bigg)}_{g} + \underbrace{\bigg( \cfrac{r_2\mathbf{x}^{(1)} - r_1\mathbf{x}^{(2)}}{r_2 - r_1} \bigg)}_{h} \\ y_i^* = rg_i + h_i , \;\; i= 1, ..., d.$$ 

Therefore

$$\sigma^2(r) = \displaystyle\sum_{i=1}^d \displaystyle\sum_{j=1}^d \sigma_{ij} (rg_i + h_i) (rg_j + h_j) \\ \quad = r^2 \bigg( \displaystyle\sum_{i=1}^d \displaystyle\sum_{j=1}^d \sigma_{ij} g_i g_j \bigg) + 2r \bigg( \displaystyle\sum_{i=1}^d \displaystyle\sum_{j=1}^d \sigma_{ij} g_i h_j \bigg) + \bigg( \displaystyle\sum_{i=1}^d \displaystyle\sum_{j=1}^d \sigma_{ij} h_i h_j \bigg)$$ 

The $$d-$$ asset frontier has the same structure as the 2-asset frontier. 

## Mean-Variance with a Risk-Free Asset

### Definition

New asset: pays net return $$r_f$$ with no risk \(deterministic return\)

$$x_0=$$ fraction invested in the risk-free asset. 

Mean-variance problem: $$x_0 $$ does **not** contribute to risk. 

$$\max \big( (r_fx_0 + \displaystyle\sum_{i=1}^d \mu_i x_i) - \tau ( \displaystyle\sum_{i=1}^d  \displaystyle\sum_{j=1}^d \sigma_{ij} x_i x_j) \big) \; \text{ s.t. } \; x_0 +  \displaystyle\sum_{i=1}^d x_i = 1$$ 

Only meaningful for $$r \geq r_f$$ 

Substituting $$x_0 = 1 - \displaystyle\sum_{i=1}^d x_i$$ we get

$$\max \big(r_f + \displaystyle\sum_{i=1}^d (\mu_i - r_f ) x_i - \tau (\displaystyle\sum_{i=1}^d \displaystyle\sum_{j=1}^d \sigma_{ij} x_i x_j)\big)$$ 

$$\hat{\mu}_i = \mu_i - r_f=$$ excess return of asset $$i$$ 

### Mean-variance Optimal Portfolio

Taking derivatives $$\partial x_i$$ we get

$$\hat{\mu}_i - 2\tau \displaystyle\sum_{i=1}^d \sigma_{ij} x_j = 0, \;\; i = 1, ..., d$$ 

Matrix formulation

![](../.gitbook/assets/image%20%2852%29.png)

The family of frontier portfolio as a function of $$\tau$$ 

$$\bigg\{  \bigg( 1 - \displaystyle\sum_{i=1}^d x_i(\tau) , \bm{x}(\tau) \bigg) : \tau \geq 0 \bigg\}$$ 

### One-Fund Theorem

The positions in the risky assets in the frontier portfolio

$$\mathbf{x} = \cfrac{1}{2\tau} \mathbf{V}^{-1} \mathbf{\hat\mu}$$ 

do not add up to 1. 

Define a portfolio of risky assets by dividing x by the sum of its components

$$s^* = \bigg( \cfrac{1}{\sum_{i=1}^d x_i} \bigg) \cdot \mathbf{x} = \bigg( \cfrac{1}{\cfrac{1}{2\tau} \sum_{i=1}^d (\mathbf(V)^{-1}\mathbf{\hat\mu})_i} \bigg) \big( \cfrac{1}{2\tau} \mathbf{V}^{-1} \mathbf{\hat\mu} \big)$$ 

The portfolio $$s^*$$ is independent of $$\tau$$ . Since $$\displaystyle\sum_{i=1}^d x_i = 1-x_0 , \; \bm{x} = (1-x_0) \cdot \bm{s}^*$$ 

Family of frontier portfolios $$= \{ (x_0, (1- x_0) \cdot \bm{s}^*) : x_0 \in R \}$$ 

**Theorem.**  All efficient portfolios in a market with a risk-free asset can be constructed by diversifying between the risk-free asset and the single portfolio $$\bm{s}^*$$ .

### Efficient Frontier with Risk-Free Asset

Return and risk of portfolio $$\bm{s}^*$$ :

$$\text{Return : } \mu_s^* = \displaystyle\sum_{i=1}^d \mu_i s_i^* \\ \text{Risk : } \sigma_x^* = \sqrt{\displaystyle\sum_{i=1}^d \displaystyle\sum_{j=1}^i \sigma_{ij}^2 s_i^* s_j^*}$$ 

Return on a generic frontier portfolio: $$x_0$$ in risk-free and $$(1-x_0), \bm{s}^*$$ 

$$\mu_x = x_0 r_f + (1+x_0)\mu_s^* \\ \sigma_x = (1-x_0) \sigma_s^*$$ 

![](../.gitbook/assets/image%20%2855%29.png)

![](../.gitbook/assets/image%20%2856%29.png)

The portfolio $$\bm{s}^*$$ maximizes the angle $$\theta$$ or equivalently

$$\tan(\theta) = \cfrac{ \sum_{i=1}^d \mu_i x_i - r_f }{ \sqrt{\sum_{i=1}^d \sum_{j=1}^d \sigma_{ij} x_i x_j}} = \cfrac{\text{expected excess return}}{\text{volatility}}$$ 

### Sharpe Ratio

**Definition.** The **Sharpe ratio** of a portfolio or an asset is the ratio of the expected excess return to the volatility. The **Sharpe optimal portfolio** is a portfolio that maximizes the Sharpe ratio.

The portfolio $$\bm{s}^*$$ is a Sharpe optimal portfolio

$$\mathbf{s}^* = \displaystyle\arg\max_{\{ x: \sum_{i=1}^d x_i = 1 \}} \bigg\{ \cfrac{\mu_x - r_f}{\sigma_x} \bigg\}$$ 

Investors diversify between the risk-free asset and the Sharpe optimal portfolio. 

The investment in the various risky assets are in fixed proportions ... prices/returns should be correlated! This insight leads to the Capital Asset Pricing Model.

## Capital Asset Pricing Model

### Market Portfolio

**Definition.** Let $$C_i, i = 1, ..., d,$$ denote the market capitalization of the $$d$$ assets. Then the market portfolio $$\bm{x}^{(m)}$$ is defined as follows. 

$$x_{i}^{(m)} = \cfrac{C_i}{\sum_{j=1}^d} C_j \;, \;i = 1, ..., d $$ 

Let $$\mu_m$$ denote the **expected net rate** of return on the market portfolio, and let $$\sigma_m$$ denote the **volatility** of the market portfolio. 

Suppose all investors in the market are mean-variance optimizers. Then all of them invest in the Sharpe optimal portfolio $$\bm{s}^*$$ . Let

* $$w^{(k)} : $$ wealth of the k-th investor
* $$x_0^{(k)}:$$ fraction of wealth of the k-investor in the risk-free asset. 

Then

$$C_i = \displaystyle\sum_k w^{(k)} (1 - x_0^{(k)}) s_i^*$$ 

The market portfolio $$\bm{x}^{(m)} =$$ Sharpe optimal portfolio $$\bm{s}^*$$ .

## Words

{% hint style="info" %}
* aversion
  * a feeling of intense dislike
  * the act of turning yourself \(or your gaze\) away
* feasible
  * capable of being done with means at hand and circumstances as they are
{% endhint %}



