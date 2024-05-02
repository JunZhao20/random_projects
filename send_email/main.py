import smtplib
import datetime as dt
# def gui():
#     while True:
#         ui = input('What email you want to send to? ')
#         if '@' in ui:
#             print('Sent')
#             return ui, False
#         else:
#             print('Incorrect email. Try again.')
            

email = 'zhaogaming21@gmail.com'
password = 'zmeh moeu eiev gtvl'
connection = smtplib.SMTP("smtp.gmail.com")

connection.starttls()

connection.login(user=email, password=password)
connection.sendmail(from_addr=email, to_addrs='junzhao1111@gmail.com', msg='OI')
connection.close()
