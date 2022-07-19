from django.db import models
from django.core.validators import RegexValidator

class user(models.Model):
    name = models.CharField(max_length=64, verbose_name='User name', null=False)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=16, null=False)
    role = models.CharField(max_length=64)


class partner(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='Partners name', null=False)
    last_name = models.CharField(max_length=64, verbose_name='Partners last name', null=False)
    phone = models.CharField(max_length=13, verbose_name='phone number')
    description = models.CharField(max_length=264, verbose_name='Description for org', null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class organizatsion(models.Model):
    name = models.CharField(max_length=64, verbose_name='Organizatsion name', null=False, unique=True)
    partner = models.ForeignKey(partner, verbose_name='Director', on_delete=models.CASCADE)
    description = models.CharField(max_length=264, verbose_name='Description for org', null=True)
    phone = models.CharField(max_length=13, verbose_name='phone number')
    logo = models.ImageField(upload_to='org_logo/', blank=True, null=True)

    def __str__(self):
        return self.name


class platform_user(models.Model):
    organization = models.ForeignKey(organizatsion, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=64, verbose_name='co-worker name')
    phone = models.CharField(max_length=13, verbose_name='phone number')
    email = models.EmailField()
    password = models.CharField(max_length=16, unique=True)
    ENUM = (
        (1, 'director'),
        (2, 'manager'),
        (3, 'waiter'),
    )
    role = models.PositiveSmallIntegerField(verbose_name='wat role', choices=ENUM)

    def __str__(self) -> str:
        return f'{self.organization}, {self.full_name}'


class room(models.Model):
    name = models.CharField(max_length=64, verbose_name='Room name', null=False, unique=True)
    oraganizatsion_id = models.ForeignKey(organizatsion, verbose_name='Which organizatsion', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'


class organization_table(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name='Table numbers', unique=True)
    room_id = models.ForeignKey(room, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.room_id.oraganizatsion_id.name}: {self.room_id.name} table {self.number}'






