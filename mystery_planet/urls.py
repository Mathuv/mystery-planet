from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .users.views import UserViewSet, UserCreateViewSet
from .persons.views import CompanyVieSet, PersonViewSet, PersonFavouriteFoodView, CompanyEmployeeView

router = DefaultRouter()
# users
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)

# persons
router.register(r"companies", CompanyVieSet)
router.register(r"persons", PersonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/persons/<int:person_id>/favourite-food', PersonFavouriteFoodView.as_view()),
    path('api/v1/companies/<int:company_id>/employees', CompanyEmployeeView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
