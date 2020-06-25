def latest(scores):
    return scores[-1]


def personal_best(scores):
    max = 0
    for i in scores:
        if i > max:
            max = i
    return max

def personal_top_three(scores):
    top_three = []
    dummy = scores.copy()
    for i in range(3):
        if dummy == []:
            return top_three
        else:
            score = personal_best(dummy)
            top_three.append(score)
            dummy.remove(score)
    return top_three
