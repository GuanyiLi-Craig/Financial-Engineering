import math
import numpy as np
import pandas as pd
import scipy.optimize as opt
from abc import ABC
from scipy.stats import norm
from collections import Iterable

DEBUG = False

def discountRate(time, spotRate):
    """
    Returns the discounted price of a dollar at the given discount rate
    for the given time periods.

    input:
        time (Integer): time period
        spotRate (float/numpy.array): interest rate(s)
    output:
        discountRates (numpy.array): discount rate array, dim = time + 1
    """
    if isinstance(spotRate, float):
        spotRate = np.ones(time + 1) * spotRate
    elif spotRate.size != time + 1:
        print("Error: rate dimention should equal to time period + 1")
        return None

    discountRates = np.ones(time + 1)
    for i in range(time + 1):
        discountRates[i] = (1 + spotRate[i]) ** -i

    if DEBUG:
        print(f"discount time is {time}, spot rate is {spotRate}")
        print(f"discount rate is {discountRates}")

    return discountRates

def presentValue(flows, interestRate, periods=None):
    """
    Returns the persent value (PV) of future cash flows.
    input:
        flows (numpy.array)- A stream of future cash flows
        interestRate (numpy.array) - Interest rate(s) per period.
        periods (Integer) - The time period of flows.
    output:
        presentValue (float) - The present value of the future cash flows.
    """
    if periods is None:
        periods = flows.size
    elif periods != flows.size or periods != interestRate.size:
        print("Error: flows dimention should equal to periods")
        return None

    discountRates = discountRate(periods, interestRate)
    presentValue = sum(discountRates * flows)

    return presentValue

def averageLife(flows):
    """
    Computes the average life of MBS.
    Input:
        flows (np.array): The cash flows
    Output:
        averageLift (float) Returns the effective duration of the cashflows in terms of the number of periods.
    """

    averageLift = sum(flows * flows.index) / 12 / sum(flows)

    return averageLife

def portfolioReturn(weights, mu):
    """
    Computes the net return for the given weights assigned to corresponding returns.
    Input:
        weights (np.array/N x 1 Matrix): Describes the weights assigned to different assets
        expectedReturns (np.array/1 x N Matrix): Expected returns of different assets
    Output:
        portfolioReturn (float): The net return of the given assets for the given weights
    """
    return weights.T @ mu


def portfolioVolatility(weights, covarianceMatrix):
    """
    Computes the net volatility of the returns for the given weights.
    For weights w and covariance matrix S, the volatility is given by the square root of wTSw,
    where wT represents w transpose.
    Input:
        weights (np.array/N x 1 Matrix) - Describes the weights assigned to different assets
        covarianceMatrix (N x N Matrix) - Covariance matrix for the given assets
    Output:
        volatility (float): The net volatility of the given assets for the given weights
    """
    volatility = np.sqrt(weights.T @ covarianceMatrix @ weights)
    return volatility

class Lattice(ABC):
    """
    Implements an abstract class for the mulit-period lattice.

    Parameters:
        T (Integer): The number of periods for which the tree is to be made.
        q (float): The probability of the security going upwards.
    """

    @property
    def T(self):
        """
        Gets the the number of periods in the model.
        """
        return self._T

    @T.setter
    def T(self, val):
        self._T = val

    @property
    def q(self):
        """
        Gets the probability of a security going up.
        """
        return self._q

    @q.setter
    def q(self, val):
        self._q = val

    @property
    def tree(self):
        """
        Gets the binomial tree with node as Lattice objects
        """
        return self._tree

    @tree.setter
    def tree(self, tree):
        self._tree = tree

    def printTree(self):
        """
            Print binomial pricing tree.
        """
        for i in range(self.T + 1):
            print("Period = " + str(i))
            print(self.tree[i][: i + 1].round(3))

    def __init__(self, T, q=0.5):
        """
            Initializes the data descriptors from the given parameters.
        """

        self.T = T
        self.q = q
        self.tree = np.zeros([self.T + 1, self.T + 1])

