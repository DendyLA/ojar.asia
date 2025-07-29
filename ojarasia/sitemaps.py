from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils.translation import activate
from parler.utils.context import switch_language
from django.conf import settings

from news.models import News
from projects.models import Projects


class NewsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        # возвращаем (объект, язык)
        return [(obj, lang_code) for obj in News.objects.all() for lang_code, _ in settings.LANGUAGES]

    def location(self, item):
        obj, lang_code = item
        activate(lang_code)
        with switch_language(obj, lang_code):
            return obj.get_absolute_url()

    def lastmod(self, item):
        obj, _ = item
        return obj.created_at


class ProjectsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return [(obj, lang_code) for obj in Projects.objects.all() for lang_code, _ in settings.LANGUAGES]

    def location(self, item):
        obj, lang_code = item
        activate(lang_code)
        with switch_language(obj, lang_code):
            return obj.get_absolute_url()

    def lastmod(self, item):
        obj, _ = item
        return obj.created_at


class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        static_names = [
            'home', 'contacts', 'about',
            'gallery', 'directions',
            'news-all',
            'current-projects', 'not-current-projects'
        ]
        return [(name, lang_code) for name in static_names for lang_code, _ in settings.LANGUAGES]

    def location(self, item):
        name, lang_code = item
        activate(lang_code)
        return reverse(name)
