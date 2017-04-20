__author__ = 'maximkuleshov'

import os

from json import loads
from subprocess import Popen, PIPE

from pyvep.config import config

vep_homedir = config('vep_homedir')
vep_refdir = config('vep_refdir')
pyvep_results = config('pyvep_results')


def run(species, ref, file):
    # Local cache version
    res_file = pyvep_results + os.path.basename(file)
    bash_command = 'vep --gencode_basic --species {} -i {} ' \
                   ' --coding_only --pick --filter "SYMBOL"' \
                   ' --json --symbol --canonical --cache --offline' \
                   ' --fork 4 --no_stats --input_file {}' \
                   ' --output_file {}.txt'.format(species, ref, file, res_file)

    process = Popen(bash_command.split(), stdout=PIPE, cwd=vep_homedir)
    output, error = process.communicate()
    print(str(output, 'utf-8'))
    return res_file


def run_dev(species, ref, file):
    # Ensembl db version
    res_file = pyvep_results + os.path.basename(file)
    bash_command = 'vep --gencode_basic --species {} -i {} ' \
                   ' --coding_only --pick --filter "SYMBOL"' \
                   ' --json --symbol --canonical --database --input_file {}' \
                   ' --output_file {}.txt'.format(species, ref, file, res_file)

    process = Popen(bash_command.split(), stdout=PIPE, cwd=vep_homedir)
    output, error = process.communicate()
    print(str(output, 'utf-8'))
    parse_json(res_file)
    return res_file


def parse_json(res_file):
    json = open(res_file, 'r').readlines()
    for line in json:
        json_line = loads(line)
    return None


def main():
    # parse_json()
    return None


if __name__ == '__main__':
    main()
