import json
from pathlib import Path

from model import get_model
from news_data import get_news_data
from tags import get_tags
from tqdm.contrib.concurrent import thread_map


def get_event_categories(model, news_article_json):
    prompt = f"{json.dumps(news_article_json)}.\n\n"

    out, _ = model.predict(prompt)
    try:
        result = json.loads(out)
    except:
        result = out
    return result


def predict(fpath: Path):

    model = get_model()

    with open(fpath, "r", encoding="utf-8") as f:
        news_items = json.load(f)

    news_items = news_items

    # Label
    # for news_item in news_items:
    #     news_item["label"] = get_event_categories(model, news_item)

    labels = thread_map(
        get_event_categories, [model] * len(news_items), news_items, max_workers=20
    )

    # [news_item["label"] = label for (news_item, label) in zip(news_items, labels)]

    for news_item, label in zip(news_items, labels):
        news_item["label"] = label

    # Save
    # outpath = f"data/labelled_news/{year}-{month}.json"
    outpath = Path("data") / "labelled_news" / fpath.name
    # outpath = Path(outpath)
    # news_item =
    outpath.parent.mkdir(parents=True, exist_ok=True)
    with open(outpath, "w") as f:
        json.dump(news_items, f, indent=2)


if __name__ == "__main__":
    # fname = f"data/news/{year}-{month}.json"

    news_path = Path("data/news")

    paths = news_path.glob("*")
    paths = list(paths)
    # print(paths)

    thread_map(predict, paths, max_workers=2)
