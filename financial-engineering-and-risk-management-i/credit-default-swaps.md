# Credit Default Swaps

## Credit Default Swaps

The seller of a credit default swap \(CDS\) agrees to compensate the buyer in the event of a loan default or some other credit event on a reference entity, e.g

* a corporation
* sovereign

in return for periodic premium payment. 

![](../.gitbook/assets/image%20%2839%29.png)

* $$N=$$ notional principal amount of credit protection
* Accrued\* interest = interest accumulated from last coupon to default
* $$S=$$ coupon or spread
* $$R=$$ recovery rate
* CDS seller has to compensate\* the buyer$$(1-R)N$$ on default.

### Example

Consider a \(hypothetical\) 2-year CDS

* Notional principal $$N = \$1M$$ 
* Spread $$S=160 \; bps$$ 
* Quarterly premium payments

Suppose a default event occurs in month 16 of the 24 month protection period and the recovery rate $$R=45\%$$ , payment of protection **buyer** 

* Fixed premiums in months $$3,6,9,12,15 = \cfrac{SN}{4} = \$4000$$ 
* Accrued interest in month **18** $$= \cfrac{SN}{12} = \$ 1333.33$$ 

Payment of protection **seller**

* Default contingent payment in month **18** $$=(1-R)N = \$550,000$$ 

### Basic Model for the CDS Cash Flows

* Let $$\{ t_k = \delta k: k = 1,2,...,n\}$$ denote times of coupon payments. 
  * Typically $$\delta = \cfrac{1}{4}$$ , i.e. quarterly payments, and the dates of the payments are Mar. 20, Jun. 20, Sept. 20, Dec. 20
* If reference entity **is not in default** at time $$t_k$$  , the buyer pays the premium $$\delta \cdot S \cdot N$$ 
* If the reference entity defaults at time $$\tau \in ( t_{k-1}, t_k ]$$ , the contract terminates at time $$t_k$$ . At time $$t_k$$ 
  * the buyer pays the accrued interest $$(t_k - \tau) \cdot S \cdot N$$ , and
  * the buyer receives $$(1-R)\cdot N$$ 

### CDS Details

* Standardized by the International Swaps and Derivative Association in 1999. 
* Changes were made in 2003, and then again in 2009, may happen yet again if CDSs become exchange traded. 
* Many difficult issues 
  * How does one decide a credit event has occurred? 
  * How does one determine the recovery rate? 
* Many many details . . . 
  * How is the spread set? 
    * For junk bonds vs investment grade bonds? 
    * For sovereigns? 
  * When is coupon paid? 
    * In advance or in arrears? 
  * How is the spread quoted? 
* Will focus on the basic model to illustrate the details of pricing and sensitivity to hazard rates.

### CDS Spreads Measure of Default Risk

* CDS spread $$S \approx (1-R)\cdot h$$ where $$h$$ is the hazard rate, or conditional probability of default
* For fixed $$R$$ , the CDS spreads are directly proportional to the hazard rate $$h$$ 

Example

* Plot of the 5yr CDS spreads for Ford, GM and AIG in the first 9 months of 2008.

![](../.gitbook/assets/image%20%2840%29.png)

* Sovereign CDS

![](../.gitbook/assets/image%20%2841%29.png)

### Development and Application of CDS

* Development credited to Blythe Masters from J. P. Morgan in 1994 
  * J. P. Morgan extended a $4.8 billion credit line to Exxon to cover the possible punitive damage from Exxon Valdez spill 
  * Bought protection from the European Bank for Reconstruction and Development using a CDS. 
* CDS market has grown tremendously 
  * By the end of 2007, the CDS market had notional value of $62 trillion. 
  * The Depository Trust and Clearing Corporation \(DTCC\) estimates gross notional amount in 2012 as $25 trillion. 
* Initially developed for hedging 
  * Hedge concentrations of credit risk privately - maintain good client relations. 
  * Hedge credit exposures where no publicly traded debt exists.
* Although a CDS can be used to protect against losses it is very different from an insurance policy. 
  * A CDS is a contract that can be written to cover anything. 
  * Can buy protection even when one does not hold the debt. 
  * CDS are easy to create and \(until recently\) completely unregulated. 
* Investing \(speculation\) quickly became the main application 
  * Unfunded way to take a credit risk – leverage possible. 
  * Tailor credit exposure to match precise requirements. 
  * Taking views on the credit quality of an reference credit. 
  * Buying protection is easier than shorting the asset. 
  * Arbitrage between the reference bond coupon and CDS spreads.

### Crisis

* CDS positions are not transparent.
  * Riskiness of financial intermediaries cannot be accurately evaluated.
  * Threatened trust in all counterparties – since no one knew who faced losses.
* CDS trades are conducted on an OTC market.
  * Impossible for any dealer to know the previous deals of a customer.
  * Result: AIG was able to leverage its high credit rating to sell approximately     $500 billion worth of CDS.
  * Allowed a small number of CDS dealers to take a huge amount of risk.
  * The interconnected obligations of the dealers let to worries about contagion.
