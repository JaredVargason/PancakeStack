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

To create a ball variable, you must say "ball <NAME>".
It is the more common structure used in Snowman. 
A ball has the following attributes:

size
nose
eyes
mouth
buttons
hat
arms

Similarly, if you want to create a snowman variable, use "snowman <NAME>".
A snowman is a stack of balls. However, there are rules to follow:

1) A ball must be smaller than the one below it. This is just how snowmen were meant to be.
2) There are limits to the number of each type of item.

Variables can be named using lowercase and uppercase letters, digits, and underscores.

It is easy to get confused with naming, so we recommend naming balls after their respective snowmen. For example, on a snowman "charlie" name your ball variable "charlie_base".

Variables can be assigned to other variables:

`ball carl_head = robert_head` 
`carl = robert

 However, this will copy the value to the assigned variable, not the reference. This is because if a ball is part of one snowman, it cannot be part of another.

#####Commands
Snowman supports a variety of fascinating commands.


######destroy(snowman)
Removes a snowman, freeing up the space it occupied.
`destroy(carl)` will destroy the snowman named carl.

######push(ball, snowman)
Adds a ball to the specified snowman. This will remove the variable

######pop(snowman)
Removes the top ball from the snowman given. 
Throws an error if the snowman has no balls.

######eye
Adds an eye, if available. A snowman can have at most eight eyes. Otherwise, throws an error.

######nose
Creates or deletes the nose on the ball, depending if it has one or not.`
