if __name__ == '__main__':
    n = int(raw_input())
    arr =list( map(int, raw_input().split()))
max_num = max(arr)
j=0
while (j<n) :
    if max_num == max(arr):
        arr.remove(max(arr))
    j=j+1    
print(max(arr)) 
