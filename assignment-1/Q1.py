# Q1. [Incoming path-based ranking] We want to rank the flip-flops of the netlist 
# in the descending order of  the total number of incoming path(s) to them.  
# Therefore, by definition of “incoming path” as described above, we want to obtain 
# ranking of flip-flops as below: 
# Say,  Flip-flops  are represented  as Fi, Fj, Fk and  so on. They respectively have 
# incoming paths as 23, 45, 13 and so on. So, the descending order of ranking 
# would be: Fj, Fi, Fk and so on.   
# Write a python program to obtain this ranking given input as following  2  different 
# test inputs (which are basically input.txt files mentioned in the above problem 
# description):  
#  a) input_1    
#  b)input_2


def rank_flip_flops(file_path):
    with open(file_path,"r") as file:
        lines = file.readlines()

    flip_flop_paths = {}

    for line in lines:
        elements = line.strip().split()
        
        start_flip_flop = elements[0]
        end_flip_flop = elements[-1]
    
        if end_flip_flop in flip_flop_paths:
            flip_flop_paths[end_flip_flop] += 1
        else:
            flip_flop_paths[end_flip_flop] = 1

    sorted_flip_flops = sorted(flip_flop_paths.items(), key = lambda x: x[1],reverse = True)   
    return sorted_flip_flops     

file_path = "assignment-1\input_2.txt"

paths = rank_flip_flops(file_path)
print("Ranking of flip flop in Desecednig order of incoming paths:")
for flip_flop, count in paths:
    print(f"{flip_flop}:{count} incoming paths")

    