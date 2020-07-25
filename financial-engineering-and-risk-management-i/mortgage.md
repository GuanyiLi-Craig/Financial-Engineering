# Mortgage

## Mortgage Mathematics & Security

* Mortgage Backed Securities \(MBS\) are a particular class of asset-backed securities \(ABS\)
  * Assets backed by underlying pools of securities such as
    * mortgage
    * auto-loans
    * credit-card receivables
    * student loans etc
  * The process by which ABS are created is often called securitization. 

![](../.gitbook/assets/image%20%2842%29.png)

* Process of securitization
  * Combined the mortgages into a mortgage pool
  * Categrate the mortgages into different securities labeled by tranches, each with different risk and etc. 
  * Why? to share the risk
* We will look at some examples of MBS but first must consider the mathematics   of the underlying mortgages.
* There are many different types of mortgages including: 
  * **level-payment mortgages** 
  * **adjustable-rate mortgages \(ARMs\)** 
    * subprime crisis
  * **balloon mortgages** 
  * and others. 
* We will only consider level-payment mortgages 
  * but MBS may be constructed out of other mortgage types as well. 
* The construction of MBS is an example of securitization 
  * the same ideas apply to asset-backed securities more generally

## Mortgage Mathematics

### Basics for Level-Payment Mortgage

We consider a standard level-payment mortgage

* Initial mortgage principal is $$M_0 := M$$ 
* We assume equal periodic payments of size $$B$$ dollars.
* The _coupon rate_ is $$c$$ per period
* There are a total of $$n$$ repayment periods
* After the $$n$$ payments, the mortgage principal and interest have all been paid
  * the mortgage is then said to be fully **amortizing**

This means that each payment, $$B$$ , pays both interest and some of the principal. 

If $$M_k$$ denotes the mortgage principal remaining after the $$k^{th}$$ period then

$$M_k = (1+c) \cdot M_{k-1} - B \quad \text{for } k= 0,1,2,...,n$$ 

with $$M_n = 0$$ 

Can iterate this equation to obtain 

$$M_k = (1 +c)^k \cdot M_0 - B \displaystyle\sum^{k-1}_{p=0} (1+c)^p \\ \quad = (1+c)^k \cdot M_0 - B \cdot \bigg[ \cfrac{(1+c)^k -1}{c} \bigg]$$ 

But $$M_n = 0$$ and we can obtain 

$$B = \cfrac{c\cdot(1+c)^nM_0}{(1+c)^n -1}$$ 

Then we can get

$$M_k = M_0 \cfrac{(1+c)^n - (1+c)^k}{(1+c)^n - 1}$$ 

### Present Value of Level-Payment Mortgage

* Suppose now that we wish to compute the present value of the mortgage assuming a deterministic world
  * with no possibility of defaults or prepayments.
* Then assuming a risk-free interest rate of $$r$$ per period, we obtain that the fair mortgage value as

$$F_0 = \displaystyle\sum_{k=1}^{n} \cfrac{B}{(1+r)^k} \\ \quad = \cfrac{c\cdot (1+c)^n \cdot M_0}{(1+c)^n - 1} \cdot \cfrac{(1+r)^n - 1}{r\cdot(1+r)^n}$$ 

Note that if $$r = c$$ then implies that $$F_0 = M_0$$, as expected

In reality, $$r < c$$ , to account for the possibility of default, prepayment, servicing fees, profits, payment uncertainty etc. 

### Scheduled Principal and Interest Payments

Since we know $$M_{k-1}$$ we can compute the interest 

$$I_k := c\cdot M_{k-1}$$ 

on $$M_{k-1}$$ that would be due in the next period, i.e. period $$k.$$ 

This also means we can interpret the $$k^{th}$$ payment as paying

$$P_k := B - c\cdot M_{k-1}$$ 

of the remaining principal, $$M_{k-1}$$ 

So in any time period, $$k$$ , we can easily break down the payment $$B$$ into a scheduled principal payment, $$P_k$$ , and a scheduled interest payment, $$I_k$$ , called **principal-only** and **interest-only** MBS respectively. 

## Prepayment Risk and Mortgage Pass-Throughs

