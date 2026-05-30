sentence = " Hello, my name is Vraj and I am learning Python. "

print(sentence.strip())
print(sentence.strip().lower())
print(sentence.strip().upper())
print(sentence.strip().replace("Vraj","Hunter"))
print(sentence.strip().count("a"))
print(sentence.strip().find("Python"))
print(sentence.strip().startswith("Hello"))
print(sentence.strip().split())

words = ["Python", "is", "powerful"]
print(" ".join(words))
print("—".join(words))

name = "Vraj"
day = 6
topic =  "strings"
print(f"Day {day}: {name} learned about {topic}")

score = 95.6789
print(f"{score:.2f}")