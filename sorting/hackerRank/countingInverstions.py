



def countInversions(arr):

    count = [0]

    def merge_sort(array, left_index, right_index):
        if left_index >= right_index:
            return

        middle = (left_index + right_index)//2
        merge_sort(array, left_index, middle)
        merge_sort(array, middle + 1, right_index)
        merge(array, left_index, right_index, middle)

    def merge(array, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge
        #print("array: ",array)
        # The second parameter is non-inclusive, so we have to increase by 1
        left_copy = array[left_index:middle + 1]
        right_copy = array[middle+1:right_index+1]

        # Initial values for variables that we use to keep
        # track of where we are in each array
        left_copy_index = 0
        right_copy_index = 0
        sorted_index = left_index

        l0 = len(left_copy)
        r0 = len(right_copy)

        # Go through both copies until we run out of elements in one
        while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

            # If our left_copy has the smaller element, put it in the sorted
            # part and then move forward in left_copy (by increasing the pointer)
            if left_copy[left_copy_index] <= right_copy[right_copy_index]:
                array[sorted_index] = left_copy[left_copy_index]
                left_copy_index = left_copy_index + 1
            # Opposite from above
            else:
                #print("left:",left_copy[left_copy_index], "right",right_copy[right_copy_index] )
                array[sorted_index] = right_copy[right_copy_index]
                right_copy_index = right_copy_index + 1



                remaining = l0-left_copy_index
                #print("remaining: ",remaining)
                count.append(count[-1]+remaining)

            # Regardless of where we got our element from
            # move forward in the sorted part
            sorted_index = sorted_index + 1

        # We ran out of elements either in left_copy or right_copy
        # so we will go through the remaining elements and add them
        while left_copy_index < len(left_copy):
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
            sorted_index = sorted_index + 1

        while right_copy_index < len(right_copy):
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1
            sorted_index = sorted_index + 1
            

    #print(arr)
    merge_sort(arr,0,len(arr)-1)
    #print(arr)
    
    print(count[-1])
    return count[-1]

countInversions([1,1,1,2,2])
countInversions([2,1,3,1,2])


countInversions([1,5,3,7])
