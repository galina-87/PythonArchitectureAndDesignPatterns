from my_framework import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/about/': views.about_view,
    '/contacts/': views.contacts_view,
}


# FC дописывает "/" в конце URL запроса
def slash_controller(request):
    if request['path'][len(request['path']) - 1] != '/':
        request['path'] = request['path'] + '/'


front_controllers = [
    slash_controller
]

application = Application(urlpatterns, front_controllers)

