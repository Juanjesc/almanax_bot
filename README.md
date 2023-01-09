# Almanax Bot
![image](https://user-images.githubusercontent.com/89318618/211227748-eb0c8602-9951-47c3-861f-e260cc2b56ce.png) 
<img src="https://user-images.githubusercontent.com/89318618/211230071-11125888-0768-46f9-a102-982c7e4ddaaf.png" width="200">
## What it is?

This is a bot for the discord platform that takes a webhook URL, and every day at 00:00 queries an API and shows Almanax information in the correct channel of the discord server.

To give some more context, the Almanax is a daily bonus that is changing in a video game called Dofus, game developed by Ankama Games, in-game there is a daily mission that asks us for certain items to complete it, both the bonus and the materials of each day are given as an answer by the bot.

## Why this proyect?
<img src="https://user-images.githubusercontent.com/89318618/211228514-63673f7c-f148-4f61-8362-9f18fb13a22b.png" width="200">
I have not invented anything new, this is a bot that already exists in many other servers, but I wanted to learn how to make my own and to have a first contact with Python, <strong>what better way to learn than learning by doing</strong>

This bot is hosted on AWS Lambda, it allows me to trigger my script at 00:00 every day of the 365 days of the year, contrary to other bots, this one does not need to be permanently running, which could cause high memory and/or cpu resources, the logic is implemented in such a way that you only need a trigger at 00:00 to run it and it works, and AWS Lambda satisfies these needs very well.

<img src="https://user-images.githubusercontent.com/89318618/211228328-ea15e0b9-9665-4156-8c80-c4e3018a8b10.png" width="200"> 




