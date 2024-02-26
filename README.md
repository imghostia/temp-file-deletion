# temp-file-deletion

Welcome to my simple aumation task to protect your computer with unneccesary temporary files. 

Step 1: Download this tempfiledel.py file(Assuming you have installed python).

Step 2: 

**For Windows:**

You can use Task Scheduler. Here are the steps:

Open Task Scheduler.
Click on "Create Basic Task".
Name the task and add a description.
Choose the trigger (daily, weekly, etc.).
Choose "Start a program" as the action.
Browse and select your Python executable file (usually located in the Scripts folder of your Python installation directory).
In the "Add arguments" field, type the path of your Python script.
Finish the setup.


**For Linux:**

You can use cron jobs. Here's how:

Open the terminal.
Type crontab -e to edit the cron file.
Add a new line that defines the schedule (in cron format) and the command to run your script. For example, to run it daily at noon, you would add:
Save and close the file.

**For MacOS:**

You can use launchd. Here's how:

Create a .plist file that defines the schedule and command.
Place this file in the ~/Library/LaunchAgents directory.
Load the job using the launchctl load command.

**Remember to replace /path/to/your/script.py with the actual path to your Python script, and /usr/bin/python3 with the path to your Python executable, which you can find by running which python3 in the terminal.**
