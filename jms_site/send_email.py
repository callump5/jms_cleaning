from django.core.mail import send_mail
from jms_cleaning.settings import EMAIL_HOST_USER

from django.contrib import messages

def send_my_mail(request, name, email, number, service, message):

    subject = 'Contact Request'

    message = """
    
      Hello, You have a new contact request from """ + name + """
        
        \n Name: """ + name + """
        \n Email: """ + email + """
        \n Number: """ + number + """
        \n Service: """ + str(service.service) + """
        \n Message: """ + message + """
        
        """

    send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER, str(email)])


def authError(request):

    messages.warning(request, 'Sorry, Your email can not be sent at this time!')


