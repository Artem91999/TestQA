def test_listen_network(page):
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))

    """
    Функция ниже блокирует картинку с юрл https://osinit.com/asset/vsk.b9ee66c0a38acc328d41.svg
    """

    page.route("**/*vsk*b9ee66c0a38acc328d41.svg", lambda route: route.abort())


    page.goto('https://osinit.ru/')