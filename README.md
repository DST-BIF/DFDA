# DFDA - Danish Football Data Analysis

## Introduction

This GitHub page for Danish Football Data Analysis was created for the Football Performance Summit 2023 but is intended to provide professionals in Danish football and hobbyists worldwide with <strong>*a basic*</strong> starting point for doing data analysis.

## Data use
By downloading any data you accept the following [terms of use](https://github.com/DST-BIF/DFDA/blob/6880efd546e15e28850cab1761027c4496dd670b/LICENSE.md)

## Presentation from Football Performance Summit 2023
Link to [presentation](https://sijedivfor.github.io/footballperformancesummit/)

## Translating your style of play
Link to [KPI Generator](https://divisionsforeningen.shinyapps.io/summit/)

## How to get started with the data 
The following guide will go through both basic PowerBI, which can be utilized as a quick and free tool to create visualizations, as well as some fundamental steps into Python, a programming language which allows the user to do almost everything.

Additional info on open data sets and other more detailed and specialized guides can be found at the end.
Please check the Open Data Section at the end for access to further data from the Danish Superliga.

The guide below assumes that you have downloaded and extracted the code to your desktop like this - <strong>*C:\Users\YOUR_USER\Desktop\Github\DFDA*</strong> - if you have placed it somewhere else, you *will* need to change some paths. The guide also assumes the use of a Windows operating system.

## Table of content

- [PowerBI:](#powerbi)
  - [Installing PowerBI](#Installing-PowerBI)
  - [Loading in your data](#loading-in-your-data)
  - [Creating your first visualization](#creating-your-first-visualization)
  - [Add slicers and go interactive](#add-slicers-and-go-interactive)

- [Python:](#python)
  - [Installing Python](#installing-python)
  - [Loading in event data](#loading-in-event-data)
  - [Creating your first KPIs](#creating-your-first-kpi)
  - [Creating your first plots](#creating-your-first-plot)
  - [Loading and plotting tracking data](#Tracking-data)
  
- [Data access:](#data-access)
  - [Club acccess](#club-access)
  - [Open data](#open-data)
    - [DFDA](#dfda-1)
    - [Others - Aggregated](#others---aggregated)
    - [Others - Event](#others---event)
    - [Others - Tracking](#others---tracking)
    - [Create your own event data](#create-your-own-event-data)

- [Further reading](#further-reading)

## PowerBI

### Installing PowerBI

Installing PowerBI is straightforward on all Windows PCs - just follow the link below, download the installer and run it. There is no need to sign up, and the PowerBI Desktop version is free.

https://www.microsoft.com/en-us/download/details.aspx?id=58494

If you are using a non-Windows operating system, you can run PowerBI in a virtual windows environment. You can use an alternative like Tableau - or skip PowerBI and go straight to Python.

### Loading in your data

After installing, opening PowerBI, and closing the "Get Started" prompt, you can load one of the mock GPS data files from the "Aggregated Data" folder using the Excel import shown below:

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/PowerBI%20-%20Data.PNG)

If you want to load data from <strong>*all files*</strong>, as you would likely want to do with your own data. Use the "Get data" import to the left of the Excel import. Choose "folder" in the right-hand menu, and press connect.

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Folder.PNG)

Navigate to the C:\Users\YOUR_USER\Desktop\Github\DFDA\Data\Aggregated Data folder - which should leave you with a prompt similar to the one below - press OK:

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Folder%20import.PNG)

This should give you a list of all the files in the folder like this:

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Combine.PNG)

Selecting "Combine & Load" should prompt you to choose which excel sheets to import - simply select Sheet1/Ark1 and press OK.

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Sheet%201.PNG)

When combining data files, make sure that the files are formatted in the same way (the number of columns and column names must be identical).

If you have done it correctly, you should see a loading prompt telling you that 18 rows have been imported, and under "Fields" on the right, you should have something like this:

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Data.PNG)

### Creating your first visualization

Utilizing either one or all the files, you can now create a dashboard with physical performance for the players. The most basic thing would be to create a table or a bar chart - this can be done using one of the two visualizations highlighted below.

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Visualizations.PNG)

Adding a table to the current page is as simple as clicking the table visual - which should result in a page looking like this:

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Table.PNG)

Drag variables to the highlighted "Columns" field - if you add Date - select date rather than date hierarchy as shown:

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Date%20fix.PNG)

Add Player, Position, Data set, and Total Distance - then expand the table size half of the page to get the following:

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Table%20Step%20One.PNG)

To create some context, you can start calculating the average distance on each date. First, add a new column by clicking on one of the highlighted options.

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/New%20column.PNG)

Rename the column and make the calculation as shown below. To calculate the average distance on a date level, we specify it in the 'ALLEXCEPT' statement (see picture). If you replace date with player or position, then you will get an average of total distance for each player/position across all dates.

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Average%20by%20date.PNG)

Adding some color or highlights can be a quick way of spotting outliers. You can create a color column to show players above the average daily distance.

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Color.PNG)

Using this column, you can add conditional formatting by going to formats as shown below.

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Format%20column.PNG)

Now, implement a rule based on the color column and set everything above 1 to be red, as shown below.

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Rule%20based%20color.PNG)

After clicking okay, you should have a table with every date and player, with a red background color on the players running more than the daily average.

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Result.PNG)

### Add slicers and go interactive

Start by resizing the table so that it takes up the left half of your PowerBI page.
Then click on the empty part of the page, lastly add a slicer by clicking on the highlighted icon below.

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Slicer.PNG)

Then add the player list to the slicer.

Now, you can use the slicer/checkmarks to filter between different views of players. Alternatively, you can add a slicer with the date, MD date, week, position, team, etc.

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Table%20and%20slicer.PNG)

You can then transform your table into a bar chart by first clicking on the table and then on the highlighted visualization bottom.

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Simple%20bars.PNG)

To make it a bit prettier, remove "Position" from the legend area on the right, and move "Player" from "Small multiples" to the "Legend" - the result should look like this.

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Bar%20chart.PNG)

To simplify the view, you can change the slicer to a "Single select" by clicking the slicer &rarr; "Format visual" &rarr; "Slicer selection" &rarr; "Selection" and turning on "Single select".

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Single%20select.PNG)

While Total Distance can be interesting, you might want to look at Distance or HI meters per minute played. To calculate this, add a new column and type in the following.

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Per%20min.PNG)

Replace "Total Distance" in your bar chart by simply dragging your new "HI meters per min" column onto the "Total Distance" in the "Y-Axis" field. The resulting screen should then look like this.

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Bar%20chart%20HI.PNG)

