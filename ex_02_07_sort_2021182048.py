array = [
       46,      82,      21,      58,      22,      54,      71,     215,      99,     227, 
       73,      24,      17,      44,     244,      78,      25,      66,      47,       3, 
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92, 
       83,     100,      94,      40,       5,     458,     364,      26,      64,     735, 
       90,     489,      72,     504,      88,      97,     226,     218,     186,     168, 
]

def sort_bubble(arr):
  print('-' * 60)
  print(f'before: {arr}')
  
  end = len(arr) - 1
  while end > 0:
    last = 1
    for i in range(end):
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        last = i + 1
    end = last - 1
        
  print(f'after : {arr}')

def sort_select(arr):
  print('-' * 60)
  print(f'before: {arr}')
  
  end = len(arr)
  
  for i in range(end):
    swapTarget = i
    for j in range(i + 1, end):
      if arr[swapTarget] > arr[j]:
        swapTarget = j
    arr[i], arr[swapTarget] = arr[swapTarget], arr[i]
    
  print(f'after : {arr}')

def sort_insert(arr):
  print('-' * 60)
  print(f'before: {arr}')
  
  count = len(arr)
  for i in range(1, count):
    swapTarget = arr[i]
    j = i
    while j > 0 and arr[j - 1] > swapTarget:
      arr[j] = arr[j - 1]
      j -= 1
    arr[j] = swapTarget
    
  print(f'after : {arr}')

def sort_shell(arr):
  print('-' * 60)
  print(f'before: {arr}')

  GAPS = (701, 301, 132, 57, 23, 10, 4,1)
  count = len(arr)
  findG = count / 2.5
  for gap in GAPS:
    if gap > findG: continue
    for i in range(gap, count):
      temp = arr[i]
      j = i
      while j >= gap and arr[j - gap] > temp:
        arr[j] = arr[j - gap]
        j -= gap
      arr[j] = temp
      
  print(f'after : {arr}')
  

    

def main():
  sort_bubble(array[:])
  sort_insert(array[:])
  sort_select(array[:])
  sort_shell(array[:])

if __name__ == '__main__':
  main()

