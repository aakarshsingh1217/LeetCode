from collections import defaultdict

def findWinners(matches: list[list[int]]) -> list[list[int]]:
    loss_records = defaultdict(int)

    for winner, loser in matches:
        if winner not in loss_records:
            loss_records[winner] = 0

        loss_records[loser] += 1

    ans = [[], []]

    for key in loss_records:
        if loss_records[key] == 0:
            ans[0].append(key)
        elif loss_records[key] == 1:
            ans[1].append(key)

    return [sorted(sublist) for sublist in ans]

"""
def findWinners(matches: List[List[int]]) -> List[List[int]]:
    losses_count = [-1] * 100001

    for winner, loser in matches:
        if losses_count[winner] == -1:
            losses_count[winner] = 0
        if losses_count[loser] == -1:
            losses_count[loser] = 1
        else:
            losses_count[loser] += 1

    answer = [[], []]
    for i in range(100001):
        if losses_count[i] == 0:
            answer[0].append(i)
        elif losses_count[i] == 1:
            answer[1].append(i)

    return answer
"""