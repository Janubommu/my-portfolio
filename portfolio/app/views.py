from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse

def send_email(request):
    if request.method == 'POST':
        # Getting the form details
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')  # Correct the typo: 'meagess' to 'message'
        # Email subject and message content
        subject = f"New Contact Form Submission from {name}"
        email_message = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

        # Sender email
        from_email = 'bommujanu@gmail.com'

        # Recipient list: send the email to both the user and the admin (bommujanu@gmail.com)
        recipient_list = [email, 'bommujanu@gmail.com']

        try:
            # Sending the email
            send_mail(subject, email_message, from_email, recipient_list)

            # Success message
            messages.success(request, "Your message has been sent successfully!")

            # Redirect to the home page after successful submission
            return redirect('home')

        except Exception as e:
            # Handle failure in sending email
            messages.error(request, f"Failed to send your message: {str(e)}")
            return redirect('home')

    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')
