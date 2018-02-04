import logging
import numpy
import math
from operator import itemgetter


class Debt(object):
    def __init__(self, name: str ='', balance: float =0, interest: float=0, payment: float=0):
        self.name = name
        self.balance = balance
        if interest > 1:
            self.interest = interest / 100
        else:
            self.interest = interest
        self.payment = payment
        if (self.interest / 12) * self.balance > self.payment:
            logging.info('Payment of ${} is not sufficient to cover the monthly '
                         'interest of {}%'.format(self.payment, self.interest * 100))
        logging.info('Creating debt class instance for {}'.format(self.name))

    def __str__(self) -> str:
        return """Settings:
Name = {}
Balance = ${}
Interest = {}%
Payment = ${}
Remaining payments = {}
""".format(self.name,
           format(self.balance, '.2f'),
           self.interest * 100,
           format(self.payment, '.2f'),
           math.ceil(abs(self.remaining_payments())))

    def remaining_payments(self) -> float:
        return float(numpy.nper(self.interest/12, self.payment, self.balance))

    def payment_interest(self) -> float:
        return self.balance * self.interest / 12

    def payment_principle(self) -> float:
        return self.payment - self.payment_interest()

    def set_balance(self, balance):
        self.balance = balance

    def set_payment(self, payment):
        self.payment = payment

    def add_to_payment(self, payment):
        self.payment += payment


def snowball(debts: list, addition_funds: int=0):
    """Take the list of sorted Debt objects (quickest to pay off to longest) and describe how to pay them off."""
    payments_made = 0

    while len(debts) > 0:
        debt = debts.pop()
        # Make accumulated payments to this debt.
        print("Adding ${} to next debt's payment.".format(addition_funds))
        debt.add_to_payment(addition_funds)
        debt.set_balance = numpy.fv(debt.interest, payments_made, debt.payment, debt.balance)
        print("Pay off {} over {:.1f} payments.".format(debt.name, abs(debt.remaining_payments())))
        payments_made += debt.remaining_payments()
        addition_funds = debt.payment


def sort_debts(debts: list) -> list:
    unsorted_debts = []
    for debt in debts:
        unsorted_debts.append((debt, debt.remaining_payments()))
    long_sorted_debts = sorted(unsorted_debts, key=itemgetter(1))
    sorted_debts = []
    for debt in long_sorted_debts:
        sorted_debts.append(debt[0])
    return sorted_debts
