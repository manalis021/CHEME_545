unit_operations_data = {
    "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
    "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
    "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}
}

def extract_parameter(unit_operations_data, unit_name, parameter_name, index):
    try:
        # Access the value for the unit_name, parameter_name, and index
        value = unit_operations_data[unit_name][parameter_name][index]
        # Return the formatted string
        return f"{unit_name}_{parameter_name}_{value}"
    except (KeyError, IndexError):
        # If any KeyError or IndexError occurs, return "Invalid input"
        return "Invalid input"

result = extract_parameter(unit_operations_data, "distillation_column", "temperature", 1)
print(result)  # Output: distillation_column_temperature_160

result2 = extract_parameter(unit_operations_data, "reactor", "pressure", 3) #index out of range
print(result2)  # Output: Invalid Input

result3 = extract_parameter(unit_operations_data, "reactor", "pressure", 2)
print(result3)  # Output: reactor_pressure_6

result4 = extract_parameter(unit_operations_data, "hello", "pressure", 2) #hello is not in the dictionary
print(result4)  # Output: invalid input

result5 = extract_parameter(unit_operations_data, "heat_exchanger", "temperature_in", 0) #hello is not in the dictionary
print(result5)  # Output: heat_exchanger_temperature_in_80
