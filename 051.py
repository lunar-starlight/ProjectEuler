from strah import sieve, is_prime
import itertools, time

# def sieve(n: int) -> list:
#     '''Return list of primes up to `n`'''
#     bit_field = [True] * n
#     bit_field[0] = False
#     bit_field[1] = False
#     for i in range(2, math.floor(math.sqrt(n) + 1)):
#         if bit_field[i]:
#             for multiple_of_i in range(2 * i, n, i):
#                 bit_field[multiple_of_i] = False
#     return bit_field

goal = 8
end = 7

bit_field = sieve(10**end, ret_bit_field=True)
primes = [i for i in range(10**end) if bit_field[i] and i >= 56003]

print(time.process_time())
for p in primes:
# for p in range(10**6 + 1, 10**7, 2):
#     if not is_prime(p):
#         continue
    for lst in itertools.combinations_with_replacement([0, 1], len(str(p))):
        if not any(lst):
            continue
        for cover in set(itertools.permutations(lst)):
            # print('------------', cover, p)
            if len(set([ f for f, t in zip(list(str(p)), cover) if t])) != 1:
                # print('cont\'d', p)
                continue
            count = 0
            for k in range(10):
                n = list(str(p))
                for i, c in enumerate(cover):
                    if c:
                        n[i] = str(k)
                n = int(''.join(n))
                if bit_field[n] and len(str(n)) == len(str(p)):
                    count += 1
                    # print(n)
            if count == goal:
                print(p)
                print(time.process_time())
                exit()