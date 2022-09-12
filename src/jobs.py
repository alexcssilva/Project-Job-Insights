from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as csvfile:
        jobs_reader = csv.DictReader(csvfile, delimiter=",", quotechar='"')
        jobs_array = []
        for row in jobs_reader:
            jobs_array.append(row)
        return jobs_array
