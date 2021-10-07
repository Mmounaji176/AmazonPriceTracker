from selenium import webdriver
import selenium
import smtplib
import  os
path = "C:\Program Files\chromedriver.exe"
driver= webdriver.Chrome(path)

driver.get("https://www.amazon.com/Apple-MacBook-Retina-MPTT2LL-Refurbished/dp/B07FQQ8DSY/ref=sr_1_6?dchild=1&keywords=macbook%2Bpro&qid=1631725870&s=computers-intl-ship&sr=1-6&th=1")

title = driver.find_element_by_id("productTitle").text
print("your product is : ")
print(title)
price = driver.find_element_by_id("priceblock_ourprice").text.replace(",","")
price= price[1:5]
converted = int(price)+1
print("the actual price is : ")
print(converted," dollar")



#sending email if the price reduced
email_adress = os.environ.get('email')
email_password = os.environ.get('password')


sender = email_adress
receiver = "codestermn@gmail.com"
password = email_password
subject = "your product price has been reduced"
body = "check out the product : https://www.amazon.com/Apple-MacBook-Retina-MPTT2LL-Refurbished/dp/B07FQQ8DSY/ref=sr_1_6?dchild=1&keywords=macbook%2Bpro&qid=1631725870&s=computers-intl-ship&sr=1-6&th=1"

# header
message = f"""From: amazontracker{sender}
To: {receiver}
Subject: {subject}\n
{body}
"""
if converted <= 1300:
   server = smtplib.SMTP("smtp.gmail.com", 587)
   server.starttls()

   try:
       server.login(sender,password)
        
       print("Logged in...")
       server.sendmail(sender, receiver, message)
       print("Email has been sent! check out the procuct")

   except smtplib.SMTPAuthenticationError:
        print("unable to sign in")


   server.quit()
else :
	print("the price is not 1100")