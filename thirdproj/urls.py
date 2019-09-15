from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.contrib import admin

urlpatterns = [
    url(r'^', include('fruits.urls')),
    url(r'^admin/', admin.site.urls),
]



#terns = patterns('',
    # Examples:
    # url(r'^$', 'thirdproj.views.home', name='home'),
    # url(r'^thirdproj/', include('thirdproj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

#
#
#
#
##
#
#
#
#@
#
#
#
#
#
#
#
#

