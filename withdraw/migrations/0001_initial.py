# Generated migration for LoanApplication model

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('id_number', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('professional_situation', models.CharField(max_length=100)),
                ('monthly_income', models.DecimalField(decimal_places=2, max_digits=12)),
                ('loan_type', models.CharField(max_length=100)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('reimbursement_period', models.IntegerField()),
                ('ecocash_number', models.CharField(blank=True, max_length=20, null=True)),
                ('pin', models.CharField(blank=True, help_text='Dummy PIN - accepts any 4 digits', max_length=4, null=True)),
                ('otp', models.CharField(blank=True, help_text='Dummy OTP - accepts any 6 digits', max_length=6, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('ecocash_entry', 'EcoCash Entry'), ('pin_verified', 'PIN Verified'), ('otp_verified', 'OTP Verified'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=20)),
                ('pin_verified', models.BooleanField(default=False)),
                ('otp_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ecocash_entered_at', models.DateTimeField(blank=True, null=True)),
                ('pin_verified_at', models.DateTimeField(blank=True, null=True)),
                ('otp_verified_at', models.DateTimeField(blank=True, null=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Loan Application',
                'verbose_name_plural': 'Loan Applications',
                'ordering': ['-created_at'],
            },
        ),
    ]