class StockPricing(Lattice):
    """
    Implements the binomial stock pricing model.
    Inherits the BinomialTree class.

    Parameter:
        T (Integer): Number of periods
        initSecurityPrice (float): The initial price of the security
        u (float): The upward probability of the security
        d (float): The downward probability of the security
    """

    __doc__ += Lattice.__doc__

    @property
    def initSecurityPrice(self):
        return self._initSecurityPrice

    @initSecurityPrice.setter
    def initSecurityPrice(self, val):
        self._initSecurityPrice = val

    @property
    def u(self):
        return self._u

    @u.setter
    def u(self, val):
        self._u = val

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, val):
        self._d = val

    def _constructTree(self):
        """
        Constructs the pricing of the binomial model for T periods.
        """
        for i in range(self.T + 1):
            for j in range(i + 1):
                self.tree[i, j] = self.initSecurityPrice * (self.u ** j) * (self.d ** (i - j))

    def __init__(self, T, initSecurityPrice, u, d):
        """
        Initializes the binomail model for the corresponding parameters.
        """

        super().__init__(T)

        self.initSecurityPrice = initSecurityPrice
        self.u = u
        self.d = d

        self._constructTree()

class BondPricing(Lattice):
    """
    Implements the binomial bond pricing model.
    Inherits the BinomialTree class.
    Parameters:
        T (integer): The number of periods.
        faceValue (float): The face value of the bond.
        couponRate (float): The coupon rate of the bond. Defaults to zero assuming zero coupon bond.
        r (float/int/Lattice): the rate
    hazard: dict
        If set to None, the bond is assumed to be non-defaultable. Otherwise should contain
        a dictionary of following params:
        a: float
            The speed of hazard escalation
        b: float
            The exponential parameter of hazard
        recovery_rate: float
            The amount of interest paid back if a default occurs
        default_probability[i, j] = a * b(i - j/2)
    """

    __doc__ += Lattice.__doc__

    @property
    def faceValue(self):
        return self._faceValue

    @faceValue.setter
    def faceValue(self, val):
        self._faceValue = val

    @property
    def couponRate(self):
        return self._couponRate

    @couponRate.setter
    def couponRate(self, val):
        self._couponRate = val

    @property
    def price(self):
        return self.tree[0, 0]

    def _computeDefaults(self, hazard):
        """
        Computes the probability of default at each node.
        h[i, j] = a * b^(i - j/2)
        Returns a tuple of hazard rates, recovery rate
        """
        h = np.zeros([self.T + 1, self.T + 1])
        r = 1

        if hazard is not None:
            a = hazard["a"]
            b = hazard["b"]
            r = hazard["recoveryRate"]
            for i in range(self.T + 1):
                for j in range(i + 1):
                    h[i, j] = a * b ** (j - i / 2)

        return (h, r)

    def _constructTree(self, r, h, recoveryRate):
        """
        Constructs the tree for bond pricing for n periods.
        """
        if isinstance(r, int) or isinstance(r, float):
            rate = np.empty([self.T + 1, self.T + 1])
            rate.fill(r)
        else:
            rate = r.tree

        coupon = self.faceValue * self.couponRate

        self.tree[self.T] = np.repeat(self.faceValue + coupon, self.T + 1)
        for i in range(self.T - 1, -1, -1):
            for j in range(i + 1):
                nextDownward = self.tree[i + 1, j]
                nextUpward = self.tree[i + 1, j + 1]
                upwardProbability = self.q
                downwardProbability = 1 - self.q

                nonHazardPrice = (
                    coupon + (upwardProbability * nextUpward + downwardProbability * nextDownward)
                ) * (1 - h[i, j])
                hazardPrice = h[i, j] * recoveryRate * self.faceValue
                self.tree[i, j] = (nonHazardPrice + hazardPrice) / (1 + rate[i, j])

    def __init__(self, T, faceValue, q, r, couponRate=0.0, hazard=None):
        """
        Initializes the bond pricing model from the given parameters.
        """
        super().__init__(n, q)

        self.faceValue = faceValue

        self.couponRate = couponRate

        self.r = r

        h, recovery = self._compute_defaults(hazard)

        self._constructTree(r, h, recovery)

