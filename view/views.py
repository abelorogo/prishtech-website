from django.shortcuts import render
import smtplib
import ssl
from django.conf import settings
from django.contrib import messages
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .forms import EmailForm

def contact(request):
    form = EmailForm()  # Initialize empty form
    email_sent = False  # Flag to track if email was sent successfully

    if request.method == 'POST':
        form = EmailForm(request.POST)  # Bind form with data

        if form.is_valid():
            sender = form.cleaned_data.get('your_email')
            phone = form.cleaned_data.get('phone_number')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            recipient = settings.EMAIL_RECEIVER  # Auto-receiver

            full_message = f"""
            Subject: {subject}
            Message: {message}
            Phone: {phone}
            From: {sender}
            """

            try:
                context = ssl._create_unverified_context()

                # Create the email message
                msg = MIMEMultipart()
                msg['From'] = f"PrishTech <{settings.EMAIL_HOST_USER}>"  # Sender's name with email
                msg['To'] = recipient
                msg['Subject'] = subject

                # Attach the message content
                msg.attach(MIMEText(full_message, 'plain'))

                # Send the email
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls(context=context)
                    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                    server.sendmail(settings.EMAIL_HOST_USER, recipient, msg.as_string())

                messages.success(request, "Your message has been sent successfully!")
                email_sent = True  # Update flag when email is sent
                form = EmailForm()  # Reset form after success

            except Exception as e:
                messages.error(request, f"Failed to send email. Error: {e}")  
                # Don't reset form, so data remains

    return render(request, 'contact.html', {'form': form, 'email_sent': email_sent})

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def about(request):
    return render(request, 'about.html')
