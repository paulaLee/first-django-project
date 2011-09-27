from django.conf.urls.defaults import patterns, include, url
from contact.views import contact

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
		("^contact/$", contact)
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
