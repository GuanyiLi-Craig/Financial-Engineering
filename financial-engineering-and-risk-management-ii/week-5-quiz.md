# Week 5 Quiz

## Instruction

Download the spreadsheet  [StructuredCredit\_PSet4.xlsx](https://d396qusza40orc.cloudfront.net/fe2/class_resources/StructuredCredit_PSet4.xlsx). The first worksheet, "_LossDistributionCalculations_," displays the default probabilities for $$N=20$$ credits that are numbered 11 to 2020. Over the course of this quiz you will use the Gaussian copula model with $$\rho=0$$ to compute the expected tranche losses in various tranches.

Before beginning the specific questions below you should use the default probabilities to compute the loss distribution, $$p^N(l) = \text{Prob}(l \text{ losses out of } N)$$. This can be done via the iterative algorithm that we described in one of the video modules. You should also assume that each credit has a notional of $$A=1$$ unit and that the recovery is $$R=0$$ for all credits.

Note

When you have completed this quiz it will actually be quite straightforward to extend your work to non-zero values of \rhoρ as described in the video modules. In particular, you could use the 11-factor Gaussian copula model and then compute the distribution of the number of losses conditional on the value of the common factor, $$M$$ . One could do this for nn representative values of $$M$$ , say $$m_1, \ldots , m_n$$, and then approximate

$$p(l) = \displaystyle\int_{-\infty}^{\infty} p^N(l| M) \; \phi (M) \; dM$$ 

with

$$p(l) \approx \displaystyle\sum_{i=1}^n p^N(l| M = m_i) \text{Prob}(M \in \Delta_i)$$ 

where $$\Delta_i$$ is an interval centered at $$m_i$$ with $$\Delta_i \; \cap \; \Delta_j = \phi \text{ for } i \neq j \text{ and } \cup \; \Delta_i = (-\infty, \infty)$$ . Note that this can be done very quickly using your work from Question 1 and an Excel Data Table. You could then compute the expected tranche losses easily for different values of $$\rho$$ and reproduce similar figures to those in the video "A ~~~~Simple Example: Part II." \(In practice, of course, one would not do this in Excel but would instead use a more suitable programming language.\)

## Quiz 1

What is $$p^N(3)$$ ?



## Quiz 2

What is the expected number of losses in the portfolio? \(There is a simple way to calculate this that we discussed in one of the video modules. Moreover, you can use this simple way to check that you computed the distribution of the number of losses correctly.\)

$$E = \displaystyle\sum_{i=0}^{20} p^{20}(i) \cdot i = 3.67$$

## Quiz 3

Compute the variance of the number of losses in the portfolio.

$$\text{Var} = \displaystyle\sum_{i=0}^{20} (i - E)^2 \cdot p^N(i) = 2.54$$ 

## Quiz 4

What is the expected tranche loss in the tranche with lower and upper attachment points of 0 and 2, respectively?

$$E_{n-m} = \displaystyle\sum_{i=n}^{m-1} (i-n)\cdot p^N(i) + (m-n) \cdot \displaystyle\sum_{i=m}^{N} p^N(i) = 1.91$$ 

## Quiz 5

What is the expected tranche loss in the tranche with lower and upper attachment points of 2 and 4, respectively?

1.28

## Quiz 6

What is the expected tranche loss in the tranche with lower and upper attachment points of 4 and 20, respectively? \(Your answer to this question and the previous two questions should be consistent with your answer to the second question.\)

0.47

