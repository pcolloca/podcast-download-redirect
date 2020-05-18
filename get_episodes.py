import feedparser

class GetEpisodes:
    def __init__(self, feed_url):
        self.url = feed_url

    def main(self):
        pod_feed = feedparser.parse(self.url)
        episodes = len(pod_feed.entries)
        ep_list = []

        for episode, num in zip(pod_feed.entries, range(1, episodes + 1)):
            link = episode.links[1]['href']
            ep_num = episodes - num + 1
            ep_list.append({"link": link, "ep_number": ep_num})

        ep_list.reverse()
        return ep_list

if __name__ == '__main__':
    ge = GetEpisodes("http://podcast.com/feed")
    episodes = ge.main()
    print(episodes)
