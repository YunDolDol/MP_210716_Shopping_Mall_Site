from django.db import models

# Create your models here.
class Shopping(models.Model) :
    title = models.CharField(max_length=30)
    body = models.TextField()
    image = models.ImageField(upload_to = "shoppingsite/", blank=True, null=True)
    author = models.ForeignKey('account.User', on_delete = models.CASCADE)
    
    def __str__(self) :
        return self.title

