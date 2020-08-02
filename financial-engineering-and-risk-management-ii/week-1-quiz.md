# Week 1 Quiz

## Quiz Instruction

Mean-Variance Analysis and CAPM

Consider a market with d=3 risky assets and 1 risk-free asset with the following parameters:

![](../.gitbook/assets/image%20%2853%29.png)

Note that the mean returns on the assets are in % but the variance is not. You can compute the answers to these questions either by directly using the data above or by using the spreadsheet [Assignment1.xlsx](https://d396qusza40orc.cloudfront.net/fe2/class_resources/Assignment1.xlsx). You will have to appropriately use the formulas in the spreadsheet [mvo.xlsx](https://d396qusza40orc.cloudfront.net/fe2/class_resources/mvo.xlsx). that went with the mean-variance modules.

Note that the asset returns and variances are not representative of realistic market conditions.

## Quiz 1

Compute the mean return on the portfolio $$\textbf{x} =\frac{1}{3}(1, 1, 1)$$ consisting only of the risky assets

$$\mu_x = \displaystyle\sum_{i=1}^d \mu_i x_i = 0.04$$ 

## Quiz 2

Compute the volatility of the return on the portfolio $$\textbf{x} =\frac{1}{3}(1, 1, 1)$$ consisting only of the risky assets

$$\sigma_x^2 = \mathbf{var}(r_x(t)) = \mathbf{var}\bigg( \displaystyle\sum_{i=1}^d   r_i x_i\bigg) = \displaystyle\sum_{i=1}^d \displaystyle\sum_{j=1}^d \mathbf{cov}(r_i(t), r_j(t))x_i x_j \\     \quad \;= \mathbf{x} \cdot \mathbf{V} \cdot \mathbf{x}^{\top} = 0.002444  \\ \triangle \quad \sigma_x = \sqrt{0.002444} = 0.04944$$ 

## Quiz 3

Compute the mean return on the minimum variance portfolio of just the risky assets.

The minimum variance portfolio is defined as the portfolio of risky assets that has the least volatility among all possible portfolios of just the risky assets.





