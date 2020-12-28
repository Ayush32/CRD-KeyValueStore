import threading
#import threading library
from threading import*
#import time
import time

dataStorage = {}  #dictionary in which we store data

# for create operation we use

############## Create ###############

def create(key,value,timeout = 0):
    if key in dataStorage:
        # error message
        print("error: this key is already exist!! Please try again")
        
    else:
        if(key.isAlpha()):
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
            print("error: Invalid Key_Name!! Key name must contain only alphabets and no special characters or numbers")
            
############### crate opeartion function end #####################
              

