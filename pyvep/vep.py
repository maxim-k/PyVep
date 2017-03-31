__author__ = 'maximkuleshov'

import subprocess
vep_dir = ''

def download():
    bash_command = 'wget -i ftp://ftp.ensembl.org/pub/release-87/variation/VEP/homo_sapiens_vep_87_GRCh38.tar.gz'
    # RUN tar xfz homo_sapiens_vep_87_GRCh37.tar.gz
    # RUN rm homo_sapiens_vep_87_GRCh37.tar.gz
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE, cwd=vep_dir)
    output, error = process.communicate()
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
