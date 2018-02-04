#! /usr/bin/env python3

from helper import *
import logging

unsorted_debts = [
    Debt(name='Chase', balance=203000, interest=4, payment=1400),
    Debt(name='Chev', balance=13500, interest=3, payment=500),
    Debt(name='Medical', balance=20000, interest=2, payment=300),
    Debt(name='IRS', balance=2000, interest=24, payment=300),
]

extra_starting_cash = 500


def main():
    logging.getLogger(__name__).addHandler(logging.NullHandler())

    logging_format = '%(asctime)s - %(levelname)s:%(filename)s:%(lineno)s - %(message)s'
    logging_dateformat = '%Y/%m/%d-%H:%M:%S'
    logging_level = logging.INFO
    logging_filename = 'output.log'
    logging.basicConfig(format=logging_format,
                        datefmt=logging_dateformat,
                        filename=logging_filename,
                        filemode='w',
                        level=logging_level)

    snowball(sort_debts(debts=unsorted_debts), addition_funds=extra_starting_cash)
    logging.info("Done.")


if __name__ == '__main__':
    main()
