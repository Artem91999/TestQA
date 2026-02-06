def test_cart_zero_quantity(page):

    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))

    page.goto('https://httpbin.org/forms/post')  # ✅ Реальный сайт

    page.route("**org/post", lambda route: route.continue_(
        post_data='{"items": [], "total": 0}'  # Мокаем пустую корзину
    ))

    # Кликаем по форме (она отправит POST /post)
    page.get_by_role("button", name="Submit").click()

    # Проверяем в Network вкладке DevTools что данные подменен
    page.pause()