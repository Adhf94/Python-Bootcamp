import smtplib
import datetime as dt
import random
#Make a list with the inspiracional quotes
with open("quotes.txt", "r") as quotes:
    quote_list = [quote for quote in quotes]
#Hold the current day
current_day = dt.datetime.now().weekday()
#Send mail with random quote if it fits the condition
my_email = "email"
password = "pasword"
#Conectarse al servidor de google smtp
random_quote = random.choice(quote_list)
if current_day == 3:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        #CONECTARSE AL TLS
        connection.starttls()
        #logearse al servidor
        connection.login(user=my_email, password=password)
        # Send the email if meets the condition
        connection.sendmail(from_addr=my_email, to_addrs="dummie@yahoo.com",
                            msg=f"Subject:Challenge1\n\n{random_quote}")
