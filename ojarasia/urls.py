"""
URL configuration for ojarasia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from about.views import about
from directions.views import directions
from gallery.views import gallery

from django.contrib.sitemaps.views import sitemap
from .sitemaps import NewsSitemap, ProjectsSitemap, StaticViewSitemap


from django.conf import settings

urlpatterns = [
    # Для редиректов и переключения языка
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
	path('', include('home.urls')),
    path('about/', about, name='about'),
    path('directions/', directions, name='directions'),
    path('projects/', include('projects.urls')),
    path('news/', include('news.urls')),
    path('gallery/', gallery, name='gallery')
)

sitemaps = {
    'news': NewsSitemap,
    'projects': ProjectsSitemap,
    'static': StaticViewSitemap,
}

urlpatterns += [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)