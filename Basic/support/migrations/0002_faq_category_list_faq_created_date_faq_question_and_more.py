# Generated by Django 4.0.4 on 2022-04-16 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='category_list',
            field=models.CharField(choices=[('GE', '일반'), ('AC', '계정'), ('ET', '기타')], default='GE', max_length=2, verbose_name='카테고리'),
        ),
        migrations.AddField(
            model_name='faq',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='생성일시'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question',
            field=models.TextField(default='GE', verbose_name='질문'),
        ),
        migrations.AddField(
            model_name='faq',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='최종 수정일'),
        ),
        migrations.AddField(
            model_name='faq',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='생성자'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(default='GE', verbose_name='답변'),
        ),
    ]
