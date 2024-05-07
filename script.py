import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import requests
import time
import datetime



class_status = {}

while True:
    url = lambda crn: f'https://oscar.gatech.edu/bprod/bwckschd.p_disp_detail_sched?term_in=202402&crn_in={str(crn)}'

    # Add the classes you want to monitor here
    courses = {
                '''
                "Class name": url(CRN)
                "Class name": url(CRN)
                "Class name": url(CRN)
                '''
               }

    status_changed = False
    message = ""

    for course, link in courses.items():
        response = requests.get(link)
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')
        rows = soup.find_all('tr')

        for row in rows:
            cells = row.find_all('td')
            if cells and 'Seats' in row.text:
                remaining_seats = int(cells[4].text.strip())
                print(f'{course}: {remaining_seats}')
                
                if course not in class_status or class_status[course] != remaining_seats > 0:
                    status_changed = True
                    class_status[course] = remaining_seats > 0
                    status = "OPEN" if remaining_seats > 0 else "CLOSED"
                    message += f"{course} is now {status}.\n"

                break

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    print()

    if status_changed:
        print("Status Changed")

        # Add your email here
        user_email = ""

        from_email = user_email
        to_email = user_email

        # Add your email app password here
        email_password = ""

        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = "Class Status Update"

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, email_password)
        server.send_message(msg)
        server.quit()

    time.sleep(1.5)