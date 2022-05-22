from random import randrange
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def load():
    """
    Loads the news data from the URLs.
    """

    driver = webdriver.Chrome()
    driver.implicitly_wait(0.5)

    urls = ["https://habr.com/ru/hub/programming/", "https://habr.com/ru/hub/nix/", "https://habr.com/ru/hub"
                                                                                    "/machine_learning/"]
    for url in urls:
        driver.get(url)

        # tm-article-snippet__title-link
        tittles = driver.find_elements(By.CLASS_NAME, "tm-article-snippet__title-link")
        # tm - article - snippet__hubs
        contents = driver.find_elements(By.CLASS_NAME, "article-formatted-body")

        print(len(tittles))
        print(len(contents))

        index = 0
        for content in contents:
            print(tittles[index].text + "\n")
            print(content.text)
            print("\n\n-----------------------------------------------------\n\n")

        timeout = randrange(2, 6, 2)
        print("Timeout: " + str(timeout))
        time.sleep(timeout)

    driver.quit()


if __name__ == '__main__':
    load()

# Биржа
# https://bcs-express.ru/category/rossiyskiy-rynok

# Железо
# https://www.ixbt.com/news/

# Программирование
# https://habr.com/ru/hub/programming/

# Linux
# https://habr.com/ru/hub/nix/

# AI / ML
# https://habr.com/ru/hub/machine_learning/

#
# https://www.cnews.ru/
