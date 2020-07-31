# Mean Variance Analysis

## Overview

* Assets and portfolios
* Quantifying random asset and portfolio returns: mean and variance
* Mean-variance optimal portfolios
* Efficient frontier
* Sharpe ratio and Sharpe optimal portfolios
* Market portfolio
* Capital Asset Pricing Model

## Mean Variance Optimization

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



