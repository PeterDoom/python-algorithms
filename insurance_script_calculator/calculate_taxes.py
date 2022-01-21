

from hashlib import new


def main(salary_brute:int, max_ceil=3000, percentage_for_employee=13.78, years_of_employemnt=0):
    rate_for_employment = 0.006
    flat_rate = 0.1

    if years_of_employemnt > 0:
        to_add = salary_brute * rate_for_employment * years_of_employemnt
        salary_brute += to_add

    diff_between_ranges = abs(salary_brute - max_ceil)

    calc1 = (max_ceil - (max_ceil * (percentage_for_employee / 100))) + diff_between_ranges
    calc2 = calc1 - (calc1 * flat_rate)
    return(calc2)


if __name__ == "__main__":
    old_salary = float("{:.2f}".format(main(14700, years_of_employemnt=3)))
    new_salary = float("{:.2f}".format(main(14700, years_of_employemnt=3, max_ceil=3400)))
    diff = "{:.2f}".format(abs(old_salary - new_salary))
    statement = f"The difference between {old_salary} vs {new_salary} is {diff}"
    print(statement)