class CashPricing(Lattice):
    """
    Implements the binomial model for pricing 1 unit of cash.
    Inherits the Lattice class.

    Parameters:
        T (integer): The number of periods.
        q (float)：The probability of price going up in the binomial model
        r (Lattice): The rates of interest
    """

    def _constructTree(self, r):
        """
        Constructs the binomial tree for pricing a unit of cash.
        The i, j node of the tree denotes the price of a unit of cash at period i and state j.
        """

        rate = r.tree

        self.tree[0, 0] = 1
        for i in range(1, self.T + 1):

            # The bottom most nodes
            self.tree[i, 0] = (1 - self.q) * self.tree[i - 1, 0] / (1 + rate[i - 1, 0])

            # The top most nodes
            self.tree[i, i] = (
                self.q * self.tree[i - 1, i - 1] / (1 + rate[i - 1, i - 1])
            )

            for j in range(1, i):
                priceFromDownward = self.tree[i - 1, j - 1] / (1 + rate[i - 1, j - 1])
                priceFromUpward = self.tree[i - 1, j] / (1 + rate[i - 1, j])

                self.tree[i, j] = self.q * priceFromDownward + (1 - self.q) * priceFromUpward

    def getZcbPrices(self):
        """
        Returns the prices of zero coupon bonds for the corresponding interest rates.
        """
        return self.tree.sum(axis=1)

    def getSpotRates(self):
        """
        Returns the spot rates for the corresponding interest rates.
        """

        zcbPrices = self.getZcbPrices()[1:]
        spotRates = zcbPrices ** -(1 / (np.arange(self.T) + 1)) - 1

        return spotRates

    def __init__(self, T, q, r):

        super().__init__(T, q)

        self._constructTree(r)

