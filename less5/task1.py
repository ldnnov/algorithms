from collections import namedtuple

Company = namedtuple('Company', 'name, q1, q2, q3, q4, year_income')

companies = []
allover_income = 0

while True:
    name = input("Insert company name (0 - to finish adding companies): ")

    if name == '0':
        break

    q1 = float(input("Insert income in first quarter: "))
    q2 = float(input("Insert income in second quarter: "))
    q3 = float(input("Insert income in third quarter: "))
    q4 = float(input("Insert income in fourth quarter: "))

    total_income = q1 + q2 + q3 + q4
    allover_income += total_income

    companies.append(Company(name, q1, q2, q3, q4, total_income))

avg_income = allover_income / len(companies)
lower_income = []
higher_income = []

for company in companies:
    if company.year_income <= avg_income:
        lower_income.append(company.name)
    else:
        higher_income.append(company.name)

print(f'Average income: {avg_income}')
print(f'Companies with higher income: {", ".join(higher_income)}')
print(f'Companies with lower income: {", ".join(lower_income)}')
