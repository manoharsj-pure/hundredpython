def calcualate_love_score(first, second , metric):
    metric_list = list(metric)

    metric_count = 0
    first_name = first.lower()
    second_name = second.lower()
    couple_list = [first_name, second_name]
    for name in couple_list:
        for true_letter in metric_list:
            for name_letter in name:
                if true_letter == name_letter:
                    metric_count += 1
    return metric_count


truth_score = calcualate_love_score("kanye West", "Kim Kardashian" , "true")
love_score = calcualate_love_score("Kanye West", "Kim Kardashian" , "love" )

print(f"love score is {truth_score}{love_score}")
#print(f"true score is {love_score}")


