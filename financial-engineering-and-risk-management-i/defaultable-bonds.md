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

$$\bar{Z}_{i,j,0}^T = \cfrac{1}{1+r_{ij}} \bigg[ q_u (1-h_{i,j}) \bar{Z}_{i+1,j+1,0}^T + q_d(1-h_{ij})\bar{Z}_{i+1,j,0}^T \bigg] \\ + \cfrac{1}{1+r_{ij}} \bigg[ q_u h_{i,j} \bar{Z}_{i+1,j+1,1}^T + q_dh_{ij}\bar{Z}_{i+1,j,1}^T \bigg] $$ 

Where $$\bar{Z}_{i+1,j+1,1}^T \equiv 0 \text{ and  }\bar{Z}_{i+1,j,1}^T \equiv 0$$ . Calibrate $$h_{ij}$$ using the prices of the defaultable ZCBs. 

The risk-neutral prices is 

$$\bar{Z}_{i,j,0}^{T} = \cfrac{1-h_{ij}}{1+r_{ij}} \bigg[  q_u\bar{Z}_{i+1,j+1,0}^T + q_d\bar{Z}_{i+1, j ,0}^T \bigg] \\ \approx e^{-(r_{ij}+h_{ij})}E^{\bar{\Bbb{Q}}}_i[\bar{Z}_{i+1,.,.}^T]$$ 

where $$\bar{\Bbb{Q}}$$ is the default-free risk-neutral probability.

Price of a defaultable ZCB is set by discounting the expected value by $$(r_{ij} + h_{ij})$$ 

* $$h_{ij} $$ is the 1-period **credit spread**
* conditional probability of default $$h_{ij}$$ also called the **hazard rate**

### ZCBs with Recovery

Assumption: random recovery $$\tilde{R}$$ is independent of the default and interest dynamics. Let $$R=\Bbb{E}[\tilde{R}]$$ 

* $$\bar{Z}_{i,j,\eta}^T=$$ price of a bond maturing on date $$T$$ in node $$(i,j,\eta)$$ after recovery
* $$\bar{Z}_{i,j,1}^T \equiv 0$$ in all default nodes $$(i,j,1)$$ 

Risk-neutral pricing

$$\bar{Z}_{i,j,0}^T = \cfrac{1}{1+r_{ij}} \bigg[ q_u (1-h_{i,j}) \bar{Z}_{i+1,j+1,0}^T + q_d(1-h_{ij})\bar{Z}_{i+1,j,0}^T \bigg] \\ \quad \quad \;\;\;\; + \cfrac{1}{1+r_{ij}} \bigg[ q_u h_{i,j} R + q_dh_{ij}R \bigg] $$ 

## Pricing Defaultable Bonds

### State-Independent Hazard Rates

**Assumption:** hazard rates $$h_{ij}$$ are state-independent, i.e. $$h_{ij} = h_i$$ 

* Ensures that the default event is independent of interest rate dynamics
* Let $$q(t)=$$ risk-neutral probability that the bond survives until date $$t$$ 
* Then $$q(t+1) = (1-h_t)q(t) = \displaystyle\prod_{k=0}^{t} (1-h_k)$$ 

Let $$I(t)$$ denote the indicator variable that bond survives up to time $$t$$, i.e.

$$I(t) = \begin{cases} 1 \quad \text{Bond is not in default at time }t  \\ 0 \quad \text{Otherwise} \end{cases}$$ 

Then the indicator variable for default at time $$t$$ is $$I(t-1) - I(t)$$ 

From the definition of $$I(t)$$ is follows that

$$\Bbb{E}_{0}^{\Bbb{Q}} [I(t)] = q(t) $$ 

### Pricing Bonds with Recovery

**Assumption:** Random recovery rate $$\tilde{R}$$ is independent of interest rate dynamics under $$\Bbb{Q}$$ . Let $$R = \Bbb{E}^{\Bbb{Q}}_{0}[\tilde{R}]$$ 

