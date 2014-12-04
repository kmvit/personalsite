from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings # New Import
from django.conf.urls.static import static # New Import
from django.core.urlresolvers import reverse
from foundation import views


urlpatterns = [
    # Examples:
    #url(r'^$', 'kmvit.views.home', name='home'),
    
    url(r'^$',  views.index, name='index' ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),



    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
