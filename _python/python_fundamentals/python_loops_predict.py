#1: 1 2 3 4 5 6 7 8 9
for i in range(1, 10, 1):
    print(i)

#2: 1 4 7
for t in range(1, 10, 3):
    print(t)

#3: 0 1 2 3 4
for y in range(5):
    if y < 5:
        print(y)
    elif y == 3:
        print("y is 3")

#4: 20 17 14 11 8 5 2
for j in range(20, 1, -3):
    print(j)

#5: London Paris Tokyo
cities = ["London", "Paris", "Tokyo"]
for city in cities:
    print(city)

#6: 0 7 1 13 2 8 3 42 The answer to life, the universe, and everything.
numbers = [7, 13, 8, 42]
for x in range(0, len(numbers)):
    print(x)
    print(numbers[x])
if numbers[len(numbers) - 1] == 42:
    print("The answer to life, the universe, and everything.")

#7: Hello 1 Hello 3 Hello 5 Hello 7 Hello 9
for num in range(10):
    if num % 2 == 0:
        print("Hello")
    elif num % 4 == 0:
        print("World")
    else:
        print(num)

#8: Hello 1 World 3 Hello 5 World 7 Hello 9
for num in range(10):
    if num % 4 == 0:
        print("Hello")
    elif num % 2 == 0:
        print("World")
    else:
        print(num)

#9: name Fido age 4 trick rolls over
pet_info = {
    "name": "Fido", 
    "age": 4, 
    "trick": "rolls over"
}
for key in pet_info:
    print(key)
    print(pet_info[key])

#10: First, I will use the 20 minute rule and use the platform and other resources to fine my answer
# Second, I will ask my classmates for help, like how I would ask a fellow employee at my job
# Third, I will ask an available TA ina  public setting, so everyone can benefit from my question
# Fourth, I will ask an available instructor
things_to_remember = {
    "First": "use the 20 minute rule and use the platform and other resources to find my answer",
    "Second": "ask my classmates for help, like how I would ask a fellow employee at my job",
    "Third": "ask an available TA in a public setting, so everyone can benefit from my question",
    "Fourth": "ask an available instructor"
}
for num, step in things_to_remember.items():
    print(num + ", I will " + step)

