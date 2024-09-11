import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(**context):
    subject = context["var"]["value"].get("subject_mail")
    from_mail = context["var"]["value"].get("email")
    password = context["var"]["value"].get("email_password")
    to = context["var"]["value"].get("to_address")

    # Create a MIMEText object
    msg = MIMEMultipart()
    msg['From'] = from_mail
    msg['To'] = to
    msg['Subject'] = subject

    # Create HTML content
    html_msg = f"""
    <html>
    <body>
        <p>Hey!</p>
        <p>La ETL de Spotify del proyecto de Hazzael Aligehri</p>
        <p>se ha completado con éito</p>
    </body>
    </html>
    """

    # Attach HTML content
    msg.attach(MIMEText(html_msg, 'html'))

    try:
        # Create an SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  

        # Login to the server
        server.login(from_mail, password)

        # Send the email
        text_msg = msg.as_string()
        server.sendmail(from_mail, to, text_msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")