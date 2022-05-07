from django.db import models


class Roles(models.Model):
    name = models.CharField(max_length=20)
    features = models.ManyToManyField("userRole.Features", through="userRole.RolesFearutes")


class Features(models.Model):
    name = models.CharField(max_length=20)


class RolesFearutes(models.Model):
    role_id = models.ForeignKey("userRole.Roles", on_delete=models.CASCADE)
    feature_id = models.ForeignKey("userRole.Features", on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    write = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)



class U_Roles(models.Model):
    name = models.CharField(max_length=20)


class U_Features(models.Model):
    name = models.CharField(max_length=20)
    features = models.ManyToManyField("userRole.U_Roles", through="userRole.U_RolesFearutes")


class U_RolesFearutes(models.Model):
    role_id = models.ForeignKey("userRole.U_Roles", on_delete=models.CASCADE)
    feature_id = models.ForeignKey("userRole.U_Features", on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    write = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)