# Option Pricing in the 1-PBM

## Option Pricing in the 1-Period Binomial Model

![](../.gitbook/assets/image%20%284%29.png)

Assume now that $$R = 1.01$$, there are two questions

1. How much is a call option that pays $$\max(S_1 - 102, 0)$$  at $$t=1$$ worth?
2. How will the price vary as $$p$$ varies?

In order to answer these, we need to construct a **replicating portfolio**

## The Replicating Portfolio

In short words, the replicating portfolio is a portfolio that attempts to **match**, as closely as possible, some **benchmark or index**.

* Consider buying $$x$$ shares and investing $$$y$$ in cash at $$t=0$$
* At $$t=1$$ this portfolio is worth

$$107x + 1.01y$$  when $$S = 107$$ 

$$93.46x + 1.01y$$ when $$S = 93.46$$ 

In order to make portfolio **equals option payoffs** $$\max(S_1 - 102, 0)$$ at $$t=1$$ , we must solve

 $$\begin{cases}107x + 1.01y = 5 \\ 93.46x + 1.01y = 0 \end{cases}$$

Then we have the solution

$$\begin{cases} x = 0.3693 \\ y=-34.1708 \end{cases} $$ 

which is the **replicating portfolio**. The negative $$y$$ means we borrow money. 

* The cost of this portfolio at $$t=0$$ is 
  * $$x\cdot 100 + y\cdot 1 = 0.3693\times 100 - 34.1708 \times 1 \approx 2.76$$ 
* So the fair value of the option is 2.76
  * it is also the arbitrage-free value of the option
* The options price does not directly depend on buyer's \(or seller's\) utility function. 

## Derivative Security Pricing

A derivative security is a financial instrument whose value depends upon the value of another asset.

Suppose here we have a more general model,  we can use same replicating portfolio argument to find price, $$C_0$$ , of any **derivative security** with payoff function,  $$C_1(S_1)$$ , at time t = 1.

![](../.gitbook/assets/image%20%289%29.png)

Here we have 

 $$\begin{cases}uS_0x + Ry = C_u \\ dS_0x + Ry = C_d \end{cases}$$

Solve x and y and then we can find $$C_0$$ 

$$C_0 = \cfrac{1}{R} [\cfrac{R-d}{u-d}C_u + \cfrac{u-R}{u-d}C_d] \\ = \cfrac{1}{R}[\color{red}{q} C_u + \color{red}{(1-q)}C_d] \\ = \cfrac{1}{R} E_0^{\color{red}{Q}} [C_1]$$ 

From this equation we can observe that

* if there is no-arbitrage then $$0< q <1$$  
  * we call this equation is risk-neutral pricing
  * and $$(q, 1-q)$$ are the risk-neutral probability
* this represent an equation that can solve **any** derivative security in this type of 1 period model
* the problem is , $$p$$ didn't impact the result at all. 

