# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a Python dictionary.
#              Add the each dictionary "row" to a Python list "table".
# ChangeLog (Who,When,What):
#     RRoot,1.1.2030,Created started script
#     CMathews,8.10.2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# Declare variables and constants.
strFile = "ToDoList.txt"  # Data storage file.
objFile = None  # An object that represents a file.
strData = ""  # A row of text data from the file.
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}.
lstTable = []  # A list that acts as a 'table' of rows.
strMenu = ""  # A menu of user options.
strChoice = ""  # A capture the user option selection.

# -- Processing -- #
# Step 1 - When the program starts, load any current data.
# In a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open(strFile, "a")
lstHeader = ["Task", "Priority"]

# -- Input/Output -- #
# Step 2 - Display a menu of options to the user and collect input.
while (True):
    print("""
    Menu of Options:\n
    \t1) Show current tasks.
    \t2) Add a new task.
    \t3) Remove an existing task.
    \t4) Exit program.
    """)
    strChoice = str(input("Which option would you like to perform? [1 - 4]: "))
    # Step 3 - Show the current items in the table.
    if (strChoice.strip() == '1'):
        objFile = open(strFile, "r")
        print("\n\tYour current items:")
        print("\t" + lstHeader[0], lstHeader[1] + "\n", sep=" | ")
        for row in objFile:
            lstRow = row.split(',')
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
            print('\t' + dicRow["Task"] + " | " + dicRow["Priority"])
        continue
    # Step 4 - Add a new item to the list/table and save changes to the .txt file.
    elif (strChoice.strip() == '2'):
        objFile = open(strFile, "a")
        print("\nEnter a to-do list task and the associated priority.\n")
        strItem = input("\tTask: ")
        strPriority = input("\tPriority: ")
        lstTable.append([strItem, strPriority])
        for row in lstTable:
            objFile.write(row[0] + "," + row[1] + '\n')
        print("\nTask added!")
        continue
    # Step 5 - Remove an existing item from the list/table.
    elif (strChoice.strip() == '3'):
        objFile = open(strFile, "r")
        print("\n\tYour current items:")
        print("\t" + lstHeader[0], lstHeader[1] + "\n", sep=" | ")
        for row in objFile:
            lstRow = row.split(',')
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
            print('\t' + dicRow["Task"] + " | " + dicRow["Priority"])
        task = input("\nRemove which task?: ")
        if task in lstTable:
            del lstTable[task]
            print("Task was deleted from the to-do list.")
        else:
            print(task, "isn't on the to-do list.")
        continue
    # Step 6 - Exit program.
    elif (strChoice.strip() == '4'):
        objFile.close()
        print("\n\tGoodbye!")
        break
    else:
        print("\n**Please enter a number from the listed options.**")
