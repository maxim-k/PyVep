__author__ = 'maximkuleshov'

import configparser


def config(key):
    config = configparser.ConfigParser()
    config.read('pyvep/config.ini')
    return config['PyVEP'][key]


def main():
    return None


if __name__ == '__main__':
    main()