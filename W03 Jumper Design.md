# Jumper Design

To design our jumper program, we are going to start with 4 classes:
1. Director
2. Terminal Service
3. Animation
4. Word List

Each of the 4 classes will have different responsibilities. 

# Director 
will be responsible for
directing the program and organizing the way that it runs the different methods from each class. 
It will consist of a few methods like _do_updates, and _render. These methods will be encapsulated
to let others know what they should not alter within the code. 

# Terminal Service
will work directly through the console to print and to take inputs from the user.

# Animation
will be used to create the animation of the hangman character that we will be creating. It
will also animate any of the changes to the hangman as we guess correctly and make incorrect guesses. 

# Word List 
will be used to keep track of all the variables that will be changing throughout the program, 
like choosing the initial guess word, keeping track of the blank word, and changing the arrays that hold
each of those words as we make new guesses. 