* $$\tilde{R}$$ is the fraction of the face value $$F$$ paid on default. 

Pricing details

* $$t=0$$ is the current date
* $$\{ t_1, t_2, ..., t_n \}$$ are the future dates at which coupons are paid out. 
* The coupon is paid on date $$t_k$$ only if $$I(t_k) = 1$$ . Therefore the random cash flow associated with the coupon payment on date $$t_k$$ is $$cI(t_k)$$ 
* The face value $$F$$ is paid on date $$t_n$$ only if $$I(t_n) = 1$$ . Therefore, the random cash flow associated with the face value payment on date $$t_n$$ is $$FI(t_n)$$ 
* The recovery $$\tilde{R}(t_k)F$$ is paid on date $$t_k$$ is the bond defaults on date $$t_k$$ . Therefore, the random cash flow associated with recovery on date $$t_k$$ is 

$$\tilde{R}(t_k)F\big(I(t_{k-1}) - I(t_k)\big)$$ 

Let $$B(t)$$ denote the value of the cash account at time $$t$$ . Then the price $$\bar{P}(0)$$ of defaultable fixed coupon bond is given by

$$\bar{P}(0) = \Bbb{E}^{\Bbb{Q}}_0 \bigg[ \displaystyle\sum_{k=1}^{n} \cfrac{cI(t_k)}{B(t_k)} + FI(t_n) \cfrac{1}{B(t_n)} + \displaystyle\sum_{k=1}^{n} \cfrac{\tilde{R}(t_k)F}{B(t_k)}\big( I(t_{k-1}) - I(t_k) \big) \bigg]$$ $$\quad \quad = \displaystyle\sum_{k=1}^n c\Bbb{E}^{\Bbb{Q}}_0\big[ I(t_k) \big] \cdot \Bbb{E}^{\Bbb{Q}}_0 \bigg[ \cfrac{1}{B(t_k)} \bigg] + F\Bbb{E}^{\Bbb{Q}}_0 \big[ I(t_n) \big] \cdot \Bbb{E}^{\Bbb{Q}}_0\cfrac{1}{B(t_n)} \\ \quad \quad \quad + RF\displaystyle\sum_{k=1}^n \big( \Bbb{E}^{\Bbb{Q}}_0\big[ I(t_{k-1}) \big] - \Bbb{E}^{\Bbb{Q}}_0 \big[ I(t_k) \big] \big) \cdot \Bbb{E}^{\Bbb{Q}}_0\bigg[ \cfrac{1}{B(t_k)} \bigg]$$ $$\quad \quad = \displaystyle\sum_{k=1}^n cq(t_k)Z_0^{t_k} + Fq(t_n)Z_0^{t_n} + RF\displaystyle\sum_{k=1}^n\big( q(t_{k-1}) - q(t_k) \big) Z_0^{t_k} \\ \quad \quad = \displaystyle\sum_{k=1}^n cq(t_k)d(0, t_k) + Fq(t_n)d(0, t_n) + RF\displaystyle\sum_{k=1}^n\big( q(t_{k-1}) - q(t_k) \big) d(0,t_k)$$ 

### Calibrating Hazard Rates

* Assume interest rate $$r$$ is deterministic and known.
* Model price $$P(\bm{h})$$ of defaultable bond is a function $$\bm{h} = (h_0, h_1, ..., h_{n-1})$$ 
* Observe market prices for $$m$$ bonds
  * $$P^{mkt}_i=$$ market price for $$i^{th}$$ bond with expected recovery $$R_i, i=1,2,...,m$$ 
* Assumption: default of all bonds induced by the same "credit event"
* Model calibration
  * Model price of $$i^{th}$$ bond: $$P_i(\bm{h})$$ 
  * Pricing error: $$f(\bm{h}) = \displaystyle\sum_{i=1}^{m}\big( P^{mkt}_i - P_i(\bm{h}) \big)^2$$ 
  * Calibration problem: $$\min_{\bm{h}\geq 0} f(\bm{h})$$ 



