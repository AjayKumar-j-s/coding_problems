def merge(a,l,mid,r):
    left = l
    print(l,r,"=")
    t = []
    right = mid+1
    # print(l,mid,right)
    while(left<=mid and right<=r):
        if(a[left]<a[right]):
            t.append(a[left])
            left+=1
        else:
            t.append(a[right])
            right+=1
    while(left<=mid):
        t.append(a[left])
        left+=1
    while(right<=r):
        t.append(a[right])
        right+=1
    for i in range(l,r+1):
        print(i,"=",i)
        a[i] = t [i-l]
    print(a)


def ms(a,l,r):
    if(l<r):

        mid = (l+r)//2
        print(l, mid, r)
        ms(a,l,mid)
        ms(a,mid+1,r)
        merge(a,l,mid,r)



a = [5,4,6,7,1,2]
ms(a,0,len(a)-1)



# def merge(arr, left, mid, right):
#     n1 = mid - left + 1
#     n2 = right - mid
#
#      # Create temp arrays
#      L = [0] * n1
#      R = [0] * n2
#
#      # Copy data to temp arrays L[] and R[]
#      for i in range(n1):
#          L[i] = arr[left + i]
#      for j in range(n2):
#          R[j] = arr[mid + 1 + j]
#
#      i = 0  # Initial index of first subarray
#      j = 0  # Initial index of second subarray
#      k = left  # Initial index of merged subarray

# #     # Merge the temp arrays back
# #     # into arr[left..right]
# #     while i < n1 and j < n2:
# #         if L[i] <= R[j]:
# #             arr[k] = L[i]
# #             i += 1
# #         else:
# #             arr[k] = R[j]
# #             j += 1
# #         k += 1
# #
# #     # Copy the remaining elements of L[],
# #     # if there are any
# #     while i < n1:
# #         arr[k] = L[i]
# #         i += 1
# #         k += 1
# #
# #     # Copy the remaining elements of R[],
# #     # if there are any
# #     while j < n2:
# #         arr[k] = R[j]
# #         j += 1
# #         k += 1
# #     print(arr)
# #
# #
# # def mergeSort(s,e,a):
# #     if(s>=e):
# #         return
# #     if(s<e):
# #         m = (s+e)//2
# #         print(s,e)
# #         mergeSort(s,m,a)
# #         mergeSort(m+1,e,a)
# #         merge(a,s,m,e)
# #
# # l = [9,8,7,6,5,4,3,2,1]
# # mergeSort(0,len(l)-1,l)
#  print(l)