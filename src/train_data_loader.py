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

    class_index = 1
    urls = ["https://habr.com/ru/hub/programming/", "https://habr.com/ru/hub/nix/", "https://habr.com/ru/hub"
                                                                                    "/machine_learning/"]
    pages = range(1, 51)
    for base_url in urls:
        for page in pages:
            url = base_url
            if page > 1:
                url = base_url + "page" + str(page) + "/"

            driver.get(url)

            # tm-article-snippet__title-link
            tittles = driver.find_elements(By.CLASS_NAME, "tm-article-snippet__title-link")
            # tm - article - snippet__hubs
            contents = driver.find_elements(By.CLASS_NAME, "article-formatted-body")

            index = 0
            for content in contents:
                csv_line = "\"" + str(class_index) + "\",\"" + normalize_string(tittles[index].text) + "\",\"" + normalize_string(content.text) + "\""
                write_line_to_file(csv_line)
                index += 1

            timeout = randrange(5, 10, 2)
            print("Timeout: " + str(timeout))
            time.sleep(timeout)

        class_index += 1

    driver.quit()


def write_line_to_file(line):
    with open("train-data-source/train.csv", "a") as file:
        file.write(line + "\n")


def normalize_string(s):
    return s.replace("\"", "\"\"").replace("$", "\\$")


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
