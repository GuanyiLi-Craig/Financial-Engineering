# Cheat Sheet

## Fixed Income

**Fixed income** refers to any type of investment under which the **borrower or issuer** is obliged to make payments of a **fixed amount** on a **fixed schedule.**

### **Interest Rate**

Consider rate **r** per period with n periods. 

* **Simple Interest**

$$W = A\cdot(1 + n\cdot r)$$ 

* **Compound Interest**

$$W=A\cdot(1 + n)^r$$ 

* **Compound Interest less than a fixed period**
  * **n** compounding periods in a fixed period

$$W = A\cdot(1+\cfrac{r}{n})^{y\cdot n}$$ 

* **Continuous compounding**

$$W = \lim\limits_{n\to \infty}A\cdot(1-\cfrac{r}{n})^{y\cdot n} = A\cdot e^{r\cdot y}$$ 

### Present Value

Present value \(PV\) is the current value of a future sum of money or stream of cash flows given a specified rate of return. 

**Description**. A contract pays $$\mathbf{c} = (c_0, c_1, c_2, ... c_N)$$where $$c_k > 0 \equiv$$cash inflow, and $$c_k < 0 \equiv$$cash outflow, and for each pay the interest rate $$\mathbf{r} = (0, r_1, r_2, ..., r_N)$$ . 

$$PV(\mathbf{c}, \mathbf{r}) = \displaystyle\sum_{k=0}^N \cfrac{c_k}{(1+r_k)^k}$$

* **Bounded the contract price** $$p$$ when lending rate $$r_L <$$ borrowing rate $$r_B$$ , they 

  $$PV(\mathbf{c}, r_B) \leq p \leq PV(\mathbf{c}, r_L)$$

* **For perpetuity case,** suppose $$c_k = A, r_k = r$$ , 

$$p=\displaystyle\sum_{k=1}^{\infty} \cfrac{A}{(1+r)^k} = \cfrac{A}{r}$$

### Bond

* **Yield to maturity\(YTM\)** $$\lambda$$ **and bond price** $$P$$ 
  * Face value F
  * pays $$c = \alpha F /2$$every half a year

\*\*\*\*$$P = PV = \cfrac{F}{(1+\lambda/2)^{2T}} + \displaystyle\sum_{k=1}^{2T} \cfrac{c}{(1+\lambda/2)^k}$$

### Linear Pricing

**Theorem**. \(**Linear Pricing**\) Suppose there is no arbitrage. Suppose also

* Price of cash flow $$c_A$$ is $$p_A$$
* Price of cash flow $$c_B$$ is $$p_B$$ 

Then the price of cash flow that pays $$c = c_A + c_B$$ must be $$p_A + p_B$$. 

* **Floating Rate Price** $$P_f$$ 
  * Face price $$F$$ 

 $$P_f = F$$ ****

### Term Structure of Interest Rates

* **Spot rate** $$s_t =$$ interest rate for a loan maturing in  $$t$$ years

 $$A$$ in year  $$t \to PV = \cfrac{A}{(1+s_t)^t}$$

* **Discount rate**

  $$d(0, t) = \cfrac{1}{(1+s_t)^t}$$

* **Forward rate**  $$f_{uv}$$ : interest rate quoted _today_ for lending from year  $$u$$ to  $$v$$
  * From no-arbitrage , at time  $$v$$ the income should be the same. So that

 $$f_{uv} = (\cfrac{(1+s_v)^v}{(1+s_u)^u})^{\cfrac{1}{v-u}} - 1$$

* **Relation between spot and forward rates is**

 $$(1+s_t)^t = \displaystyle\prod_{k=0}^{t-1}(1+f_{k,k+1})$$

### **Forward Contract**

* **Forward price** $$F_t$$ is the forward price at time $$t$$ for delivery at time $$T$$

$$F_t = \cfrac{S_t}{d(t, T)}$$

* **Forward value** $$f_t$$ 
  * $$F_0$$ : Forward price at time 0 for delivery at time $$T$$
  * $$F_t$$ : Forward price at time $$t$$ for delivery at time $$T$$

\*\*\*\*$$​f_t = (F_t - F_0) \cdot d(t,T)$$ 

## Derivative Security

### 

