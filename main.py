import smtplib
import datetime as dt
import pandas as pd
import random as r
import os

# ---------------------------- EMAIL ------------------------------- #
my_email = ""
my_password = ""
dob = {}
name = ""
email = ""
message = ""
directory_path = ""
# ---------------------------- SELECTING MESSAGE------------------------------- #


def send_birthday_message(email, name):
    files = os.listdir(directory_path)
    letter_template = r.choice(files)

    with open(os.path.join(directory_path, letter_template), "r") as file:
        content = file.read()
        message = content.replace("[NAME]", name)
        sending_message(email, message)

# ---------------------------- SENDING MESSAGE------------------------------- #


def sending_message(email, message):
    try:
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password=my_password)

    except smtplib.SMTPAuthenticationError:
        print("Authentication error")

    except smtplib.SMTPException as e:
        print("An error occurred:", str(e))

    else:
        from_addr = my_email
        to_addrs = email
        subject = f"Happy Birthday  {name}"
        email_body = f"Subject:{subject}\n\n{message}"
        connection.sendmail(from_addr, to_addrs, email_body)
        print("Message sent")

    finally:
        connection.quit()

# ---------------------------- READING DOBS------------------------------- #


def select_name():
    global name, dob, email
    now = dt.datetime.now()

    for entry in dob:
        if now.day == entry["day"] and now.month == entry["month"]:
            name = entry["name"]
            email = entry["email"]
            send_birthday_message(email, name)


try:
    data = pd.read_csv(
        '')

except FileNotFoundError:
    print("File not found")

else:
    dob = data.to_dict(orient="records")
    select_name()
