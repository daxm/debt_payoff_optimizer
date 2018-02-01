#! /usr/bin/env python3

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
        balance = 0 - self.balance
        return math.ceil(float(numpy.nper(self.interest/12, self.payment, balance)))

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


def snowball(debts: list):
    """Take the list of sorted Debt objects (quickest to pay off to longest) and describe how to pay them off."""
    payments_made = 0
    accumlated_money = 0
    debts.reverse()
    while(len(debts) > 0):
        debt = debts.pop()
        # Make accumulated payments to this debt.
        print("Adding ${} to next debt's payment.".format(accumlated_money))
        debt.add_to_payment(accumlated_money)
        debt.set_balance = numpy.fv(debt.interest, payments_made, debt.payment, debt.balance)
        print("Pay off {} over {} payments.".format(debt.name, debt.remaining_payments()))
        payments_made += debt.remaining_payments()
        accumlated_money += debt.payment


def sort_debts(debts: list=[]) -> list:
    unsorted_debts = []
    for debt in debts:
        unsorted_debts.append((debt, debt.remaining_payments()))
    long_sorted_debts = sorted(unsorted_debts, key=itemgetter(1))
    sorted_debts = []
    for debt in long_sorted_debts:
        sorted_debts.append(debt[0])
    return sorted_debts


def main():
    logging.getLogger(__name__).addHandler(logging.NullHandler())

    logging_format = '%(asctime)s - %(levelname)s:%(filename)s:%(lineno)s - %(message)s'
    logging_dateformat = '%Y/%m/%d-%H:%M:%S'
    logging_level = logging.INFO
    # logging_level = logging.DEBUG
    logging_filename = 'output.log'
    logging.basicConfig(format=logging_format,
                        datefmt=logging_dateformat,
                        filename=logging_filename,
                        filemode='w',
                        level=logging_level)

    mortgage = Debt(name='Chase', balance=200000, interest=6, payment=1400)
    truck = Debt(name='Chev', balance=13000, interest=3, payment=500)
    unsorted_debts = [mortgage, truck]
    snowball(sort_debts(debts=unsorted_debts))

if __name__ == '__main__':
    main()
