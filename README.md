# craigslist

This is my Craigslist Scraper application that scrapes listing from a user generated craigslist url and emails a csv file of the listings to a sepcified To and From email address

* Clone the repo into an python enviorment
* Install the modules listed in requirements.txt
* Sign up for a free heroku account if you havent already done so
* Create app ie. myapp #name of app
* Assign these buildpacks:
  * Headless Google Chrome: https://github.com/heroku/heroku-buildpack-google-chrome
  * Chromedriver: https://github.com/heroku/heroku-buildpack-chromedriver
* Add the Config Vars:
  * CHROMEDRIVER_PATH = /app/.chromedriver/bin/chromedriver 
  * GOOGLE_CHROME_BIN = /app/.apt/usr/bin/google-chrome 
* Type heroku login --> This will take you to a web based login page
* cd to your directory on your local drive
* Type 'git init'
* Type 'heroku git:remote -a myapp'
* Type 'git add .'
* Type ' git commit -am "version 1"'
* Type 'git push heroku master'
* Now you need to allocate a dyno to do the work. Type 'heroku ps:scale worker=1'
* If you want to check the logs to make sure its working type 'heroku logs --tail'

![Screenshot_2020-04-20 myscrapingapp2 Heroku](https://user-images.githubusercontent.com/25403763/79792235-8c09d900-831c-11ea-931c-83db8abbf16c.png)

![Screenshot_2020-04-20 An email with attachment from Python - ddphillyfan gmail com - Gmail](https://user-images.githubusercontent.com/25403763/79792519-0c303e80-831d-11ea-82e4-bfd3cd362b7b.png)

