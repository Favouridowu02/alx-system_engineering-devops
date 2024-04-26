# This is The readme for the Loops, Conditions and Parsing

##Bash Scripting

The For loop
The while loop
The until loop - Thus executes as long as the Command has not been met yet

$@ - this refers to all the arguments that are [ased to the file, this is usually the exit status of the last command that was ran

for boy [in LIST]; do COMMANDS; done

Comparison Operators
ne, eq, lt, gt,  ge, le, 
Compound Comaprison
-a the add operator
-o the or opertaor

File Test Operator
-e, -a Checkes if the file exists
-f Checks if the file is a regular file
-s If the file is not zero in size
-d The file is a Directory
-b CHecks if the file is a device block
-h, -L Checks if the file is a symbolic link
-c Checks if the file is a chartacter
f1 -nt f2 : This checks if f1 is newer than f2
-ot
f1 -ef f2 : if f1 and f2 are hard links to the same file

the type command is used to find the location of a global variable

