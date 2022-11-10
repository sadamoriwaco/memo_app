from django.core import validators
from django.db import models
from django.core.validators import MaxLengthValidator, MinValueValidator,MaxValueValidator
from django.core.validators import MinLengthValidator
# from django.core.validators import RegexValidator
import re
from django.core.validators import ValidationError

def number_only(value):
    if(re.match(r'^[0-9]*$',value)==None):
        raise ValidationError('%(value)s in not Number!',params={'value':value},)


# Create your models here.
class Custmer(models.Model):
        # name=models.CharField(max_length=100,validators=[RegexValidator(r'^[a-z]*$')])
        company=models.CharField(max_length=100,validators=[number_only])
        name=models.CharField(max_length=100,validators=[number_only])
        mail=models.EmailField(max_length=200)
        gender=models.BooleanField()
        visitday=models.DateField()
        # name=models.CharField(max_length=100,validators=[MinLengthValidator(10)])
        # mail=models.EmailField(max_length=200,validators=[MinLengthValidator(10)])
        # gender=models.BooleanField()
        # age=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(150)])
        # birthday=models.DateField()

        def __str__(self):
            return '<Custmer:id=' + str(self.id) + ','+\
                self.name + '(' + str(self.company) + ')>'

class Message(models.Model):
    custmer=models.ForeignKey(Custmer, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=300)
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<Message:id=' + str(self.id) + ','+\
            self.title + '(' + str(self.pub_date) + ')>'

    class Meta:
        ordering=('pub_date',)