# initialise variables
cell_pos=0
freed_count=0
freed_list=[]


# Get cells initial structure and lock status
cells_info_str = input("please enter each cells lock status' (1 = unlocked and 0 = locked) separated by commas:").split(",")
#print ("As strings cell locks status is: " + str(cells_info_str))

# Validate input and convert to integers and make sure only 0's or 1's
cells_info_int = []
for cell in cells_info_str:
  if cell.isnumeric() and int(cell) > -1 and int(cell) <2:
    cells_info_int.append(int(cell))
  else:
    print ("Entry needs to be 1's and 0's only, please start again")
    cells_info_int = []
    exit()

#test if anybody is getting released
if cells_info_int[cell_pos]==0:
  print("It's all over! - I'm locked in and nobody's getting out today!")
  print("Freed today: " + str(freed_count))
  exit()

#summarise starting point
print ("Initial lock status of cells: ", end=" ")
print (str(cells_info_int) + " here")



#lock and unlock cells
for cell in range(len(cells_info_int)):
  if cells_info_int[cell] == 0:
    cells_info_int[cell] = 1
  else:
    cells_info_int[cell] = 0
print ("new cell status " +str(cells_info_int))



#Free prisoners - so far only freeing prisoner in cell 1
freed_list.append("Prisoner from cell "+str(cell_pos+1))
freed_count = len(freed_list)



#output
print ("Final results: ")
print ("Freed count = " + str(freed_count))
print ("Freed prisoners: " + str(freed_list))

