from django.db import models

# Create your models here.


class Cmdr(models.Model):
    text = models.TextField() #creats textfield inside Admin 
    #py manage.py makemigrations <appname> 
    #py manage.py migrate <cmdr> or class? Double check this
    #py manage.py createsuperuser


    def __str__(self): #for renaming text field object name
        return self.text