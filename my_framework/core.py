class Application:

    def __init__(self, urlpatterns: dict, front_controllers: list):
        """
        :param urlpatterns: словарь связок url: view
        :param front_controllers: список front controllers
        """
        self.urlpatterns = urlpatterns
        self.front_controllers = front_controllers

    def __call__(self, env, start_response):
        # текущий url
        path = env['PATH_INFO']
        # Добавила в reqest, чтобы проверить в FC на наличие слеша в конце
        request = {"path": path}
        # примеряем front controllers
        for controller in self.front_controllers:
            controller(request)

        if request["path"] in self.urlpatterns:
            # получаем view по дополненному при необходимости url
            view = self.urlpatterns[request["path"]]

            # вызываем view, получаем результат
            code, text = view(request)
            # возвращаем заголовки
            start_response(code, [('Content-Type', 'text/html')])
            # возвращаем тело ответа
            return [text.encode('utf-8')]
        else:
            # Если url нет в urlpatterns - то страница не найдена
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b"Page Not Found"]
