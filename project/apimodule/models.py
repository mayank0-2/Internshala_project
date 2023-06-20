from django.db import models

''' 

Please develop a simple CRM system based on Django and MySQL, taking inspiration from Zoho CRM. Focus on understanding the relationship & dynamic system in Zoho CRM to replicate its functionality.

Assignment Details:

Build a CRUD system with basic authentication, including teacher username, password, and role. Teachers can have different roles, such as senior teachers, which allows them to edit or delete users in the system. Establish a relationship between users and roles.

Implement a feature similar to Zoho CRM that allows for creating dynamic fields (refer to https://youtu.be/1L8uuBYWx_c?t=21). This should enable the creation of custom labels, boxes, and text fields. Ensure that only the admin (senior teacher) can create these fields and that they are visible to regular users once added. As a demo, create a "teacher department" field that can be linked with teacher details dynamically.

Adhere to the following design patterns in your code:
a. SOLID principles
b. Strategy pattern
c. Dependency Injection pattern (if possible)
d. MVC pattern (already followed by Django)

The system should be based on a REST API built with Django. You may use any front-end technology you prefer.

Upon completion, please send a video demonstrating the assignment's functionality & the GitHub link to your code'''


# Create your models here.
class apiModel(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
