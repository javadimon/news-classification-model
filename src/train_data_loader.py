from selenium import webdriver
from selenium.webdriver.common.by import By

def load():
    """
    Loads the news data from the URLs.
    """

    driver = webdriver.Chrome()

    driver.get("https://habr.com/ru/hub/programming/")

    driver.implicitly_wait(0.5)

    # tm-article-snippet__title-link
    # tm - article - snippet__hubs

    contents = driver.find_elements(By.CLASS_NAME, "article-formatted-body")
    print(len(contents))
    for content in contents:
        print(content.text)
        print("\n\n-----------------------------------------------------\n\n")

    driver.implicitly_wait(2.5)

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