from flask import Flask, redirect, request
from get_episodes import GetEpisodes

app = Flask(__name__)

URL_FEED = "https://jovemnerd.com.br/feed-nerdcast/"

@app.route("/ep/<int:ep>")
def redirect_ep(ep):
    ge = GetEpisodes(URL_FEED)
    ep_list = ge.main()
    return redirect(ep_list[ep-1]['link'], code=302)

@app.route("/get_link", methods=['GET'])
def dynamic_redirect():
    ep = int(request.args.get('ep'))
    url_feed = str(request.args.get('feed'))
    ged = GetEpisodes(url_feed)
    epd_list = ged.main()
    return redirect(epd_list[ep - 1]['link'], code=302)

@app.route("/")
def home():
    return "hi :)"


if __name__ == "__main__":
    app.run(host="localhost")