from crop import*
from seed import*
from bank import*
import time

def main():
    #initialize the crop matrix using the following syntax:
	crop_matrix = [[crop("NULL") for x in range(5)] for x in range(5)]
	seed_list = []
	bank_balance = bank(250)
	numb_of_seeds = [0,0,0,0,0,0]
	seed_list.append(seed("Wheat"))
	seed_list.append(seed("Rice"))
	seed_list.append(seed("Cotton"))
	seed_list.append(seed("Jute"))
	seed_list.append(seed("Banana"))
	seed_list.append(seed("Apple"))
	start_time = time.time()
	print(start_time)
	print_crop_matrix(crop_matrix,bank_balance,seed_list,numb_of_seeds)
	add_seed("Wheat",seed_list,numb_of_seeds,bank_balance)
	print_crop_matrix(crop_matrix,bank_balance,seed_list,numb_of_seeds)
	add_seed("Cotton",seed_list,numb_of_seeds,bank_balance)
	print_crop_matrix(crop_matrix,bank_balance,seed_list,numb_of_seeds)
	add_to_crop_matrix("Wheat",0,0,crop_matrix,seed_list,numb_of_seeds)
	crop_matrix[0][0].water()
	crop_matrix[0][0].water()
	crop_matrix[0][0].water()
	crop_matrix[0][0].water()
	crop_matrix[0][0].water()
	crop_matrix[0][0].water()
	print_crop_matrix(crop_matrix,bank_balance,seed_list,numb_of_seeds)
	crop_matrix[0][0].water()
	print_crop_matrix(crop_matrix,bank_balance,seed_list,numb_of_seeds)
	crop_matrix[0][0].water()
	print_crop_matrix(crop_matrix,bank_balance,seed_list,numb_of_seeds)
	
	print(time.time()-start_time)


#in order to add a seed to the created crop_matrix use this function and it 
#checks whether the location is empty and it checks whether you have the seed as well
def add_to_crop_matrix(crop_name,i,j,crop_matrix,seed_list,numb_of_seeds):
        if(check_for_empty_cell_crop_matrix(crop_matrix,i,j)==True):
                if(delete_seed(crop_name,seed_list,numb_of_seeds)==True):
                        crop_matrix[i][j] = crop(crop_name)

#implemented in the add_to_crop_matrix function and is used to check if a specific
#cell in the crop matrix is empty or not, returns true if empty and False if not.
def check_for_empty_cell_crop_matrix(crop_matrix,i,j):
        if(crop_matrix[i][j].name=="NULL"):
                return True
        else:
                return False

#deletes any elemtent from the crop matrix.
def remove_from_crop_matrix(i,j,crop_matrix):
        crop_matrix[i][j]=crop("null")

#harvests from the crop matrix and adds the value of the seling price to the bank_balance, checks the harvest status and the dead status
def harvest_from_crop_matrix(i,j,crop_matrix,bank_balance):
        if(crop_matrix[i][j].name!="NULL"):
                if(crop_matrix[i][j].check_harvest_status==True):
                        if(crop_matrix[i][j].check_dead_status==False):
                                bank_balance.add(crop_matrix[i][j].selling_price)
                                remove_from_crop_matrix(i,j,crop_matrix)
        
        
#adds the seed after purchasing to the number of seeds list and checks if you have the funds and then subtracts the price as well from bank balance
def add_seed(seed_name,seed_list,numb_of_seeds,bank_balance):
        i=0
        while i<6:
                if(seed_name==seed_list[i].name):
                        if(bank_balance.bank_balance>=seed_list[i].buying_price):
                                numb_of_seeds[i]=numb_of_seeds[i]+1
                                bank_balance.subtract(seed_list[i].buying_price)
                i = i+1

#remove the seed when you plant and checks if you have the seeds to actually plant, if not returns false and doesnt do anything to the seed lists
def delete_seed(seed_name,seed_list,numb_of_seeds):
        i=0
        while i<6:
                if(seed_name==seed_list[i].name):
                        if(numb_of_seeds[i]>0):
                                numb_of_seeds[i]=numb_of_seeds[i]-1
                                return True
                        else:
                                return False
                i = i+1

#not relevant to you as we are doing separate decrementations for every value
def decrement_crop_matrix(crop_matrix):
        i = 0
        j = 0
        while i<5:
                while j<5:
                        crop_matrix[i][j].decrement_life
                        j+=1
                i+=1
                        

def print_crop_matrix(crop_matrix,bank_balance,seed_list,numb_of_seeds):
        i = 0
        j=0
        while i<5:
                while j<5:
                        print(crop_matrix[i][j].name+":"+str(crop_matrix[i][j].life))
                        j=j+1
                j=0
                i=i+1
                print("\n")
        print("\nBank Balance: ",bank_balance.bank_balance)
        print("\n")
        i=0
        while i<6:
                print(seed_list[i].name, ":",numb_of_seeds[i])
                i=i+1
        print("---------------------------------------------------")

