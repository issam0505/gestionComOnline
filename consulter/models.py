from django.db import models
class category(models.Model):
  name=models.CharField(max_length=250,unique=True)
  slug = models.SlugField(max_length=50,unique=True)
   
  def __str__(self):
     return self.name

class produit (models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places= 2)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(category,on_delete=models.SET_NULL,null=True,related_name='consulter')
    image = models.ImageField(upload_to='media\consulter')

    def __str__(self):
      return self.name