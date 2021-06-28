from datetime import date
year = input("year: ")
month = input("month(1-12): ")
day = input("day: ")

now = date.today()

age = date(int(year), int(month), int(day))

print(f"your age is {(now-age) / 365}")