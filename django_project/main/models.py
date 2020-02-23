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


class Profile(models.Model):
    # autoincrement and pk field
    id = models.AutoField(primary_key=True, unique=True, null=False)
    total_kill = models.IntegerField(default=0)
    total_death = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return "id: " + self.id + "rank : "+ self.rank


class Bullet(models.Model):
    # autoincrement and pk field
    id = models.AutoField(primary_key=True, unique=True, null=False)
    sniper = models.IntegerField(default=0)
    assault = models.IntegerField(default=0)
    engineer = models.IntegerField(default=0)
    support = models.IntegerField(default=0)


class Event(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    # TODO one to one relation to date collection
    start_time = models.DateTimeField(auto_created=True, auto_now=True)
    end_time = models.DateTimeField(auto_created=True, auto_now=True)

    # TODO array field
    robot_to_user_a = models.Field()
    robot_to_user_b = models.Field()
    team_nations = models.Field()
    is_private = models.BooleanField(default=False)
    # TODO define on_delete
    game_mode = models.OneToOneField('GameMode', on_delete=models.CASCADE)
    result = models.TextField(default="kir")


class Robot(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    name = models.TextField(default="Jia lissa")
    # TODO define relation type
    nation = models.OneToOneField('Nation', on_delete=models.CASCADE)
    weapon_name = models.TextField()
    # these integer fields have a 0 to 10 value
    attack = models.IntegerField()
    armor = models.IntegerField()
    speed = models.IntegerField()
    # not able to implement yet
    accuracy = models.IntegerField()
    rate_of_fire = models.IntegerField()
    max_health = models.IntegerField()
    current_health = models.IntegerField()  # this field's value changes while user is playing the game
    max_ammo = models.IntegerField()
    current_ammo = models.IntegerField()  # this field's value changes while user is playing the game
    max_clip = models.IntegerField()
    current_clip = models.IntegerField()  # this field's value changes while user is playing the game
    # based on images cached on apk file
    image_id = models.IntegerField()


class Nation(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    name = models.TextField(default="Elena Koshka")
    # based on images cached on apk file
    image_id = models.IntegerField()


class Daate(models.Model):
    # autoincrement and pk field
    id = models.AutoField(primary_key=True, unique=True, null=False)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()
    minute = models.IntegerField()


class GameMode(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    name = models.TextField()
    max_users = models.IntegerField()
    max_time = models.IntegerField()
