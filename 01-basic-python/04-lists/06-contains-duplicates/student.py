# # Write your code here
# ```javascript
# function containsDuplicates(xs)
# {
#     for ( let i = 0; i !== xs.length; ++i )
#     {
#         for ( let j = i + 1; j < xs.length; ++j )
#         {
#             if ( xs[i] === xs[j] )
#             {
#                 return true;
#             }
#         }
#     }

#     return false;
# }
# ```
def contains_duplicates(xs):
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] == xs[j]:
                return True

    return False