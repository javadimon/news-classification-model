import feedparser


def read_feeds(urls):
    for url in urls:
        feed = feedparser.parse(url)
        print(len(feed.entries))
        # for entry in feed.entries:
        #     print(entry.keys())


if __name__ == '__main__':
    urls = ["https://habr.com/ru/rss/hub/java/all?limit=-1"]
    read_feeds(urls)
