Simple Todo App

    Strategy -
        
        - add items
        - remove items (by number in list)
        - mark items completed
        - show items pending
        - show items completed
        - show all items
        - reset
    
    Data -
        
        items = {item -> state}
            ex: {'did this' -> 'completed', 'do that' -> 'pending'}
            
    Actions -
    
        add -
            items.update({item:'pending'})
        remove -
            show list of items pending with number
                (method - show pending items)
            itemToBeRemoved = items[numberSelected]
            items.pop(itemToBeRemoved)
            Give confirmation of item removed
        show pening items
            show pending items with numbers
        show completed items
            show completed items with numbers
        show all items
            show all items with number and state
        reset
            reset all items

    Structure -

        App structure: 
            SimpleToDoApp   - top layer
            ToDoItems       - data layer
            ToDoList        - functionality layer

        SimpleToDoApp
                |
                |----- ToDoItems
                |           |----- addItems(key)        :getItemsWithState()
                |           |----- removeItems(key)     :getItemsWithState()
                |           |----- getItems             :items(keys)
                |           |----- getItemsWithState    :items
                |           |----- reset                :items
                |
                |----- ToDoList
                |           |----- showPendingItems     :items(value=pending)
                |           |----- showCompletedItems   :items(value=completed)
                |           |----- showAllItems         :items
                |           |----- addNewItem           :items
                |           |----- removeItem           :items
                |           |----- markItemCompleted    :item, items
                |           |----- markItemPending      :item, items
        
