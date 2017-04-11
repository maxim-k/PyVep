__author__ = 'maximkuleshov'

from json import loads
from subprocess import Popen, PIPE

from pyvep.config import config

vep_homedir = config('vep_homedir')
vep_refdir = config('vep_refdir')


def download(species, ref):
    cmd = 'sudo perl INSTALL.pl -a ac -s {} -y {} -l --NO_TEST'.format(species, ref)
    process = Popen(cmd, shell=True, stdout=PIPE, close_fds=True, cwd=vep_homedir)
    output, error = process.communicate()
    return None


def snv_to_json():
    return None


def run(species, ref, file):
    bash_command = 'vep --gencode_basic --species {} -i {} --no_stats --json --symbol --cache --input_file {}'.format(species, ref, file)
    process = Popen(bash_command.split(), stdout=PIPE, cwd=vep_homedir)
    output, error = process.communicate()
    print(str(output, 'utf-8'))
    return None


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
