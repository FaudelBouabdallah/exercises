# # Write your code here
# ```javascript
# // Note that Python and JavaScript have different naming conventions (https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)
# // In Python you should name this function card_value instead of cardValue
# function cardValue(string)
# {
#     if ( string === 'Jack' )
#     {
#         return 11;
#     }
#     else if ( string === 'Queen' )
#     {
#         return 12;
#     }
#     else if ( string === 'King' )
#     {
#         return 13;
#     }
#     else if ( string === 'Ace' )
#     {
#         return 1;
#     }
#     else
#     {
#         // Converts string to integer
#         return parseInt(string);
#     }
# }
# ```
def card_value(string):
    if string == 'Jack':
        return 11
    elif string == 'Queen':
        return 12
    elif string == 'King':
        return 13
    elif string == 'Ace':
        return 1
    else:
        return int(string)