from django.db import models


class Mode(models.Model):  # mode is the same GameMode
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
    # based on images cached on apk file or static files on the host
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
    nation = models.ForeignKey(Nation, models.DO_NOTHING)

    class Meta:
        db_table = 'robot'

    def __str__(self):
        return "{0} {1}".format(self.name, self.nation)




class Event(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    # TODO this should be a model method that provides a special date pattern
    start_time = models.TextField(default="00:00:00 00/00/00")
    end_time = models.TextField(default="00:00:00 00/00/00")
    created_at = models.DateField(blank=True, null=True, auto_created=True, auto_now=True)
    # a contract sentence with Mason Fakhraee
    result = models.TextField(default="khoy sokhari ba ablimu")
    # this is for next features
    is_private = models.IntegerField(default=False)
    # game mode defines how much time and robots should've
    mode = models.ForeignKey('Mode', models.DO_NOTHING)
    team_nations = models.ManyToManyField(Nation)
    # a way to separate team nations if needed to be separated instead ManyToManyField
    # team_nations_a = models.ForeignKey('Nation', models.DO_NOTHING)
    # team_nations_b = models.ForeignKey('Nation', models.DO_NOTHING)
    # related robots to each team, first five to team1, second five to team2
    robot_to_users = models.ManyToManyField(Robot)

    class Meta:
        db_table = 'event'

    def __str__(self):
        return "{0} {1}".format(self.mode, self.created_at)


# this should be a views.py method :|
# class Daate(models.Model):
#     # autoincrement and pk field
#     id = models.AutoField(primary_key=True, unique=True, null=False)
#     year = models.IntegerField()
#     month = models.IntegerField()
#     day = models.IntegerField()
#     hour = models.IntegerField()
#     minute = models.IntegerField()