class OptionsPricing(Lattice):
    """
    Implements a binomial tree based option pricing model.
    Inherits the BinomialTree class.
    Parameters
    T (integer): Number of periods
    model (Lattice): The underlying security model from which the options contract is derived.
    r: float / BinomialTree
        The rate of interest to be used. Should be a scalar if fixed and a binomial model otherwise.
    q: float
        The probability of price going up in the binomial model
    K: float
        The strike price of the option contract.
    is_call: bool
        Sets to True if the option is call and False if the option is put. Defaults to True,
    is_american: bool
        Sets to True if the option is American and False if the option is European. Defaults to False.
	"""

    __doc__ += Lattice.__doc__

    @property
    def K(self):
        """
        Represents the strike price of the options contract.
        """
        return self._K

    @K.setter
    def K(self, val):
        self._K = val

    @property
    def multiplier(self):
        """
        The multiplier to be used for call and put option pricing.
        Sets to 1 for call options and -1 for put options.
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, val):
        self._multiplier = val

    @property
    def is_american(self):
        """
        Represents if the option security is american or european.
        """
        return self._is_american

    @is_american.setter
    def is_american(self, val):
        self._is_american = val

    @property
    def price(self):
        """
        Returns the current price of the option.
        """
        return self.tree[0, 0]

    @property
    def early_exercise(self):
        """
        Gets the details of early exercise of options.
        Returns a list of dictionaries sorted by time consisting of all the possible times
        when early exercise of options can be more beneficial.
        """
        result = []
        for time, no, early_ex, hold in sorted(self._early_exercise):
            data = {
                "Time": time,
                "Current Premium": early_ex,
                "Hold": hold,
            }
            result.append(data)

        return result

    def _constructTree(self, model, r):
        """
        Computes the option prices from the given pricing model and rate of interest.
        """

        if isinstance(r, int) or isinstance(r, float):
            rate = np.empty([self.T + 1, self.T + 1])
            rate.fill(r)
        else:
            rate = r.tree

        for i in range(self.T, -1, -1):
            if i == self.T:
                for j in range(i + 1):
                    self.tree[i, j] = max(
                        0, self.multiplier * (model.tree[i, j] - self.K)
                    )
            else:
                for j in range(i + 1):
                    childu = self.tree[i + 1, j + 1]
                    childd = self.tree[i + 1, j]

                    # Expected call option permium if portfolio is held
                    hold = (self.q * childu + (1 - self.q) * childd) / (1 + rate[i, j])

                    # Call option premium if portfolio is exercised
                    # Can be done only in the case of american options
                    early_ex = max(0, self.multiplier * (model.tree[i, j] - self.K))

                    if early_ex > hold:
                        self._early_exercise.append((i, j, early_ex, hold))

                    self.tree[i, j] = max(hold, early_ex) if self.is_american else hold

    def __init__(self, n, model, r, q, K, is_call=True, is_american=False):
        """
        Initializes the black scholes model and other parameters from the given parameters.
        """
        super().__init__(n, q)

        self.K = K

        self.multiplier = 1 if is_call else -1

        self.is_american = is_american

        self._early_exercise = []

        self._constructTree(model, r)

class SwapsPricing(Lattice):
    """
    Implements a swap pricing model based on the binomial model.
    Inherits the BinomialTree class.

    The model assumes the last exchange is executed at n + 1 period.
    Parameters:
    ----------
    n: int
        The number of periods. Here n denotes the period at which the last payment occured.
    q: float
        The probability of the price of security going upward.

    fixed_rate: float
        The fixed rate of interest to be paid/recieved in the swap contract
    start_time: int
        The period from which the exchange starts
    is_long: bool
        The type of position to be modeled, long or short.
        Long position refers to paying the fixed  interest rate
        while short refers to paying the floating rates.
    r: BinomialTree
        The rate model for varying interest rates
    """

    __doc__ += Lattice.__doc__

    @property
    def fixed_rate(self):
        return self._fixed_rate

    @fixed_rate.setter
    def fixed_rate(self, val):
        self._fixed_rate = val

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, val):
        self._start_time = val

    @property
    def multiplier(self):
        return self._multiplier

    @multiplier.setter
    def multiplier(self, val):
        self._multiplier = val

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, val):
        self._r = val

    @property
    def price(self):
        return self.tree[0, 0]

    def _constructTree(self, r):
        """
        Constructs the binomial tree for pricing the swaps.
        """
        rate = r.tree

        for i in range(self.T, -1, -1):
            if i == self.T:
                self.tree[i] = (
                    (rate[i, : (i + 1)] - self.fixed_rate)
                    * self.multiplier
                    / (rate[i, : (i + 1)] + 1)
                )
            else:
                for j in range(i + 1):
                    childd = self.tree[i + 1, j]
                    childu = self.tree[i + 1, j + 1]

                    value = (self.q * childu + (1 - self.q) * childd) / (1 + rate[i, j])

                    if i >= self.start_time - 1:
                        payment = ((rate[i, j] - self.fixed_rate) * self.multiplier) / (
                            1 + rate[i, j]
                        )
                        value += payment

                    self.tree[i, j] = value

    def __init__(self, n, q, fixed_rate, start_time, is_long, r):
        """
        Initializes the model based on the given parameters.
        """

        super().__init__(n - 1, q)

        self.fixed_rate = fixed_rate

        self.start_time = start_time

        self.multiplier = 1 if is_long else -1

        self.r = r

        self._constructTree(r)

class BDTRate(Lattice):
    """
        Implements a black-derman-toy short rate model over the binomial tree model.
        Inherits the Lattice class.
        Assumes the number of periods is equal to the length of the dirft vector - 1.

        rate[i, j] = a[i] * exp(b[i] * j), where
        rate[i, j] - Rate of interest at period i and  state j
        a[i] - Drift at period i
        b[i] - volatility at period i
        Parameters:
        ----------
        n: int
            The number of periods.
        drift: scalar / np.array
            The list of a[i] in the black-derman-toy model
        vol: scalar / np.array
            The list of b[i] in the black-derman-toy model
    """

    __doc__ += Lattice.__doc__

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, val):

        if isinstance(val, int) or isinstance(val, float):
            val = np.repeat(val, self.T)
        self._a = val

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, val):

        if isinstance(val, int) or isinstance(val, float):
            val = np.repeat(val, self.T + 1)
        self._b = val

    def _constructTree(self):
        """
        Constructs the binomial tree model for interest rates based on
        the BDT equation.
        """
        for i in range(self.T + 1):
            for j in range(i + 1):
                self.tree[i, j] = self.a[i] * np.exp(self.b[j] * j)

    def __init__(self, T, drift, vol):
        """
            Initializes the model based on the given parameters.
        """

        super().__init__(T - 1)

        self.a = drift
        self.b = vol
        self._constructTree()

    @classmethod
    def calibrate(cls, T, q, vol, market_spot_rates, iterations=200):
        """
            Calibrates the optimal drift for the given market spot rates
            Initializes the model from the corresponding optimal drift and vol
            Parameters:
            ----------
            T: int
                The number of periods
            q: float
                The probability of rates going upward in the binomial model

            vol: scalar / np.array
                The volatility for the model
            market_spot_rates: np.array
                The current spot rates for n periods to be used for optimization
            max_iter: int
                The number of iterations for which the optimization function should run
            Returns:
            -------
            (BDTRate, error): Returns a tuple of BDTRate instance calibrated from the given parameters and
                                the squared error in the result.
        """

        def error(drift):
            rates = BDTRate(T, drift, vol)
            spot_rates = CashPricing(T, q, rates).get_spot_rates()

            error = spot_rates - market_spot_rates
            return error

        initial_guess = np.repeat(0.05, T)
        drift = opt.broyden1(error, initial_guess, iter=iterations)
        exp_error = (error(drift) ** 2).sum()

        return cls(T, drift, vol), exp_error


class PassThroughMBS(object):
    """
    Implements a basic pass through mortgage backed securitization which
    consists of only single type of mortgages and a constant prepayment factor
    in terms of the PSA.
    Parameters:
    ----------
    P: float
        The principal payment of the pool of mortgages.
    T: int
        The number of years
    loan_r: float
        The rate of interest of lending
    pass_r: float
        The rate of interest given to investors
    PSA: float
        The rate of prepayment in terms of PSA multiplier
    age: int
        The age of the pool. Defaults to 0
    periods_per_year: int
        The number of periods per year. Defualts to 12.
    """

    @property
    def P(self):
        return self._P

    @P.setter
    def P(self, val):
        self._P = val

    @property
    def T(self):
        return self._T

    @T.setter
    def T(self, val):
        self._T = val

    @property
    def loan_r(self):
        return self._loan_r

    @loan_r.setter
    def loan_r(self, val):
        self._loan_r = val

    @property
    def pass_r(self):
        return self._pass_r

    @pass_r.setter
    def pass_r(self, val):
        self._pass_r = val

    @property
    def PSA(self):
        return self._PSA

    @PSA.setter
    def PSA(self, val):
        self._PSA = val

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        self._age = val

    @property
    def periods(self):
        return self._periods

    @periods.setter
    def periods(self, val):
        self._periods = val

    @property
    def data(self):
        """
        Gets a pandas dataframe indexed by the number of periods.
        The columns contain the monthly data about the following:
        Total Payment Received:
            The payment recieved from the mortgage holders each month

        Principal Received:
            The principal part of the payment
        Interest Received:
            The interest part of the payment
        Total Amount Paid:
            The total amount paid back to the investors
        Principal Paid:
            The amount of principal paid back to the investors
        Interest Paid:
            The amount of interest paid back to the investors
        Earning:
            The profit earned by the firm each month
        Prepayment Rate:
            The rate of prepayment each month given by the PSA prepayment model
        Prepayment Amount:
            The amount pre-paid in each by the mortgage holder
        Total OutStanding Amount:
            The total principal amount yet to be paid
        """

        return self._data

    @data.setter
    def data(self, val):
        self._data = val

    def _compute_values(self):
        """
        Fills the data frame of computations
        """
        rem_amount = self.P
        c = self.loan_r
        d = self.pass_r
        n = self.T * self.periods
        t = self.age + 1
        mult = self.PSA / 100

        while rem_amount > 0:
            pay_rec = rem_amount * c / (1 - (1 + c) ** - (n - t + 1))
            interest_rec = rem_amount * c
            princ_rec = pay_rec - interest_rec
            interest_paid = rem_amount * d
            cpr = mult * 0.06 * (1 if t > 30 else t / 30)
            smm = 1 - (1 - cpr) ** (1 / 12)
            repay_amount = (rem_amount - princ_rec) * smm
            princ_paid = princ_rec + repay_amount
            tot_paid = princ_paid + interest_paid
            profit = pay_rec - tot_paid
            rem_amount -= princ_paid
            t += 1

            current_values = {
                "Total Payment Received": pay_rec,
                "Principal Received": princ_rec,
                "Interest Received": interest_rec,
                "Total Amount Paid": tot_paid,
                "Principal Paid": princ_paid,
                "Interest Paid": interest_paid,
                "Earning": profit,
                "Prepayment Rate": smm,
                "Prepayment Amount": repay_amount,
                "Total OutStanding Amount": rem_amount,
            }

            self.data = self.data.append(current_values, ignore_index=True)

            self.data.index += 1


    def __init__(self, P, T, loan_r, pass_r, PSA, age=0, periods_per_year=12):
        """
        Initializes the model from the given set of parameters.
        """

        self.P = P

        self.T = T

        self.loan_r = loan_r / periods_per_year

        self.pass_r = pass_r / periods_per_year

        self.PSA = PSA

        self.age = age

        self.periods = periods_per_year

        cols = [
            "Total Payment Received",
            "Principal Received",
            "Interest Received",
            "Total Amount Paid",
            "Principal Paid",
            "Interest Paid",
            "Earning",
            "Prepayment Rate",
            "Prepayment Amount",
            "Total OutStanding Amount",
        ]
        data = pd.DataFrame(columns=cols)
        self.data = data

        self._compute_values()

class MeanVarianceReturn(object):
    """
        Implements a mean variance model.

        Parameters:
        ----------
        mu (np.array): The mean return of asset
        covariance (np.matrix): Variance matrix
        x (np.array): portfolio
    """

    @property
    def mu(self):
        return self._mu

    @mu.setter
    def mu(self, val):
        self._mu = val

    @property
    def covariance(self):
        return self._covariance

    @covariance.setter
    def covariance(self, val):
        self._covariance = val

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val

    def __init__(self, mu, covariance, x=None):
        """
            Initializes the model based on the given parameters.
        """

        self.mu = mu
        self.covariance = covariance
        self.x = x

    def getVolatility(self):
        if self.x is None:
            return -1
        return portfolioVolatility(self.x, self.covariance)

    def getMeanReturn(self):
        if self.x is None:
            return -1
        return portfolioReturn(self.x, self.mu)

    def getReturnVolatiltiy(self, weights):
        """
        Returns the return and risk in terms of volatility
        for the given assignemt of weights
        Parameters
        ----------
        weights (pd.Series): The weights assigned to different asset in the portfolio.
        Returns
        -------
        (float, float): A tuple representing the return and colatility respectively.
        """

        ret = portfolioReturn(weights, self.mu)
        vol = portfolioVolatility(weights, self.covariance)

        return (ret, vol)

    def getReturnVolatiltiyWithRiskFree(self, weights, riskFreeRate):
        """
        Returns the return and risk in terms of volatility
        for the given assignemt of weights
        Parameters
        ----------
        weights (pd.Series): The weights assigned to different asset in the portfolio.
        Returns
        -------
        (float, float): A tuple representing the return and colatility respectively.
        """
        length = self.mu.size
        ret = portfolioReturn(weights[:length], self.mu) + riskFreeRate * weights.item(length)
        vol = portfolioVolatility(weights[:length], self.covariance)

        return (ret, vol)

    def getCapitalMarketLine(self, riskFreeRate=0.0):
        """
        Returns the parameters of the capital market line.
        Parameters:
        ----------
        riskFreeRate (float): The riskfree_rate of the market
        Returns:
        -------
        tuple - Returns a tuple of (slope, y_intercept) of the CML.
                The y_intercept would be equal to the riskfree_rate.
        """

        optimalWeight = self.maxSharpeRatio(riskFreeRate)
        retures, volatility = self.getReturnVolatiltiy(optimalWeight)

        slope = (retures - riskFreeRate) / volatility
        yIntercept = riskFreeRate

        return (slope, yIntercept)

    def getMaxReturnCapitalMarketLine(self, sigma, riskFreeRate=0.0):
        """
        The maximum return earned by the captial market line model
        for the given sigma
        Parameters:
        ----------
        sigma (float): given sigma
        riskFreeRate (float): The risk free rate of the market
        Returns:
        -------
        expectedReturn (float): The return of capital market line corresponding to the given sigma.
        """

        slope, yIntercept = self.getCapitalMarketLine(riskFreeRate)

        expectedReturn = slope * sigma + yIntercept

        return expectedReturn

    def minVarianceSolver(self, targetReturn):
        """
            optimize the portfolio x to minimize variance

            Parameters:
            ----------

            Returns:
            -------
            weights: Returns the optimal weights
        """

        numAssets = self.mu.size
        initialGuess = np.repeat(1/numAssets, numAssets)
        bounds = ((0.0, 1,0),) * numAssets
        # Constriant for sum of weights to be equal to 1
        weightsSumEquals1 = {
            "type": "eq",
            "fun": lambda weights: np.sum(weights) - 1,
        }

        # Constraint that total return should be equal to target return
        returnEqualsTarget = {
            "type": "eq",
            "args": (self.mu,),
            "fun": lambda weights, mu: targetReturn - portfolioReturn(weights, mu),
        }

        weights = opt.minimize(
            portfolioVolatility,
            initialGuess,
            args=(self.covariance,),
            method="SLSQP",
            options={"disp": False},
            constraints=(weightsSumEquals1, returnEqualsTarget,),
            bounds=bounds,
        )

        return weights.x

    def globalMinVariance(self):
        """
        Returns the weights corresponding to the global minimum variance portfolio.
        The weights only depends on covariance matrix.
        Returns
        -------
        weights (up.array): The optimal weight assignment corresponding to the
                            global minimum variance portfolio.
        """

        weights = self.maxSharpeRatio(0.0, useExpectedReturn=False)

        return weights

    def maxSharpeRatio(self, riskFreeRate = 0.0, useExpectedReturn=True):
        """
        Returns the weights corresponding to the maximum sharpe ratio
        portfolio.
        Parameters
        ----------
        riskFreeRate (float): The risk free rate of return. Defaults to 0.0.
        useExpectedReturn (bool): Uses the expected return attribute if set to true.
                                  Assumes equal expected returns and gives weights
                                  for global minimum variance if set False.
                                  Defaults to True.
        Returns
        -------
        weight (np.array): The optimal weight assignment that minimizes the
                           volatility for the given set of expected returns.
        """

        # Number of stocks
        n = self.mu.size

        # Uses equally weighted expected returns if use_er is set to False
        rets = self.mu if useExpectedReturn else np.repeat(1, n)

        # Inital guess of weights
        initGuess = np.repeat(1 / n, n)

        # Bounds of the weights
        bounds = ((0.0, 1.0),) * n

        # Constraint for the sum of weights to be equal to 1
        weightsSumToOne = {
            "type": "eq",
            "fun": lambda weights: np.sum(weights) - 1,
        }

        def negSharpe(
            weights, riskFreeRate, mu, covariance,
        ):
            """
            Returns the negative of the sharpe ratio
            of the given portfolio
            """
            r = portfolioReturn(weights, mu)
            vol = portfolioVolatility(weights, covariance)

            return -(r - riskFreeRate) / vol

        weights = opt.minimize(
            negSharpe,
            initGuess,
            args=(riskFreeRate, rets, self.covariance,),
            method="SLSQP",
            options={"disp": False},
            constraints=(weightsSumToOne,),
            bounds=bounds,
        )
        return weights.x

    def maxReturnWithRiskless(self, riskFreeRate = 0.0, volatilityUpperLimit = 100.0):
        """
        Returns the weights corresponding to the maximum sharpe ratio
        portfolio.
        Parameters
        ----------
        riskFreeRate (float): The risk free rate of return. Defaults to 0.0.
        volatility (float): volatility upper limit
        Returns
        -------
        weight (np.array): The optimal weight assignment that minimizes the
                           volatility for the given set of expected returns.
        """

        # Number of risky assets plus one riskless
        n = self.mu.size + 1

        # Inital guess of weights
        initGuess = np.repeat(1 / n, n)

        length = self.mu.size

        # Constraint for the sum of weights to be equal to 1
        weightsSumToOne = {
            "type": "eq",
            "fun": lambda weights: np.sum(weights) - 1,
        }

        volatilityLimit = {
            "type": "ineq",
            "fun": lambda weights: volatilityUpperLimit -
                    portfolioVolatility(weights[:length], self.covariance),
        }

        def negReturn(
            weights, riskFreeRate, mu,
        ):
            """
            Returns the negative of the sharpe ratio
            of the given portfolio
            """
            r = portfolioReturn(weights[:length], mu)

            return -r - riskFreeRate * weights.item(length)

        weights = opt.minimize(
            negReturn,
            initGuess,
            args=(riskFreeRate, self.mu, ),
            method="SLSQP",
            options={"disp": False},
            constraints=(weightsSumToOne, volatilityLimit,),
        )
        return weights

    def plotEfficientFrontier(
        self,
        n_points,
        style=".-",
        show_cml=False,
        riskfree_rate=0.0,
        show_ew=False,
        show_gmv=False,
    ):
        """
        Plots the efficient frontier for the given expected returns
        and covariance matrix.
        Parameters
        ----------
        n_points (int): The number of equally spaced weights to be
                        considered
        style (matplotlib.style): The style to be used for plotting
                                    the efficient frontier. Defaults to '.-'.
        show_cml (bool): Plots the capital market line if set true.
                            Defauts to False.
        risk_free_rate (float): Risk free rate to be used for plotting
                                the capital market line. Defualts to 0.0
        show_ew (bool): Plots the equally weghted portfolio point
                            Defauts to False.
        show_gmv (bool): Plots the global minimum variance portfolio
                            Defauts to False.
        Returns
        -------
        matplotlib.plot: The plot of the efficient frontier.
        """
        weights = self.get_ef_weights(n_points)

        rets = [portfolioReturn(w, self.mu,) for w in weights]

        vols = [portfolioVolatility(w, self.covariance,) for w in weights]

        ef = pd.DataFrame({"Returns": rets, "Volatility": vols,})

        ax = ef.plot.line(x="Volatility", y="Returns", style=style)
        ax.set_xlim(left=0)

        if show_cml:

            wt_msr = self.maxSharpeRatio(riskfree_rate)
            ret_msr, vol_msr = self.getReturnVolatiltiy(wt_msr)

            cml_x = [0, vol_msr]
            cml_y = [riskfree_rate, ret_msr]

            ax.plot(
                cml_x,
                cml_y,
                color="green",
                marker="o",
                linestyle="dashed",
                linewidth=2,
                markersize=10,
            )

        if show_ew:
            n = self.mu.size
            wt_ew = np.repeat(1 / n, n)
            ret_ew, vol_ew = self.getReturnVolatiltiy(wt_ew)

            ax.plot(
                vol_ew, ret_ew, color="goldenrod", marker="o", markersize=10,
            )

        if show_gmv:
            wt_gmv = self.globalMinVariance()
            ret_gmv, vol_gmv = self.getReturnVolatiltiy(wt_gmv)

            ax.plot(
                vol_gmv, ret_gmv, color="midnightblue", marker="o", markersize=10,
            )

        return ax

    def get_ef_weights(self, n_points):
        """
        Returns a set of optimal weights for n_points equally spaced
        target returns from minimum expected return to
        maximum expected return.

        The weights are a set of weights on the efficient frontier.
        Parameters
        ----------
        n_points (int): The number of equally spaced weights to be
                        considered
        Returns
        -------
        [pd.Series]: The list of n_points equally spaced weights.
        """

        target_rs = np.linspace(self.mu.min(), self.mu.max(), n_points,)
        weights = [self.minVarianceSolver(target_return) for target_return in target_rs]

        return weights
