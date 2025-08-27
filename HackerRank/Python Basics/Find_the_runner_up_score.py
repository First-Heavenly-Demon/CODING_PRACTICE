if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    Highest_score = max(arr)
    new_list = []
    for score in arr:
        if score != Highest_score:
            new_list.append(score)
    runner_up = max(new_list)
    print(runner_up)
