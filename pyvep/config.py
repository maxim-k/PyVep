__author__ = 'maximkuleshov'

import configparser
import os


def config(key):
    wd = os.path.dirname(os.path.abspath(__file__)) + '/'
    config = configparser.ConfigParser()
    config.read(wd + 'config.ini')
    return config['PyVEP'][key]


def main():
    config('')
    return None


if __name__ == '__main__':
    main()