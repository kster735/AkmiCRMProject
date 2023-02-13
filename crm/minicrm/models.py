from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass 

# class ManagerManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter()

# class AgentManager(models.Manager):
#     def get_queryset(self, user):
#         return super().get_queryset().get(user = user)


# Create your models here.
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agent_phone = models.CharField(max_length=10)
    agent_photo = models.ImageField(null=True, blank=True, upload_to = 'images/')
    agent_levelaccess = models.IntegerField()
     
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_absolute_url(self):
        return reverse("agent", kwargs={"pk": self.pk})

class Contact(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    contact_firstname = models.CharField(max_length=256)
    contact_lastname = models.CharField(max_length=256)
    contact_email = models.CharField(max_length=256)
    contact_phone = models.CharField(max_length=10)
    contact_phone2 = models.CharField(max_length=10)
    contact_address = models.CharField(max_length=256)
    contact_company = models.CharField(max_length=256)
    contact_vat_no = models.CharField(max_length=9)

    def __str__(self):
        return self.contact_firstname + ' ' + self.contact_lastname

    def get_absolute_url(self):
        return reverse('minicrm:detail_contact', kwargs={'pk': self.pk})

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class SoftDeleteModel(models.Model):

    is_deleted = models.BooleanField(default=False)
    obects = models.Manager()
    undeleted_objects = SoftDeleteManager()

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True

class Message(SoftDeleteModel):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="contact_message")
    message_title = models.CharField(max_length=256)
    message_content = models.CharField(max_length=1024)
    message_datetime = models.DateTimeField()
    message_channel = models.CharField(max_length=256)
    message_due_date = models.DateField()

    def get_absolute_url(self):
        return reverse('minicrm:detail_message', kwargs={'pk': self.pk})
    
class File(models.Model):
    message = models.ForeignKey(Message, on_delete=models.DO_NOTHING)
    file_name = models.FilePathField()     