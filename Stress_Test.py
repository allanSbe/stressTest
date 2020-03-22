try:
    import time
    
except:
    while True:
        print("Cannot continue! Error 0.01 - Please exit compiler")
    
 



print("Are you ready? y/n")
inpt = input()
##########


def stress_test():
    start_time = time.time()
    print("Please wait...")
    i = 999999999**9999999
    end_time = time.time()
    time_lapsed = end_time - start_time    
    

    print(str(time_lapsed) + " seconds for stage 1")#999999999 to the power of 999999
    
    
    
    ########################################
    start_time2 = time.time()
    while True:
        i - 1
        if 1 == 1:
            end_time2 = time.time()
            time_lapsed2 = end_time2 - start_time2    
            print(str(time_lapsed2) + " seconds for stage 2")#integer subtration 999999999 to the power of 999999 - 1
            break
            
        
        
        
        #####################################
    
    nterms = 10000

    n1 = 0
    n2 = 1
    count = 0


    if nterms <= 0:
        print('Error! "0.02" ')
    elif nterms == 1:
        print("Error! 0.03")
        
    else:
        start_time3 = time.time()
        while count < nterms:
            #print(n1,end=' , ')
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
            if count == 5000:#5000   ''''' 11.1 '''''
                
                end_time3 = time.time()
                time_lapsed3 = end_time3 - start_time3   
                print(str(time_lapsed3) + " seconds for stage 3")
                main_time = time_lapsed + time_lapsed2 + time_lapsed3
                main_time2 = 1000 - (main_time * 10)
                print("Final score - "+ str(main_time))

    
###         #######
if inpt == "y":
    a = 1
    stress_test()