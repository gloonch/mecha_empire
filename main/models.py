from django.db import models


# Create your models here.
class User(models.Model):
    # autoincrement and pk field
    id = models.AutoField(primary_key=True, unique=True, null=False)
    # nickname and phone_number required for first time creating
    nickname = models.TextField(default="guest", null=False)
    phone_number = models.TextField(default="000000000", unique=True, null=False)
    # token is made when nick_name and phone_number
    token = models.TextField(unique=True, null=True, default="")
    created_at = models.TimeField(auto_created=True, auto_now=True)
    # not working for now (sms.ir)
    last_code_send = models.IntegerField(default=0, null=True)
    # default profile photo
    avatar_url = models.TextField(default="", null=True)

    # TODO profile_id not null error
    # has a oneToOne rel with wallet collection
    # wallet = models.OneToOneField('Wallet', on_delete=models.CASCADE)

    # has a oneToOne rel with profile collections
    # profile = models.OneToOneField('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname


class Wallet(models.Model):
    # autoincrement and pk field
    id = models.AutoField(primary_key=True, unique=True, null=False)
    # not sure about these dataTypes
    coin = models.IntegerField(default=0)
    extra_health = models.IntegerField(default=0)
    # maybe a list field
    special_attacks = models.IntegerField(default=0)
    # has a oneToOne rel to bullet collection
    bullet = models.OneToOneField(to='Bullet', on_delete=models.CASCADE)


class Account(models.Model):
    # autoincrement and pk field
    id = models.AutoField(primary_key=True, unique=True, null=False)
    total_kill = models.IntegerField(default=0)
    total_death = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)



class Bullet(models.Model):
    # autoincrement and pk field
    id = models.AutoField(primary_key=True, unique=True, null=False)
    sniper = models.IntegerField(default=0)
    assault = models.IntegerField(default=0)
    engineer = models.IntegerField(default=0)
    support = models.IntegerField(default=0)