* CDS can be adversely affect the cost of borrowing of a firm or a country.
  * Speculators purchase CDS without holding underlying debt – naked CDS.
  * This drives the spread higher, i.e. the firm starts to appear riskier.
  * The cost of borrowing of the firm increases, and can lead to its collapse.

## Pricing CDSs

_**Value of CDS to buyer = Risk-neutral value of protection - Risk-neutral value of premiums**_

* Assumption: Default event uniformly distributed over the premium interval $$\delta$$ 
* Risk-neutral value of single premium payment on date $$t_k$$ 

$$\delta \cdot  S \cdot N \cdot \Bbb{E}^{\Bbb{Q}}_0\bigg[ \cfrac{I(t_k)}{B(t_k)} \bigg] = \delta\cdot S \cdot N \cdot q(t_k) \cdot Z_0^{t_k} = \delta \cdot S \cdot N \cdot q(t_k) \cdot d(0,t_k)$$

where $$I(t_k)$$ is the indicator function that entity is not in default. $$B(t_k)$$ is the cash account at time $$t_k.$$And here we assume they are independent.  

* Risk-neutral value of **all premium payments** 

$$\displaystyle\sum_{k=1}^n \delta \cdot S \cdot N \cdot q(t_k) \cdot d(0,t_k)$$ 

* Risk-neutral value of **accrued interest** if default $$\tau \in (t_{k-1}, t_k]$$ 

$$\cfrac{\delta}{2} \cdot S \cdot N \cdot \Bbb{E}_0^{\Bbb{Q}} \bigg[ \cfrac{I(t_{k-1} ) - I(t_k)}{B(t_k)} \bigg] = \cfrac{\delta}{2} \cdot S \cdot N \cdot \big(q(t_{k-1}) - q(t_k)\big) Z_0^{t_k} \\  \quad \quad \quad \quad =  \cfrac{\delta}{2} \cdot S \cdot N \cdot \big(q(t_{k-1}) - q(t_k)\big) d(0,t_k)$$ 

* Risk-neutral value of **premium and accrued interest** can approximated by 

$$\delta\cdot S \cdot N \cdot \displaystyle\sum_{k=1}^n  q(t_k) d(0,t_k) + \cfrac{\delta}{2} \cdot S \cdot N \cdot \displaystyle\sum_{k=1}^n \big(q(t_{k-1}) - q(t_k)\big) d(0,t_k) \\  \quad \quad \quad \quad =  \cfrac{\delta}{2} \cdot S \cdot N \cdot \displaystyle\sum_{k=1}^n \big(q(t_{k-1}) + q(t_k)\big) d(0,t_k)$$ 

* Risk-neutral present **value of the protection** \(contingent payment\)

$$(1-R) \cdot N \cdot \displaystyle\sum_{k=1}^n \Bbb{E}^{\Bbb{Q}}_0 \bigg[ \cfrac{I(t_{k-1}) - I(t_k)}{B(t_k)} \bigg] \\ \quad \quad = (1-R) \cdot N \cdot \displaystyle\sum_{k=1}^n \big( q(t_{k-1}) - q(t_k) \big) d(0, t_k)$$ 

* **Par spread** $$S_{par} = $$ spread that makes the value of the contract equal to zero

$$S_{par} = \cfrac{(1-R) \cdot \displaystyle\sum_{k=1}^n \big( q(t_{k-1}) - q(t_k) \big) d(0, t_k)}{\cfrac{\delta}{2} \cdot \displaystyle\sum_{k=1}^n \big( q(t_{k-1}) + q(t_k) \big) d(0, t_k)}$$ 

* Suppose $$q(t_k) \approx (1-h)\cdot q(t_{k-1})$$ , then

$$S_{par} \approx \cfrac{(1-R)\cdot h}{1 - \cfrac{h}{2} } \approx (1-R)\cdot h$$ 

where $$h \to 0. $$ So the value increasing in the hazard rate $$h$$ and decreasing in recovery rate $$R$$ .

## Words

{% hint style="info" %}
* _compensate_
  * adjust for
  * make amends for; pay compensation for

    _"She was compensated for the loss of her arm in the accident"_

  * make up for shortcomings or a feeling of inferiority by exaggerating good qualities
  * make reparations or amends for
  * do or give something to somebody in return
  * make payment to; compensate
* _accrue_
  * grow by addition

    _"The interest accrues"_

  * come into the possession of

    _"The house accrued to the oldest son"_
* _speculation_
  * a message expressing an opinion based on incomplete evidence
  * a hypothesis that has been formed by speculating or conjecturing \(usually with little hard evidence\)

    _"speculations about the outcome of the election"_

  * an investment that is very risky but could yield great profits

    _"he knew the stock was a speculation when he bought it"_

  * continuous and profound contemplation or musing on a subject or series of subjects of a deep or abstruse nature
* _premium_
  * n.
    * payment for insurance
    * the amount that something in scarce supply is valued above its nominal value

      _"they paid a premium for access to water"_

    * a fee charged for exchanging currencies
    * payment or reward \(especially from a government\) for acts such as catching criminals or killing predatory animals or enlisting in the military
  * adj. having or reflecting superior quality or value
{% endhint %}

