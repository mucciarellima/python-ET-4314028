import os

def clear_terminal():
    """Clears the terminal screen."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

# Clear the terminal before printing
clear_terminal()


# Print "hello, world!" to the terminal
#print('Hello, World!')

# Python code​​​​​​‌‌‌​‌​​​‌‌​​‌‌​​‌‌‌​‌​‌‌‌ below
hexValues = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}




# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    hexNum = hexNum.upper()  # Ensure uppercase for consistency
    conversion = 0 
    lenthofstring = len(hexNum)
    counter = lenthofstring-1
    #for position in hexNum:
    #    conversion = 16**counter
    #    print(f'for {hexNum} the {position} is at {conversion} x {hexValues[position]}')
    #    counter=counter-1
    #return conversion
    if hexNum == '':
        return None
    
    for position in hexNum:
        if position in hexValues:
            conversion = conversion + 16**counter*hexValues[position]
        else:
            return None
        counter=counter-1
    return conversion



# Test cases
print(f'1A3F converts to {hexToDec('1A3F')}')  # Should print 6719
print(f'BEEF converts to {hexToDec('BEEF')}')  # Should print 48879
print(f'12XY is invalid and so converts to {hexToDec('12XY')}')  # Should print None - invalid hex
print(f'\'\' is the empty string and converts to {hexToDec('')}')      # Should print None - empty string

print(f'1A3F is converted using the built in function for comparison {int('1A3F', 16)}')  # Built-in function for comparison

