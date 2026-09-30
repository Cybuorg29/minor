class UserModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length = 200)
    age = models.IntegerField()