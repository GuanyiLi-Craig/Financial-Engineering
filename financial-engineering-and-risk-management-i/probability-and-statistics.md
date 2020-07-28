# Probability and Statistics

## Review of Basic Probability

### Discrete random Variable

**Definition.** The _cumulative distribution function \(CDF\)_, $$F(\cdot)$$ , of a random variable, $$X$$ , is defined by 

$$\text{F}(x) := \text{P}(X \leq x).$$ 

**Definition.** A discrete random variable, $$X$$ , has _probability mass function \(PMF\)_, $$p(\cdot)$$, if $$p(x) \geq 0$$ and for all events $$A$$  we have

$$\text{P}(X \in A ) = \displaystyle\sum_{x\in A} p(x).$$ 

**Definition.** The _expected value_ of a discrete random variable, $$X$$ , is given by

$$\text{E}[X] := \displaystyle\sum_{i} x_i \cdot p(x_i). $$ 

**Definition.** The _variance_ of any random variable, $$X$$, is defined as 

$$\text{Var}(X) := \text{E}\big[( X - \text{E}[X])^2 \big] \\ \quad \quad \quad \quad = \text{E}[X^2] - \text{E}[X]^2$$ 

### The Binomial Distribution

We say $$X$$ has a binomial distribution, or $$X \sim \text{Bin}(n, p)$$ , if

$$\text{P}(X = r) = \dbinom{n}{r} p^r(1-p)^{n-r}$$ 

For example, $$X$$ might represent the number of heads in $$n$$ independent coin tosses, where $$p = \text{P(head)}$$ . The mean and variance of the binomial distribution satisfy

$$\text{E}[X] = n\cdot p\\ \text{Var}(X) = n \cdot p \cdot (1-p)$$ 

* Suppose a fund manager outperforms the market in a given year with probability $$p$$ and that the underperforms the market with probability $$1-p$$ 
* She has a track record of 10 years and has outperformed the market in 8 of the 10 years. 
* Moreover, performance in any one year is independent of performance in other years. 
* The probability of a random player \( $$p = 0.5, n=10, r=8$$ \) has the same outcome is

$$\text{P}(X\geq 8) = \displaystyle\sum_{r=8}^{10} 0.5^r \cdot (1-0.5)^{10-r}$$ 

* Suppose there are M random players, the expectation of the best one over 10 years is
  * \(Order statistic\)

### The Poisson Distribution

The Poisson distribution $$\text{Poisson}(\lambda)$$ of $$X$$ is

$$\text{P}(X = r) = \cfrac{\lambda^r\cdot e^{-\lambda}}{r!}$$ 

and $$\text{E}[X] = \lambda \text{ and } \text{Var}(X) = \lambda$$ 

### Bayes' Theorem

Let $$A$$ and $$B$$ be two events for which $$P(B) \neq0$$ . then

$$\text{P}(A|B) = \cfrac{\text{P}(A\bigcap B)}{\text{P}(B)} \\ \quad \quad \quad = \cfrac{\text{P}(B | A) \text{P}(A)}{\text{P}(B)} \\ \quad \quad \quad = \cfrac{\text{P}(B | A) \text{P}(A)}{\sum_j \text{P}(B | A_j) P(A_j)}$$ 

where the $$A_j $$ 's form a partition of the sample-space, where

$$A_i \bigcap A_j  = \text{\O}, \text{ for } i \neq j$$ and at least one $$A_i$$ must occur.

### Continuous Random Variables

Definition. A continuous random variable, $$X$$ , has _probability density function \(PDF\)_, $$f(\cdot)$$ , if $$f(x) \geq 0$$ and for all events $$A$$ 

$$\text{P}(X \in A) = \displaystyle\int_{A} f(y) dy.$$ 

The CDF and PDF are related by 

$$\text{F}(x) = \displaystyle\int_{-\infty}^{x} f(y) dy$$ 

It is often convenient to observe that

$$\text{P} \big( X \in (x - \cfrac{\epsilon}{2}, x + \cfrac{\epsilon}{2}) \big) \approx \epsilon \cdot f(x)$$ 

### The Normal Distribution

We say $$X$$ has a Normal distribution, or $$X \sim \text{N}(\mu, \sigma^2)$$ if 

$$f(x) = \cfrac{1}{\sqrt{2\pi\sigma^2}}\text{exp}\bigg( -\cfrac{(x-\mu)^2}{2\sigma^2} \bigg)$$ 

The mean and variance of the normal distribution satisfy

$$\text{E}[X] = \mu\\ \text{Var}(X) = \sigma^2$$ 

### The Log-Normal Distribution

[&lt;-- wiki --&gt;](https://en.wikipedia.org/wiki/Log-normal_distribution)

We say $$X$$ has a log-normal distribution, or $$X \sim \text{LN}(\mu, \sigma^2),$$ if 

$$\text{log}(X) \sim \text{N}(\mu, \sigma^2)$$ 

The mean and variance of the log-normal distribution satisfy

$$\text{E} [X] = \text{exp}(\mu + \sigma^2/2) \\ \text{Var}(X) = \text{exp}(2\mu + \sigma^2) \cdot (\text{exp}(\sigma^2) - 1)$$ 

The log-normal distribution plays a very important in financial application

Examples

![](../.gitbook/assets/image%20%2846%29.png)

![](../.gitbook/assets/image%20%2847%29.png)

