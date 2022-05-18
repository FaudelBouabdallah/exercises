# # Write your code here
# ```javascript
# function coins(one, two, five, goal)
# {
#     for ( let x = 0; x <= one; ++x )
#     {
#         for ( let y = 0; y <= two; ++y )
#         {
#             for ( let z = 0; x <= five; ++z )
#             {
#                 if ( x + 2*y + 5*z === goal )
#                 {
#                     return true;
#                 }
#             }
#         }
#     }

#     return false;
# }
# ```
def coins(one, two, five, goal):
    for x in range(0, one+1):
        for y in range(0, two+1):
            for z in range(0, five+1):
                if x + 2*y + 5*z == goal:
                    return True

    return False