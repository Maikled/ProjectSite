from django.db import models


class Authentication(models.Model):
    login = models.CharField('login', max_length=50)
    password = models.CharField('password', max_length=50)
    type = models.CharField('type', max_length=8)

    def __str__(self):
        return ' '.join([self.login, ' ', self.type])


class Admin(models.Model):
    firstname = models.CharField('firstname', max_length=50)
    lastname = models.CharField('lastname', max_length=50)
    patronymic = models.CharField('patronymic', max_length=50)
    dateOfBirth = models.DateField('dateOfBirth')
    gender = models.CharField('gender', max_length=16)
    position = models.CharField('position', max_length=100, null=True)
    aut = models.ForeignKey('Authentication', on_delete=models.PROTECT, null=True)
    link_to_photo = models.TextField('link_to_photo', null=True, blank=True)

    def __str__(self):
        return ' '.join([self.firstname, ' ', self.lastname])


class Manager(models.Model):
    firstname = models.CharField('firstname', max_length=50)
    lastname = models.CharField('lastname', max_length=50)
    patronymic = models.CharField('patronymic', max_length=50)
    dateOfBirth = models.DateField('dateOfBirth')
    gender = models.CharField('gender', max_length=16)
    position = models.CharField('position', max_length=100, null=True)
    aut = models.ForeignKey('Authentication', on_delete=models.PROTECT, null=True)
    link_to_photo = models.TextField('link_to_photo', null=True, blank=True)

    def __str__(self):
        return ' '.join([self.firstname, ' ', self.lastname])


class Employee(models.Model):
    firstname = models.CharField('firstname', max_length=50)
    lastname = models.CharField('lastname', max_length=50)
    patronymic = models.CharField('patronymic', max_length=50)
    dateOfBirth = models.DateField('dateOfBirth')
    gender = models.CharField('gender', max_length=16)
    position = models.CharField('position', max_length=100)
    level = models.IntegerField('level', null=True)
    idmanager = models.ForeignKey('Manager', on_delete=models.PROTECT, null=True)
    aut = models.ForeignKey('Authentication', on_delete=models.PROTECT, null=True)
    link_to_photo = models.TextField('link_to_photo', null=True, blank=True)

    def __str__(self):
        return ' '.join([self.firstname, ' ', self.lastname, ' - ', self.position])