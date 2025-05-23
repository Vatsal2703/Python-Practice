# Q2.We want to have a ranking based on only the unique paths between a set of flip-
# flops. In the above example, even though we have 4 incoming paths to G7 from 
# G1, we would  consider only one path from G1 to G7.  G7 may have other 
# incoming paths from other flip-flops. But, in this unique incoming path based 
# ranking, we need to take only one incoming path from other flip-flops to G7. 
  
# Write a python program to obtain this unique incoming path-based ranking given 
# input same as that of Q1


def rank_flip_flops(file_path):
    with open(file_path,"r") as file:
        lines = file.readlines()

    flip_flop_paths = {}

    for line in lines:
        elements = line.strip().split()
        
        start_flip_flop = elements[0]
        end_flip_flop = elements[-1]
    
        if end_flip_flop in flip_flop_paths:
            flip_flop_paths[end_flip_flop] = set()
        flip_flop_paths[end_flip_flop].add(start_flip_flop)  

    rank_flip_flops = {flip_flop:len(paths) for flip_flop,paths in flip_flop_paths.items()}      
    
    sorted_flip_flops = sorted(rank_flip_flops.items(), key = lambda x: x[1],reverse = True)   
    
    return sorted_flip_flops     

file_path = "assignment-1/input_1.txt"

paths = rank_flip_flops(file_path)
print("Ranking of flip flop in Desecednig order of unique incoming paths:")
for flip_flop, count in paths:
    print(f"{flip_flop}:{count} unique incoming paths")

    