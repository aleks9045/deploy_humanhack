from django.db import models

# Create your models here.
class Math_theory(models.Model):
    number_theory = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    condition = models.TextField()

    def __str__(self):
        return self.content


class Math_task(models.Model):
    number_task = models.IntegerField()
    condition = models.TextField()
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.condition



class Animals_theory(models.Model):
    number_theory = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    condition = models.TextField()

    def __str__(self):
        return self.content


class Animals_task(models.Model):
    number_task = models.IntegerField()
    text = models.TextField()
    condition = models.TextField()
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.condition


class Read_theory(models.Model):
    number_theory = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    condition = models.TextField()

    def __str__(self):
        return self.content


class Read_task(models.Model):
    number_task = models.IntegerField()
    text = models.TextField()
    condition = models.TextField()
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.condition


class English_theory(models.Model):
    number_theory = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    condition = models.TextField()

    def __str__(self):
        return self.content


class English_task(models.Model):
    number_task = models.IntegerField()
    text = models.TextField()
    condition = models.TextField()
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.condition
