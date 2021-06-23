#print("hello friends")
print("Welcome to love calculator!")
name1 = input("Enter person1 name:\n")
name2 = input("Enter person2 name:\n")
l1 = name1.lower()
l2 = name2.lower()
final = list(l1+l2)
# TRUE count
t = final.count('t')
r = final.count('r')
u = final.count('u')
e = final.count('e')
print(f"T occurs {t} time")
print(f"R occurs {r} time")
print(f"U occurs {u} time")
print(f"E occurs {e} time")
total_occurs = t+r+u+e
print(f"total true occurs {total_occurs}")

# LOVE count
l = final.count('l')
O = final.count('o')
V = final.count('v')
print(f"L occurs {l} time")
print(f"O occurs {O} time")
print(f"V occurs {V} time")
print(f"E occurs {e} time")
total_love = l+O+V+e
print(f"total love occurs {total_love} time")
score = str(total_occurs)+str(total_love)
Score=int(score)


if Score<=10 or Score>=90:
    print(f"Your score {Score},you go together like coke and mentos.")
elif Score>=40 and Score<=50:
    print(f"Your score {Score}, you are alright together.")
else:
    print(f"Your score {Score}")

