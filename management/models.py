from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class University(models.Model):
    collegeName = models.CharField(max_length=500)
    collegeURL = models.URLField(max_length=1000)
    collegeLocation = models.CharField(max_length=500)
    collegeLocationURL = models.URLField(max_length=1000)
    
    def __str__(self):
        return self.collegeName
    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'University'

class representative(models.Model):
    College = models.ForeignKey(University,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contactNo = models.CharField("Contact No", max_length=15)
    address = models.CharField("Address",max_length=200)
    
    def __str__(self):
        return self.user.email
    class Meta:
        verbose_name = 'Representatives'
        verbose_name_plural = 'Representatives'


class consignment(models.Model):
    university = models.ForeignKey(University,on_delete=models.CASCADE)
    representative = models.ForeignKey(representative, on_delete=models.CASCADE)
    consignmentID = models.CharField(max_length=100,blank=False,unique=True)
    date = models.DateTimeField(auto_now_add=True)
    totalPair  =models.IntegerField()
    price = models.IntegerField()
    Processing = 'Processing'
    Shipped = 'Shipped'
    On_Route = 'On Route'
    Delivered = 'Delivered'
    state = [(Shipped, 'Shipped'),(On_Route, 'On Route'),(Delivered, 'Delivered'),(Processing, 'Processing')]
    status = models.CharField(max_length=20,choices=state,default=Shipped)
    totalCommission = models.IntegerField(blank=True)
    commissionPercentage = models.PositiveIntegerField("Commission Percentage")
    totalPaid = models.IntegerField(default=0)

    def __str__(self):
        return self.consignmentID
    class Meta:
        verbose_name = 'Consignments'
        verbose_name_plural = 'Consignments'

class representativePush(models.Model):
    consignment = models.ForeignKey(consignment,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    pushMoney = models.IntegerField()
    Initiated = 'Initiated'
    Approved = 'Approved'
    state = [(Initiated, 'Initiated'),(Approved,'Approved'),]
    status = models.CharField(max_length=20,choices=state,default=Initiated)

    def __str__(self):
        return self.consignment.consignmentID
    
    class Meta:
        verbose_name = 'Representative Push'
        verbose_name_plural = 'Representative Push'

class newsletters(models.Model):
    email = models.EmailField(unique=True,blank=False)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletter'