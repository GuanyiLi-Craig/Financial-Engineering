# Defaultable Bonds

## Defaultable Bonds

Characterized by 

* Coupon $$c$$ 
* Face value $$F$$ 
* Recovery value $$R=$$random fraction of face value recovered on default

As before, we use risk neutral probability $$\Bbb{Q}$$ , model the term structure of default using a 1-step default probability

$$h(t) = \Bbb{Q}(\text{bond default in } [t, t+1] \;| \; \cal{F}_t)$$ 

* Calibrate $$h(t)$$ to market prices
* Modify the binomial lattice to include defaults

### Binomial Lattice for Short Rates

Binomial lattice for the shart rate

* Nodes $$(i,j)$$ : time $$i = 0,1,...,n$$ and state $$j=0,1,...,i$$ 
* stort rate $$r_{ij}$$ 
* state transition probability

$$\Bbb{Q}\big((i+1, s) \;|\;(i,j) \big) = \begin{cases} q_u \;\;\; s = j+1 \\ q_d \;\;\; s= j \\ 0 \;\;\;\; \text{otherwise} \end{cases}$$ 

"Split" node $$(i,j)$$ by introducing a variable that encodes whether or not default has occurred before date $$i$$ 

* $$(i,j,0)=$$ state $$j$$ on date $$i$$ with default time $$\tau > i$$ 
* $$(i,j,1)=$$ state $$j$$ on date $$i$$ with default time $$\tau \leq i$$ 

![](../.gitbook/assets/image%20%2838%29.png)

Transitions from no-default state $$(i,j,0)$$ 

$$\Bbb{Q}\big((i+1, s, \eta) \;|\;(i,j,0)\big) = \begin{cases}  q_u \textcolor{blue}{h_{ij}} \;\;\;\;\;\;\;\;\;\;\;\; s=j+1, \eta = 1 \;(\text{default}) \\     q_u \textcolor{blue}{(1-h_{ij})} \;\;\; s=j+1, \eta=0 \; (\text{no default}) \\   q_d \textcolor{blue}{h_{ij}} \;\;\;\;\;\;\;\;\;\;\;\; s=j, \eta = 1 \;(\text{default}) \\     q_d \textcolor{blue}{(1-h_{ij})} \;\;\; s=j, \eta=0 \; (\text{no default}) \\ 0 \quad \quad \quad \quad \;\;\; \text{otherwise} \end{cases}$$ 

Transitions from default state $$(i,j,1)$$ : default state is an "absorbing" state

$$\Bbb{Q}\big((i+1, s, \eta) \;|\;(i,j,0)\big) = \begin{cases}  q_u   \quad \quad \quad s=j+1, \eta = 1 \;(\text{default}) \\      q_d  \quad \quad \quad s=j, \eta = 1 \;(\text{default}) \\ 0 \quad \quad \quad \; \text{otherwise} \end{cases}$$ 

Conditional default probability $$h_{ij}$$ is state dependent.

## Zero-Coupon Bonds

### Default-free Zero-Coupon Bonds

Default-free zero-coupon bonds with expiration T 

* pay $1 in every state at the expiration date T 
* no default possible

Pricing

* $$Z_{i,j,\eta}^{T} =$$ price of a bond maturing on date $$T$$ in node $$(i,j,\eta)$$ 
* Default events do not affect default-free bonds

$$Z_{i,j,1}^T = Z_{i,j,0}^T := Z_{i,j}^T$$ 

* Risk-neutral price

$$Z_{i,j}^T = \cfrac{1}{1+r_{ij}}\bigg[ q_uZ_{i+1, j+1}^T + q_d Z_{i+1, j}^T \bigg]$$ 

Calibrate the short-rate lattice using the prices of the default-free ZCBs and other default-free instruments. 

### Defaultable ZCBs with no recovery

Defaultable zero-coupon bonds with expiration T and no-recovery on default 

* pay $1 in every state at the expiration date $$T$$ provided default has not occurred at any date $$t\leq T$$ . 
* If default occurs at any date $$t\leq T$$ , the bond pays 0, i.e. there is **no recovery**

Pricing 

* $$\bar{Z}_{i,j,\eta}^T=$$ price of a bond maturing on date $$T$$ in node $$(i,j,\eta)$$ 
* No recovery implies that $$\bar{Z}_{i,j,1}^T \equiv0$$ in all default nodes $$(i,j,1)$$ 
* Risk-neutral pricing:

$$\bar{Z}_{i,j,0}^T = \cfrac{1}{1+r_{ij}} \bigg[ q_u (1-h_{i,j}) \bar{Z}_{i+1,j+1,0}^T + q_d(1-h_{ij})\bar{Z}_{i+1,j,0}^T \bigg] \\ + \cfrac{1}{1+r_{ij}} \bigg[ q_u h_{i,j} \bar{Z}_{i+1,j+1,1}^T + q_dh_{ij}\bar{Z}_{i+1,j,1}^T \bigg] $$ Calibrate $$h_{ij}$$ using the prices of the defaultable ZCBs. 



