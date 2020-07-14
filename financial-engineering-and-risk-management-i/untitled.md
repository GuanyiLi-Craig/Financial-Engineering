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

$$r_{i,j} = a_i e^{b_ij}$$ 

* where
  * $$log(a_i)$$ is a drift parameter for $$log(r)$$ 
  * $$b_i$$ is a volatility parameter for $$log(r)$$ 
* Need to calibrate the model to observed term-structure in the market
  * and, ideally, other security prices
* This is done by choosing the $$\{a_i\}  \text{ and } \{b_i\}$$ to match market prices
* Have an n-period binomial lattice
* $$(s_1, s_2, ..., s_n)$$ is the term-structure of interest rates **observed** in the market 
  * assume spot rates are compounded per period
* Assume for now that $$b_i = b$$ is known for all $$i$$ , then

$$\cfrac{1}{(1+s_i)^i} = \displaystyle\sum_{j=0}^i P_{i,j}^e \\ = \cfrac{P_{i-1,0}^e}{2\cdot(1+a_{i-1})} + \displaystyle\sum_{j=1}^{i-1} \bigg( \cfrac{P_{i-1,j}^e}{2\cdot(1+a_{i-1}e^{bj})} + \cfrac{P_{i-1,j-1}^e}{2\cdot(1+a_{i-1}e^{b(j-1)})} \bigg) + \cfrac{P_{i-1,i-1}^e}{2\cdot(1+a_{i-1}e^{b(i-1)})}$$ 



