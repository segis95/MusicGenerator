
def cut_and_lengths(sg):
    
    res = sg.res
    GENERAL_BAG = []
    
    lgs = [4 * res, 2 * res, res, res / 2, res / 4, res / 8, res / 16]
    
    
    for track in sg.extract_collection():
        tr = copy.copy(track)
        
        i = 0
        while(len(tr) > 0):
            if (i == len(tr) - 1):
                if (len(tr) > 1):
                    GENERAL_BAG.append(tr)
                break
            if (tr[i].length >= lgs[0] + lgs[2]):
                if (i == 0):
                    tr = tr[1:]
                    i = 0
                else:
                    GENERAL_BAG.append(tr[:i])
                    tr = tr[i + 1:]
                    i = 0
            elif (tr[i].length >= lgs[1] + lgs[2]):
                tr[i].length = 1
                i = i + 1
                
            elif (tr[i].length >= lgs[2] + lgs[3]):
                tr[i].length = 2
                i = i + 1
                
            elif (tr[i].length >= lgs[3] + lgs[4]):
                tr[i].length = 4
                i = i + 1
            
            elif (tr[i].length >= lgs[4] + lgs[5]):
                tr[i].length = 8
                i = i + 1
                
            elif (tr[i].length >= lgs[5] + lgs[6]):
                tr[i].length = 16
                i = i + 1
                
            elif (tr[i].length >= lgs[6] * 1.5):
                tr[i].length = 32
                i = i + 1
            else:
                tr[i].length = 64
                i = i + 1
    
    GENERAL_BAG_CORRECTED = []
    
    for tr in GENERAL_BAG:
        
        if (len(tr) == 1):
            continue
            
        tr_prime = tr[0] 
        current_tick = tr_prime.tick
        current_length = tr_prime.length
        current_pitch = tr_prime.pitch
        
        resulting_bag = []
        resulting_bag.append(tr_prime)
        
        i = 1
        while(i < len(tr) - 1):
            
            diff = tr[i].tick - current_tick 
            
            if diff < res * 4 / current_length:
                i_new = i
                diff_new = diff
                
                while( (i_new < len(tr) - 1) and (diff_new < res / current_length)):
                        i_new = i_new + 1
                        diff_new = tr[i_new].tick - current_tick
                
                
                try:
                    number_of_max = np.argmax(tr[i : i_new])
                except:
                    number_of_max = 0
                
                resulting_bag.pop()
                

                resulting_bag.append(tr[i + number_of_max])

                current_tick = tr[i + number_of_max].tick
                current_length = tr[i + number_of_max].length
                current_pitch = tr[i + number_of_max].pitch
                
                i = max([i_new, i + 1])
                           
            else:
                resulting_bag.append(tr[i])
                current_tick = tr[i].tick
                current_length = tr[i].length
                current_pitch = tr[i].pitch
                
                i = i + 1
                
        #print(float(len(tr))/(len(resulting_bag) - len(tr)))
        GENERAL_BAG_CORRECTED.append(resulting_bag)
    
    return GENERAL_BAG_CORRECTED