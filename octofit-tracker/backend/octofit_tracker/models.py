from djongo import modelsfrom djongo import models
































        app_label = 'octofit_tracker'    class Meta:    difficulty = models.CharField(max_length=50)    name = models.CharField(max_length=100)class Workout(models.Model):        app_label = 'octofit_tracker'    class Meta:    points = models.IntegerField()    team = models.CharField(max_length=50)class Leaderboard(models.Model):        app_label = 'octofit_tracker'    class Meta:    duration = models.IntegerField()    type = models.CharField(max_length=50)    user = models.CharField(max_length=100)class Activity(models.Model):        app_label = 'octofit_tracker'    class Meta:    name = models.CharField(max_length=50, unique=True)class Team(models.Model):        app_label = 'octofit_tracker'    class Meta:    team = models.CharField(max_length=50)    name = models.CharField(max_length=100)    email = models.EmailField(unique=True)class User(models.Model):
class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.user} - {self.type}"

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team}: {self.points}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    def __str__(self):
        return self.name
