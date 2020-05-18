# Redirect for Podcast

This simple app have was developed to redirect the download link from a Podcast RSS feed to a more easy link.

To run, please follow the instructions bellow.

## Static Mode 
1. Get the packages needed.

    ```pip install -r requirements.txt```

2. Change the desired URL in `app.py`

    ```URL_FEED = "http://podcast.com/feed"```

3. Run using `python app.py`

Now just set a domain host and use like the following url `http://example.com/ep/1`

## Dynamic Mode

Just start the application with `python app.py` and request the url like `http://example.com/get_link?feed=http://podcast.com/feed&ep=1`