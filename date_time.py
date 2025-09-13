import datetime 

now = datetime.datetime.now()

name = "Mohamed"
day_name = now.strftime("%A")        # e.g. Friday
month_name = now.strftime("%B")      # e.g. July
day = now.day                        # e.g. 18
year = now.year                      # e.g. 2025
hour = now.strftime("%I")            # 12-hour format
minute = now.strftime("%M")
am_pm = now.strftime("%p")           # AM or PM

text = f"Good morning {name}. Today is {day_name}, {month_name} {day}, {year}. The time is {hour}:{minute} {am_pm}."

if __name__ == "__main__" :
    print (f"{day_name} : {month_name}")

