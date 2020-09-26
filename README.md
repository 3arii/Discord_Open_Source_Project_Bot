# Discord_Open_Source_Project_Bot
This Discord bot is for creating a database in a discord server, keeping track of it and adding a helpful bot to display it to anyone of interest.

HOW TO:

First of all as this bot will be hosted in your computer you must:

1- Go to the http://discordapp.com/developers/applications create or login to your account.
2- Create a new application by clicking on new application.
3- Scroll to the bots tab at the right hand side of the screen.
4- Click to the add bot button.(Give it a cool name)
5- Scroll to the OAuth2 at the right hand side of the screen.
6- From this window, you’ll see the OAuth2 URL Generator. This tool generates an authorization URL that hits Discord’s OAuth2 API and authorizes API access using your application’s credentials. In this case, you’ll want to grant your application’s bot user access to Discord APIs using your application’s OAuth2 credentials. To do this, scroll down and select bot from the SCOPES options and Administrator from BOT PERMISSIONS.
7- Copy the URL that will appear after you have selected the OAuth2 credential.
8- Paste it into any browser and follow the instructions.

HOW TO USE THE BOT IN A GUILD

Before you even start the bot you must change the string in the 173rd line to your own token which you can get in the bots tab of the discord developer portal.

All of the bot commands can be accessed throught the !help command but here is a preview:

!changeprefix:
Put anything after that and it will be the new prefix.

!clear:
Put any integer after clear with a space and that amoun of messages will be cleared. The deafult amount is 5.

!projects:
Displays current projects.

!addproject:
Gives you instructions about how a new project can be added.

!createproject:
Starts the process of adding a new open source project and makes you it's owner.

This project is made in order to keep track in our discord servers projects. Any contribution to the code is welcome. You must download the Discord Bot file and run it in your favorite IDE and host it.

