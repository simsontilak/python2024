input_file = open("data/input.csv","r")
input_heading = input_file.readline()
input_data = input_file.readline().strip().split(",")
input_file.close()

loan_amount = float(input_data[0])
years = int(input_data[1])
interest = float(input_data[2]) / 100

months = years * 12
monthly_interest = interest / 12

interest_comp = (1 + monthly_interest) ** months
payment = round((loan_amount * monthly_interest * interest_comp) / (interest_comp - 1),2)

output_file = open("data/output.csv", "w")
output_file.write("Payment No, Payment, Principle Paid, Interest Paid, Amount remaining\n")

amount_remaining = loan_amount
for month in range(1,months + 1):
    current_interest_amt = round(amount_remaining * monthly_interest,2)
    principle_comp = round(payment - current_interest_amt,2)
    amount_remaining = round(amount_remaining - principle_comp,2)
    output_file.write(f"{month}, {payment}, {principle_comp}, {current_interest_amt}, {amount_remaining}\n")
output_file.close()

print("done")