Many mortgage-holders in the US are allowed to **pre-pay** the mortgage principal earlier than scheduled

* payments made in excess of the scheduled payments are called **prepayments**. 

There are many possible reasons for prepayments: 

* homeowners must prepay entire mortgage when they sell their home 
* homeowners can refinance their mortgage at a better interest rate 
* homeowners may default on their mortgage payments
  * if mortgage is insured then insurer will prepay the mortgage
*  home may be destroyed by flooding, fire etc.
  * again insurance proceeds will prepay the mortgage. 

Prepayment modeling is therefore an important feature of pricing MBS

* and the value of some MBS is extremely dependent on prepayment behavior

Will now consider the simplest type of MBS

* the mortgage pass-through.

### Pass-Throughs

* In practice, mortgages are often sold on to third parties who can then pool these mortgages together to create **mortgage-backed securities \(MBS\)**. 
* In the US the third parties are either **government sponsored agencies \(GSAs\)** such as Ginnie Mae, Freddie Mac or Fannie Mae, or other **non-agency** third parties such as commercial banks. 
* MBS that are issued by the government-sponsored agencies are guaranteed against default
  * not true of non-agency MBS. 
* The modeling of MBS therefore depends on whether they are agency or non-agency MBS. 
* The simplest type of MBS is the **pass-through** MBS where a group of mortgages are pooled together. 
* Investors in this MBS receive monthly payments representing the interest and principal payments of the underlying mortgages.

![](../.gitbook/assets/image%20%2845%29.png)

* The **pass-through coupon rate**, however, is strictly less than than the average coupon rate of the underlying mortgages
  * due to fees associated with servicing the mortgages. 
* Will assume that our MBS are agency-issued and are therefore default-free.

**Definition.** The **weighted average coupon rate \(WAC\)** is a weighted average of the coupon rates in the mortgage pool with weights equal to mortgage amounts still outstanding. 

**Definition.** The **weighted average maturity \(WAM\)** is a weighted average of the remaining months to maturity of each mortgage in the mortgage pool with weights equal to the mortgage amounts still outstanding.

### Payment Conventions

There are important prepayment conventions that are often used by market participants when quoting yields and prices of MBS. 

* but first need some definitions. 

**Definition.** The **conditional prepayment rate \(CPR\)** is the annual rate at which a given mortgage pool prepays. It is expressed as a percentage of the current outstanding principal level in the underlying mortgage pool. 

**Definition.** The **single-month mortality rate \(SMM\)** is the CPR converted to a monthly rate assuming monthly compounding. 

The CPR and SMM are therefore related by

$$\text{SMM} = 1 - (1 - \text{CPR})^{\frac{1}{12}} \\ \text{CPR} = 1 - ( 1 - \text{SMM})^{12}$$ 

In practice, the CPR is stochastic and depends on the mortgage pool and other economic variables. 

However, market participants often use a deterministic prepayment schedule as a mechanism to quote MBS yields and so-called option-adjusted spreads etc. 

The standard benchmark is the **Public Securities Association \(PSA\)** benchmark. 

The PSA benchmark assumes the following for 30 year mortgages:

$$\text{CPR} = \begin{cases} 6\% \times (t/30), \text{   if  } t\leq 30 \\ 6\%, \quad \quad \quad \quad \text{if } t> 30  \end{cases}$$ 

where $$t$$ is the number of months since the mortgage pool originated. 

Slower or faster prepayment rates are then given as some percentage or multiple of PSA

### The Average Life of an MBS

Given a particular prepayment assumption the **average life** of an MBS is defined as

$$\text{Average Life} = \displaystyle\sum_{k=1}^{T} \cfrac{k\cdot P_k}{12 \times TP}$$ 

* where $$P_k$$ is the principal \(scheduled and projected prepayment\) paid at time $$k$$ 
* $$TP$$ is the total principal amount
* $$T$$ is the total number of months
* and we divide by 12 so that average life is measured in years

It is immediate that the average life decreases as the PSA speed increase. 

### Mortgage Yields

