
from django.contrib import admin
from django.urls import path,include
admin.site.site_header="Letscode Admin"
admin.site.site_title="Letscode Admin Panel"
admin.site.index_title="Welcome to Letscode Admin Panel"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    
]
