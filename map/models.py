from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class Article(models.Model):
    title = models.CharField(_('title'), max_length=128)
    announce_text = models.TextField(_('announce'), max_length=512, blank=True, null=True)
    text = models.TextField(_('text'), max_length=4096)
    start_date = models.DateTimeField(_('start at'), blank=True)
    end_date = models.DateTimeField(_('end at'), blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def announce(self):
        return self.announce_text or self.text[:512].rsplit(' ', 1)[0]

    class Meta:
        ordering = ['-start_date']
        verbose_name = _('article')
        verbose_name_plural = _('articles')