* In practice the price of a given MBS security is observed in the market place and from this a corresponding **yield-to-maturity** can be determined. 
* This yield is the interest rate that will make the present value of the expected cash-flows equal to the market price. 
* The expected cash-flows are determined based on some underlying prepayment assumption such as 100 PSA, 300 PSA etc.
  * so any quoted yield must be with respect to some prepayment assumptions. 
* When the yield is quoted as an annual rate based on semi-annual compounding it is called a bond-equivalent yield. 
* Yields are clearly very limited when it comes to evaluating an MBS and indeed fixed-income securities in general. 
* Indeed the option-adjusted-spread \(OAS\) is the market standard for quoting yields on MBS and indeed other fixed income securities with embedded options.

### Prepayment Risks for Mortgage Pass-Throughs

* An investor in an MBS pass-through is of course exposed to interest rate risk in that the present value of any fixed set of cash-flows decreases as interest rates increase.
* However, a pass-through investor is also exposed to **prepayment risk**, in particular **contraction risk** and **extension risk**. 

When interest rates decline prepayments tend to increase and the additional prepaid principal can only be invested at lower interest rates

* this is **contraction risk.** 

When interest rates increase, prepayments tend to decrease and so there is less prepaid principal that can be invested at the higher rates

* this is **extension risk**

## Principal-Only and Interest-Only MBS

Since we know $$M_{k-1}$$ we can compute the interest rate 

$$I_k := c\cdot M_{k-1}$$ 

on $$M_{k-1}$$ that would be due in the next period, i.e. period $$k.$$ 

This also means we can interpret the $$k^{th}$$ payment as paying

$$P_k := B - c\cdot M_{k-1}$$ 

of the remaining principal, $$M_{k-1}$$ 

Now recall our earlier expression for $$M_k$$ :

$$M_k = (1+c)^k \cdot M_0 - B \bigg[ \cfrac{(1+c)^k - 1}{c} \bigg]$$ 

Therefore obtain

$$P_k = B -c\bigg( (1+c)^{k-1} \cdot M_0 + B\cdot\bigg[ \cfrac{(1+c)^{k-1} - 1}{c} \bigg] \bigg)\\ \quad = (B -c\cdot M_0)(1+c)^{k-1}$$ 

### Principal-Only MBS

The present value, $$V_0$$ , of the **principal payment stream** is therefore given by 

$$V_0 = (B - c\cdot M_0) \cfrac{(1+r)^n - (1+c)^n}{(r-c)(1+r)^n}$$ 

where, as before, $$r$$ , is the per-period risk-free interest rate. 

Can use I'Hopital's rule to check that

$$\displaystyle\lim_{c\to r} V_0 = \cfrac{n\cdot(B - r\cdot M_0)}{1+r}$$ 

Now recall our earlier expression

$$B = \cfrac{c\cdot (1+c)^n M_0}{(1+c)^n - 1}$$ 

If we use above equation to substitute for $$B$$ then we obtain

$$V_0 = \cfrac{cM_0}{(1+c)^n - 1} \times \cfrac{(1+r)^n -(1+c)^n}{(r-c)(1+r)^n}$$ 

in the case $$\color{red}{r=c}$$ 

$$V_0 = \cfrac{r\cdot n \cdot M_0}{(1+r)\cdot \big[ (1+r)^n  - 1\big]}$$ 

It is clear that the earlier mortgage payments comprise of interest payments rather than principal payments

* only later in the mortgage is this relationship reversed. 

Indeed this property is reflected in the fact that

$$\displaystyle\lim_{n\to \infty} V_0 = 0$$ 

### Interest-Only MBS

Assume there are no mortgage prepayment, the present value $$W_0$$ of the **interest payment stream** is

$$W_0 = \displaystyle\sum_{k=1}^n\cfrac{I_k}{(1+r)^k}$$ 

* The sum of the principal-only and interest-only streams must equal the total value of the mortgage, $$F_0 = W_0 + V_0$$, where $$F_0$$ is

$$F_0 = \cfrac{c\cdot (1+c)^n \cdot M_0}{(1+c)^n - 1} \cdot \cfrac{(1+r)^n - 1}{r\cdot(1+r)^n}$$ 

so that 

