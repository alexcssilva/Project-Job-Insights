from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    unique_list = {}
    for row in jobs_list:
        job_type = row['job_type']
        if job_type not in jobs_list:
            unique_list[job_type] = 0
        unique_list[job_type] += 1
    return unique_list


def filter_by_job_type(jobs, job_type):
    result = []
    for job in jobs:
        if job['job_type'] == job_type:
            result.append(job)
    return result


def get_unique_industries(path):
    jobs_list = read(path)
    unique_list = {}
    for row in jobs_list:
        industry = row['industry']
        if industry not in "":
            unique_list[industry] = 0
    return unique_list


def filter_by_industry(jobs, industry):
    result = []
    for job in jobs:
        if job['industry'] == industry:
            result.append(job)
    return result


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = []
    for row in jobs_list:
        list_max_salary = row['max_salary']
        if list_max_salary not in "" and list_max_salary.isnumeric():
            max_salary.append(int(list_max_salary))
    return max(max_salary)


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = []
    for row in jobs_list:
        list_mix_salary = row['min_salary']
        if list_mix_salary not in "" and list_mix_salary.isnumeric():
            min_salary.append(int(list_mix_salary))
    return min(min_salary)


def matches_salary_range(job, salary):
    try:
        max_salary = job["max_salary"]
        min_salary = job["min_salary"]
    except KeyError:
        raise ValueError()
    if (type(max_salary) != int or type(salary) != int
            or max_salary < min_salary or type(salary) != int):
        raise ValueError()
    if int(min_salary) <= int(salary) and int(salary) <= int(max_salary):
        return True
    return False


def filter_by_salary_range(jobs, salary):
    result = []
    for row in jobs:
        max_salary = row['max_salary']
        min_salary = row['min_salary']
        if (type(max_salary) == int and type(salary) == int
                and max_salary > min_salary):
            if min_salary <= salary <= max_salary:
                result.append(row)
    return result
