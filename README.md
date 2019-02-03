# Automated Craigslist Searcher web app

## About the project

I'm a volunteer at the [Idea Fab Labs](https://santacruz.ideafablabs.com/) maker/hacker/artspace here in Santa Cruz, 
and was asked to do a web app that would search Craigslist every 15 minutes for items they're wanting to get for the 
facility that were posted today and are within an 80 mile radius of our zip code, and display them in clickable 
format in a reasonable UI. I'm using Python/Django, Bootstrap, and a little JavaScript, and right now it looks like 
this:

![Automated Craigslist Searcher web app screenshot](https://github.com/tachyonlabs/automated-craigslist-searcher-web-app/blob/master/screenshot.png "Automated Craigslist Searcher web app screenshot")

Later I'll have "Edit Search" let you edit the search terms, zip code, radius, and search frequency instead of having 
them hard-coded, but this is the initial quick get-it-up-and-running version before I have eye surgery in a few days.

This app uses [Julio M. Alegria's Simple Craigslist wrapper library](https://github.com/juliomalegria/python-craigslist).
