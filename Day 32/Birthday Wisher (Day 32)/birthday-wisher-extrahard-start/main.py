import random
import pandas
import datetime as dt
import smtplib
MY_EMAIL =  "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"
#Save current day
check_day = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")
dic_cumples = data.to_dict(orient="records")
#Check and send emails
for item in dic_cumples:
    birthday = (item["month"], item["day"])
    name = item["name"]
    email = item["email"]
    print(birthday, check_day)
    if birthday == check_day:
        print(birthday, email)
        file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=email,
                                msg=f"Subject:Happy Birthday\n\n {contents}")
