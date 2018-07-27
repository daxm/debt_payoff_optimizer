#! /usr/bin/env python3

from helper import *
from ruamel.yaml import YAML
import logging

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


def main():
    unsorted_debts = []
    userdata_file = 'userdata.yml'

    yaml = YAML(typ='safe')
    with open(userdata_file, 'r') as stream:
        try:
            userdata = (yaml.load(stream))
            if 'extra_starting_cash' in userdata:
                extra_starting_cash = userdata['extra_starting_cash']
            else:
                extra_starting_cash = 0.0
            logging.info(f"Opened and loaded {userdata_file}")
            for debt in userdata['debts']:
                unsorted_debts.append(Debt(name=debt['name'],
                                           balance=debt['balance'],
                                           interest=debt['interest_rate'],
                                           payment=debt['payment']))

            snowball(sort_debts(debts=unsorted_debts), addition_funds=extra_starting_cash)
            logging.info("Done.")
        except OSError:
            logging.error(f"An error has occurred trying to open {userdata_file}.")
            exit(1)



if __name__ == '__main__':
    main()
