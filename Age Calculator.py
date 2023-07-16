import datetime

def age_calculator(birthday):
    today_date = datetime.date.today()
    differnce = today_date - birthday
    age_in_years = differnce.days // 365
    return age_in_years

year = int(input("Inserisci l'anno di nascita (YYYY): "))
month = int(input("Inserisci il mese di nascita (MM): "))
day = int(input("Inserisci il giorno di nascita (DD): "))

birthday = datetime.date(year, month, day)
age = age_calculator(birthday)

print("You are:", age, "years old")
