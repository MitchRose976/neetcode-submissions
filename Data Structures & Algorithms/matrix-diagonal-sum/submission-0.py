class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total_sum = 0  # Initialize the total sum
        mat_len = len(mat)
        is_top_half = True

        if mat_len == 1:
            return mat[0][0]

        left_val_index = 0
        right_val_index = len(mat[0]) - 1
        middle_index = mat_len // 2
        
        for index, value in enumerate(mat):
            if left_val_index == right_val_index:
                total_sum += value[left_val_index]
            else:
                total_sum += value[left_val_index] + value[right_val_index]

            if index == middle_index:
                is_top_half = False

            if is_top_half:
                left_val_index += 1
                right_val_index -= 1
            else:
                left_val_index -= 1
                right_val_index += 1

        return total_sum  # Return the calculated total sum