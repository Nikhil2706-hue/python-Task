l = [
      {"a":["hockey","volley ball","foot ball"],
       "b": ("pushpa","dragon","Varanasi","aarya")},
      True,
      "67890",
      "5678.897",
      [78,False]
    ]

#1. 8.8
print(l[3][3:6])

#2. "79"
print(l[2][1:4:2])
print(l[3][-2:][::-1])

#3. ("pushpa","aarya")
print(l[0]["b"][0:4:3])

#4. nasi
print(l[0]["b"][2][4:])

#5. [78,False]
print(l[4])

#6. e al
print(l[0]["a"][1][4:11:2])

#7. key
print(l[0]["a"][0][3:])

#8."aphsup"
print(l[0]["b"][0][::-1])

#9. foot
print(l[0]["a"][2][:4])

#10.True
print(l[1])
