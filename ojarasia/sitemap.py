from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils.translation import activate
from parler.utils.context import switch_language
from django.conf import settings

from news.models import News
from projects.models import Projects


class MultiLangSitemapMixin:
    def get_urls(self, site=None, **kwargs):
        urls = []
        for lang_code, _ in settings.LANGUAGES:
            activate(lang_code)
            for item in self.items():
                with switch_language(item, lang_code):
                    url_info = {
                        'location': f'/{lang_code}{item.get_absolute_url()}',
                        'lastmod': self.lastmod(item) if hasattr(self, 'lastmod') else None,
                        'changefreq': self.changefreq,
                        'priority': self.priority,
                    }
                    urls.append(url_info)
        return urls


class NewsSitemap(MultiLangSitemapMixin, Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.created_at


class ProjectsSitemap(MultiLangSitemapMixin, Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Projects.objects.all()

    def lastmod(self, obj):
        return obj.created_at


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return [
            'home', 'contacts', 'about',
            'gallery', 'directions',
            'news-all',
            'current-projects', 'not-current-projects'
        ]

    def location(self, item):
        return reverse(item)

    def get_urls(self, site=None, **kwargs):
        urls = []
        for lang_code, _ in settings.LANGUAGES:
            activate(lang_code)
            for item in self.items():
                url = reverse(item)
                urls.append({
                    'location': f'/{lang_code}{url}',
                    'changefreq': self.changefreq,
                    'priority': self.priority,
                })
        return urls