By adding lines to your bar chart, you can add some context or guidelines, e.g., if you have a set target, you can show this using a "constant line".

If you would rather look at what days the player is running more or less than his average over the period, you can use an "average line".

A constant line can also use a dynamic value, like the average performance of a player's position, team or week. You have to calculate this value as you did in column "Avg. Daily Distance".

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Add%20lines.PNG)

## Python

### Installing Python

The easiest way to install python is to download and install Anaconda. Besides installing python, Anaconda also installs a few different IDEs (Integrated Development Environment)/user interfaces for coding.

<https://docs.anaconda.com/anaconda/install/index.html>

The rest of this GitHub will utilize Jupyter Notebooks as the IDE as it is very beginner friendly.

After installing Anaconda, you need to install some packages (libraries of code, e.g., code that makes it easier to handle football data). 
To install packages, open "anaconda prompt" on your computer - simply run "Anaconda Prompt (Anaconda 3)" from your windows start menu.

To install the modules, simply type in the following:
"pip install MODULE"

An example of how to install the "kloppy" package is shown below:

![Image](https://github.com/DST-BIF/DFDA/blob/main/Screenshots/Anaconda%20prompt.PNG)

Then press enter and wait for the installation to happen - you might need to press "y" and enter once or twice.

To run the notebooks (code) in this GitHub repository, you will need to install the following modules:

- kloppy
- mplsoccer
- numpy
- pandas
- opencv-python
- os
- tqdm

To open the notebooks on your computer, run "Jupyter Notebook (Anaconda 3)" from your windows start menu. Assuming you have downloaded this repository and saved it here: <strong>*C:\Users\YOUR_USER\Desktop\Github\DFDA*</strong>. You can navigate to the code by clicking Desktop &rarr; Github &rarr; DFDA &rarr; Jupyter Notebooks.

The notebooks contain comments (explanations) of all code. To run the code, you must replace "YOUR_USER" in the file paths with your username.
If you are starting from scratch, it is advised to start at "1. Load event data" and read through all notebooks, as 2.-4. build on lessons from 1.

Each box in the notebook is a self-contained bit of code that you can run by clicking the "Run" button at the top to run the code or clicking (ctrl + Enter).
In general, each box relies on the previous, so you need to run them in the order they are presented.

### Loading in event data

The notebook "1. Load event data" teaches you to load event data from OPTA and some basic functions for working with data.

[Loading in event data](https://github.com/DST-BIF/DFDA/blob/main/Jupyter%20Notebooks/1.%20Load%20event%20data.ipynb)

### Creating your first KPI

The notebook "2. What counts" teaches a few more basic things about working with data and how to extract simple metrics from the event data.

[What counts](https://github.com/DST-BIF/DFDA/blob/main/Jupyter%20Notebooks/2.%20What%20counts.ipynb)

### Creating your first plot

The notebook "3. On to the pitch" teaches you how to plot a football pitch. You will learn to add simple events and how to customize the plot to make it easy to add to a report/slide show.

[On to the pitch](https://github.com/DST-BIF/DFDA/blob/main/Jupyter%20Notebooks/3.%20On%20to%20the%20pitch.ipynb)

### Tracking data

The notebook "4. Tracking data" teaches you how to import data from CSV files, plot a frame of tracking data, create an animation and save it as a video clip.

[Tracking data](https://github.com/DST-BIF/DFDA/blob/main/Jupyter%20Notebooks/4.%20Tracking%20data.ipynb)

## Data access

### Club access

Contact Divisionsforeningen to get access to the data warehouse - in which most pre-processing has been done for you.

### Open data

##### DFDA

- Aggregated data folder
  - Made up data, mimicking a *very* simplified output from GPS systems
  - Data uploaded in excel format to "mimic" output formats

- Event data folder
  - Match info and event data from OPTA/Stats Perform - covering "Week 32 - Vejle v OB" in the Superliga Season 2021-2022
  - No pre-processing done - data is uploaded in raw XML formats

- Tracking data folder
  - Snippets of tracking data from Second Spectrum - covering the goals in "Week 32 - Vejle v OB" in the Superliga Season 2021-2022
  - Pre-processing has been done - data is uploaded in CSV format
  - Data in 3 files, one with ball and frame info, one with the home team and one with the away team

<strong>*To get access to more data from the 2021-2022 Season of the Danish Superliga please contact divisionsREMOVETHISforeningen [at] kmd.com*</strong>

##### Others - Aggregated

<https://fbref.com/en/>

<http://clubelo.com/API>

##### Others - Event

<https://github.com/statsbomb/open-data>

<https://footballdata.wyscout.com/download-samples/>

##### Others - Tracking

<https://github.com/metrica-sports/sample-data>

<https://github.com/SkillCorner/opendata>

##### Create your own event data

<https://fcpythonvideocoder.netlify.app/>

<https://torvaney.github.io/projects/tracker>

## Further reading

<https://fcpython.com/>

<https://github.com/devinpleuler/analytics-handbook>

<https://github.com/Friends-of-Tracking-Data-FoTD>

<https://github.com/eddwebster/football_analytics>

<https://github.com/ML-KULeuven/socceraction>

## Python module guides/getting started's

<https://mplsoccer.readthedocs.io/en/latest/>

<https://kloppy.pysport.org/>

<https://numpy.org/doc/stable/user/index.html>

<https://pandas.pydata.org/docs/getting_started/index.html>
