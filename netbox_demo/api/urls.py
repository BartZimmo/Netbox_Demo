from netbox.api.routers import NetBoxRouter

from . import views

app_name = 'netbox_demo'

router = NetBoxRouter()
router.register('access-lists', views.AccessListViewSet)
router.register('access-list-rules', views.AccessListRuleViewSet)

urlpatterns = router.urls