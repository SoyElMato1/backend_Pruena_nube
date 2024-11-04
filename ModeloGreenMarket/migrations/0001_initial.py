# Generated by Django 5.1.1 on 2024-10-11 17:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1, null=True)),
                ('correo_electronico', models.EmailField(max_length=50, null=True)),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('direccion', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id_metodo_pago', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_metodo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('correo_electronico', models.EmailField(max_length=50)),
                ('contrasena', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('verificacion', models.BooleanField(default=False)),
                ('recompensa', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CarritoM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('actualizado_en', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ModeloGreenMarket.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.JSONField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pagado', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModeloGreenMarket.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('imagen_producto', models.CharField(max_length=100)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModeloGreenMarket.categoria')),
                ('id_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModeloGreenMarket.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ModeloGreenMarket.carritom')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModeloGreenMarket.producto')),
            ],
        ),
        migrations.CreateModel(
            name='transaccion',
            fields=[
                ('id_transaccion', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField()),
                ('fecha', models.DateField()),
                ('id_metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModeloGreenMarket.metodopago')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateField()),
                ('monto_total', models.IntegerField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModeloGreenMarket.cliente')),
                ('metodo_pago', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ModeloGreenMarket.metodopago')),
                ('transaccion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ModeloGreenMarket.transaccion')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('correo_user', models.EmailField(max_length=100, unique=True, verbose_name='Correo')),
                ('rut', models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='RUT')),
                ('nom_user', models.CharField(blank=True, default='(Sin Nombre)', max_length=20, null=True, verbose_name='Nombre')),
                ('ap_user', models.CharField(blank=True, default='(Sin Apellido)', max_length=20, null=True, verbose_name='Apellido')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('rol', models.CharField(choices=[('admin', 'Administrador'), ('cliente', 'Cliente'), ('proveedor', 'Proveedor')], max_length=30)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CalificacionProveedor',
            fields=[
                ('id_calificacionProve', models.AutoField(primary_key=True, serialize=False)),
                ('puntuacion', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('comentario', models.TextField(blank=True)),
                ('id_proveedor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='calificacion', to='ModeloGreenMarket.proveedor')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificaciones_proveedor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CalificacionProducto',
            fields=[
                ('id_calificacionProduc', models.AutoField(primary_key=True, serialize=False)),
                ('puntuacion', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('comentario', models.TextField(blank=True)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificaciones', to='ModeloGreenMarket.producto')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificaciones_productos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
