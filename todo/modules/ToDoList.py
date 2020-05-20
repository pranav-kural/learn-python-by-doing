""" Simple To Do App - list manager """

# importing required modules
import modules.ToDoItems as items

""" 
Show list of all items in pending state

Returns:
    items in pending state   
"""


""" 
Show list of all items in completed state

Returns:
    items in completed state   
"""


""" 
Show list of all items

Returns:
    list of all items   
"""
def showAllItems():
    
    ##print("ToDoList invoked")
    
    # get all items
    AllItems: dict = items.getItemsWithState()
    
    # check if there are no items available
    if len(AllItems) == 0:
        print("No tasks present in the ToDo list.")
        
        # ask user if he wants to add new task
        user_input = input("Would you like to add new tasks? (y or n): ")
        
        ##print(f"{user_input} .. {len(user_input)}")
        
        while user_input != "y" and user_input != "n":
            print("Invalid entry!")
            user_input = input("Would you like to add new tasks? (y or n)")
    
        if user_input == 'y': AddNewItems() 
        else: return
             
    i: int = 1
    ToDoList: dict = dict()
    
    for (item, state) in AllItems.items():
        ToDoList.update({i: item})
        print(f"{i}. {item} -> {state}")
        i += 1
        
    return ToDoList


""" 
Add item to the to do list

Returns:
    getItemsWithState()    
"""
def AddNewItems():
    
    # ask user for item to add
    user_input: str = input("\nEnter an item to be added\nEnter 'done' once finished\n--> ")
    # define list to hold items to be added
    itemsToAdd: list = list()
    
    # run until user enters 'done' as input
    while user_input != "done":
        # add the last provided value to list
        itemsToAdd.append(user_input)
        # ask for next item
        user_input: str = input("\nEnter an item to be added\nEnter 'done' once finished\n--> ")
    
    # add items
    items.addItems(itemsToAdd)
        
        
def removeItem():
    """ 
    Remove item from the to do list

    Returns:
        getItemsWithState()    
    """

    # show list of current items
    ToDoList: dict = showAllItems()
    
    # check to make sure the list is not empty
    if len(ToDoList) == 0: 
        print("Please add items to the list before they can removed.")
        return
    
    # ask for item number from list to be deleted
    user_input = input("\nEnter the number of the item which you want removed from the above list.\n(or enter 'done' once finished)\n--> ")
    
    # define list to hold items to be removed
    itemsToRemove: list = list()
    
    # run until user enters 'done' as input
    while user_input != "done":
        
        try:
            # convert input to number
            itemNumber: int = int(user_input)
            
            ##print(f"len todolist: {len(ToDoList)}")
            ##print(f"todolist: {ToDoList}")
            
            # check to make sure the number is within range
            if itemNumber <= 0 or itemNumber > len(ToDoList): raise Exception("Number out of range")
        
            # check if number entered was already entered previously
            if ToDoList[itemNumber] in itemsToRemove: raise Exception("Item already selected for removal.")
        
            # add the last provided value to list
            # NOTE: need to handle index out of range error;
            #       or put a check for range before this step
            itemsToRemove.append(ToDoList[itemNumber])
            
        except:
            print(f"Your entry of {user_input} is invalid. Enter a valid number from the list.")
          
        finally:  
            # if all items have been selected to delete
            if len(itemsToRemove) == len(ToDoList): 
                print("All items have been selected to be deleted.")
                break
            else:
                # ask user for input again
                user_input: str = input("Enter an item to be removed\nEnter 'done' once finished\n--> ")
    
    ##print(f"items to remove: {itemsToRemove}")
    
    # remove items
    items.removeItems(itemsToRemove)
   
     
""" 
Mark an item as complete

Returns:
    list of all items    
"""     

""" 
Mark an item as pending

Returns:
    list of all items    
"""