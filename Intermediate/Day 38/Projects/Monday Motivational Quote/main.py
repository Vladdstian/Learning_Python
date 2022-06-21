# Create an app that sends an email with a random motivational quote from the list if it is a particular day of the week
import smtplib
import datetime as dt
import random

# Date set-up
now = dt.datetime.now()
today = now.weekday()
print(today)

# Email set-up
my_email = "randomemail@gmail.com"
password = "123456"

if today == 7:  # Check to see if it is Monday
    # Generate a random quote from a random line
    lines = open('quotes.txt').read().splitlines()
    new_line = random.choice(lines)
    print(new_line)

    # Send email with the new generated quote
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # encrypting the email - secure connection
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="vlad.c.nichifor@gmail.com",
            msg=f"Subject:Hello! Your motivational quote for Monday is here!\n\n{new_line}"
            )
