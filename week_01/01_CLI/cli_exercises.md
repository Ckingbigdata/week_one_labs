# Fundamentals Exercise 1: CLI

Perform the following tasks using the CLI and copy and paste
the commands and results below.

- Navigate to your home directory
cd ~
- Create a new directory called CodingNomads. We will use this folder
to house materials for the course.
mkdir CodingNomads

- Move into the CodingNomads folder
cd CodingNomads

- Create new folder cli_testing
mkdir cli_testing

- Inside of folder cli_testing,
    a. print the directory path
pwd
    
    b. create 3 new .txt files all with different names (file1.txt,
    file2.txt, file3.txt)
    
touch file1.txt file2.txt file3.txt
 
    c. list the contents of the folder
ls-al   
    d. rename one of the files
mv file_1 birdman.txt   
 
- Inside of folder cli_testing, create a new folder
mkdir new_folder

- Copy a file from cli_testing to the new folder
cp birdman.txt new_folder

- Move a different file from cli_testing to the new folder
cp file.txt2 new_folder

- Demonstrate removing:
    a. A file
rm file3.txt

    b. A folder
rm -rf new_folder


## vim

- Use `$ vim` to write some text inside a file
vim birdman.txt
- Use `$ cat` print contents of file
cat birdman.txt
"the rubbing hands is a symbol of hustling"
# to exit use esc then :wq
- Use `$ grep` to search for a word inside file
grep "hustling" birdman.txt


## explore advanced CLI

- What is the difference between the two commands > and >>?
While both create files if they do not exist, > will overwrite a file if it exists
and >> will append to the file if it exists

# not sure about navigating in and out of vim..for review
Create a file hello.txt with the text "how?!", then append the text to another file called my_file.txt 
touch hello.txt 
vim i
hello.txt 
touch my_file.txt 
--> cat hello.txt >> my_file.txt

Overwrite the content of my_file.txt with "tell me" 
--> echo "tell me" > my_file.txt
- Create a file hello.txt with the text "how?!", then append the text
    to another file called my_file.txt
    
- Overwrite the content of my_file.txt with "tell me"
tell me >> my_file.txt
