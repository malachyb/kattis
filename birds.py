input()
ans_key = input()

answers = {"Adrian": "ABC", "Bruno": "BABC", "Goran": "CCAABB"}
correct_answers = {"Adrian": 0, "Bruno": 0, "Goran": 0}
for i in range(len(ans_key)):
    for j, k in answers.items():
        if ans_key[i] == k[i % len(k)]:
            correct_answers[j] += 1

max_score = 0
for i in correct_answers:
    if max_score < correct_answers[i]:
        max_score = correct_answers[i]

print(max_score)
for i in correct_answers:
    if correct_answers[i] == max_score:
        print(i)
