
def test_inner(page):
    page.goto('https://zimaev.github.io/table/')
    page.screenshot(path="data/screen.png", full_page=True)
    row = page.locator("tr")
    print(row.all_inner_texts())