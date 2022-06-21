# sending emails with Python
import smtplib

my_email = "appbreweryinfo@gmail.com"
password = "abcd1234()"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # encrypting the email - secure connection
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="vlad.c.nichifor@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email"
        )

# connection.close() - no need since we opened the connection the same way we opened a file
# - at the end it will be closed automatically

