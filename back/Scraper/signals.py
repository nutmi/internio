from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import JobListings, Emails


@receiver(post_save, sender=JobListings)
def send_email_on_creation(sender, instance, created, **kwargs):
    if created:  # Only trigger when a new JobListing is created
        email_subject = (
            f"New Job Listing Created: {instance.company} - {instance.title}"
        )
        email_message = f"Job Title: {instance.title}\nCompany: {instance.company}\nApply Link: {instance.apply_link}"

        # Retrieve all email addresses from the Emails model
        recipient_list = [email_obj.email for email_obj in Emails.objects.all()]

        # Send the email
        send_mail(
            subject=email_subject,
            message=email_message,
            from_email="noreplyinternio@gmail.com",
            recipient_list=recipient_list,
            fail_silently=False,
        )
