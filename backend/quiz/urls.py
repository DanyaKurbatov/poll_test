from .views import PollViewSet, QuestionViewSet, ChoiceViewSet, ResultViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'poll', PollViewSet, basename='poll')
router.register(r'question', QuestionViewSet, basename='question')
router.register(r'choice', ChoiceViewSet, basename='choice')
router.register(r'result', ResultViewSet, basename='result')

urlpatterns = router.urls