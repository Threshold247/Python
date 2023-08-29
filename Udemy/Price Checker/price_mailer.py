import smtplib
import os
from dotenv import load_dotenv
load_dotenv(".env")


class EmailNotify:
    user_email = os.getenv("my_email")
    user_password = os.getenv("my_password")

    # function takes 2 parameters
    def send_email(self, price, url):
        # setup connection
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # enable encryption
            connection.starttls()
            # login
            connection.login(user=self.user_email, password=self.user_password)
            # sending email from sender to recipient with message
            connection.sendmail(from_addr=self.user_email,
                                to_addrs="threshold247@gmail.com",
                                msg=f"Price Alert at Loot!\n\nThe latest price for the Instant Pot is R{price}\n"
                                    f"The link to the product is {url}")


