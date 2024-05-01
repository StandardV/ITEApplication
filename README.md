# ITEApplication
Track and streamline your job search with ease. Add, sort, and keep track of places you've applied to, keep a log of your progress, and never miss an opportunity to re-apply with this program. And did you know that, for several companies the re-apply period might be short enough that you could try it again after 1 or 2 months no matter if it's an internship, grad position or professional one? this program also keep track of that and will automatically turn the switch off of those that you've applied to for long enough time(You can choose how long it is as well). Try it out!
![Screenshot (180)](https://user-images.githubusercontent.com/76143641/218628040-080fdb16-b7af-4eb1-a05a-97e752be39c3.png)

## Set up steps!!
Required Libraries: tkinter, customtkinter, pickle, time, winreg  :: suggest (pip install <library name>)

The program ("Application.Li") is already ready to use once you download the zip file and extract it (Download button at top right corner)

For any problems that may occur: **"pickledum"** is the debug file, just run it once, it will fix the wrong information stored within "dictionstoring", but just once and don't run it again because it will reset what you did (all of the switches) to the initial state.


# Demonstration.
Default color mode: Dark (switchable between dark, light)

I've put one-hundred companies up there first just everyone to experience it out, you could pull request and add more tho :) I don't mind (Easiest is just to go to Chat-gpt and ask for a list from it, chat-gpt tend to give replicate result a lot but nothing a filtering tool won't fix Note: I've not make it tho, check {What will be improve})

![Screenshot (177)](https://user-images.githubusercontent.com/76143641/218628241-7f2870ee-8929-4114-9cd6-355c955db251.png)

And this would be Applied filter:
![Screenshot (178)](https://user-images.githubusercontent.com/76143641/218627076-c76d462c-7842-4c2d-ba67-bea973c99422.png)

### Funtionalities
Keeping tracks of company applied
Automatically de-select the applied company based on the set application expiration time
Machine Learning to classify companies page for faster access and reduce searching times
Future iteration: (Auto-apply..)

![Screenshot (179)](https://user-images.githubusercontent.com/76143641/218627146-a4f158a9-1fb9-4344-be69-16456af6589e.png)

### How it work
Left panel is where company application are tracked, by pressing this, it will save them to log and index company name for website ranking from google
Links to companies sites will show up after going through parsing and classification (Note: need internet)

the middle text box in the middle is used to add in value:
  Each company is based off 1 line bracket next to companies is needed but content is user's choice, forexample 
  Microsoft (Global)
  Google (Global)
  Apple (Global)
  **Press submit**
  


Right panel is log and mode selection, it will display what you did from toggling to submiting, apply mode at bottom right is for link display mode, display all and top display is reccomended, auto open page still need improving on classification but would still work

## What will be improve
- Delete dialogue box keep hoping around (Planning to change this later)
- Limit input length in 1 line of entry (since longer is possible but you'll only be able to see limited information display on switches anyway)
- Perhaps place holder text for the middle input box?
- Add location sorting (Check for nearest state)
- And uhh, I'm still thiking
