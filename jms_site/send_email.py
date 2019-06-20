from django.core.mail import send_mail
from jms_cleaning.settings import EMAIL_HOST_USER

from django.contrib import messages


def send_receipt(request, name, email):
    subject = 'Thanks for getting in touch!'

    message = """

        Hello, """ + name + """, We appreciate you taking the time to contact us. We will get in contact with you as soon as possible!
        \n
        Callum Pullinger 
        0741090817
        info.jmscleaningservices@gmail.com
        """

    send_mail(subject, message, EMAIL_HOST_USER, [str(email)])


def send_contact_request(request, name, email, number, service, message):

    subject = 'Contact Request'

    message = """
    
        Hello, You have a new contact request from """ + name + """
        
        \n Name: """ + name + """
        \n Email: """ + email + """
        \n Number: """ + number + """
        \n Service: """ + str(service.service) + """
        \n Message: """ + message + """
        """

    send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER])


def authError(request):

    messages.warning(request, 'Sorry, Your email can not be sent at this time!')


def send_my_mail(request, name, email, number, service, message):
    send_contact_request(request, name, email, number, service, message)
    send_receipt(request, name, email)




