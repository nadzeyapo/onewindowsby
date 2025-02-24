from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, procedures, juridical, architecture, education, housingrelations, laborandsocialprotection, \
    guardianship, sport, transport, nature, agriculture, archieve, army, rege, archieve1, archieva2, educationj
from .views import money, stroitelstvo, oos, svyz, shop, sportj, finansy, imysh, doc
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('procedures', procedures, name = 'procedures'),
    path('juridical', juridical, name = 'juridical'),
    path('architecture', architecture, name = 'architecture'),
    path('education', education, name='education'),
    path('housingrelations', housingrelations, name = 'housingrelations'),
    path('laborandsocialprotection', laborandsocialprotection, name = 'laborandsocialprotection'),
    path('money', money, name = 'money'),
    path('stroitelstvo', stroitelstvo, name='stroitelstvo'),
    path('svyz', svyz, name='svyz'),
    path('oos', oos, name = 'oos'),
    path('shop', shop, name='shop'),
    path('sportj', sportj, name='sportj'),
    path('finansy', finansy, name='finansy'),
    path('imysh', imysh, name ='imysh'),
    path('doc', doc, name='doc'),
    path('guardianship', guardianship, name = 'guardianship'),
    path('sport', sport, name='sport'),
    path('nature', nature, name='nature'),
    path('transport', transport, name='transport'),
    path('agriculture', agriculture, name='agriculture'),
    path('archieve', archieve, name='archieve'),
    path('army', army, name='army'),
    path('rege', rege, name='rege'),
    path('archieve1', archieve1, name='archieve1'),
    path('archieva2', archieva2, name='archieva2'),
    path('educationj', educationj, name='educationj'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
