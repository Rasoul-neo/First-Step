h= input("your high in Meter: ")
m= input("your weigh in kilogram: ")
bmi = float(m)/(float(h)**2)
print("your Bmi is: ", bmi)
if bmi<18.5:
    print("You are Underweight")
elif bmi>24.9:
    print("You are Overweight")
else:
    print("congratulation! You are Healthy")
