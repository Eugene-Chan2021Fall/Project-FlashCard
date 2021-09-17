https://github.com/Eugene-Chan2021Fall/Project-FlashCard

**Date**: September 14,2021

**Product name**:Study Helper 

**Members:** Eugene Chan, Shehab Alnaimi, Seyoung Oh, William Nguyen

**Problem Statement**:To help students who are not able to study effectively

**Non-functional Requirements**:able to support English and Spanish, support Windows, Mac OS and Android systems; dark mode and light mode



**Use Case #1 Name:** input a Markdown file and output Flashcards 

 - Flashcards is powerful tool to provide efficient memorizing for all updates and information need to be memorized and fast way to take notes, create 
content and produce PDF to print.
\##Actors: students

\##Triggers

\##Primary Sequence

\##Primary Postconditions

**Use Case #2 Name:** Share PDF cards add to their accounts

 - Make printable flashcards as PDF file, create online flashcards, share a link or send to accounts digitally to refer when need it.
\##Actors

\##Triggers
D
\##Actors

- System

##Preconditions

- Markdown file ready to convert

##Triggers

- System use online converter to converter

##Primary Sequence

1- Use online converter to convert markdown file to pdf flash cards
2- Flash cards saved in the System and ready to use 

##Primary Postconditions

System update Flash cards ready to use

## Alternate Sequences

Error converting to pdf Flash cards 

##Alternate Trigger

- Fix the Error / convert again

##Alternate Postconditions

- Markdown file failed convert to pdf Flash cards 
  
**Use Case #2 Name:** Share PDF cards add to their accounts

\##Primary Sequence

\##Primary Postconditions6


##Actors

1- User
2- System

##Preconditions

1- pdf Flash cards created and ready to to share 
2- log in to the system
3- Accounts to share with

##Triggers

- Use system to share pdf Flash cards with their accounts 

##Primary Sequence

1- Prompt the system to share pdf Flash cards with users accounts 
2- Account user able to access pdf cards 
3- Select account users to share pdf cards with
4- Sharew pdf cards wit hprefered accounts 

##Primary Postconditions

1- Account users have access to pdf cards 
2- Able to use pdf cards

## Alternate Sequences

1- Accounts are not exist 
2- System gives error message Fail to share pdf cards 
3- System prompt to use exist or valid  accounts

##Alternate Trigger

Use valid or exist accounts

##Alternate Postconditions

Failed to share pdf with their accounts
 
**Use Case #3 Name:** Render Markdown notes 

 - Share markdown notes by creating GitHub repository, push the notes (file.md) to GitHub.
D
##Actors

1- users
2- System

##Preconditions

- Markdown notes created and ready 
- use app or online tool to render the markdown notes into HTML or pdf 
- Github repository created and ready or APP ready to recieve the notes

##Triggers

- Use render app or any online tools to render the markdown notes then push into Github or to the APP

##Primary Sequence

1- Choose App or online tool to render text into HTML or pdf
2- convert the sample text edited to HTML or pdf b 

##Primary Postconditions

- Markdown notes rendered to the new format HTML or PDt 

## Alternate Sequences

- Fail to render text into new format 

##Alternate Trigger

- Fix the error or use different tool

##Alternate Postconditions

- Fail to to render the markdown notes
=
\##Actors

\##Triggers

\##Primary Sequence

\##Primary Postconditions6

**Use Case #4 Name:** Find text in files

 - having a search a bar that allows user to input a word or series of alphabets to allow user to go straight to that specific note for review

\##Actors

\##Triggers

\##Primary Sequence

\##Primary Postconditions


**Use Case #5 Name:** Quickly rename files using regular expressions

 - showing a menu and have the files settings button to change the name of the file using regular expression if the user want to change it later on
\##Actors

\##Triggers

\##Primary Sequence

\##Primary Postconditions


**Use Case #6 Name:** Track hours worked per day

 - showing a track record of the hours worked once the "START" button is clicked and the timer should be counting therefore accumulating number of hours each day
\##Actors

\##Triggers

\##Primary Sequence

\##Primary Postconditions


**Use Case #7 Name:** Visualize hours worked and projects

 - showing time blocks in the calendar form which the user will in month-by-month basis which will show the hours worked and project title named in that day of the month.
\##Actors

\##Triggers

\##Primary Sequence

\##Primary Postconditions


**Use Case #8 Name:** Convert Markdown to PDF

* Ability to convert markdown notes to a pdf file. 

\##Actors

1. User
2. System

\##Preconditions

* Has to be logged in.
* Has to be on the page to view markdown files.

\##Triggers

User selects button to convert markdown file to pdf.

##Primary Sequence

1. System converts markdown file to pdf
2. Prompts user to choose where the new pdf file will be saved
3. System shows a confirmation that the converting process was sucessful

##Primary Postconditions

* User recieves the converted pdf file

\## Alternate Sequences

1. Prompts the user an error has occured.

\##Alternate Trigger

\###Alternate Postconditions

* User does not recieve a converted pdf file

