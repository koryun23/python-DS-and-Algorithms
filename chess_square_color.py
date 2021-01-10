def color(letter,number):
    letters = ['a','b','c','d','e','f','g','h']
    ans = ['white', 'black']
    index = (letters.index(letter) + number) %2
    return ans[index]

print(color('f', 5))