$$W_0 = \cfrac{c \cdot M_0}{\big[(1+c)^n - 1\big] (1+r)^n} \cdot \bigg[(1+c)^n\cfrac{(1+r)^n - 1}{r} - \cfrac{(1+r)^n - (1+c)^n}{r-c}\bigg]$$ 

Moreover when $$r \to c$$ it is easy to check that this reduces to 

$$W_0 = M_0 - \cfrac{r\cdot n \cdot M_0}{(1+r)\big[  (1+r)^n - 1 \big]}$$ 

Consider $$V_0$$ which implies that $$F_0 = M_0 \text{ when } r=c$$ 

## Risks of Principal-Only and Interest-Only MBS

### Duration of the Principal-Only MBS

Again we assume no prepayments and consider the durations of the PO and IO cash-flow streams. 

The duration of a cash-flow is a weighted average of the times at which each component of the cash-flow is received

* a standard measure of the risk of a cash-flow. 

It should be clear that the principal stream has a longer duration than the interest stream.

If we let $$D_p$$ denote the duration of the principle stream, then it is given by

$$D_p = \cfrac{1}{12\cdot V_0}\displaystyle\sum_{k=1}^n \cfrac{k\cdot P_k}{(1+r)^k} = \displaystyle\sum_{k=1}^n w_k \cdot k$$ where 

$$w_k = \cfrac{1}{12\cdot V_0} \cdot \cfrac{P_k}{(1+r)^k}, \text{ where } V_0 = \displaystyle\sum_{k=1}^{n} \cfrac{P_k}{(1+r)^k}$$ 

### Duration of the Interest-Only MBS

Similarly, we can compute the duration, $$D_I$$ , of the interest-only stream as

$$D_I = \cfrac{1}{12\cdot W_0} \cdot \displaystyle\sum_{k=1}^{n}\cfrac{I_k \cdot k}{(1+r)^k} \\ \quad = \cfrac{1}{12\cdot W_0} \cdot \displaystyle\sum_{k=1}^{n}\cfrac{(B - P_k) \cdot k}{(1+r)^k}  \\ \quad = \cfrac{1}{12\cdot W_0} \cdot \displaystyle\sum_{k=1}^{n}\cfrac{B \cdot k}{(1+r)^k} - \cfrac{V_0}{W_0}\cdot D_p$$ 

### Principal-Only and Interest-Only MBS in Practice

To this point we have assumed that prepayments do not occur.

But this is not realistic: in practice pass-throughs do experience prepayments and the PO and IO cash-flows must reflect these prepayments correctly.

But this is straightforward: the interest payment in period $$k$$ is simply, as before,

$$I_k := c\cdot M_{k−1}$$ 

where $$M_{k−1}$$ is the mortgage balance at the end of period $$k − 1$$ .

Mk must now be calculated iteratively on a path-by-path basis as

$$M_k = M_{k−1} − \text{Scheduled-Principal-Payment}_k − \text{Prepayment}_k $$ 

for $$k = 1, . . . , n $$ and where $$\text{Scheduled-Principal-Payment}_k $$ is now the scheduled principal payment \(adjusted for earlier prepayments\) in period $$k$$ 

### The Risks of PO and IO MBS

* The risk profiles of principal-only and interest-only securities are very different   from one another.
* The principal-only investor would like prepayments to increase.
* The interest-only investor wants prepayments to decrease
  * after all the IO investor only earns interest at time k on the mortgage     balance remaining at time $$k$$ .
* In fact the IO security is that rare fixed income security whose price tends to   follow the general level of interest rates:
  * when interest rates fall the value of the IO security tends to decrease
  * and when interest rates increase the expected cash-flow increases due to     fewer prepayments but the discount factor decreases
  * the net effect can be a rise or fall in value of the IO security.

## Collateralized Mortgage Obligations \(CMOs\)

### CMOs

* Collateralized mortgage obligations \(CMOS\) are mortgage-backed securities that have been created by redirecting the cash-flows from other mortgage securities
  * created mainly to mitigate prepayment risk and create securities that are better suited to potential investors. 
