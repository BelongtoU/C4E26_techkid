cm_height = float(input("Your height (cm): "))
weight = float(input("Your weight (kg): "))
m_height = cm_height/100
BMI = weight/(m_height**2)
if BMI < 16:
    print("Your Body Mass Index is", BMI, ", severly underweight !!!")
elif BMI <= 18.5:
    print("Your Body Mass Index is", BMI, ", underweight !!!")
elif BMI <= 25:
    print("Your Body Mass Index is", BMI, ", nomal !!!")
elif BMI <= 30:
    print("Your Body Mass Index is", BMI, ", overweight !!!")
else:
    print("Your Body Mass Index is", BMI, ", obese !!!")
