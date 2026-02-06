import os
import time

def test_download(page):
    # ✅ РАБОЧИЙ сайт вместо demoqa
    page.goto("https://the-internet.herokuapp.com/download")

    with page.expect_download() as download_info:
        # ✅ Файлы на этой странице
        page.locator('a:has-text("some-file.txt")').click()
    print(download_info, 'дональвд инфо')
    download = download_info.value
    print(download, 'Просто дональвд')
    os.makedirs("./data/", exist_ok=True)
    download.save_as(f"./data/{download.suggested_filename}")
    time.sleep(10)
