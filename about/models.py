from django.db import models

from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields


class AboutMain(TranslatableModel):
	translations = TranslatedFields(
		title =  models.CharField(max_length=250, verbose_name="Название", blank=True, null=True),
		text = models.TextField(verbose_name='Текст', blank=True, null=True)
	)
	
	video = models.FileField(upload_to="videosAbout/",verbose_name='Видео',  blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


	class Meta:
		verbose_name = 'О нас видео на главной'
		verbose_name_plural = 'О нас видео на главной'
		ordering = ['-created_at']
		
	def __str__(self):
		return self.safe_translation_getter('title', any_language=True) or 'Без названия'
	

class Info(TranslatableModel):
	translations = TranslatedFields(
		category = models.CharField(max_length=250, verbose_name="Название", blank=True, null=True)
	)

	number = models.CharField(max_length=250, verbose_name="число", blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


	class Meta:
		verbose_name = 'О нас статистика'
		verbose_name_plural = 'Статистики'
		ordering = ['-created_at']

	def __str__(self):
		return self.safe_translation_getter('category', any_language=True) or 'Без названия'
	

class Comment(TranslatableModel):
	translations = TranslatedFields(
		author = models.CharField(max_length=250, verbose_name="Автор", blank=True, null=True),
		position = models.CharField(max_length=250, verbose_name="Должность", blank=True, null=True),
		text = RichTextField(verbose_name='Текст', blank=True, null=True)
	)
	
	image = models.ImageField(upload_to='comment/', verbose_name='Фото')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


	class Meta:
		verbose_name = 'Цитата'
		verbose_name_plural = 'Цитаты'
		ordering = ['-created_at']
		
	def __str__(self):
		return self.safe_translation_getter('position', any_language=True) or 'Без названия'