* In practice CMOs are often created from pass-through’s but they can also be created from other MBS including, for example, principal-only MBS. 
* There are many types of CMOs including
  * **sequential** CMOs
  * CMOs with **accrual bonds**
  * CMOs with **floating-rate** and **inverse-floating-rate** tranches
  * **planned amortization class \(PAC\)** CMOs.
* We’ll briefly describe sequential CMOs.

### Sequential CMOs

* The basic structure of a sequential CMO is that there are several tranches which are ordered in such a way that they are retired sequentially. 
* For example, the payment structure of a sequential CMO with tranches A, B, C and D might be as follows

 Sequential CMO Payment Structure 

* Periodic coupon interest is disbursed to each tranche on the basis of the amount of principal outstanding in the tranche at the beginning of the period. 
* All principal payments are disbursed to tranche A until it is paid off entirely. 
  * After tranche A has been paid off all principal payments are disbursed to tranche B until it is paid off entirely. 
  * After tranche B has been paid off all principal payments are disbursed to tranche C until it is paid off entirely. 
  * After tranche C has been paid off all principal payments are disbursed to tranche D until it is paid off entirely.

## Pricing Mortgage-Backed-Security

### Prepayment Modeling

* In many respects, the prepayment model is the most important feature of any residential MBS pricing engine. 
* Term-structure models are well understood in the financial engineering community
  * but this is not true of prepayment models. 
* The main problem is that there is relatively little publicly available information concerning prepayments rates
  * so very difficult to calibrate prepayment models. 
* One well known publicly available model is due to Richard and Roll \(1989\) 
  * they model the conditional prepayment rate \(CPR\) whose definition we recall:

**Definition**. The CPR is the rate at which a given mortgage pool prepays. It is expressed as a percentage of the **current** outstanding principal level in the underlying mortgage pool.

### A Particular Prepayment Model

The model of Richard and Roll \(1989\) assumes

$$CPR_k = RI_k \times AGE_k \times MM_k \times BM_k$$ 

where

* $$RI_k$$ is the refinancing incentive, e.g.

$$RI_k = 0.28 + 0.14 \tan^{-1}(-8.57 + 430\cdot (WAC - r_k(10)))$$ 

where $$r_k(10)$$ is the prevailing 10-year spot rate at time $$k$$ 

* $$AGE_k$$ is the seasoning multiplier, e.g.
  * $$AGE_k = \min(1, t/30)$$ 
* $$MM_k$$ is the monthly multiplier
* $$BM_k$$ is the burnout multiplier, e.g.
  * $$BM_k = 0.3 + 0.7 \cfrac{M_{k-1}}{M_0}$$ 
  * where $$M_k$$ is the remaining principal balance at time $$k$$ .

### Choosing a Term Structure Model

* We also need to specify a term-structure model in order to fully specify the mortgage pricing model.
* The term structure model will be used to: 
  * discount all of the MBS cash-flows in the usual risk-neutral pricing framework
  * to compute the refinancing incentive according to equation $$RI_k$$ , for example. 
* Whatever term-structure model is used, it is important that we are able to compute the relevant interest rates **analytically**
  * for example, $$r_{10}(k)$$ in the prepayment model of Richard and Roll. 
* Such a model would first need to be calibrated to the term structure of interest rates in the market place as well as liquid interest rate derivatives. 
* The actual pricing of MBS then requires Monte-Carlo simulation
  * very computationally intensive
  * analytic prices not available

### The Financial Crisis

* The so-called sub-prime mortgage market played an important role in the   financial crisis of 2008-2009.
* Sub-prime mortgages are mortgages that are issued to home-owners with very   weak credit
  * the true credit quality of the home-owners was often hidden
  * the mortgages were often ARMs with so-called teaser rates
  * very low initial mortgage rates intended to “tease” the home-owner into     accepting the mortgage.
* The financial engineering aspect of the MBS-ABS market certainly played a role   in the crisis
  * particularly when combined with the alphabet soup of CDO’s and     ABS-CDO’s
  * these products are too complex and too difficult to model.
* But there were many other causes including: moral hazard problem of mortgage   brokers, ratings agencies, bankers etc, inadequate regulation, inadequate risk   management and poor corporate governance.

## Words

{% hint style="info" %}
* tranche
  * a portion of something \(especially money\)
{% endhint %}

