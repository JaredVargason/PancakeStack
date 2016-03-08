#Snowman

##An interactive stacking experience

###Documentation

#####Running Snowman
To run Snowman, enter "snowman.py" for an interactive shell.
Otherwise, enter "snowman.py <FILENAME>" to interpret a script.
Maybe possible to save and load.

#####How it works
This language is used to build snowmen.  

#####Variables
Snowman is a statically typed language. 
Snowman supports two types of variables: ball and snowman. 
If you want to create a ball variable, you must say "ball <NAME>".
Similarly, if you want to create a snowman variable, use "snowman <NAME>".

Variables can be named using lowercase and uppercase letters, digits, and underscores.

It is easy to get confused with naming, so we recommend naming balls after their respective snowmen. For example, on a snowman "charlie" name your ball variable "charlie_base".

Variables can be assigned to other variables:

`ball bill = c` 

 However, this will copy the value to the assigned variable, not the reference. This is because if a ball is part of one snowman, it cannot be part of another.

#####Commands
Snowman supports a variety of fascinating commands.

######new
Allocates a spot for a new snowman.
Used by itself, it will allocate one spot for a snowman.

######destroy
Removes a snowman.

-Used by itself, it will destroy the current snowman.
-Used with a number (ie. destroy 2), it will destroy

######eye
Adds an eye, if available. A snowman can have at most eight eyes. Otherwise, throws an error.

######nose
Creates or deletes the nose on the ball, depending if it has one or not.`
