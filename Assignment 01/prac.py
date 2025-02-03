# Read the input string
s = input()

# Initialize variables
segments = []
segment = ""
l_count = 0
r_count = 0

# Iterate over the characters in the string
for char in s:
    segment += char
    if char == 'L':
        l_count += 1
    else:
        r_count += 1
    
    # If the number of 'L's equals the number of 'R's, split the string
    if l_count == r_count:
        segments.append(segment)
        segment = ""
        l_count = 0
        r_count = 0

# Output the number of segments and the segments themselves
print(len(segments))
for segment in segments:
    print(segment)
