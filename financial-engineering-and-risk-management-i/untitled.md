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

### Pricing a Payer Swaption

* Consider a 2-8 **payer swaption** in the BDT model with fixed rate = 11.65%
  * An option to enter an 8-year swap in 2 years time
  * settled in arrears so payments would take place in years 3 through 10
    * each payment based on the prevailing short-rate of previous year
  * "payer" feature of option means that if option is exercised, the exerciser "pays fixed and receives floating"
  * owner of a **receiver swaption** would "receive fixed and pay floating"
* In this example, we use 10-period lattice with 1 period corresponding to 1 year
* Assume $$b_i = b = 0.005$$ \(this is a significant assumption\)
* The $$\{a_i\}$$ are calibrated to match the market term structure

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

