from django.db import models


# Create your models here.
# class User(models.Model):
#     # autoincrement and pk field
#     id = models.AutoField(primary_key=True, unique=True, null=False)
#     # nickname and phone_number required for first time creating
#     nickname = models.TextField(default="guest", null=False)
#     phone_number = models.TextField(default="000000000", unique=True, null=False)
#     # token is made when nick_name and phone_number
#     token = models.TextField(unique=True, null=True, default="")
#     created_at = models.TimeField(auto_created=True, auto_now=True)
#     # not working for now (sms.ir)
#     last_code_send = models.IntegerField(default=0, null=True)
#     # default profile photo
#     avatar_url = models.TextField(default="", null=True)
#     # has a oneToOne rel with wallet collection
#     wallet = models.OneToOneField('Wallet', on_delete=models.CASCADE, null=True)
#     # has a oneToOne rel with profile collections
#     account = models.OneToOneField('Account', on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return self.nickname
#
#
# class Wallet(models.Model):
#     # autoincrement and pk field
#     id = models.AutoField(primary_key=True, unique=True, null=False)
#     # not sure about these dataTypes
#     coin = models.IntegerField(default=0)
#     extra_health = models.IntegerField(default=0)
#     # maybe a list field
#     special_attacks = models.IntegerField(default=0)
#     # has a oneToOne rel to bullet collection
#     bullet = models.OneToOneField('Bullet', on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return "wallet no. " + str(self.id)
#
#
# class Account(models.Model):  # account is profile
#     # autoincrement and pk field
#     id = models.AutoField(primary_key=True, unique=True, null=False)
#     total_kill = models.IntegerField(default=0)
#     total_death = models.IntegerField(default=0)
#     score = models.IntegerField(default=0)
#     rank = models.IntegerField(default=0)
#
#
# class Bullet(models.Model):
#     # autoincrement and pk field
#     id = models.AutoField(primary_key=True, unique=True, null=False)
#     sniper = models.IntegerField(default=0)
#     assault = models.IntegerField(default=0)
#     engineer = models.IntegerField(default=0)
#     support = models.IntegerField(default=0)


class Profile(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    total_kill = models.IntegerField(default=0)
    total_death = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    class Meta:
        db_table = 'profile'


class Wallet(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    # not sure about these dataTypes
    coin = models.IntegerField(default=0)
    extra_health = models.IntegerField(default=0)
    # maybe a list field
    special_attacks = models.IntegerField(default=0)
    # has a oneToOne rel to bullet collection
    bullet = models.ForeignKey('Bullet', models.DO_NOTHING)

    class Meta:
        db_table = 'wallet'


class Bullet(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    sniper = models.IntegerField(default=0)
    assualt = models.IntegerField(default=0)
    engineer = models.IntegerField(default=0)
    support = models.IntegerField(default=0)

    class Meta:
        db_table = 'bullet'

class User(models.Model):
    # autoincrement and pk field
    id = models.AutoField(primary_key=True, unique=True, null=False)
    # nickname and phone_number required for first time creating
    nickname = models.TextField(default="guest", null=False)
    phone_number = models.TextField(default="000000000", unique=True, null=False, max_length=10)
    # token is made when nick_name and phone_number
    token = models.TextField(unique=True, null=True, default="")
    created_at = models.DateField(blank=True, null=True, auto_created=True, auto_now=True)
    # not working for now (sms.ir)
    last_code_send = models.IntegerField(blank=True, null=True, default=0)
    # default profile photo
    avatar_url = models.TextField(blank=True, null=True)
    # has a oneToOne rel with wallet collection
    wallet = models.ForeignKey(Wallet, models.DO_NOTHING, db_column='wallet_id')
    profile = models.ForeignKey(Profile, models.DO_NOTHING, db_column='profile_id')

    class Meta:
        db_table = 'user'