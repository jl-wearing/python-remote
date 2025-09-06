# Program to calculate whether Joe made a profit from buying and selling stock.

# Constants used by the program.
BROKER_COMMISSION = 0.03

# Inputs
number_of_shares_purchased = 2000
price_per_share = 40.00

# Calculate the broker's commission when Joe bought.
broker_commission_buying = (number_of_shares_purchased * price_per_share * BROKER_COMMISSION)

# Calculate the amount Joe paid for the stock, accounting for broker commissions.
price_paid = (number_of_shares_purchased * price_per_share) + broker_commission_buying

# New price per share.
price_per_share = 42.75

# Calculate the broker's commission when Joe sold the stock.
broker_commission_selling = number_of_shares_purchased * price_per_share * BROKER_COMMISSION

# Calculate the amount Joe made when he sold the stock.
amount_made_when_selling = number_of_shares_purchased * price_per_share - broker_commission_selling
profit_loss = amount_made_when_selling - price_paid

# Output whether Joe made a profit or a loss.
print(f"Joe paid: ${price_paid:,.2f} to purchase stock.")
print(f"Commission paid when purchasing stock: ${broker_commission_buying:,.2f}")
print(f"Joe made : ${amount_made_when_selling:,.2f} when selling stock.")
print(f"Commission paid when selling stock: ${broker_commission_selling:,.2f}")
print(f"Joe's profit/loss: ${profit_loss:,.2f}")