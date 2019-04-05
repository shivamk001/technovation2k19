from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.shortcuts import reverse
# Create your models here.
class Event_Type(models.Model):
    TYPE_CHOICES=(
    ('TECHNICAL','TECHNICAL'),
    ('NON-TECHNICAL','NON-TECHNICAL')
    )
    event_type = models.CharField(max_length=200, choices=TYPE_CHOICES, help_text='Enter Event Type (e.g. Tech)')

    class Meta:
        ordering=['event_type']
    def __str__(self):
        return ("{}".format(self.event_type))

class Event(models.Model):
    EVENT_CHOICES=(
    ('EVENT1','EVENT1'),
    ('EVENT2','EVENT2'),
    ('EVENT3','EVENT3'),
    ('EVENT4','EVENT4'),
    ('EVENT5','EVENT5'),
    ('EVENT6','EVENT6'),
    ('EVENT7','EVENT7'),
    ('EVENT8','EVENT8'),
    ('EVENT9','EVENT9'),
    ('EVENT10','EVENT10'),
    )
    event_name = models.CharField(max_length=200,choices=EVENT_CHOICES, help_text='Enter Event Name (e.g. CodeGolf)')

    event_type=models.ForeignKey('Event_Type',on_delete=models.SET_NULL,null=True)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the event',default='')

    class Meta:
        ordering=['event_type','event_name']

    def __str__(self):
        return ("{} {}".format(self.event_name, self.event_type))

    '''
    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])

    '''

class Event_Choice(models.Model):
    EVENT_CHOICES=(
    ('EVENT1 TECHNICAL','EVENT1 TECHNICAL'),
    ('EVENT2 TECHNICAL','EVENT2 TECHNICAL'),
    ('EVENT3 TECHNICAL','EVENT3 TECHNICAL'),
    ('EVENT4 TECHNICAL','EVENT4 TECHNICAL'),
    ('EVENT5 TECHNICAL','EVENT5 TECHNICAL'),
    ('EVENT6 NON-TECHNICAL','EVENT6 NON-TECHNICAL'),
    ('EVENT7 NON-TECHNICAL','EVENT7 NON-TECHNICAL'),
    ('EVENT8 NON-TECHNICAL','EVENT8 NON-TECHNICAL'),
    ('EVENT9 NON-TECHNICAL','EVENT9 NON-TECHNICAL'),
    ('EVENT10 NON-TECHNICAL','EVENT10 NON-TECHNICAL'),
    )
    event = models.CharField(max_length=200,choices=EVENT_CHOICES, help_text='Enter Event Name (e.g. CodeGolf Teechnical)')

    def __str__(self):
        return ("{} {}".format(self.event))

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    phone = PhoneNumberField(null=False,blank=False,unique=True, default='+919999999999')

    college = models.CharField(max_length=100,null=False,blank=False, default='IERT')

    YEAR_CHOICES=(
    ('first','1'),
    ('second','2'),
    ('third','3'),
    ('forth','4'),
    )
    year=models.CharField(max_length=10,null=False, choices=YEAR_CHOICES,default='first')

    payment_status=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Participation(models.Model):
    participant=models.ForeignKey('profile', on_delete=models.SET_NULL, null=True)
    event=models.ForeignKey('Event', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.participant.user.first_name} {self.participant.user.last_name}'
        #return f'{self.participant.user.first_name} {self.participant.user.last_name}'

    class meta:
        ordering=['participant']
    '''
    def display_event_name(self):
        return ', '.join(event.event_name for event in self.event.all())

    def display_event_type(self):
        return ', '.join(event.event_type for event in self.event.all())
    '''
