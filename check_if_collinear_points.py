def solution(coordinates):
    
    # check if input coordinates are less than 2
    if len(coordinates) < 2:
        return "Invalid input: At least two coordinates are required to determine a straight line."
    
    # extract first 2 points
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    
    # calculate slope ratio (using cross product)
    for i in range(2, len(coordinates)):
        x3, y3 = coordinates[i]
        # Cross product to check collinearity
        if (y2 - y1)*(x3 - x2) != (y3 - y2)*(x2 - x1):
            return False
    return True

# Example usage
coordinate2 = [[2]]  # Invalid input
coordinate1 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]  # Invalid input
print(solution(coordinate1))
print(solution(coordinate2))