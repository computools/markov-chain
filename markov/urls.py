from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static


from markov_alg.views import WordView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', WordView.as_view(), name='word')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

