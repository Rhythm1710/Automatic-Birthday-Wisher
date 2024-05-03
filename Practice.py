# import smtplib

# my_email = "rhythm.hacker17@gmail.com"
# password =    

# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     # connection.sendmail(from_addr=my_email,to_addrs="soumyadev56@gmail.com",msg="Hello")
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="soumyadev56@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#         )


# # import smtplib

# # my_email = "your_email@gmail.com"
# # password = "your_password"

# # Establish a connection to the SMTP server
# try:
#     connection = smtplib.SMTP("smtp.gmail.com", port=587)
#     connection.starttls()  # Upgrade the connection to a secure TLS connection
#     connection.login(user=my_email, password=password)
# except smtplib.SMTPAuthenticationError:
#     print("Authentication error. Please check your email and password.")
# except smtplib.SMTPException as e:
#     print("An error occurred while establishing the connection:", str(e))
# else:
#     # Send an email
#     from_addr = my_email
#     to_addr = "soumyadev56@gmail.com"  # Replace with the recipient's email address
#     subject = "Test Email"
#     message = "Hello, this is a test email sent from Python."

#     email_body = f"Subject: {subject}\n\n{message}"

#     try:
#         connection.sendmail(from_addr, to_addr, email_body)
#         print("Email sent successfully!")
#     except smtplib.SMTPException as e:
#         print("An error occurred while sending the email:", str(e))
#     finally:
#         connection.quit()

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# date_of_birth = dt.datetime(year=2020,month=12,day=12,hour=4)
# print(date_of_birth)
