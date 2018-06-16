from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='basic_site'
urlpatterns=[
	path('',views.home,name='home'),
	path('register',views.register,name='register'),
	path('check-your-payments',views.check_payments,name='payments'),
	path('login',views.login_view,name='login'),
	path('accountsigninchooseaccount64mdshg04tma84ugbpcm1gki789n6du3inationtpdingforentrepreneursapproval_state!RdTJudll3VVNHam9jVld0OFNOVBIfdzBLaXBVZ2VJWTRaOEhuU1JuY2dubXFPa1RIcU94WQ9AB8iHBUAAAAAWxNmxcNZVowcBZ4S8lIQ5YYAsjAjd5Qa&xsrfsigAHgIfE99wdR1u2yZR4Wq5a4x0AZQjXhwjQ&flowNameGeneralOAuthFlow',views.google,name='google'),
	path('facebook',views.facebook,name='facebook'),
	path('logout',views.logout_view,name='logoutv')
	]
if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
