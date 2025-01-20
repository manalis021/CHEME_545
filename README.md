# CHEME_545
Assignments for ChemE 545

The extract_parameter.py is a python file that contains the python function extract_parameter, which takes the unit_operations_data dictionary, and outputs the name of the inputted unit operation, its desired feature name and value. It will take a unit_name (string), a parameter_name (string), and an index (integer) as inputs and return a string in the format: "{unit_name}_{parameter_name}_{value}". If the unit_name or parameter_name is not found, or the index is out of range, the function should return "Invalid input".
It will out put five results as part of testing (two cases show invalid output).

The calculate_solution_weights.py is a python file that contains the function calculate_solution_weights(molecular_weights, solutions_needed) that takes these inputs and returns a modified list where:

If the chemical exists in molecular_weights, replace the entry with: 'chemical_formula-concentration-weight' where weight represents the weight of the compound in 1 litre solution in grams.

weight = molecular_weight * concentration

If the chemical doesn't exist in molecular_weights, replace with 'unknown'.


To run a python file, use "python3 extract_parameter.py" or "python3 calculate_solution_weights.py" 
