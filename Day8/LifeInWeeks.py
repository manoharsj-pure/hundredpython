def life_in_weeks(age):
    # print(f"life in weeks{age}")
    years_left_in_life = 70 - age
    # print(f"age in years{years_left_in_life}")
    weeks_remaining = years_left_in_life * 52
    # print(f"You have {life_in_weeks} weeks left")
    print(f"You have {weeks_remaining} weeks left.")
    return life_in_weeks

#age = input("Enter your Currrent Age")
life_in_weeks(int(input("Enter your Current Age")))

