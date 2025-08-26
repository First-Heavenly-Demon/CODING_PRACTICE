subscribed_english = int(input())
E = set(map(int, input().split()))
 
subscribed_french = int(input())
F = set(map(int, input().split()))

print(len(E.difference(F)))