**Use Case #9 Name:** Share notes with other users

* Users can send notes from their portal directly to other users.

\##Actors

1. User
2. System

\##Preconditions

* Has to be logged in.
* Has to have notes stored within the account that are shareable
* Has to be on the page/portal that displays all of the user's notes
* User needs another user to share to

\##Triggers

User presses the share button that is located next to the desired file. 

##Primary Sequence

1. A share screen is prompted for the user where they can enter the username of the recipient.
2. System checks to see if the user is entering valid usernames.
3. After a user has added the recipient's account, their profile will be displayed on the screen to indicate that the recipient has been selected.
4. When the user has selected all recipients, they must select a confirmation button. 
5. System sends the notes to the recipients where they are notified and able to view it in their portal. 

\##Primary Postconditions

* User was able to share their notes directly to the recipient's portal. 
  * Recipient recieves notes in their portal.
  * Recipient are notified that someone has shared notes with them.

\## Alternate Sequences

1. User has entered in an invalid recipient.

\###Alternate Postconditions

* Recipient does not recieve notes.
  * Recipient displays an error message.

**Use Case #10 Name:** Create time blocks

* Users can create time block schedules to help with their time managment. 

\##Actors

1. User
2. System

\##Preconditions

* Has to be logged in.
* Has to be on the time managment page.

\##Triggers

Users press the create time block schedule button.

##Primary Sequence

1. System creates a schedule in their portal with a generated name for the schedule.
2. Users are given the option to rename the schedule so it can be organized in their portal.
3. Users can input events and times for specific weeks.
4. System checks to see if events are overlapping and will warn the user if so.
5. After the user has finished entering events, the system takes these inputs and displays them on a calendar for users to visually see.
6. When the user is finished they can hit the save button which will add it to their portal. 

\##Primary Postconditions

* User will have a time block schedule that can be acessed through their portal. 

\## Alternate Sequences

1. User has overlapping events that need to be resolved before saving the schedule.
2. System warns the user untill the issue is resolved.

###Alternate Postconditions

* Time block schedule could not be saved to portal due to invalid inputs.

**Use Case #11 Name:** Use pomodoro timer

* A timer that lets users manage their break time between study sessions. 

\##Actors

1. User
2. System

\##Preconditions

* Has to be logged in.
* Has to be on the time managment page.

\##Triggers

Has to press the pomodoro timer button.

##Glossary

* Pomodoro - a studying technique that uses a timer to split work into 25 min intervals and is followed by a short break. 

##Primary Sequence

1. Opens a pomodoro timer. 
2. User will be able to add tasks and notes to the pomodoro timer.
3. Users can press start to begin timer.
4. The pomodoro timer will notify the user whenever the timer on a task is completed. 
5. Users can choose between short and long break options and press start on the timer.
6. After the user's break is over the pomodoro timer will notify the user.
7. When the user is finished they can close the pomodoro timer. 

\##Primary Postconditions

* User will have a timer that notifies them when time is up. 

\## Alternate Sequences

1. User can pause and move to the next timer option timer if necessary.
2. User can clear all tasks from the timer.
3. User can import templates from pomodoro.

###Alternate Postconditions

* User stops the timer


Use Case #12 Name: Mind map of flash cads

- Users can create and see the mind map of flash cards

##Actors: 

1. Users
2. System

\##Preconditions

- User has an account for the app
- Has to be logged in

\##Triggers

- Concrete action made by users to start the Use Case.

##Primary Sequence: 

1. User login-in and access to own account
2. Prompt user to choose which one user wants to see with mind map

##Primary Postconditions

- There are flash cards to make with mind map

##Alternate Sequences

1. If have not an account, users have to create an account first
2. Once you got account, you can access to own portal

\###Alternate Postconditions

- If there is no flash card, users have to create flash card first.


Use Case #13 Name: Change order of flash cards basd on how often user got answer correct

- User can study more what he didn't get answer correct

\##Actors

1. User
2. System

\##Preconditions

- There must be flash card to change order.

\##Triggers

-  User presses the Change Order button 

\##Primary Sequence

1. Press the Change Order button
2. System change the order of flash card basd on how often user got answer correct

##Primary Postconditions

- There mush be flash cards more than 1
- System have to record how often user got answer correct

\## Alternate Sequences

1. If there is no flashcard, System shows that "Invalid request"

\###Alternate Postconditions

- Sysetm didn't get flash card
  - Displays error message


Use Case #14 Name: Create pdf of flash cards to print

- User can create pdf file of flash cards that he made

\##Actors

- User
- System

\##Preconditions

- Has to be logged in
- There must be flash cards to change to PDF to print

\##Triggers

- User press the change to PDF button

\##Primary Sequence

1. User presses the change to PDF button 
2. User can change the name of PDF file
3. User can designate the location of file

\##Primary Postconditions

- User was able to print the flash card with PDF file

\## Alternate Sequences

1. There is no flash card to change to PDF
2. Create flash card

\###Alternate Postconditions

- There can be error message if there is no flash card to change to PDF
