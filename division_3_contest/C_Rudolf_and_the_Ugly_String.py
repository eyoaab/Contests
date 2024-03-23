t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    pie=s.count('pie')
    map=s.count('map')
    map_pie=s.count('mapie')
    print(pie+map-map_pie)