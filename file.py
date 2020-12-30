import threading
#import threading library
from threading import*
#import time
import time

dataStorage = {}  #dictionary in which we store data

# for create operation we use

############## Create Opeartion ###############

def create(key,value,timeout = 0):
    if key in dataStorage:
        # error message
        print("error: this key is already exist!! Please try again")
        
    else:
        if(key.isalpha()):
            if(len(dataStorage) < (1024*1024*1024) and value <= (16*1024*1024)): # constraints range for file less than 1Gb and jsonObject value less than 16KB
                if(timeout == 0):
                    z = [value,timeout]
                else:
                    z = [value,time.time()+timeout]
                    # for input key_name capped at 32chars
                if (len(key) <= 32):
                    dataStorage[key] = z
                    
            else:
                print("Error: Memory Limit Exceeded!!!!!!")
                
        else:
            print("Error: Invalid Key_Name!! Key name must contain only alphabets and no special characters or numbers")
            
############### Crete opeartion function end #####################

############### FOR READ OPERATION ###################

def read(key):
    if key not in dataStorage:
        # error message displayed  when the key is not in dictionary for read..
        print("Error: given key does not exist in database. Please enter a valid key")
        
    else:
        c = dataStorage[key]
        if(c[1] != 0):
            #comparing the present time with expiry time
            if(time.time() < c[1]):
                #for returning the key value pair like jsonObject i.e "key_name: value"
                string = str(key) + ":" + str(c[0])
                return string;
            else:
                print("Error: time-to-live of",key," has expired")
        else:
            string = str(key) + ":" + str(c[0])
            return string
        
        
############### READ OPERATION COMPLETE #################

################ DELETE OPERATION ######################

def delete(key):
    # error message when key is not present
    if key not in dataStorage:
        print("Error: The key is not exists in Database. Please enter a valid key!!!!")
    else:
        c = dataStorage[key]
        if (c[1] != 0):
           
           #comapring the current time with expiry time
           
            if(time.time() < c[1]):
               del dataStorage[key]
               print("$ Hurray Key is successfully delete $")
            else:
            # Error Message
               print("Error: time-to-live of","Key->",key, "has expired")
        else:
            ## key is successfully deleted
            del dataStorage[key]
            print("Key is Successfully Deleted")
            

############## Delete Operation Complete ################

            
               
               
        


            

              

