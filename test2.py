# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

# def bubble_sort(li):
#     for i in range(len(li)-1):
#         for j in range(len(li)-i-1):
#             if li[j] > li[j+1]:
#                 li[j], li[j+1] = li[j+1], li[j]

# def select_sort(li):
#     for i in range(len(li)):
#         min_loc = i
#         for j in range(i+1, len(li)):
#             if li[j] < li[min_loc]:
#                 min_loc = j
#         li[i],li[min_loc] = li[min_loc],li[i]

# def insert_sort(li):
#     for i in range(1, len(li)):
#         tmp = li[i] #找到的牌
#         j = i - 1 #手牌下标
#         while j >= 0 and li[j] > tmp:
#             li[j+1] = li[j]
#             j -= 1
#         li[j+1] = tmp

def partition(li, left, right):
    #去标志值
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left

def _quick_sort(li, left, right):
    if left < right:  #保证至少两个元素
        mid = partition(li, left, right)
        _quick_sort(li, left, mid-1)
        _quick_sort(li, mid+1, right)


import random

li = [random.randrange(1,10) for i in range(100)]
print(li)

_quick_sort(li, 0, len(li) - 1)
print(li)