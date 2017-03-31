__author__ = 'maximkuleshov'

import subprocess


def main():
    bash_command = './vep.pl --gencode_basic --species homo_sapiens --symbol --cache --input_file test.vcf '
    vep_dir = '/Users/maximkuleshov/Work/snpEff/'
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE, cwd=vep_dir)
    output, error = process.communicate()
    print(str(output, 'utf-8'))

    return None


if __name__ == '__main__':
    main()
