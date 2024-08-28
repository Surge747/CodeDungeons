# CodeDungeons
 This was my 12th grade graduation project
 I received a 30/30 for my practicals including this project
 It only works in IDLE because I used sys.stout.shell which is an IDLE function, this is for coloured text

My idea was to make python fun to learn, and the solution was CODEDUNGEONS a dungeon crawling rpg answering python mcqs
I had a restriction to use only the external modules taught like tkinter and mysql connector
check the report of the project for the details and flowchart of how it works

I learnt many things making this project like splitting things into reusable functions and basic file organisation of assets in this project.
I got the assets of the monsters and backgrounds online and made them into assets for the game by combining the images on word.
The questions.txt file questions, the WOAH colourmatic code was also obtained online

While messing around with file organisation I discovered an exploit in file generation
A 5 line python script "boop.py" would let you create unlimited directories wherever you like
This has no checks in place in macos and windows and can really slow the computer if run for a while
It has the potential to create tens of thousands of empty directories in seconds
And after finding out about this I wanted to include it in the game
For the final boss which is the python snake itself
While you are fighting it file generation is going on in the directory where the game is saved
So if you take too long it will slow and may crash your computer

There are 2 versions, with and without the virus threat
I recommend playing without the virus threat just in case
