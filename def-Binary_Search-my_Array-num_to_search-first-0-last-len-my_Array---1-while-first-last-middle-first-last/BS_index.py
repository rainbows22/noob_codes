def Binary_Search(my_Array,num_to_search):
  first = 0;
  last = len(my_Array) - 1
  while(first <= last): 
    middle = (first + last)//2
    if my_Array[middle] ==num_to_search:
      print middle;
      print ("is the index");
      return True
    elif(my_Array[middle]< num_to_search):
      first = middle + 1
    elif(my_Array[middle]> num_to_search):
      last = middle-1
    else:
      return False
if __name__ == "__main__":
  my_Array_S = []
  my_Array = []
  num_of_numbers = int(input('Number of elements in sorted array? '))

  for i in range(0, num_of_numbers):
    my_numbers = int(input('Number to be added to array: '))
    my_Array_S.append(my_numbers)
#why this step? You can convert them to int when you get them in the input itself no?
  my_Array = list(map(int, my_Array_S))
# ====
  num_to_search = int(input("Number to be searched in the Sorted Array?"))
  if Binary_Search(my_Array,num_to_search):
    print(" where the number is Found!!")
  else:
    print("Nah!")
