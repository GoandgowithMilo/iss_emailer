# This file contains a wrapper function for sending a simple email using Python
def gmail_function(password, sender_email, receiver_email, message):
    import smtplib, ssl

    port = 465 # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
