from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField ,EmailField, DateField, IntegerField,TextField
from django.db.models.fields.related import ForeignKey
from django.urls import reverse




# from MyWeb.views import Consumer





class consumer( models.Model):

    consumer_id = models.AutoField(primary_key=True)
    consumer_email = models.EmailField(max_length=255 ,unique=True,null=True)
    consumer_password = models.CharField(max_length=255,null=True)
    consumer_fname = models.CharField(max_length=255,null=True)
    consumer_lname = models.CharField(max_length=255,null=True)
    consumer_dob = models.DateField( null= True)
    consumer_gender = models.CharField(max_length=10,null=True)
    consumer_province = models.CharField(max_length=255,null=True)
    consumer_address = models.TextField(null=True)
    consumer_postal = models.CharField(max_length=10,null=True)
    consumer_phone = models.CharField(max_length=255,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
    def __str__(self):
        return str(self.consumer_id)

class enturpreneur(models.Model):
    enturpreneur_id = models.AutoField(primary_key=True)
    enturpreneur_email = models.CharField(max_length=255 ,null=True)
    enturpreneur_password = models.CharField(max_length=255,null=True)
    bissiness_name = models.CharField(max_length=255,null=True)
    enturpreneur_fname= models.CharField(max_length=255,null=True)
    enturpreneur_lname= models.CharField(max_length=255,null=True)
    enturpreneur_idcard = models.CharField(max_length=13,null=True)
    enturpreneur_province =models.CharField(max_length=255,null=True)
    enturpreneur_address=models.TextField(null =True) 
    enturpreneur_postal = models.CharField(max_length=10,null=True)
    enturpreneur_phone = models.CharField(max_length=255,null=True)
    juristic_code=models.CharField(max_length=13)
    juristic_document=models.TextField(null =True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
    def __str__(self):
        return str(self.enturpreneur_id)



class category (models.Model):
    cetegory_name = models.CharField (max_length=255,null=True)
    cetegory_slug = models.SlugField(max_length=255 , null=True)
    def __str__(self):
        return str(self.cetegory_name)
    


    def get_url(self):
        return reverse('product_by_category',args=[self.cetegory_slug ])

    




class type (models.Model):
    type_name = models.CharField (max_length=255,null=True)
    type_slug = models.SlugField(max_length=255 , null=True)
    def __str__(self):
        return str(self.type_name)
    def get_url2(self):
        return reverse('product_by_type',args=[self.type_slug ])


class product_and_service (models.Model):
    product_and_service_id = models.AutoField(primary_key=True)
    product_and_service_name= models.CharField (max_length=255)
    product_and_service_deail= models.TextField (null = True)
    product_and_service_image=models.ImageField (upload_to = 'product' ,null = True)
    product_and_service_amount = models.IntegerField (null = True)
    product_and_service_status= models.BooleanField (default= True,null=True)
    product_and_service_create = models.DateTimeField(auto_now_add= True)
    product_and_service_update =models.DateTimeField(auto_now= True)
    product_and_service_slug = models.SlugField(max_length=255 , null=True)

    type_name = ForeignKey(type, on_delete=models.CASCADE , null=True)
    cetegory = ForeignKey(category, on_delete=models.CASCADE , null=True)
    enturpreneur = models.ForeignKey(enturpreneur, on_delete=models.CASCADE , null=True)
    def __str__(self):
        return str(self.product_and_service_name)
    
    def get_url(self):
        return reverse('product_detail',args=[self.cetegory.cetegory_slug ,self.product_and_service_slug])

    


class trial (models.Model):
    trial_id = models.AutoField(primary_key=True)
    trial_amoun = models.IntegerField(null=True)
    ##trial_create_time  = models.CharField(max_length=255,null=True)
    ##trial_update_time  = models.CharField(max_length=255,null=True)
    consumer  = models.ForeignKey(consumer, on_delete=models.CASCADE , null=True)
    product  = models.ForeignKey(product_and_service, on_delete=models.CASCADE ,null=True)
    def __str__(self):
            return str(self.trial_id)

class question(models.Model):
   question_id = models.AutoField(primary_key=True)
   question_single = models.TextField(null =True)
   answer_number= models.IntegerField(null =True) 
   question_multiple = models.TextField(null =True) 
   question_text = models.TextField(null =True)
   product_and_service  = models.ForeignKey(product_and_service, on_delete=models.CASCADE)
   
   def __str__(self):
        return str(self.question_id)

class answer(models.Model):
   answer_id = models.AutoField(primary_key=True)
   answer_1 = models.TextField(null =True)
   answer_2 = models.TextField(null =True)
   answer_3 = models.TextField(null =True)
   answer_4 = models.TextField(null =True)
   answer_5 = models.TextField(null =True)
   answer_6 = models.TextField(null =True)
   answer_7 = models.TextField(null =True)



   '''answer_single = models.TextField(null =True) 
   answer_number= models.IntegerField(null =True) 
   answer_multiple = models.TextField(null =True) 
   answer_text = models.TextField(null =True)'''
   product_and_service  = models.ForeignKey(product_and_service, on_delete=models.CASCADE,null =True)
   def __str__(self):
        return str(self.answer_id)



class survey (models.Model):
   survey_id = models.AutoField(primary_key=True)
   survey_question = models.CharField (max_length=255,null=True)
   survey_answer = models.CharField (max_length=255,null=True)
   product_and_service =models.ForeignKey(product_and_service, on_delete=models.CASCADE)
   answer_id  = models.ForeignKey(answer, on_delete=models.CASCADE)
   question  = models.ForeignKey(question, on_delete=models.CASCADE)
   def __str__(self):
     return str(self.survey_id)

class survey_has_product (models.Model):
    survey_has_product = models.AutoField(primary_key=True)
    survey_id  = models.ForeignKey(survey, on_delete=models.CASCADE)
    product  = models.ForeignKey(product_and_service, on_delete=models.CASCADE)
    def __str__(self):
       return str(self.survey_has_product_id)

class trial_has_product (models.Model):
    trial_has_product = models.AutoField(primary_key=True)
    trial_id  = models.ForeignKey(survey, on_delete=models.CASCADE)
    product  = models.ForeignKey(product_and_service, on_delete=models.CASCADE)
    def __str__(self):
       return str(self.trial_has_product_id)



class trial_has_survey (models.Model):
    trial_has_survey = models.AutoField(primary_key=True)
    trial_amoun = models.IntegerField(null=True)
    trial_id  = models.ForeignKey(trial, on_delete=models.CASCADE)
    survey_has_product  = models.ForeignKey(survey_has_product , on_delete=models.CASCADE)
    def __str__(self):
       return str(self.trial_has_survey_id)

