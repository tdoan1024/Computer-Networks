#Tai Doan
#Computer Networks
#Warm up assignment
#Python

import re


def Hello():
    name = input("What's your name? ")
    print("Hello " , name , ", nice to meet you!")

def LowerLine():
    fileName = input("Please type in file name(with .txt): ")
    file = open(fileName, 'r').read()
    file = file.lower()
    file = re.sub(r"[\n\t\s]*", "", file)
    print(file)
    for i in range(97,123):
        print(chr(i),file.count(chr(i)))
    for i in range(48,58):
        print(chr(i), file.count(chr(i)))

def ReverseList(list):
    rev_list = list[::-1]
    return rev_list

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
            self.head = None
    def __add__(self,data):
        nNode = Node(data)
        nNode.next = self.head
        self.head = nNode
    def CycleLinkedList(self):
        key = set()
        temp = self.head
        while (temp):
            if (temp in key):
                return 1
            else:
                key.add(temp)
                temp=temp.next
        return 0

#Test function Hello()
Hello()

#Test function LowerLine()
#file name to put in: Fn2Text.txt
LowerLine()

#Test function ReverseList(list)
l = ['1','2','3','hello','my','friend'] #original list
l2 =[]                                  #reversed list
l2 = ReverseList(l)
print(l)
print(l2)

#Test function CycleLinkedList()
l = LinkedList()
l.__add__(1)
l.__add__(10)
l.__add__(2)
l.__add__(4)

l1 = LinkedList()
l1.__add__(2)
l1.__add__(4)
l1.__add__(6)

#l is a cycle linked list
l.head.next.next.next.next = l.head.next.next
if(l.CycleLinkedList() == 0):
    print("List l is not a cycle linked list")
else:
    print("List l is a cycle linked list")

#l1 is not a cycle linked list
if(l1.CycleLinkedList() == 0):
    print("List l1 is not a cycle linked list")
else:
    print("List l1 is a cycle linked list")
