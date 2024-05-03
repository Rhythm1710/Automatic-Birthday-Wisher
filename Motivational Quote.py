import smtplib
import datetime as dt
import random

my_email = "rhythm.hacker17@gmail.com"
my_password = "xkkxieymtseyzcqu"


def send_msg():
    now = dt.datetime.now()
    day_of_week = now.weekday()

    if day_of_week == 3:
        with open("E:/Python/Course/Birthday+Wisher+(Day+32)+start/Birthday Wisher (Day 32) start/quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes)
    return quote


try:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)

except smtplib.SMTPAuthenticationError:
    print("Authentication error")

except smtplib.SMTPException as e:
    print("An error occured:", str(e))

else:
    from_addr = my_email
    to_addrs = "soumyadev56@gmail.com"
    subject = "Motivational Quote"
    message = send_msg()

    email_body = f"Subject:{subject}\n\n{message}"

    connection.sendmail(from_addr, to_addrs, email_body)

finally:
    connection.quit()
