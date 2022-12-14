# python_crash_course

 This project is to document my progress through the Python Crash Course book by Matthes. I will be uploading all of the exercises present throughout the chapters and the multiple large projects outlined in the book will be highlighted independently. 


## Project 1: Python Game
This project is aimed at the development of a python based game called, Alien Invasion. In this game the user will control a rocket ship located at the bottom of the screen. The ship's functionality will be to move left and right on the screen via directional buttons while shooting bullets via the 'Space Bar' towards aliens that will populate from the top of the screen. The player's goal is to shoot all of the initial aliens, which will then prompt a sebsequent wave of progressively faster aliens. If an alien hits the ship or makes it to the bottom of the screen the player will lose one of their three available space ships and the fleet will repopulate. If all three ships are lost the game ends. The imported sys tools are used to develop a module that will allow the player to quit the game as well. 

Python's Pygame package will be used as the primary mode for creating the game. 

![alt text](https://github.com/bwengerDU/python_crash_course/blob/main/images/final_alien_invasion.png)

The game is initiated by mouse clicking on the play button, at which time the mouse cursor will disappear from the playing screen. Score is kept in the top right corner and with each subsequent level that is reached the aliens become quicker and the scoring is increased to reflect this increased difficulty. The current level tracked in the top right corner as well. In the top middle of the screen the game's top score is being tracked. In the top left the number of remaining player lives is tracked. The player will start with three and the game will end when they are out of lives. 
## Project 2: Data Visualization
This section is focusing on the wide range of matplotlib data visualization capabilities. 

1) The visualization below represents a list of digits being cubed and represented through increasing amounts via a color map with deeper reds achieved in higher numbers and lighter reds represented at lower numbers. 

![alt text](https://github.com/bwengerDU/python_crash_course/blob/main/images/colormap.png)

2) In the visualization below the python Random Walk method was used to generate 50,000 random movements and plotting them with a starting point highlighted in green and a finishing point highlighted in red. 
![alt text](https://github.com/bwengerDU/python_crash_course/blob/main/images/rw.png)

3) The third visual is a histogram that displays the results of rolling two 6-sided die 1,000 times. 
![alt text](https://github.com/bwengerDU/python_crash_course/blob/main/images/histogram1.png)

This histogram shows the combined number of two 6-sided die rolled 1,000 times. 
![alt text](https://github.com/bwengerDU/python_crash_course/blob/main/images/histogram2.png)

This histogram shows the combined number of a 6-sided die and a 10-sided die rolled 50,000 times. 
![alt text](https://github.com/bwengerDU/python_crash_course/blob/main/images/histogram3.png)

This line graph showcases the high and low temperatures across a year read in via CSV. The fill_between() functions was used to shade in the area between highs and lows to showcase the temperature range. 
![alt text](https://github.com/bwengerDU/python_crash_course/blob/main/images/sitkahl.png)

This visualization imports JSON files of Earthquake data and outputs a map of location and maginitude of earthquakes. 
![alt text](https://github.com/bwengerDU/python_crash_course/blob/main/images/eqmap.png)

This visual is sourced by a Github API that charts the most starred repositories on Github with the ability to hover a line to see the repository's information and it will link to the site when clicked. 
![alt text](https://github.com/bwengerDU/python_crash_course/blob/main/images/api.png)
## Project 3: Web Applications

This project is to build an application based upon Django functions. The initial phase is to set up a few topics that each have their own pages that can be accessed via the main page. 

The second phase aimed towards allowing users to create accounts and to add entries for the topics. 

The final phase is to set the styling and physical layout of the application. The site allows for a variety of topics in which entries can be added to each topic individually. User accounts are created that allow for users to create unique logins and that each account can add changes to the site while taking ownership of the changes and restricting their changes to their personal profile. Heroku is used to deploy the application. 

The final version is shown below. 
![alt text](https://github.com/bwengerDU/python_crash_course/blob/main/images/django.png)