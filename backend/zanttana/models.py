from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    home_town = models.CharField(max_length=30, blank=True)
    current_loc = models.CharField(max_length=30, blank=True)
    join_date = models.DateField(blank=True)
    invited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='invited_by')

    def __str__(self):
        return self.user.name

class Zantta(models.Model):
    zantta_name = models.CharField(max_length=140, blank=False, null=False,)
    description = models.TextField()
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    members = models.ManyToManyField(Profile, related_name='zantta_members', blank=True)


    def __str__(self):
        return self.zantta_name


class Lodging(models.Model):
    reserver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lodge_reserve')
    lodge_name = models.CharField(max_length=140, blank=False, null=False,)
    lodge_address = models.TextField()
    arrive_date = models.DateField(blank=False, null=False)
    leave_date = models.DateField(blank=False, null=False)
    members_booked = models.ManyToManyField(User, related_name='lodge_members_booked',  blank=True)


    def __str__(self):
        return  f'lodiging at {self.lodge_name} from {self.arrive_date} to {self.leave_date}'


class Logistic(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logistics_creator')
    zantta = models.ForeignKey(Zantta,on_delete=models.CASCADE, related_name='logistic_zanta' )
    method = models.CharField(max_length=10)
    depart_loc = models.CharField(max_length=140)
    arrive_loc = models.CharField(max_length=140)
    depart_time = models.DateField(blank=False, null=False)
    arrive_time = models.DateField(blank=False, null=False)
    members_booked = models.ManyToManyField(User, related_name='logistic_members_booked',  blank=True)


    def __str__(self):
        return f'{self.method} from {self.depart_loc} on {self.depart_time} to {self.arrive_loc} on {self.arrive_time}'


class Msg(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='sender')
    msg = models.CharField(max_length=250, null=False, blank=False)
    Zantta = models.ForeignKey(Zantta, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return f'{self.sender},  {self.msg},  on {self.created_at}'
