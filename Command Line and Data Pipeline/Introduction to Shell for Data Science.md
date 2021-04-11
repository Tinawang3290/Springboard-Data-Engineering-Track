
# INTRODUCTION TO SHELL FOR DATA SCIENCE

An OS controls the computer's processor, hard drive, and network connection, but its most important job is to run other programs.

Humans need an interface to interact with the OS. The most common one these days is a graphical file explorer, which translates clicks and double-clicks into commands to open files and run programs. Before computers had graphical displays, though, people typed instructions into a program called a command-line shell. Each time a command is entered, the shell runs some other programs, prints their output in human-readable form, and then displays a prompt to signal that it's ready to accept the next command. 

Remark. Typing commands instead of clicking and dragging may seem clumsy at first, but as you will see, once you start spelling out what you want the computer to do, you can combine old commands to create new ones and automate repetitive operations with just a few keystrokes.


## Manipulating files and directories

We will view commands that let you move things around in the filesystem

### Where am I?  ( pwd )
The filesystem manages files and directories (or folders). Each is identified by an absolute path that shows how to reach it from the filesystem's root directory: /home/repl is the directory repl in the directory home, while /home/repl/course.txt is a file course.txt in that directory, and / on its own is the root directory.
To find out where you are in the filesystem, run the command pwd (short for "print working directory"). This prints the absolute path of your current working directory, which is where the shell runs commands and looks for files by default.

### How can I identify files and directories? ( ls )
pwd tells you where you are. To find out what's there, type ls (which is short for "listing") and press the enter key. On its own, ls lists the contents of your current directory (the one displayed by pwd). If you add the names of some files, ls will list them, and if you add the names of directories, it will list their contents.

**Absolute and relative path**

An absolute path is like a latitude and longitude: it has the same value no matter where you are. A relative path, on the other hand, specifies a location starting from where you are: it's like saying "20 kilometers north".

For example, if you are in the directory /home/repl, the relative path seasonal specifies the same directory as /home/repl/seasonal, while seasonal/winter.csv specifies the same file as /home/repl/seasonal/winter.csv. The shell decides if a path is absolute or relative by looking at its first character: if it begins with /, it is absolute, and if it doesn't, it is relative.

### How can I move to another directory? ( cd  )

Just as you can move around in a file browser by double-clicking on folders, you can move around in the filesystem using the command cd (which stands for "change directory").

If you type cd seasonal and then type pwd, the shell will tell you that you are now in /home/repl/seasonal. If you then run ls on its own, it shows you the contents of /home/repl/seasonal, because that's where you are. If you want to get back to your home directory /home/repl, you can use the command cd /home/repl.

How can I move up a directory? ( .. ) , ( . ) and ( ~ )
The parent of a directory is the directory above it. For example, /home is the parent of /home/repl, and /home/repl is the parent of /home/repl/seasonal. You can always give the absolute path of your parent directory to commands like cd and ls. More often, though, you will take advantage of the fact that the special path ..(two dots with no spaces) means "the directory above the one I'm currently in". If you are in /home/repl/seasonal, then cd .. moves you up to /home/repl.

A single dot on its own, ., always means "the current directory", so ls on its own and ls . do the same thing, while cd . has no effect.

One final special path is ~ (the tilde character), which means "your home directory", such as /home/repl. No matter where you are, ls ~ will always list the contents of your home directory, and cd ~ will always take you home.

### How can I copy files? ( cp )

You will often want to copy files, move them into other directories to organize them, or rename them. One command to do this is cp, which is short for "copy". If original.txt is an existing file, then:

cp original.txt duplicate.txt
creates a copy of original.txt called duplicate.txt. If there already was a file called duplicate.txt, it is overwritten. If the last parameter to cp is an existing directory, then a command like:

cp seasonal/autumn.csv seasonal/winter.csv backup
copies all of the files (autumn.csv and winter.csv) into that directory.

### How can I move a file? ( mv )

While cp copies a file, mv moves it from one directory to another, just as if you had dragged it in a graphical file browser. It handles its parameters the same way as cp, so the command:

