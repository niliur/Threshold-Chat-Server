from datetime import timedelta

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    # passHash = models.BinaryField
    # passSalt = models.BinaryField

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


# Model to define many-to-many relationship between chats and users
class ChatMembership(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.chat.name


class AccessRequest(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="access_sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="access_receiver")
    reason = models.CharField(max_length=512)

    def __str__(self):
        return self.chat.name


class AccessResponse(models.Model):
    request = models.ForeignKey(AccessRequest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.BooleanField(default=False)

    def __str__(self):
        return self.request.chat.name
