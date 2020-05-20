""" Simple To Do App - main app file  """

# import modules
import modules.ToDoList as todolist


""" 
Display a list of all current items with their state, and ask user for an input to continue    
"""
def displayToDoList():
    ToDoList: dict = todolist.showAllItems()

    user_input = input("Choose an option:\n1. Add a new task 2. Remove an existing task\n(or enter 'exit' to quit the application): ")
    
    while user_input != 'exit':
        if user_input == '1':
            addItem()
            todolist.showAllItems()
        elif user_input == '2':
            removeItem()
            todolist.showAllItems()
        else:
            print("Invalid option selected.")
            
        user_input = input("Choose an option:\n1. Add a new task 2. Remove an existing task\n(or enter 'exit' to quit the application): ")

    
""" 
Add item to the to do list

Returns:
    display list of all current items    
"""
def addItem():
    todolist.AddNewItems()

""" 
Remove item from the to do list

Returns:
    display list of all current items    
"""
def removeItem():
    todolist.removeItem()

""" 
Mark an item as complete

Returns:
    list of all current items    
"""


""" 
Mark an item as pending

Returns:
    list of all current items    
"""

""" Main """
def main():
    ##print("main invoked")
    displayToDoList()

# run main method if executing from shell/cmd-line
if __name__ == '__main__': 
    main()