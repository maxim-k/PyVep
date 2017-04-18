__author__ = 'maximkuleshov'

import os

from json import loads
from subprocess import Popen, PIPE

from pyvep.config import config

vep_homedir = config('vep_homedir')
vep_refdir = config('vep_refdir')
pyvep_results = config('pyvep_results')


def download(species, ref):
    cmd = 'sudo perl INSTALL.pl -a ac -s {} -y {} -l --NO_TEST'.format(species, ref)
    process = Popen(cmd, shell=True, stdout=PIPE, close_fds=True, cwd=vep_homedir)
    output, error = process.communicate()
    return None


def snv_to_json():
    return None


def run(species, ref, file):
    # Local cache version
    res_file = pyvep_results + os.path.basename(file)
    bash_command = 'vep --gencode_basic --species {} -i {} ' \
                   ' --json --symbol --cache --offline --fork 4' \
                   ' --no_stats --input_file {}' \
                   ' --output_file {}.txt'.format(species, ref, file, res_file)

    process = Popen(bash_command.split(), stdout=PIPE, cwd=vep_homedir)
    output, error = process.communicate()
    print(str(output, 'utf-8'))
    return res_file


def run_dev(species, ref, file):
    # Ensembl db version
    res_file = pyvep_results + os.path.basename(file)
    bash_command = 'vep --gencode_basic --species {} -i {} ' \
                   ' --json --symbol --database --input_file {}' \
                   ' --output_file {}.txt'.format(species, ref, file, res_file)

    process = Popen(bash_command.split(), stdout=PIPE, cwd=vep_homedir)
    output, error = process.communicate()
    print(str(output, 'utf-8'))
    return res_file


def parse_json():
    json = open('variant_effect_output.txt.json', 'r').readlines()
    for line in json:
        json_line = loads(line)
        print(json_line)
    return None


def main():
    parse_json()
    return None


if __name__ == '__main__':
    main()
