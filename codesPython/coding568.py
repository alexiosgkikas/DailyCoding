"""
Daily Coding Problem: Problem #568 [Easy] 
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given a sorted list of integers, square the elements and give the output in sorted order.
For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

"""
def square_sorted(arr):
  ls = []
  left  = 0
  right = len(arr)-1
  while(left<=right):
    if abs(arr[left])>=abs(arr[right]):
      ls.insert(0,arr[left]*arr[left])
      left+=1
    else:
      ls.insert(0,arr[right]*arr[right])
      right-=1
  return ls

if __name__ == "__main__":
    arr = [-9, -2, 0, 2, 3]
    print(arr)
    print(square_sorted(arr))
