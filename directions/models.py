from django.db import models
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields

class Companies(TranslatableModel):
	translations = TranslatedFields(
		title = models.CharField(max_length=350, verbose_name='Имя компании', blank=True,null=True),
		text = RichTextField(verbose_name='Текст компании', blank=True, null=True)
	)
	
	image = models.ImageField( upload_to='companies/', verbose_name='Лого компании')
	link = models.URLField(verbose_name='Ссылка на компанию', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

	class Meta:
		verbose_name = 'Компания'
		verbose_name_plural = 'Компании'
		ordering = ['-created_at']

	def __str__(self):
		return self.title or 'No data'
