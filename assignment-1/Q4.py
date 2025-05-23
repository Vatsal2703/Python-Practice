# Q4. [Gate counting exercise]  As explained in the problem description, between 
# any 2 flip-flops, there are gates on each path. Write a python program to count 
# the occurrences of the gates and list down top 10 such occurring gates (i.e., top 
# 10 highly ranked gates) in each of the provided input test cases.


def count_gates(file_path):
    # Read the input file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Dictionary to store the count of occurrences for each gate
    gate_counts = {}
    
    # Iterate over each line
    for line in lines:
        # Split the line into elements
        elements = line.strip().split()
        
        # The gates are the elements between the flip-flops
        gates = elements[1:-1]
        
        # Count the occurrences of each gate
        for gate in gates:
            if gate in gate_counts:
                gate_counts[gate] += 1
            else:
                gate_counts[gate] = 1
    
    # Sort the gates in descending order of occurrences
    sorted_gates = sorted(gate_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Get the top 10 occurring gates
    top_10_gates = sorted_gates[:10]
    
    return top_10_gates

# Example 
file_path_1 = "assignment-1/input_1.txt"

# Count the occurrences of gates 
top_10_gates_1 = count_gates(file_path_1)
print("Top 10 occurring gates for input_1.txt:")
for gate, count in top_10_gates_1:
    print(f"{gate}: {count} occurrences")