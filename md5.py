import hashlib
import struct
# F(B,C,D) = (B and C) or (not B and D)
# G(B,C,D) = (B and D) or (C and not D)
# H(B,C,D) = B ^ C ^ D
# I(B,C,D) = C ^ (B or not D)

K = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501, 0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be, 0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821, 0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa, 0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8, 0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed, 0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a, 0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c, 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70, 0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05, 0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665, 0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039, 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1, 0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1, 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391]
S = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22, 5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20, 4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23, 6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]

# def shift_amount(round_number):
#     shift_list = [7,12,17,22,5,9,14,20,4,11,16,23,6,10,15,21]
#     round_number = round_number % 4 + (round_number / 16) * (4)
#     # return round_number
#     return shift_list[round_number]

def left_rotate(x, c):
    # print (x << c)
    # print (x >> (32-c))

    # print "thing", (x << c) | (x >> (32-c))
    # print ((x << c)%(2**128)) | ((x >> (32-c))%(2**128))
    # mod = 32
    # value = ((x << c)%(2**mod)) | ((x >> (32-c))%(2**mod))
    value = (x << c) | (x >> (32-c))
    # value = value % 2**32
    return value

def read_chunk(in_file):
    chunk = in_file.read(64)
    chunk = [ord(x) for x in chunk]
    if not chunk:
        return ''
    if len(chunk) < 64:
        # chunk += '\200'
        chunk.append(0x80)
    if len(chunk) < 64:
        for i in range(64 - len(chunk)):
            # chunk += '\000'
            chunk.append(0x00)
    return chunk


if __name__ == "__main__":
    A = a = 0x67452301
    # A = a = '\147' + '\105' + '\043' + '\001'
    B = b = 0xefcdab89
    C = c = 0x98badcfe
    D = d = 0x10325476


    with open("textfile", "rb") as in_file:
        # chunk = in_file.read(64)
        # for x in chunk:
        #     print ord(x)
        # chunk = [ord(x) for x in chunk]

        while True:
            M = read_chunk(in_file)
            if not M:
                break

        # for M in iter(read_chunk(in_file), ''):
            for i in range(64):
                case = i / 16
                if case == 0:
                    F = (B & C) | ((~B) & D)
                    g = i
                elif case == 1:
                    F = (D & B) | ((~D) & C)
                    g = ((5 * i) + 1) % 16
                elif case == 2:
                    F = B ^ C ^ D
                    g = ((3 * i) + 5) % 16
                else:
                    F = C ^ (B | (~D))
                    g = (7 * i) % 16
                dTemp = D
                D = C
                C = B
                # print "g", g
                # print "M[g]", M[g]
                # print "type", type(ord(M[g]))
                B = B + left_rotate((A + F + K[i] + M[g]), S[i])
                A = dTemp
            print len(str(a))
            print len(str(A))
            print len(str(b))
            print len(str(B))
            print len(str(c))
            print len(str(C))
            a += int(A)
            a += int(A)
            a += int(A)
            b += int(B)
            c += int(C)
            d += int(D)
        digest = a + b + c + d
        print "digest",hex(digest)
        print "length", len(hex(digest))



# #     # for i in range(64):
# #     #     if not i % 4:
# #     #         print
# #     #     print shift_amount(i),

# # #  7 12 17 22  7 12 17 22  7 12 17 22  7 12 17 22
# # #  5  9 14 20  5  9 14 20  5  9 14 20  5  9 14 20
# # #  4 11 16 23  4 11 16 23  4 11 16 23  4 11 16 23
# # #  6 10 15 21  6 10 15 21  6 10 15 21  6 10 15 21

# # #  0  1  2  3  0  1  2  3  0  1  2  3  0  1  2  3
# # #  4  5  6  7  4  5  6  7  4  5  6  7  4  5  6  7
# # #  8  9 10 11  8  9 10 11  8  9 10 11  8  9 10 11
# # # 12 13 14 15 12 13 14 15 12 13 14 15 12 13 14 15

# # #  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
# # # 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
# # # 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
# # # 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63
# #
