https://github.com/Eugene-Chan2021Fall/Project-FlashCard

Date: 09/15/2021

Product name: Study Helper

**Members: ** Eugene Chan, Shehab Alnaimi, Seyoung Oh, William Nguyen

Problem Statement:To help students who are not able to study effectively

**Non-functional Requirements**:able to support English and Spanish, support Windows, Mac OS and Android systems; dark mode and light mode

Use Case #1 Name: Mind map of flash cads

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

---------------------------------------------------------------------------------------------

Use Case #2 Name: Change order of flash cards basd on how often user got answer correct

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

---------------------------------------------------------------------------------------------

Use Case #3 Name: Create pdf of flash cards to print

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