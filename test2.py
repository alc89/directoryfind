
import glob, os

test_isolates = glob.glob('fastqs/*')

for i in test_isolates:
    if os.path.isdir(i) and len(glob.glob(i + '/*.fastq')) == 2:
        print i + " has two files in it"
