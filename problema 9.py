A=(input("Introduceti litere mari din alfabetul latin in multimea A:"))
x=set()
for i in A:
    if i.isupper():
        x.add(i)
B=(input("Introduceti litere mari din alfabetul latin in multimea B:"))
y=set()
for l in B:
    if l.isupper():
        y.add(l)
print("intersectia multimilor A si B:", x.intersection(y))
print("reuniunea multimilor A si B:", x.union(y))
print("diferenta multimilor A si B:", x.difference(y))
print("diferenta multimilor A si B:", y.difference(x))