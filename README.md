# Automated Craigslist Searcher web app

## About the project

I'm a volunteer at the [Idea Fab Labs](https://santacruz.ideafablabs.com/) maker/hacker/artspace here in Santa Cruz, 
and was asked to do a web app that would continually run on a desktop machine there, searching Craigslist every 15
minutes for items they're wanting to get for the facility that were posted today and are within an 80-mile radius of
our zip code, and display them in clickable format in a reasonable UI. I'm using Python/Django, HTML5/CSS, Bootstrap,
and a little JavaScript, and right now it looks like this:

![Automated Craigslist Searcher web app screenshot](https://github.com/tachyonlabs/automated-craigslist-searcher-web-app/blob/master/screenshot.png "Automated Craigslist Searcher web app screenshot")

And the Edit Search Settings screen looks like this (maybe later I'll redo it as a modal window instead):

![Automated Craigslist Searcher web app Edit Search Settings screen screenshot](https://github.com/tachyonlabs/automated-craigslist-searcher-web-app/blob/master/edit_search_settings_screenshot.png "Automated Craigslist Searcher web app screenshot")

As shown above, in addition to a zip code you need to specify a base Craigslist site. To quote from
[Julio M. Alegria's Simple Craigslist wrapper library README](https://github.com/juliomalegria/python-craigslist):

>To get the right `site`, follow these steps:
>1. Go to [craigslist.org/about/sites](https://www.craigslist.org/about/sites).
>2. Find the country or city you're interested on, and click on it.
>3. You'll be directed to `<site>.craigslist.org`. The value of `<site>` in the URL is the one you should use.

## Notes
* I used Python 3.7.2 and Django 2.0.10
* The admin account is just admin/admin.
* This app uses [Julio M. Alegria's Simple Craigslist wrapper library](https://github.com/juliomalegria/python-craigslist)
