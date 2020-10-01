board=[]
scores=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    board.append((name,score))
    scores.append(score)


second_lowest = sorted(set(scores))[1]
for k,v in sorted(board):
    if v==second_lowest:
        print(k)
