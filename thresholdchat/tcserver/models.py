from datetime import timedelta

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    passHash = models.BinaryField
    passSalt = models.BinaryField
    pubKey = models.BinaryField

    def __str__(self):
        return self.username


class Chat(models.Model):
    name = models.CharField(max_length=256)
    threshold = models.PositiveIntegerField
    timeout = models.DurationField(default=timedelta(minutes=30))
    chatHist = models.BinaryField

    def __str__(self):
        return self.name


class Invite(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.chat.name


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField

    def __str__(self):
        return self.chat.name


class Authorization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    endOfAuthTime = models.DurationField

    def __str__(self):
        return self.user.name
