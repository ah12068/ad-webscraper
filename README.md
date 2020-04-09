# ad-webscraper
My webscraper for AssessmentDay PDFs

Make sure selenium webdriver via Chrome is installed using code in terminal:

```

$ LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
$ wget http://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip
$ unzip chromedriver_linux64.zip && sudo ln -s $PWD/chromedriver /usr/local/bin/chromedriver

```

Make sure you have login to assessment day and create a ```.env``` file with the following variables (with your own credentials)

```
AD_USER=username
AD_PWD=password
```

run ```ad_webscraper.py``` if any captcha happens solve it within 30 seconds.
