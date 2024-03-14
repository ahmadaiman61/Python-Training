# Smallest Positive Integer Algorithm

# def solution(A):
#     # Implement your solution here
#     positivelist = []
    
#     for num in A:
#         if num > 0:
#             positivelist.append(num)

#     print(positivelist)
    
#     smallest_positive = 1
#     while smallest_positive in positivelist:
#         smallest_positive += 1

#     print(smallest_positive)


# solution([1, 3, 6, 4, 1, 2])


# Binary Gap , maximal sequence of consecutive zeros

# def solution(N):
#     N = bin(N) [2:]
#     print(N)
#     b = 0
#     maxb = 0
#     for k in N:
#         if int(k)==0:
#             b += 1
#         elif int(k)==1:
#             maxb = max(maxb,b)
#             b = 0
#     return maxb


# print(solution(1041))  # Output should be 5

#Cyclic Rotation 

# def solution(Arrays,num_rotation):

#     num_array = len(Arrays)
#     new_array = [None]*num_array

#     for i in range(num_array):
#         new_position_of_the_number = (i + num_rotation) % num_array  ##modulus = if you rotate the array [1, 2, 3, 4, 5, 6] by 50 positions to the right, it will end up with the same result as rotating it by 50 % 6 = 2 positions.
#         new_array[new_position_of_the_number] = Arrays[i]
    
#     return new_array

# # Example usage:
# arr = [1, 2, 3, 4, 5]
# k = 2
# print(solution(arr, k))


#Odd occurences in array

# def solution(A):
#     num_A = len(A)
#     A.sort()

#     print(A)

#     if num_A == 1:
#         return A[0]
#     else:
#         for i in range(0, num_A - 1, 2):  ##stepsize of 2 because it always have pair
#             if A[i] != A[i+1]:
#                 return A[i]
#         return A[-1]

# arr = [9, 3, 9, 3, 9, 7, 9]  # Unpaired element is 7
# print(solution(arr))  # Output: 7


#Codility Frog Jump

# x(starting position) = 1, y(final target) = 7, D(jumpstepsize) = 2

# def solution(x,y,D):
#     starting_position = x
#     final_target = y
#     jump = D
#     not_reach_target = True
#     jump_counter = 0

#     while not_reach_target:
#         starting_position += jump
#         jump_counter += 1
#         if starting_position >= final_target:
#             not_reach_target = False

#     return jump_counter
# or 

# def solution(x,y,D):
#     import math
#     jump_counter = math.ceil((y-x)/D)
#     return jump_counter

# starting_position = 1
# final_target = 16
# jump = 2
# result = solution(starting_position, final_target, jump)
# print("Jump Counter:", result)



