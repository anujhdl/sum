scores = list(map(float, input("Enter scores separated by spaces: ").split()))

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Sum =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)