# ITEApplication
Track and streamline your job search with ease. Add, sort, and keep track of places you've applied to, keep a log of your progress, and never miss an opportunity to re-apply with this program. And did you know that, for several companies the re-apply period might be short enough that you could try it again after 1 or 2 months no matter if it's an internship, grad position or professional one? this program also keep track of that and will automatically turn the switch off of those that you've applied to for long enough time(You can choose how long it is as well). Try it out!
![Screenshot (180)](https://user-images.githubusercontent.com/76143641/218628040-080fdb16-b7af-4eb1-a05a-97e752be39c3.png)

## Set up steps!!
Required Libraries: tkinter, customtkinter, pickle, time

The program(Application.Li) is already ready to use once you put them all in a big file and alter the paths file in ApplicationLi.py and ApplicationSorter.py (path instruction within files)

However, for those who encountered problems from Keyerror to list out of range ..etc. Pickledum is the debug file, change the file path within it (similar to the 2 other programs) and run it once, it will fix the wrong information stored within "dictionstoring", but just once and don't run it again because it will reset what you did to the initial state.


# Demonstration.
Default color mode: Dark (switchable between dark, light)

I've put one hundred companies up there first just for you guys to experience it out, you could pull request and add more tho :) I don't mind (Easiest is just to go to Chat-gpt and ask for a list from it, chat-gpt tend to give replicate result a lot but nothing a filtering tool won't fix Note: I've not make it tho, check {What will be improve})

![Screenshot (177)](https://user-images.githubusercontent.com/76143641/218628241-7f2870ee-8929-4114-9cd6-355c955db251.png)

And this would be Applied filter:
![Screenshot (178)](https://user-images.githubusercontent.com/76143641/218627076-c76d462c-7842-4c2d-ba67-bea973c99422.png)

### Details explaination:
You can look for companies, apply to those and turn the switch box on, here I've set the time each switch box turn off by itself would be 6480000sec, IE: 2 months and a half, to which I think would be the standard time that you could re apply (NOTEEEE: the Delete Content box can only delete one by one tho, and it have to be the right name + (Location), I did this to prevent mass deleting )
![Screenshot (179)](https://user-images.githubusercontent.com/76143641/218627146-a4f158a9-1fb9-4344-be69-16456af6589e.png)

## What will be improve
- Delete dialogue box keep hoping around (Planning to change this later)
- Limit input length in 1 line of entry (since longer is possible but you'll only be able to see limited information display on switches anyway)
- Perhaps place holder text for the middle input box?
- And uhh, I'm still thiking
