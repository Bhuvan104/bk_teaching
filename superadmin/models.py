from django.db import models
from django.contrib.auth.models import User,AbstractUser

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField()
    
    
    def __str__(self):
        custom_users = UserProfile.objects.filter(role=2)
        print([student.user.username for student in custom_users])
        return ', '.join([student.user.username for student in custom_users])
    
    
    
    
    

class Category(models.Model):
    name = models.CharField(max_length=250,blank=False)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    

class CourseDetails(models.Model):
      category_id = models.ForeignKey(Category,on_delete = models.DO_NOTHING)
      name        = models.CharField(max_length=250,blank=False)
      type        = models.CharField(max_length=250,choices=[("Audio","Audio"),("Video","Video"),("Document",'Document')],blank=False)
      price       = models.IntegerField()
      content     = models.TextField()
      how_to_use  = models.TextField()
      description = models.TextField()
      file_content = models.FileField(upload_to='course')
      status       = models.BooleanField(default=True)
      
      def __str__(self):
        return self.name
      

class DaysAccess(models.Model):
    days = models.IntegerField(blank=False)
    status = models.BooleanField(default=True)  
    
    
class Payment(models.Model):
     student_id = models.ForeignKey(UserProfile,on_delete = models.DO_NOTHING)
     course_id  = models.ForeignKey(CourseDetails,on_delete = models.DO_NOTHING)
     price      = models.IntegerField()
     payment_ref = models.CharField(max_length=250)
     payment_date = models.DateTimeField()
     payment_status = models.BooleanField()
     
      

