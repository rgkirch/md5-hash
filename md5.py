# testline


# F(B,C,D) = (B and C) or (not B and D)
# G(B,C,D) = (B and D) or (C and not D)
# H(B,C,D) = B ^ C ^ D
# I(B,C,D) = C ^ (B or not D)

def shift_amount(round_number):
    shift_list = [7,12,17,22,5,9,14,20,4,11,16,23,6,10,15,21]
    round_number = round_number % 4 + (round_number / 16) * (4)
    # return round_number
    return shift_list[round_number]

if __name__ == "__main__":
    A = a = 0x67452301
    B = b = 0xefcdab89
    C = c = 0x98badcfe
    D = d = 0x10325476

    with open("md5input", "rb") as in_file:
        raw_chunk = in_file.read(64)

#         for i in range(64):
#             case = i / 16
#             if case == 0:
#                 F = (B and C) or ((not B) and D))
#                 g = i
#             elif case == 1:
#                 F = (D and B) or ((not D) and C)
#                 g = ((5 * i) + 1) % 16
#             elif case == 2:
#                 F = B ^ C ^ D
#                 g = ((3 * i) + 5) % 16
#             else:
#                 F = C ^ (B or (not D))
#                 g = (7 * i) % 16
#             dTemp = D
#             D = C
#             C = B
#             B = B + leftrotate((A + F + K[i] + M[g]), S[i])
#             A = dTemp
#         a += A
#         b += B
#         c += C
#         d += D



#     # for i in range(64):
#     #     if not i % 4:
#     #         print
#     #     print shift_amount(i),

# #  7 12 17 22  7 12 17 22  7 12 17 22  7 12 17 22
# #  5  9 14 20  5  9 14 20  5  9 14 20  5  9 14 20
# #  4 11 16 23  4 11 16 23  4 11 16 23  4 11 16 23
# #  6 10 15 21  6 10 15 21  6 10 15 21  6 10 15 21

# #  0  1  2  3  0  1  2  3  0  1  2  3  0  1  2  3
# #  4  5  6  7  4  5  6  7  4  5  6  7  4  5  6  7
# #  8  9 10 11  8  9 10 11  8  9 10 11  8  9 10 11
# # 12 13 14 15 12 13 14 15 12 13 14 15 12 13 14 15

# #  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
# # 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
# # 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
# # 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63



