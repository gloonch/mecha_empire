from django.db import models


class Event(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    # TODO this should be a model method that provides a special date pattern
    start_time = models.TextField(default="00:00:00 00/00/00")
    end_time = models.TextField(default="00:00:00 00/00/00")
    is_private = models.IntegerField(default=False)
    result = models.TextField(default="kir sokhari ba ablimu")
    mode = models.ForeignKey('Mode', models.DO_NOTHING)
    # TODO a way to separate team nations (if manytomany will work , this separation will be not necessary)
    # team_nations_a = models.ForeignKey('Nation', models.DO_NOTHING)
    # team_nations_b = models.ForeignKey('Nation', models.DO_NOTHING)
    # TODO could not implement these two
    # robot_to_user_a = models.IntegerField()
    # robot_to_user_b = models.IntegerField()

    class Meta:
        db_table = 'event'

    def __str__(self):
        return self.start_time


class Mode(models.Model): # mode is the same GameMode
    id = models.AutoField(primary_key=True, unique=True, null=False)
    name = models.TextField(null=False)
    max_users = models.IntegerField(default=10)
    max_time = models.IntegerField(default=10)

    class Meta:
        db_table = 'mode'

    def __str__(self):
        return self.name


class Nation(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    name = models.TextField(default="Red Army")
    # based on images cached on apk file
    image_id = models.IntegerField(default=1)

    class Meta:
        db_table = 'nation'

    def __str__(self):
        return self.name


class Robot(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    name = models.TextField(default="Jia lissa")
    weapon_name = models.TextField()
    # these integer fields have a 0 to 10 value
    attack = models.IntegerField(null=True)
    armor = models.IntegerField(null=True)
    speed = models.IntegerField(null=True)
    # not able to implement yet
    accuracy = models.IntegerField(null=True)
    rate_of_fire = models.IntegerField(null=True)
    max_health = models.IntegerField(null=True)
    current_health = models.IntegerField(null=True)  # this field's value changes while user is playing the game
    max_ammo = models.IntegerField(null=True)
    current_ammo = models.IntegerField(null=True)  # this field's value changes while user is playing the game
    max_clip = models.IntegerField(null=True)
    current_clip = models.IntegerField(null=True)  # this field's value changes while user is playing the game
    # based on images cached on apk file
    image_id = models.IntegerField(null=True)
    # TODO check db_column if it's nation_id or not
    nation = models.ForeignKey(Nation, models.DO_NOTHING)

    class Meta:
        db_table = 'robot'

    def __str__(self):
        return self.name


# this should be a model method :|
# class Daate(models.Model):
#     # autoincrement and pk field
#     id = models.AutoField(primary_key=True, unique=True, null=False)
#     year = models.IntegerField()
#     month = models.IntegerField()
#     day = models.IntegerField()
#     hour = models.IntegerField()
#     minute = models.IntegerField()
