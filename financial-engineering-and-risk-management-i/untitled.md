# Model Calibration

## Model Calibration

* Until now have focused on pricing derivative securities
  * we have taken the model and its parameters as given. 
* But a model is no good unless \(at the very least\) the model prices agree with the market prices of liquid securities such as cap, floors, swaptions etc. 
* So need to calibrate the model to market prices
  * there are too many **free parameters**, e.g. $$r_{i,j}, q_{i,j} \text{ for all } i, j$$ 
  * so we **fix** some parameters, e.g. $$q_{i,j} = q = 1-q = 0.5 \text{ for all } i,j$$ 
  * and assume some **parametric** form for the $$r_{i,j}$$ 's
* Here we will focus on **Black-Derman-Toy \(BDT\)** model

### The Black-Derman-Toy Model

* The BDT model assumes that the interest rate at node $$N(i,j)$$ is given by

$$r_{i,j} = a_i e^{b_ij} \text{ apply } log \text{ we have }\\  \ \\ \log(r_{i,j}) = \log(a_i) + b_ij$$ 

* where
  * $$log(a_i)$$ is a drift parameter for $$log(r)$$ 
  * $$b_i$$ is a volatility parameter for $$log(r)$$ 
* Need to calibrate the model to observed term-structure in the market
  * and, ideally, other security prices
* This is done by choosing the $$\{a_i\}  \text{ and } \{b_i\}$$ to match market prices
* Have an n-period binomial lattice
* $$(s_1, s_2, ..., s_n)$$ is the term-structure of interest rates **observed** in the market 
  * assume spot rates are compounded per period
* Assume for now that $$b_i = b$$ is **known** for all $$i$$, where $$P_{i,j}^e$$ is the elementary price on time $$i$$ state $$j$$ , we use the forward equation to calculate then

$$\cfrac{1}{(1+s_i)^i} = \displaystyle\sum_{j=0}^i P_{i,j}^e ( = Z_0^i )\\ = \cfrac{P_{i-1,0}^e}{2\cdot(1+a_{i-1})} + \displaystyle\sum_{j=1}^{i-1} \bigg( \cfrac{P_{i-1,j}^e}{2\cdot(1+a_{i-1}e^{bj})} + \cfrac{P_{i-1,j-1}^e}{2\cdot(1+a_{i-1}e^{b(j-1)})} \bigg) + \cfrac{P_{i-1,i-1}^e}{2\cdot(1+a_{i-1}e^{b(i-1)})}$$ 

## Pricing a Payer Swaption

* Consider a 2-8 **payer swaption** in the BDT model with fixed rate = 11.65%
  * An option to enter an 8-year swap in 2 years time
  * settled in arrears so payments would take place in years 3 through 10
    * each payment based on the prevailing short-rate of previous year
  * "payer" feature of option means that if option is exercised, the exerciser "pays fixed and receives floating"
  * owner of a **receiver swaption** would "receive fixed and pay floating"
* In this example, we use 10-period lattice with 1 period corresponding to 1 year
* Assume $$b_i = b = 0.005$$ \(this is a significant assumption\)
* The $$\{a_i\}$$ are calibrated to match the market term structure

![](../.gitbook/assets/image%20%2837%29.png)

### Pricing the Swaption

* Assume a notional principal of $1M
* Let $$S_2$$ denote the value of swap at $$t=2$$ 
  * $$S_2$$ can be computed by discounting cash-flows back from $$t = 10 \text{ to } t = 2$$ 
  * recall it's easier to record time $$t$$ cash flows at their predecessor nodes, discounting appropriately.
  * which is why there are no payments recorded at $$t=10$$ in the swaption lattice
* Option is then exercised if and only if $$S_2 > 0$$ so value at $$t=2$$ is $$\max(0,S_2)$$ .
* Then discount backwards to $$t=0$$ to find swaption price at $$t = 0$$ . 
* When we calibrate to ZCB’s in market place we find swaption price of $13, 339 when $$b = 0.005$$ . 
* When we take $$b = 0.01$$ we find a swaption price of $19, 497
  * we must remember to recalibrate model when we change $$b$$ . 
* So we see a significant difference in swaption prices
  * even though both models, i.e. the model with $$b = 0.005$$ and the model with $$ b = 0.01$$ , were calibrated to the **same** ZCB prices. 
* This is not surprising: swaption prices clearly depend on model **volatility**
  * which is controlled by $$b$$ 
  * and not influenced at all by calibrating to ZCB prices. 
* This has very important implications for the calibration process in general
  * want our calibration securities to be “close” to the securities we want to price with the calibrated model

## Fixed Income Derivatives Pricing

In practice more complex models than binomial models are used to price fixed income derivatives today. But the pricing philosophy is the same:

* Specify a model under the $$\Bbb{Q}(\bm{\theta})$$-dynamics
  *  $$\bm{\theta}$$ is a vector of parameters, e.g. the $$\{a_i\} \text{ and } \{b_i\}$$ in BDT
* Price all securities using 

$$\cfrac{Z_t}{B_t} = E_t^{\Bbb{Q}(\theta)} \bigg[ \displaystyle\sum_{j=t+1}^{t+s} \cfrac{C_j}{B_j} + \cfrac{Z_{t+s}}{B_{t+s}} \bigg]$$ 

* Now choose $$\bm{\theta}$$ so that market prices of appropriate liquid securities agree with model prices of those securities. 
  * This is the model calibration procedure.

Calibration problem typically requires minimizing a sum of squares:

$$\displaystyle\min_{\bm{\theta}} \displaystyle\sum_{i} \omega_i\cdot\big( P_i(\text{model}) - P_i(\text{market}) \big)^2 + \lambda|| \bm{\theta - \bm{\theta_{prev}}} ||^2$$ 

where

* $$P_i(\text{model})$$ is the **model** price of the $$i^{th}$$ calibration security
* $$P_i(\text{market})$$ is the **market** price of the $$i^{th}$$ calibration security
* $$\omega_i$$ is a positive weight reflecting the importance of the $$i^{th}$$ security or the confidence we have in its market price
* $$\bm{\theta_{prev}} \equiv$$ previously calibrated model parameters
* and $$\lambda$$ is a parameter reflecting relative importance of remaining close to previous calibration.

Once the model has been calibrated, i.e. \(2\) has been solved to our satisfaction, we can sue the model to hedge and pricing more exotic or illiquid security. 

**However, the problem is**

* Above equation is often difficult to solve
  * a non-convex optimization problem with many local minima
* As market conditions change, need to re-calibrate frequently
  * often many times a day.
* If the model was “right” would only need to calibrate once
* Markets are too complex and there is \(unfortunately\) no right model
  * or even a model that is close to “being right”.
* Derivatives pricing in practice then is little more than using observable market prices to **interpolate** or **extrapolate** to price non-observable security prices
  * but risk-neutral pricing at the model level implies that we can extrapolate / interpolate in an arbitrage-free manner.
* True probabilities and market risk aversion enter the derivatives prices via the calibration process.