`mv autumn.csv winter.csv ..`
moves the files autumn.csv and winter.csv from the current working directory up one level to its parent directory (because .. always refers to the directory above your current location).

### How can I rename a file? ( mv )

mv can also be used to rename files. If you run:

`mv course.txt old-course.txt`
then the file course.txt in the current working directory is "moved" to the file old-course.txt. This is different from the way file browsers work, but is often handy.

One warning: just like cp, mv will overwrite existing files. If, for example, you already have a file called old-course.txt, then the command shown above will replace it with whatever is in course.txt.

### How can I delete files? ( rm )

We can copy files and move them around; to delete them, we use rm, which stands for "remove". As with cp and mv, you can give rm the names of as many files as you'd like, so:

`rm thesis.txt backup/thesis-2017-08.txt
removes both thesis.txt and backup/thesis-2017-08.txt`

`rm` does exactly what its name says, and it does it right away: unlike graphical file browsers, the shell doesn't have a trash can, so when you type the command above, your thesis is gone for good.

### How can I create and delete directories? (rmdir) and (mkdir)

mv treats directories the same way it treats files: if you are in your home directory and run mv seasonal by-season, for example, mv changes the name of the seasonal directory to by-season. However, rmworks differently.

If you try to rm a directory, the shell prints an error message telling you it can't do that, primarily to stop you from accidentally deleting an entire directory full of work. Instead, you can use a separate command called rmdir. For added safety, it only works when the directory is empty, so you must delete the files in a directory before you delete the directory. 

Since a directory is not a file, you must use the command mkdir directory_name to create a new (empty) directory. Use this command to create a new directory called yearly below your home directory.

/tmp
You will often create intermediate files when analyzing data. Rather than storing them in your home directory, you can put them in /tmp, which is where people and programs often keep files they only need briefly. (Note that /tmp is immediately below the root directory /, not below your home directory.) This wrap-up exercise will show you how to do that. 



## Manipulating data

This chapter will show you how to work with the data that's in the files. The tools we will look at are fairly simple, but are the model for everything that's more powerful. 

### How can I view a file's contents? ( cat)
Before you rename or delete files, you may want to have a look at their contents. The simplest way to do this is with cat, which just prints the contents of files onto the screen. (Its name is short for "concatenate", meaning "to link things together", since it will print all the files whose names you give it, one after the other.)
How can I view a file's contents piece by piece? ( less)
You can use cat to print large files and then scroll through the output, but it is usually more convenient to page the output. The original command for doing this was called more, but it has been superseded by a more powerful command called less. (This kind of naming is what passes for humor in the Unix world.) When you less a file, one page is displayed at a time; you can press spacebar to page down or type q to quit.
If you give less the names of several files, you can type :n (colon and a lower-case 'n') to move to the next file, :p to go back to the previous one, or :q to quit.

### How can I look at the start of a file? (head)

head prints the first few lines of a file (where "a few" means 10), so the command:

head seasonal/summer.csv
displays the fields and first 10 rows.

Tab completion

One of the shell's power tools is tab completion. If you start typing the name of a file and then press the tab key, the shell will do its best to auto-complete the path. For example, if you type sea and press tab, it will fill in the directory name seasonal/ (with a trailing slash). If you then type aand tab, it will complete the path as seasonal/autumn.csv.

If the path is ambiguous, such as seasonal/s, pressing tab a second time will display a list of possibilities. Typing another character or two to make your path more specific and then pressing tab will fill in the rest of the name.

### How can I control what commands do? (flags)

Shell lets you change head's behavior by giving it a command-line flag (or just "flag" for short). If you run the command:

head -n 3 seasonal/summer.csv
head will only display the first three lines of the file. If you run head -n 100, it will display the first 100 (assuming there are that many), and so on.

A flag's name usually indicates its purpose (for example, -n is meant to signal "number of lines"). Command flags don't have to be a - followed by a single letter, but it's a widely-used convention.

### How can I list everything below a directory?
In order to see everything underneath a directory, no matter how deeply nested it is, you can give ls the flag -R (which means "recursive"); this shows every file and directory in the current level, then everything in each sub-directory, and so on.
To help you know what is what, ls has another flag -F that prints a /after the name of every directory and a * after the name of every runnable program.  

