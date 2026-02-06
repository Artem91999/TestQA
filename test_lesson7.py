import time
def test_dialogs(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.accept("999"))
    time.sleep(10)
    page.get_by_text("Диалог Prompt").click()
    page.pause()