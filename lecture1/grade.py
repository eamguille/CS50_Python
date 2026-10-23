
score = int(input("Score: "))

if 90 <= score <= 100: # This is the same as say `if score >= 90 and score <= 100`
    print("Grade A")
elif 80 <= score < 90:
    print("Grade B")
elif 70 <= score < 80:
    print("Grade C")
elif 60 <= score < 70:
    print("Grade D")
else:
    print("Grade F")


# Optimized version: We are assuming that score can only goes from 0 to 100.
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")