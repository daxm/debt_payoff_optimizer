#! /usr/bin/env python3

from helper import *
import logging
from userdata import unsorted_debts, extra_starting_cash


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
