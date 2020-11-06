# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:42:31 2020

@author: micha
"""

# Create a program that manages a to do list.  The program should support:
# creating a new list,
# appending to an existing list,
# and printing out the current list.
# There should be exception handling when the program tries to read a file
# and it does not exist. When you run the program it should ask the user to
# Enter 1 if they want to create a list, 2 if they want to append to a current list,
# and 3 if they want to print the current list.   


# 1
# If they want to create the list you will need to ask for the file name to
# create and the number of items to add to the list.  Then ask the user to
# enter those items. When the items are added the full list should be printed out.

#structure of TO DO to_do[1] = daily_tasks
#               daily_tasks = [{'title': titles(1)}]
#                     the dictionary allows for easy search for the titles
#                     titles is a list that holds all of the titles of the to do lists

#functions to create a to do list in the notebook
def create_list(table_of_contents, num_of_to_do_lists, clean_file_boolean):
    #create file name
    file = create_title(num_of_to_do_lists, txt_file)
    #if catch_error(file, clean_file_boolean) == False:
    #    create_list(table_of_contents, num_of_to_do_lists, clean_file_boolean)
    table_of_contents.append(file)
    #create file and open
    with open(file, 'w') as note:
        pass
    notebook.append(note)
    #add items to the to do list
    note = append_items(file, note)
    note = open(file, 'r')
    print_file(note, file)
    note.close()

#try catch error for opening file - if it does not exist
def catch_error(file, clean_file_boolean):
    try:
        open(file, 'r')
        pass
    except FileNotFoundError:
        print('File does not exist')
        clean_file_boolean = False
    return clean_file_boolean

#funtion to create the file name for the to do list
def create_title(num_of_to_do_lists, txt_file):
    #concatenate title and whatever number of to do list i am on example title1
    #global temp_list_title
    temp_list_title = input("Enter to title of the to do list:    ")
    temp_list_title = temp_list_title.strip()
    temp_file = create_file(temp_list_title, txt_file)
    #temp_list_title_with_num = temp_list_title + str(num_of_to_do_lists)
    
    # increase number of to do lists in table of contents
    num_of_to_do_lists = num_of_to_do_lists + 1
    return temp_file
    
#creates file from the title for the list that the user inputs
def create_file(temp_list_title, txt_file):
    temp_file = temp_list_title + txt_file
    return temp_file

# appends items to a file            
def append_items(file, note):
    note = open(file, 'a')
    num = int(input("How many items would you like to add to the To Do list?    "))
    new_lines = []
    i = 0
    while i < num:
        new_lines.append(input("Enter new item    "))
        i = i+1
    for x in new_lines:
        note.writelines(x + "\n")
    note.close()
    return note

#finds the text file that the user wants to access #is this a necessary function??
def find_file(txt_file):
    temp_list_title = input("Enter to title of the text file you would like to open (omit .txt):    ")
    temp_list_title = temp_list_title.strip()
    file = temp_list_title + txt_file
    return file

def print_file(note, file):
    note = open(file, 'r')
    print(note.read())
    note.close()
    return note

#finds the file in the table_of_contents then uses the matching indice to open the file in the notebook
#def find_file_position(file, txt_file):
#    global note
#    for x in table_of_contents:
#        if file == table_of_contents:
#            note = table_of_contents(x)
#            break
#        else:
#            x = x+1
#    return note
    
    
#def create_list_items():
#    number_items = int(input("How many items would you like on the To-Do List?    "))
 
# 2
# If they want to append to a current list you will need to ask the name of
# the file containing the ilst and the number of items to append.  Then ask
# the user to enter those items. When the items are added the full list should be printed out.

def Append(txt_file):
    file = find_file(txt_file)
    #note = find_file_position(file, txt_file)
    if catch_error(file, clean_file_boolean) == False:
        return
    note = open(file, 'r+')
    note = append_items(file, note)
    print_file(note, file)
 
# 3
# If they want to print the list you will need to ask them for the file name
# of the list and print out those items. 

def print_existing_file(txt_file):
    #switch variable to allow to use in print function
    file = find_file(txt_file)
    if catch_error(file, clean_file_boolean) == False:
        return
    with open(file, 'r') as note:
        pass
    #note = find_file_position(file, txt_file)
    print_file(note, file)
    note.close()


#MAIN --- RUN CODE
#print(create_list(table_of_contents, num_of_to_do_lists))

# overlapping features

#stores files
notebook = []

#for usage in the create_list function to iterate in list
notebook_indice = 0

txt_file = ".txt"
# stores file titles --- variable is uselss now because the program is not looped
table_of_contents = []

# the total number of to do lists
num_of_to_do_lists = 0

tb_con_indice = num_of_to_do_lists - 1

clean_file_boolean = True

import glob
import os

#prints all txt files in the folder
os.chdir(r'C:\Users\micha\OneDrive\School\CSC 201\Project 2')
myFiles = glob.glob('*.txt')
print("Txt files in folder:" + "\t" + str(myFiles))


#repeat = True

process_num = int(input("If you want to create a new list, enter 1. If you would like to append to a current list, enter 2. If you would like to print an existing list, enter 3.    "))
#print(table_of_contents)
if process_num == 1:
    create_list(table_of_contents, num_of_to_do_lists, clean_file_boolean)
if process_num == 2:
    Append(txt_file)
if process_num == 3:
    print_existing_file(txt_file)
if process_num < 1 or process_num > 4:
    print("The number you entered is not applicable")

    #user_choice_repeat = bool(input("Would you like to preform another function? If yes, enter True. If no, enter False"))
    #if user_choice_repeat == repeat:
    #    main()
    #else:
    #    return
    
#run = main()

# You should use functions where appropriate to improve readability, reliability,
# and reusability.  Programs that do not have functions to break up the work will
# be marked down heavily, even if they work!

