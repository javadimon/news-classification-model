import os


def my_test():
    if os.path.exists("train-data-source/test.csv"):
        os.remove("train-data-source/test.csv")

    class_index = 1
    urls = ["https://habr.com/ru/hub/programming/", "https://habr.com/ru/hub/nix/", "https://habr.com/ru/hub"
                                                                                    "/machine_learning/"]
    pages = range(1, 51)
    for base_url in urls:
        for page in pages:
            url = base_url
            if page > 1:
                url = base_url + "page" + str(page) + "/"

            # tm-article-snippet__title-link
            tittles = ["One", "Two", "Three $100"]
            # tm - article - snippet__hubs
            contents = ["One Content", "Two  \"Content\"", "Three  Content"]

            index = 0
            for content in contents:
                csv_line = "\"" + str(class_index) + "\",\"" + normalize_string(tittles[index]) + "\",\"" + normalize_string(content) + "\""
                # print(csv_line)
                write_line_to_file(csv_line)
                index += 1
        class_index += 1


def write_line_to_file(line):
    with open("train-data-source/test.csv", "a") as file:
        file.write(line + "\n")


def normalize_string(s):
    return s.replace("\"", "\"\"").replace("$", "\\$")


if __name__ == '__main__':
    my_test()
