__author__ = 'Carol'

from Node import Node

def peakFindList(L):

    #print str(L.key) + ' < '  + str(L.next.key)
    if (L.next == None):
        return L


    if (L.key < L.next.key):
       return peakFindList(L.next)
    else: return L


l6 = Node(key=1)
l5 = Node(key=4,next=l6)
l4 = Node(key=6,next=l5)
l3 = Node(key=7,next=l4)
l2 = Node(key=2,next=l3)
l1 = Node(key=4,next=l2)
l0 = Node(key=13,next=l1)


print peakFindList(l0)
