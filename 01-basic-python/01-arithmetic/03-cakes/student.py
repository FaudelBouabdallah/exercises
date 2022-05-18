# # Write your code here
# ```javascript
# function cakes(eggs, butter, flour)
# {
#     // Do NOT rely on floor in your translation
#     // Use integer division as explained below
#     const maxByEggs = Math.floor(eggs / 5);
#     const maxByButter = Math.floor(butter / 250);
#     const maxByFlour = Math.floor(flour / 5);

#     return Math.min(maxByEggs, maxByButter, maxByFlour);
# }
# ```
def cakes(eggs, butter, flour):
    return min(eggs//5, butter//250, flour//5)