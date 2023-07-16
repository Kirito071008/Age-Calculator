import datetime

def age_calculator(birthday):
    today_date = datetime.date.today()
    differnce = today_date - birthday
    age_in_years = differnce.days // 365
    return age_in_years

year = int(input("Birth Year (YYYY): "))
month = int(input("Birth Month (MM): "))
day = int(input("Birth Day (DD): "))

birthday = datetime.date(year, month, day)
age = age_calculator(birthday)

print("You are:", age, "years old")
