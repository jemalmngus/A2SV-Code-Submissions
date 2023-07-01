
class Solution: 
    def select(self, arr, i):
        sm=i
        for k in range(i+1,len(arr)):
         if arr[k] < arr[sm] :  
          sm=k
        return sm
    
    def selectionSort(self, arr,n):
        for i in range(0,len(arr)-1):
            sm=self.select(arr,i)
            arr[i],arr[sm]=arr[sm],arr[i]
        return arr



if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
