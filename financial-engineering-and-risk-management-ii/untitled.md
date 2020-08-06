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

