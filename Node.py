__author__ = 'Carol'

class Node:

    key = None
    next =  None

    def __init__(self,key,next=None):

        self.key = key
        self.next = next

    def __repr__(self):

        return str(self.key)


#def createList(*args):

