#   *
#   **
#   ***
#   ****
for i in range(1,6):
    for j in range(1,i+1):
        print('*', end='')
    print('')

# star pattern for 4 to 1
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print('*', end='')
#     print('')

# star pattern space 5 to 1

# for i in range(1,6):
#     for k in range(1,6-i):
#         print(' ', end='')
#     for j in range(1,1+i):
#         print('*', end='')
#     print('')

# star pattern triangle shape

# for i in range(1,6):
#     for k in range(1,6-i):
#         print(' ', end='')
#     for j in range(1,(2*i-1)+1):
#         print('*', end='')
#     print('')

# star pattern for revers triangle shape

# for i in range(5,0,-1):
#     for k in range(1,6-i):
#         print(' ', end='')
#     for j in range(1,(2*i-1)+1):
#         print('*', end='')
#     print('')

# for i in range(1,50):
#     n = int(input('Enter Your Number\n'))
#     for row in range(1,n+1):
#         for column in range(1,row+1):
#             print('*', end='')
#         print()

# for i in range(1,50):
#     n = int(input('Enter Your Number\n'))
#     for row in range(n,0,-1):
#         for column in range(1,row+1):
#             print('*', end='')
#         print()

# for i in range(1,50):
#     n = int(input('Enter Your Number\n'))
#     for row in range(1,n+1):
#         for column in range(1,row+1):
#             print('*', end='')
#         print()
#     for row in range(n-1,0,-1):
#         for column in range(1,row+1):
#             print('*', end='')
#         print()