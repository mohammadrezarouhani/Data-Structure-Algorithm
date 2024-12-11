# A long, long time ago in a galaxy far, far away a big collision of integers is taking place right now.
# What happens when two integers collide? During collision,
#  each digit of one number compares itself to the corresponding digit of the other number (the least significant digit with the other’s least significant digit, and so on).
#  The smaller digit “falls out” of the number containing it. Additionally, if the digits are the same, nothing happens.
# If a number doesn’t consist of a corresponding digit, then we consider it to be zero.
#  After all comparisons of corresponding digits, the leftover digits in the number come closer and create a new number. For example:


# Write a program that will, for two given integers, determine their values \textbf{after collision}. If it happens that all the digits of one number fell out, then for that number output the message “Zekiii!”.
# input

# e first line of input contains the integer N, one of the integers from the task.

# The second line of input contains the integer M, one of the integers from the task.
# Output

# The two lines of output must contain the new value of the first and second given integer from the task.
# Constraints

#     1≤N,M≤1091≤N,M≤109

# Sample Test Data
# input 1

# 65743
# 9651

# Plain text
# output 1

# 673
# 95

# Plain text
# input 2

# 3412
# 7586

# Plain text
# output 2


def number_collision(m, n):
    m_res = 0
    n_res = 0
    m_flag = 1
    n_flag = 1

    while n or m:
        rm = m % 10
        rn = n % 10
        n //= 10
        m //= 10

        if rm == rn:
            m_res += rm * m_flag
            m_flag *= 10
            n_res += rn * n_flag
            n_flag *= 10
        elif rm > rn:
            m_res += rm * m_flag
            m_flag *= 10
        else:
            n_res += rn * n_flag
            n_flag *= 10
    else:
        m_res = "Zekiii!" if not m_res else m_res
        n_res = "Zekiii!" if not n_res else n_res

    print(m_res)
    print(n_res)


number_collision(65743, 9651)
number_collision(3412, 7586)
number_collision(123456789, 1)

