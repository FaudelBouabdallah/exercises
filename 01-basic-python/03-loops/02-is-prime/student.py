# Write your code here
# ```javascript
# function isPrime(n)
# {
#     for ( let k = 2; k !== n; ++k )
#     {
#         if ( n % k === 0 )
#         {
#             return false;
#         }
#     }

#     return n > 1;
# }
# ```µ
def is_prime(n):
    for k in range(2, n):
        if n % k == 0:
            return False

    return n > 1