class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # If only a single item in matrix, loop the entire thing
        if len(matrix) == 1:
            for value in matrix[0]:
                if value == target:
                    return True
            return False

        for index, value in enumerate(matrix):
            last_index = len(value) - 1
            first_val = value[0]
            last_val = value[last_index]

            # Check for single item in sub-array
            if len(value) == 1 and first_val == target:
                return True
            
            # Check if first or last value is the target before starting loop
            if first_val == target or last_val == target:
                return True

            # Only loop if target is within range of sub-array
            if target > first_val and target < last_val: 
                for num in value:
                    if num == target:
                        return True
            else:
                index = index + 1

        return False

