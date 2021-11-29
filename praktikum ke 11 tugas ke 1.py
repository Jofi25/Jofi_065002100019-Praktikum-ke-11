# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 14:15:03 2021

@author: jofi
"""

print('ini Sebelum diurutkan [1,5,10,15,20,25,30,9]')
def bubbleSort(array):
    for passnum in range(len(array)-1,0,-1):
        for i in range(passnum):
            if array[i]>array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp

def binary_search(array,num_find):

    mulai = 0
    end = len(array) - 1
    mid = (mulai + end)//2
    found = False
    position = -1
    bubbleSort(array)
    while mulai <= end:
        if array[mid] == num_find:
            found = True
            position = mid
            break
        if num_find > array[mid]:
            mulai = mid + 1
            mid = (mulai + end)//2
        else:
            end = mid - 1
            mid = (mulai + end)//2

    print("Sesudah diurutkan: ", array)
    return (found, position-1)

array=[1,5,10,15,20,25,30,9]
number = int(input('Silahkan anda Masukkan angka yang dicari: '))

found = binary_search(array,number )
if found[0]:
    print('Nomor %d ditemukan di posisi %d'%(number, found[1]+2))
else:
    print('Nomor %d tidak ditemukan'%number)
