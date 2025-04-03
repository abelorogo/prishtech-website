from django.db import models

class EmailMessage(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sender = models.EmailField()  # Email of the sender
    recipient = models.EmailField()  # Email of the single recipient
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
