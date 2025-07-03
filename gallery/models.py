from django.db import models




class Gallery( models.Model ):
	title = models.CharField( max_length=250, verbose_name='имя фото', blank=True, null=True)
	image = models.ImageField(upload_to='gallery/', verbose_name="Фото")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


	class Meta:
		verbose_name = 'Галерея'
		verbose_name_plural = 'Галерея'
		ordering = ['-created_at']

	def __str__(self):
		return self.title or 'No data'
	
        
	