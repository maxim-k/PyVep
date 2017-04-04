__author__ = 'maximkuleshov'

from subprocess import Popen, PIPE, STDOUT
from pyvep.config import config

vep_homedir = config('vep_homedir')
vep_refdir = config('vep_refdir')


def download(species, ref):
    # download_ref = 'wget -c ftp://ftp.ensembl.org/pub/release-87/variation/VEP/homo_sapiens_vep_87_GRCh38.tar.gz'
    # unpack_ref = 'tar xfz homo_sapiens_vep_87_GRCh38.tar.gz'
    # remove_ref_gz = 'rm homo_sapiens_vep_87_GRCh38.tar.gz'
    # cmd = "{}; {}; {};".format(download_ref, unpack_ref, remove_ref_gz)
    # process = Popen(cmd, shell=True, stdout=PIPE, close_fds=True, cwd=vep_refdir)
    cmd = 'perl INSTALL.pl -a ac -s {} -y {} -l'.format(species, ref)
    process = Popen(cmd, shell=True, stdout=PIPE, close_fds=True, cwd=vep_homedir)
    output, void = process.communicate()
    return None


def run():
    bash_command = './vep.pl --gencode_basic --species homo_sapiens --symbol --cache --input_file test.vcf '
    vep_dir = '/Users/maximkuleshov/Work/snpEff/'
    process = Popen(bash_command.split(), stdout=PIPE, cwd=vep_dir)
    output, error = process.communicate()
    print(str(output, 'utf-8'))

    return None


def main():
    return None


if __name__ == '__vep__':
    main()
