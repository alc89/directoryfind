
import glob, os

available_isolates = glob.glob('fastqs/*/*.fastq')
isolate_buckets = {}
for isolate in available_isolates:
    bucket_name = os.path.dirname(isolate).split('/')[-1]
    if bucket_name in isolate_buckets:
        isolate_buckets[bucket_name].append(isolate)
    else:
        isolate_buckets[bucket_name] = [isolate]

print dict((k, v) for k, v in isolate_buckets.items() if len(v) > 1)
print isolate_buckets
