from django.conf.urls.static import static
from django.urls import path
from rest_framework.routers import SimpleRouter

from config import settings
from habits.apps import HabitsConfig
from habits.views import HabitViewSet, HabitPublishedListAPIView

app_name = HabitsConfig.name

router = SimpleRouter()
router.register(r"", HabitViewSet)

urlpatterns = [
    path("published/", HabitPublishedListAPIView.as_view(), name="published"),
] + router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
