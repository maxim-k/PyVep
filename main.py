__author__ = 'maximkuleshov'

import subprocess

def main():
    bashCommand = './vep.pl --gencode_basic --species homo_sapiens --symbol --cache --input_file test.vcf '
    vep_dir = '/Users/maximkuleshov/Work/snpEff/'
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, cwd=snpEff_dir)
    output, error = process.communicate()
    print(str(output,'utf-8'))

    return None


if __name__ == '__main__':
    main()