# Automating Google Dino
In this we are gonna use the http://www.trex-game.skipser.com/ automate the Dino..which is same as that of Google Dino

# Required Packages
* Pyautogui
* Numpy
* ImageGrab,ImageOps
* Time

# Implementation:
First we are going to click on the screen to start the Dino. Here we are having 2 conditions
1. Initial Start of the Dino (That's starting the Game for the very first time)
2. Restart Mode

## 1.Normal Mode
![image](https://user-images.githubusercontent.com/36659683/55670016-7013d080-589c-11e9-80c8-fb2179466dc0.png)

## 2. Restart Mode
![image](https://user-images.githubusercontent.com/36659683/55670038-d4cf2b00-589c-11e9-9eea-7a77eb5e74d9.png)

# Step 1: To start the Game
So the basic idea is to click at the center of the screen where the restart button is located.Using mspaint we can plot the x and y as shown below

![image](https://user-images.githubusercontent.com/36659683/55670069-722a5f00-589d-11e9-98d2-b8b876fd08b6.png)

# Step 2: Detecting the Tree and bird
The idea is to locate the tree at some distance away from the dino. Considering the box to identify the tree and bird.

![image](https://user-images.githubusercontent.com/36659683/55670108-ef55d400-589d-11e9-95a7-9c8ab68c0adc.png)

In this case the box (x1,y2,x2,y2) as (485,391,500,427)

# Step 3: Detecting the color inside the box.
As the background different from the tree, it is easy to find the color of the tree using ImageGrab and process it using nump. And it leads to the condition when the color is different key up is triggered.

![nointernet_dinogame_gif](https://user-images.githubusercontent.com/36659683/55670151-7a36ce80-589e-11e9-9f7d-a64f4d01690a.gif)

Using this technic we can automate games such as Tap Soccers

![image](https://user-images.githubusercontent.com/36659683/55670190-0cd76d80-589f-11e9-8e8b-d508dec4873d.png)
