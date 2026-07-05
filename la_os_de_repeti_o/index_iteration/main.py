prices = [29.99, 45.50, 12.75, 38.20]
discount_factor = 0
for cost in range(len(prices)):
    discount_factor = cost
    if discount_factor == 0:
        updated_price = prices[cost] - (10/100) * prices[cost]
        prices[cost] = updated_price
        print(f"Updated price for item {cost}: ${updated_price:.2f}")
    elif discount_factor == 1:
        updated_price = prices[cost] - (20/100) * prices[cost]
        prices[cost] = updated_price
        print(f"Updated price for item {cost}: ${updated_price:.2f}")
    elif discount_factor == 2:
        updated_price = prices[cost] - (15/100) * prices[cost]
        prices[cost] = updated_price
        print(f"Updated price for item {cost}: ${updated_price:.2f}")
    elif discount_factor == 3:
        
        updated_price = prices[cost] - (5/100) * prices[cost]
        prices[cost] = updated_price
        print(f"Updated price for item {cost}: ${updated_price:.2f}")

