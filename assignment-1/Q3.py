# Q3.[Gate-based score ranking]  Another different way of ranking is to consider 
# the gates also in the path from one flip-flop to  another. Therefore, we devise a 
# ranking  scheme as below: 
# From any path from flip-flop Fi to Fj, count the number of gates. Say, this number 
# is N.  The value “N” is to be used as a score for that incoming path from Fi to Fj. 
# So,  as per the above problem description, “G1 G2 G5 G7” G7 flip-flop has an 
# incoming path from G1  with a score of 2.  Similarly, “G7 G6  G78 G781 G51” 
# means that G51 has an incoming path from G7 with a score of 3.  Also, “G45 
# G789 G432  G47” means that G47 has an incoming path from G45 with a score 
# of 2.   In the same manner, “G1 G22 G55 G76 G890 G7” has an incoming path 
# from G7 with a score of 4. 
 
# Thereafter, to obtain the final ranking of all flip-flops in terms  of incoming paths, 
# you just need to add all the individual scores of   these paths. 
 
# Write a python program to obtain this ranking (the score-based ranking) given 
# input as following  2  different test inputs same as Q1, Q2

def rank_flip_flops_gate_score(file_path):
    # Read the input file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Dictionary to store the gate scores for each flip-flop
    flip_flop_scores = {}
    
    # Iterate over each line
    for line in lines:
        # Split the line into elements
        elements = line.strip().split()
        
        # The first and last elements are flip-flops
        start_flip_flop = elements[0]
        end_flip_flop = elements[-1]
        
        # Count the number of gates (elements between the flip-flops)
        gate_count = len(elements) - 2
        
        # Update the score for the end flip-flop
        if end_flip_flop in flip_flop_scores:
            flip_flop_scores[end_flip_flop] += gate_count
        else:
            flip_flop_scores[end_flip_flop] = gate_count
    
    # Sort the flip-flops in descending order of gate scores
    sorted_flip_flops = sorted(flip_flop_scores.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_flip_flops

# Example usage with input_1.txt
file_path_1 = "assignment-1/input_1.txt"

# Rank the flip-flops for input_1.txt based on gate scores
result_1 = rank_flip_flops_gate_score(file_path_1)
print("Ranking for input_1.txt based on gate scores:")
for flip_flop, score in result_1:
    print(f"{flip_flop}: {score} gate score")




