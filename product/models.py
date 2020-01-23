from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=128)
    url = models.TextField()
    pub_date = models.DateTimeField(auto_now = False , auto_now_add = True)
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='icon/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete = models.CASCADE )

    def summary(self):
        return self.body[0:100]
    def pub_date_pretty(self):
        return self.pub_date.strftime("%B %e %Y")
    def __str__(self):
        return self.title