### How can I get help for a command?
To find out what commands do, people used to use the man command (short for "manual"). For example, the command man head brings up this information:

man automatically invokes less, so you may need to press spacebar to page through the information and :q to quit.

The one-line description under NAME tells you briefly what the command does, and the summary under SYNOPSIS lists all the flags it understands. Anything that is optional is shown in square brackets [...], either/or alternatives are separated by |, and things that can be repeated are shown by ..., so head's manual page is telling you that you can either give a line count with -n or a byte count with -c, and that you can give it any number of filenames.

### How can I select columns from a file? ( cut with -f -d)

head and tail let you select rows from a text file. If you want to select columns, you can use the command cut. It has several options (use man cut to explore them), but the most common is something like:

cut -f 2-5,8 -d , values.csv
which means "select columns 2 through 5 and columns 8, using comma as the separator". cut uses -f (meaning "fields") to specify columns and -d (meaning "delimiter") to specify the separator. You need to specify the latter because some files may use spaces, tabs, or colons to separate columns.

### What cut can't do?

cut is a simple-minded command. In particular, it doesn't understand quoted strings. If, for example, your file is:

Name,Age "Johel,Ranjit",28 "Sharma,Rupinder",26
then:

cut -f 2 -d , everyone.csv
will produce:

Age Ranjit" Rupinder"
### How can I repeat commands (history and  !)
history will print a list of commands you have run recently. Each one is preceded by a serial number to make it easy to re-run particular commands: just type !55 to re-run the 55th command in your history (if you have that many). You can also re-run a command by typing an exclamation mark followed by the command's name, such as !head or !cut, which will re-run the most recent use of that command.

### How can I select lines containing specific values? ( grep)

grepselects lines according to what they contain. In its simplest form, grep takes a piece of text followed by one or more filenames and prints all of the lines in those files that contain that text. For example, grep bicuspid seasonal/winter.csv prints lines from winter.csv that contain "bicuspid".

grep can search for patterns as well; we will explore those in the next course. What's more important right now is some of grep's more common flags:

-c: print a count of matching lines rather than the lines themselves
-h: do not print the names of files when searching multiple files
-i: ignore case (e.g., treat "Regression" and "regression" as matches)
-l: print the names of files that contain matches, not the matches
-n: print line numbers for matching lines
-v: invert the match, i.e., only show lines that don't match




## Combining tools

The real power of the Unix shell lies not in the individual commands, but in how easily they can be combined to do new things. This chapter will show you how to use this power to select the data you want, and introduce commands for sorting values and removing duplicates. 

### How can I store a command's output in a file? ( > )
you can use redirection to save any command's output anywhere you want. If you run this command:
head -n 5 seasonal/summer.csv > top.csv
nothing appears on the screen. Instead, head's output is put in a new file called top.csv. You can take a look at that file's contents using cat:

cat top.csv
The greater-than sign > tells the shell to redirect head's output to a file. It isn't part of the head command; instead, it works with every shell command that produces output.


### How can I use a command's output as an input?
Suppose you want to get lines from the middle of a file. More specifically, suppose you want to get lines 3-5 from one of our data files. You can start by using head to get the first 5 lines and redirect that to a file, and then use tail to select the last 3:
head -n 5 file.csv > new_file.csv
tail -n 3 new_file.csv


### What's a better way to combine commands? ( |)
The best way to so it is using a pipe .

Instead of sending head's output to a file, add a vertical bar and the tail command without a filename:

head -n 5 seasonal/summer.csv | tail -n 3
The pipe symbol tells the shell to use the output of the command on the left as the input to the command on the right.

### How can I count the records in a file? ( wc )
The command wc (short for "word count") prints the number of characters, words, and lines in a file. You can make it print only one of these using -c, -w, or -l respectively.

