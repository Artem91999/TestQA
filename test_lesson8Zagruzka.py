import time
def test_zagruzka(page:Page):
    page.goto("https://zimaev.github.io/upload")
    page.set_input_files('#formFile', 'Zagruzka.txt')
    page.click('#file-submit')
    time.sleep(3)
