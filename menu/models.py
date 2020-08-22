from django.db import models

class Menu(models.Model):
    category     = models.CharField(max_length = 50)
    name         = models.CharField(max_length = 100)
    contain_meat = models.BooleanField()
    seafood      = models.BooleanField()
    hot          = models.BooleanField()
    noodle       = models.BooleanField()
    soup         = models.BooleanField()
    greasy       = models.BooleanField()
    cool         = models.BooleanField()

    class Meta:
        db_table = 'menus'