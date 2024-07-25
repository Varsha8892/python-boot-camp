# Get the number of each fruit
y_list = list(map(int, input("Enter the number of each fruit: ").split()))
no_apples, no_bananas, no_oranges = y_list
# Define the cost of each fruit
cost_apple = 15
cost_banana = 4
cost_orange = 5
# Calculate the total cost
total_cost = (no_apples * cost_apple) + (no_bananas * cost_banana) + (no_oranges * cost_orange)
# Get the amount given by the mother
amount_given = int(input("Enter the amount given by mother: "))
# Check if the child has been cheated
if total_cost <= amount_given:
    print("Not cheated")
else:
    print("Cheated")
