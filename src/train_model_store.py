import json


class NewsTokenizer:
    def __init__(self, news_class_name, counter):
        self.news_class_name = news_class_name
        self.counter = counter


def save(tokenizers, db_file_name, is_optimize=False):
    json_data = []
    for tokenizer in tokenizers:
        news_class_name = tokenizer.news_class_name
        tokens = []
        for item in tokenizer.counter.items():
            if is_optimize and item[1] > 1:
                tokens.append({"token": item[0], "count": item[1]})
            elif is_optimize is False:
                tokens.append({"token": item[0], "count": item[1]})

        json_data.append({"news_class_name": news_class_name, "tokens": tokens})

    with open(db_file_name, "w", encoding='utf8') as f:
        json.dump(json_data, f, ensure_ascii=False)
    print("Saved to " + db_file_name)


def load(db_file_name):
    with open(db_file_name, "r", encoding='utf8') as f:
        json_data = json.load(f)

    tokenizers = []
    for data in json_data:
        news_class_name = data["news_class_name"]
        counter = {}
        for token in data["tokens"]:
            counter[token["token"]] = token["count"]
        tokenizers.append(NewsTokenizer(news_class_name, counter))

    return tokenizers
