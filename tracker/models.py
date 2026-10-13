from django.db import models
from django.contrib.auth.models import User 



class UserProfileModel(models.Model):

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile', null=True)

    name = models.CharField(max_length=200, blank=True, null=True)
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(choices=GENDER, max_length=30, null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    image = models.ImageField(upload_to='media/profile_img', null=True)
    bmr = models.FloatField(null=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):

        if self.gender == 'male':

            self.bmr = 66.47 + (13.75 * self.weight) + (5.003 * self.height) - (6.755 * self.age)

        else:

            self.bmr = 655.1 + (9.563 * self.weight) + (1.850 * self.height) - (4.676 * self.age)

        super().save(*args, **kwargs)    



class ConsumedCalorieModel(models.Model):    

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consumed_calorie', null=True)

    item_name = models.CharField(max_length=100, null=True)
    consumed_calorie = models.FloatField(null=True)

    def __str__(self):
        return f'{self.user.username}-{self.item_name}'