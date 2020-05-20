""" Simple To Do App - items manager """

# define items globally
items:dict = dict()


def getItemsWithState():
    """ 
    Get all items in items collection with both item and its state

    Returns:
        items collection
        
    """
    return items


def getItems():
    """ 
    Get all items in items collection but without state information

    Returns:
        items collection, keys only
        
    """
    return items.keys()


def addItems(itemsToAdd: list):
    """ 
    Add one or more items to the items collection

    Args:
        string value of item to be added

    Returns:
        getItemsWithState()    
    """
    [items.update({itemToAdd: 'pending'}) for itemToAdd in itemsToAdd]
    return getItemsWithState()


def removeItems(itemsToRemove: list):
    """ 
    Remove one or more items from the items collection

    Args:
        string value of item to be removed

    Returns:
        getItemsWithState()    
    """
    [items.pop(itemToRemove) for itemToRemove in itemsToRemove]
    return getItemsWithState()


def reset():
    """ 
    delete all contents of the items collection

    Returns:
        getItemsWithState()    
    """
    items.clear()