# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class JetBookmark(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    user_id = models.BigIntegerField()
    date_add = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jet_bookmark'


class JetPinnedapplication(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_label = models.CharField(max_length=255)
    user_id = models.BigIntegerField()
    date_add = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jet_pinnedapplication'


class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    rut = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pedidos_cliente'


class Comanda(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_mesa = models.BigIntegerField()
    id_usuario = models.BigIntegerField()
    id_cliente = models.BigIntegerField()
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos_comanda'


class ComandaDetalle(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_comanda = models.BigIntegerField()
    id_plato = models.BigIntegerField()
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pedidos_comanda_detalle'


class Ingrediente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    unidad = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pedidos_ingrediente'


class Mesa(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    capacidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pedidos_mesa'


class Modulo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pedidos_modulo'


class Plato(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    tiempo_preparacion_min = models.IntegerField()
    tipo = models.CharField(max_length=30)
    url_img = models.CharField(max_length=80)
    precio = models.BigIntegerField()
    id_ingrediente1 = models.BigIntegerField()
    id_ingrediente2 = models.BigIntegerField()
    id_ingrediente3 = models.BigIntegerField()
    id_ingrediente4 = models.BigIntegerField()
    id_ingrediente5 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pedidos_plato'


class Surcursales(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pedidos_sucursales'


class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    rut = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pedidos_usuario'