# BMI 2

print('BMI calculator.')

weight = float(input('Digit your weight: '))
height = float(input('Digit your height: '))
bmi = weight / height ** 2


if bmi <= 18.5:
    print("U're underweight.")
elif 18.5 < bmi <= 25:
    print("U've a normal weight.")
elif 25 < bmi <= 30:
    print("U're slightly overweight.")
elif 30 < bmi <= 35:
    print("U're obese.")
elif bmi >= 35:
    print("U're clinically obese.")

print(f'Your BMI: {bmi:.2f}')