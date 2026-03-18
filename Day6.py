transactions = []

n = int(input("No.of Transactions? "))

for i in range(n):
    amount = float(input("Enter" + str(i + 1) + ": "))
    transactions.append(amount)
categorized = {
    "normal": [],
    "large": [],
    "high_risk": [],
    "invalid": []
}

for t in transactions:
    if t <= 0:
        categorized["invalid"].append(t)
    elif t <= 500:
        categorized["normal"].append(t)
    elif t <= 2000:
        categorized["large"].append(t)
    else:
        categorized["high_risk"].append(t)
valid = [t for t in transactions if t > 0]

total = 0
for t in valid:
    total = total + t

count = 0
for t in transactions:
    count = count + 1

summary = (count, total)

print("\n--- Categorized Transactions ---")
print("Normal    :", categorized["normal"])
print("Large     :", categorized["large"])
print("High Risk :", categorized["high_risk"])
print("Invalid   :", categorized["invalid"])

print("Summary")
print("Total Transactions :", summary[0])
print("Total Amount       :", summary[1])

frequent   = count > 5
big_spend  = total > 5000
suspicious = len(categorized["high_risk"]) >= 3

print("Patterns Detected:")
if frequent:
    print("Frequent Transactions (more than 5)")
if big_spend:
    print("Large Spending (total > 5000)")
if suspicious:
    print("Suspicious Pattern (3 or more high-risk)")
if not frequent and not big_spend and not suspicious:
    print("No suspicious patterns found")

print("Final Risk Level:")
if suspicious or (frequent and big_spend):
    print("Result: High Risk")
elif frequent or big_spend:
    print("Result: Moderate Risk")
else:
    print("Result: Low Risk")