from random import randrange
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import codecs


def load():
    """
    Loads the news data from the URLs.
    """

    driver = webdriver.Chrome()
    driver.implicitly_wait(0.5)

    class_index = 1
    urls = ["https://habr.com/ru/hub/programming/", "https://habr.com/ru/hub/nix/",
            "https://habr.com/ru/hub/machine_learning/"]
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
                if index >= len(tittles):
                    break
                if tittles[index].text == "" or content.text == "":
                    break

                csv_line = "\"" + str(class_index) + "\",\"" + normalize_string(
                    tittles[index].text) + "\",\"" + normalize_string(content.text) + "\""
                print(url + " --- " + csv_line)
                write_line_to_file(csv_line)
                index += 1

            timeout = randrange(5, 10, 2)
            print("------------ Timeout: " + str(timeout) + " ------------")
            time.sleep(timeout)

        class_index += 1

    driver.quit()


def write_line_to_file(line):
    # with open("train-data-source/train.csv", "a") as file:
    with codecs.open("train-data-source/train.csv", "a", "utf-8") as file:
        file.write(line + "\n")


def normalize_string(s):
    return s.replace("\"", "\"\"").replace("$", "\\$").replace("\n", " ").replace("\r", " ").replace("—", " ")


def create_test_data():
    with codecs.open("train-data-source/train.csv", "r", "utf-8") as file:
        lines = file.readlines()

        index = 0
        for line in lines:
            index = index + 1
            if index == 15:
                print(line)
                index = 0


if __name__ == '__main__':
    # load()
    create_test_data()


# Программирование
# https://habr.com/ru/hub/programming/

# Linux
# https://habr.com/ru/hub/nix/

# AI / ML
# https://habr.com/ru/hub/machine_learning/

# News sources:

# Linux
# https://pingvinus.ru/

# Железо
# https://www.ixbt.com/news/

#
# https://www.cnews.ru/

# Биржа
# https://bcs-express.ru/category/rossiyskiy-rynok
