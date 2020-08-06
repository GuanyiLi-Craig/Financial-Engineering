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



