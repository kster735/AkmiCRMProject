from django.contrib import admin
from minicrm.models import User, Agent, Contact, Message

# Register your models here.

admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Contact)
admin.site.register(Message)

