molecular_weights = {
    'NaCl': 58.44,
    'H2SO4': 98.079,
    'NaOH': 40.00,
    'KMnO4': 158.034,
    'CH3COOH': 60.052
}

solutions_needed = ['NaCl-0.5M', 'H2SO4-0.25M', 'NaOH-1M', 'KCl-0.1M', 'CH3COOH-0.3M']

def calculate_solution_weights(molecular_weights, solutions_needed):
    result = []
    
    for solution in solutions_needed:
        # Split the solution into chemical formula and concentration
        chemical, concentration = solution.split('-')
        
        # Check if the chemical exists in the molecular_weights dictionary
        if chemical in molecular_weights:
            # Extract the molecular weight and calculate the weight for 1 liter
            molecular_weight = molecular_weights[chemical]
            weight = molecular_weight * float(concentration.replace('M', ''))
            result.append(f'{chemical}-{concentration}-{weight:.2f}g')
        else:
            # If the chemical is not found, append 'unknown'
            result.append('unknown')
    
    return result
output = calculate_solution_weights(molecular_weights, solutions_needed)
print(output)
