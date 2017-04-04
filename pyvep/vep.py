__author__ = 'maximkuleshov'

from subprocess import Popen, PIPE, STDOUT
from pyvep.config import config

vep_homedir = config('vep_homedir')
vep_refdir = config('vep_refdir')


def download(species, ref):
    cmd = 'perl INSTALL.pl -a ac -s {} -y {} -l'.format(species, ref)
    process = Popen(cmd, shell=True, stdout=PIPE, close_fds=True, cwd=vep_homedir)
    output, error = process.communicate()
    return None


def snv_to_json():
    return None


def run(species, file):
    bash_command = 'vep --gencode_basic --species {} --symbol --cache --input_file test.vcf'.format(species)
    process = Popen(bash_command.split(), stdout=PIPE, cwd=vep_homedir)
    output, error = process.communicate()
    print(str(output, 'utf-8'))

    return None


def main():
    return None


if __name__ == '__vep__':
    main()
