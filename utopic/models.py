from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return self.name

class DirectMessage(models.Model):
    message = models.TextField(max_length=1000)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='sent_messages', null=True)
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='received_messages', null=True)
    sent_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

class Report(models.Model):
    reason = models.TextField(max_length=200)
    text = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    table_name = models.CharField(max_length=30)
    table_pk = models.IntegerField()

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    forum = models.ForeignKey('Forum', on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    name = models.CharField(max_length=50)
    attachments = models.ManyToManyField(Attachment, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class Comment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)



class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class UsersTeam(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Forum(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, unique=True)

class Subforum(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    forum = models.ForeignKey(Forum, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, unique=True)

class Like(models.Model):
    like_type = models.IntegerField(default=1)
    table_name = models.CharField(max_length=16)
    table_pk = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    table_name = models.CharField(max_length=16)
    table_pk = models.IntegerField()