### How can I specify many files at once? (*)
The shell allows you to use wildcards to specify a list of files with a single expression. The most common wildcard is *, which means "match zero or more characters". Using it, we can shorten the cut command from this
cut -d , -f 1 seasonal/winter.csv seasonal/spring.csv seasonal/summer.csv seasonal/autumn.csv
to this:
cut -d , -f 1 seasonal/*

### What other wildcards can I use?

### How can I sort lines of text?
As its name suggests, sort puts data in order. By default it does this in ascending alphabetical order, but the flags -n and -r can be used to sort numerically and reverse the order of its output, while -b tells it to ignore leading blanks and -f tells it to fold case (i.e., be case-insensitive). Pipelines often use grep to get rid of unwanted records and then sortto put the remaining records in order.

### How can I remove duplicate lines? ( uniq )
uniq, its job is to remove adjacent duplicated lines. Note that the use of uniq, and  sort allows to remove all duplicate lines. The flag   -c allows to count the number of times each word occurs

Ex. Count the number of times a word  occurs inside a file

### How can I save the output of a pipe?

The shell lets us redirect the output of a sequence of piped commands:

cut -d , -f 2 seasonal/*.csv | grep -v Tooth > teeth-only.txt
How can I stop a running program?( Ctrl + C )
 If you decide that you don't want a program to keep running, you can type Ctrl + C to end it.






Batch processing

Most shell commands will process many files at once. This chapter will show you how to make your own pipelines do that. Along the way, you will see how the shell uses variables to store information.

### How does the shell store information? Environment variable
Like other programs, the shell stores information in variables. Some of these, called environment variables, are available all the time. Environment variables' names are conventionally written in upper case, and a few of the more commonly-used ones are shown below.to get a complete list, you can type set in the shell.  


### How can I print a variable's value? ( echo and  $ )
A simpler way to find a variable's value is to use a command called echo, which prints its arguments. Typing
echo hello DataCamp!
prints

hello DataCamp!
If you try to use it to print a variable's value like this:

echo USER
it will print the variable's name, USER.

To get the variable's value, you must put a dollar sign $ in front of it. Typing

echo $USER
prints

repl
This is true everywhere: to get the value of a variable called X, you must write $X. (This is so that the shell can tell whether you mean "a file named X" or "the value of a variable named X".)


### How else does the shell store information? shell variable

The other kind of variable is called a shell variable, which is like a local variable in a programming language.

To create a shell variable, you simply assign a value to a name:

training=seasonal/summer.csv
without any spaces before or after the = sign. Once you have done this, you can check the variable's value with:

echo $training
seasonal/summer.csv
How can I repeat a command many times? loops
Shell variables are also used in loops, which repeat commands many times. If we run this command:

for filetype in gif jpg png; do echo $filetype; done
it produces:

gif jpg png
Notice these things about the loop:
Notice that the body uses $filetype to get the variable's value instead of just filetype, just like it does with any other shell variable. Also notice where the semi-colons go: the first one comes between the list and the keyword do, and the second comes between the body and the keyword done.

### How can I repeat a command once for each file?

You can always type in the names of the files you want to process when writing the loop, but it's usually better to use wildcards. Try running this loop in the console:

for filename in seasonal/*.csv; do echo $filename; done
It prints:

seasonal/autumn.csv seasonal/spring.csv seasonal/summer.csv seasonal/winter.csv
because the shell expands seasonal/*.csv to be a list of four filenames before it runs the loop.

### How can I record the names of a set of files?

People often set a variable using a wildcard expression to record a list of filenames. For example, if you define datasets like this:

datasets=seasonal/*.csv
you can display the files' names later using:

for filename in $datasets; do echo $filename; done
This saves typing and makes errors less likely.

### How can I run multiple commands in a single loop?
Printing filenames is useful for debugging, but the real purpose of loops is to do things with multiple files. This loop prints the second line of each data file:
for file in seasonal/*.csv; do head -n 2 $file | tail -n 1; done
It has the same structure as the other loops you have already seen: all that's different is that its body is a pipeline of two commands instead of a single command.


### Why shouldn't I use spaces in filenames?

It's easy and sensible to give files multi-word names like July 2017.csv when you are using a graphical file explorer. However, this causes problems when you are working in the shell. For example, suppose you wanted to rename July 2017.csv to be 2017 July data.csv. You cannot type:

mv July 2017.csv 2017 July data.csv
because it looks to the shell as though you are trying to move four files called July, 2017.csv, 2017, and July(again) into a directory called data.csv. Instead, you have to quote the files' names so that the shell treats each one as a single parameter

### How can I do many things in a single loop?

The loops you have seen so far all have a single command or pipeline in their body, but a loop can contain any number of commands. To tell the shell where one ends and the next begins, you must separate them with semi-colons:

for f in seasonal/*.csv; do echo $f; head -n 2 $f | tail -n 1; done
seasonal/autumn.csv 2017-01-05,canine seasonal/spring.csv 2017-01-25,wisdom seasonal/summer.csv 2017-01-11,canine seasonal/winter.csv 2017-01-03,bicuspid






Creating new tools

History lets you repeat things with just a few keystrokes, and pipes let you combine existing commands to create new ones. In this chapter, you will see how to go one step further and create new commands of your own.

### How can I edit a file?
Unix has a bewildering variety of text editors. For this course, we will use a simple one called Nano. If you type nano filename, it will open filename for editing (or create it if it doesn't already exist). You can move around with the arrow keys, delete characters using backspace, and do other operations with control-key combinations:
Ctrl + K: delete a line.
Ctrl + U: un-delete a line.
Ctrl + O: save the file ('O' stands for 'output').
Ctrl + X: exit the editor.


### How can I record what I just did?
When you are doing a complex analysis, you will often want to keep a record of the commands you used. You can do this with the tools you have already seen.


### How can I save commands to re-run later?
Use nano dates.sh to create a file called dates.sh that contains this command:cut -d , -f 1 seasonal/*.csv
to extract the first column from all of the CSV files in seasonal.
Then, just run it by typing   bash dates.sh


### How can I re-use pipes?
A file full of shell commands is called a *shell script, or sometimes just a "script" for short. Scripts don't have to have names ending in .sh, but this lesson will use that convention to help you keep track of which files are scripts.
Scripts can also contain pipes. For example, if all-dates.sh contains this line:

cut -d , -f 1 seasonal/*.csv | grep -v Date | sort | uniq
then:

bash all-dates.sh > dates.out
will extract the unique dates from the seasonal data files and save them in dates.out.


### How can I pass filenames to scripts? ( $@ )

A script that processes specific files is useful as a record of what you did, but one that allows you to process any files you want is more useful. To support this, you can use the special expression $@ (dollar sign immediately followed by at-sign) to mean "all of the command-line parameters given to the script". For example, if unique-lines.sh contains this:

sort $@ | uniq
then when you run:

bash unique-lines.sh seasonal/summer.csv
the shell replaces $@ with seasonal/summer.csv and processes one file. If you run this:

bash unique-lines.sh seasonal/summer.csv seasonal/autumn.csv
it processes two data files, and so on.



### How can I process specific amount of arguments? ( $1, $2  , ...)

As well as $@, the shell lets you use $1, $2, and so on to refer to specific command-line parameters. You can use this to write commands that feel simpler or more natural than the shell's. For example, you can create a script called column.sh that selects a single column from a CSV file when the user provides the filename as the first parameter and the column as the second:

cut -d , -f $2 $1
and then run it using:

bash column.sh seasonal/autumn.csv 1
Notice how the script uses the two parameters in reverse order.


### How can one shell script do many things?

Our shells scripts so far have had a single command or pipe, but a script can contain many lines of commands. For example, you can create one that tells you how many records are in the shortest and longest of your data files, i.e., the range of your datasets' lengths.

Note that in Nano, "copy and paste" is achieved by navigating to the line you want to copy, pressing CTRL + K to cut the line, then CTRL + Utwice to paste two copies of it.

Ex. Obtaining the range of our datasets's length. The script isAnd the next command is

### How can I write loops in a shell script?

Shell scripts can also contain loops. You can write them using semi-colons, or split them across lines without semi-colons to make them more readable:

# Print the first and last data records of each file. for filename in $@ do         head -n 2 $filename | tail -n 1         tail -n 1 $filename done
The first line of this script is a comment to tell readers what the script does. Comments start with the # character and run to the end of the line.s



