class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, starting_index, pivot_index): #  put pivot to the right place + return index of pivot
    # 1.
    print "--------------------- tri + placement pivot"
    printarr(arr, starting_index, pivot_index)
    i = ( starting_index-1 )         # index of smaller element || per default = first element > then last element <pivot && swaped
    pivot = arr[pivot_index]     # pivot
    print "pivot=", pivot
    print "i=", i # -1 then index's value > pivot to be swap with next value < pivot || last element's ex-index of last item < pivot having been swapped with j (iterator)
    # 2.
    for j in range(starting_index , pivot_index):
        print "arr[j="+str(j)+"]=", bcolors.BOLD, arr[j], bcolors.ENDC , "<=?", "pivot=", bcolors.BOLD, pivot, bcolors.ENDC
        if   arr[j] <= pivot:
            i = i+1
            print " > i=", i
            # printarr(arr, starting_index, pivot_index),
            print " > swap arr[i=" + str(i) + "] =", bcolors.FAIL, arr[i], bcolors.ENDC, "/ arr[j=" + str(j) + "] =", bcolors.FAIL, arr[j], bcolors.ENDC
            arr[i],arr[j] = arr[j],arr[i]
            printarr(arr, starting_index, pivot_index)
    # 3. mettre le pivot a sa place
    print "------- placing pivot ---------"
    i = i+1
    print " > i=", i
    print "swap arr[i=" + str(i) + "] =", bcolors.FAIL, arr[i], bcolors.ENDC, "/ arr[pivot_index=" + str(pivot_index) + "] =", bcolors.FAIL, arr[pivot_index], bcolors.ENDC
    arr[i],arr[pivot_index] = arr[pivot_index],arr[i]
    printarr(arr, starting_index, pivot_index)
    print "--------------------- tri + placement pivot"
    print bcolors.FAIL + "new pivot_index =", i, bcolors.ENDC, "\n\n"
    return (i)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# starting_index  --> Starting index,
# pivot_index  --> Ending index

# Function to do Quick sort
def quickSort(arr, starting_index, pivot_index):
    print bcolors.WARNING + ">>>>>>>>>> start_i=", starting_index, "<? piv_i =", pivot_index, "<<<<<<<<", bcolors.ENDC
    if starting_index < pivot_index:
        # 1. pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, starting_index, pivot_index)
        print pi-1, "|| pi =", pi, "||", pi+1
        # Separately sort elements before partition and after partition
        printarr(arr, starting_index, pivot_index)
        print bcolors.OKGREEN + "[1-------P       ].quicksort(arr, " + str(starting_index) + ", " + str(pi-1) + ")" + bcolors.ENDC
        quickSort(arr, starting_index, pi-1) # [--------P       ]
        print bcolors.OKGREEN + "[        P2------].quicksort(arr, " + str(pi+1) + ", " + str(pivot_index) + ")" + bcolors.ENDC
        quickSort(arr, pi+1, pivot_index)    # [        P-------]

def printarr(arr, a, b):
    n = len(arr)
    for i in range(n):
        if i in range(a, b + 1):
            print bcolors.BOLD + str(arr[i]),
        else:
            print bcolors.OKBLUE + str(arr[i]),
        print bcolors.ENDC,
    print('')

# Driver code to test above
arr = [6, 7, 3, 4, 8, 9, 1, 5]
n = len(arr)

quickSort(arr,0,n-1)

print ("\nSorted array is:")
printarr(arr, 0, n-1)
