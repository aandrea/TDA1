#!/usr/bin/python
# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class LkdList(object):
    def __init__(self):
        self.first = self.last = None
        self.length = 0
    
    def insertFirst(self, item):
        node = ListNode(item)
        if self.length == 0 :
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node
        self.length += 1

    def insertLast(self, item):
        node = ListNode(item)
        if self.length == 0:
            self.last = node
            self.first = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1
    
    def getFirst(self):
        if self.first:
            return self.first.item

    def getLast(self):
        if self.last:
            return self.last.item

    def getByIndex(self, index):
        if index > self.length-1:
            raise IndexError("Index out of range")
        i = 0
        node = self.first
        while i < index:
            node = node.next
            i += 1
        return node.item

    def __iter__(self):
        return ListIterator(self)

    def __len__(self):
        return self.length

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "["+",".join([str(i) for i in self])+"]"

    def insertSorted(self, item):       
        if self.length==0 or item <= self.getFirst():
            return self.insertFirst(item)
        if item >= self.getLast():
            return self.insertLast(item)
        new_node = ListNode(item)
        prev = None
        node = self.first
        keepOn= True
        while keepOn:
            prev = node
            node = node.next
            if not node :
                keepOn= False
            elif node.item >= item:
                keepOn= False

        prev.next = new_node
        new_node.next = node

    def insertSortedInverse(self, item):       
        if self.length==0 or item >= self.getFirst():
            return self.insertFirst(item)
        if item <= self.getLast():
            return self.insertLast(item)
        new_node = ListNode(item)
        prev = None
        node = self.first
        keepOn= True
        while keepOn:
            prev = node
            node = node.next
            if not node :
                keepOn= False
            elif node.item <= item:
                keepOn= False

        prev.next = new_node
        new_node.next = node

class ListIterator(object):
    def __init__(self, listObj):
        self.list = listObj
        self.current = self.list.first
    
    def next(self):
        if not self.current:
            raise StopIteration
        item = self.current.item
        self.current = self.current.next
        return item
    
    def hasNext(self):
        return not self.current == None
    
    def __iter__(self):
        return self

