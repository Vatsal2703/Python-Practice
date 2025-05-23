# Q5. [Counting occurrence of combination of gates] Consider the  following 
# contents of the input.txt file:  
 
# G1 G2 G5 G7 
# G1 G21 G51 G678 G7 
# G1 G24 G51 G678 G781 G7 
# G1 G22 G55 G76 G890 G7 
 
# If we observe carefully in the above, “G51 G678” is occurring together (i.e., 
# occurring as a tuple) in more than one path, i.e., it occurs in 2 paths. Write a 
# python program to find the number of highest such occurrence of combined 
# occurrence of gates. This is to say that K-number of gates are occurring together 
# in more than one path.  Your program should provide the number of K as output. 


def rank_flip_flops_unique_paths(file_path):
    # Read the input file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Dictionary to store the unique incoming paths for each flip-flop
    flip_flop_paths = {}
    
    # Iterate over each line
    for line in lines:
        # Split the line into elements
        elements = line.strip().split()
        
        # The first and last elements are flip-flops
        start_flip_flop = elements[0]
        end_flip_flop = elements[-1]
        
        # Initialize the set for the end flip-flop if not already present
        if end_flip_flop not in flip_flop_paths:
            flip_flop_paths[end_flip_flop] = set()
        
        # Add the start flip-flop to the set of unique incoming paths for the end flip-flop
        flip_flop_paths[end_flip_flop].add(start_flip_flop)
    
    # Convert the sets to counts of unique incoming paths
    flip_flop_unique_paths_count = {flip_flop: len(paths) for flip_flop, paths in flip_flop_paths.items()}
    
    # Sort the flip-flops in descending order of unique incoming paths
    sorted_flip_flops = sorted(flip_flop_unique_paths_count.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_flip_flops

# Example 
file_path_1 = "assignment-1\input_2.txt"

# Rank the flip-flops for unique incoming paths
result_1 = rank_flip_flops_unique_paths(file_path_1)
print("Ranking for input_1.txt based on unique incoming paths:")
for flip_flop, count in result_1:
    print(f"{flip_flop}: {count} unique incoming paths")

