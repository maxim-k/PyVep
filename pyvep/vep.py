__author__ = 'maximkuleshov'

import subprocess
from pyvep.config import config

vep_homedir = config('vep_homedir')
vep_refdir = config('vep_refdir')

def bash(cmd):
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, cwd=vep_refdir)
    output, error = process.communicate()
    return print(output)


def download():
    download_ref = 'wget -i ftp://ftp.ensembl.org/pub/release-87/variation/VEP/homo_sapiens_vep_87_GRCh38.tar.gz'
    unpack_ref = 'tar xfz homo_sapiens_vep_87_GRCh37.tar.gz'
    remove_ref_gz = 'rm homo_sapiens_vep_87_GRCh37.tar.gz'
    bash(download_ref)
    bash(unpack_ref)
    bash(remove_ref_gz)
    return None

def run():
    bash_command = './vep.pl --gencode_basic --species homo_sapiens --symbol --cache --input_file test.vcf '
    vep_dir = '/Users/maximkuleshov/Work/snpEff/'
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE, cwd=vep_dir)
    output, error = process.communicate()
    print(str(output, 'utf-8'))

    return None


def main():
    return None


if __name__ == '__vep__':
    main()
