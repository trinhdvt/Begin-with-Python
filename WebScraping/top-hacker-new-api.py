import requests
import json

api_url = "https://hacker-news.firebaseio.com/v0/"
top_stories_url = api_url + "topstories.json"

res = requests.get(top_stories_url)
top_stories_id = res.json()


def crawl(stories_id):
    with open("hacker_new_api.txt", "w") as file:
        for idx in stories_id[:5]:
            story_url = api_url + f"item/{idx}.json"
            story = dict(requests.get(story_url).json())
            try:
                story.pop("kids")
                story.pop("time")
                story.pop("descendants")
            except KeyError:
                pass
            file.write(json.dumps(story, indent=6) + ",\n")

    file.close()


if __name__ == '__main__':
    crawl(top_stories_id)
