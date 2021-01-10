class Chess:
    def __init__(self):
        self.board = []
    def create_board(self):
        letters = ['a','b','c','d','e','f','g','h']
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        for j in range(len(numbers)):
            self.board.append([])
            for k in range(len(letters)):
                self.board[j].append([letters[k],numbers[7-j]])
    def pawn(self, letter, number):
        fields = []
        fields.append([letter,number+1])
        if number == 2:
            fields.append([letter,number+2])
        return fields
    def rook(self,letter,number):
        fields = []
        letters = ['a','b','c','d','e','f','g','h']
        for i in range(1,9):
            if i != number:
                fields.append([letter,i])
        for i in range(len(letters)):
            if letters[i] != letter:
                fields.append([letters[i], number])

        return fields
    def king(self,letter,number):
        letters = ['a','b','c','d','e','f','g','h']
        letter_index = letters.index(letter)
        fields = []
        directions = [
            [letter_index,number-1],
            [letter_index,number+1],
            [letter_index+1,number],
            [letter_index-1,number],
            [letter_index+1,number+1],
            [letter_index+1,number-1],
            [letter_index-1,number+1],
            [letter_index-1,number-1]
        ]
        for i in range(len(directions)):
            if directions[i][0] >= 0 and directions[i][0] <=7 and directions[i][1] >0 and directions[i][1] <=8:
                fields.append([letters[directions[i][0]],directions[i][1]])
        return fields       
    def bishop(self, letter,number):
        letters = ['a','b','c','d','e','f','g','h']
        letter_index = letters.index(letter)
        fields = []
        temp_index = letter_index
        temp_number=number
        while temp_index> 0 and temp_number <7:
            fields.append([letters[temp_index-1],temp_number+1])
            temp_index-=1
            temp_number+=1
        temp_index = letter_index
        temp_number = number
        while temp_index > 0 and temp_number >1:
            fields.append([letters[temp_index-1], temp_number-1])
            temp_index -= 1
            temp_number -= 1
        temp_index = letter_index
        temp_number = number
        while temp_number < 8 and temp_index<7:
            fields.append([letters[temp_index+1],temp_number+1])
            temp_index += 1
            temp_number += 1
        temp_index = letter_index
        temp_number = number
        while temp_number > 1 and temp_index <7:
            fields.append([letters[temp_index+1], temp_number-1])
            temp_index += 1
            temp_number -= 1
        return fields
    def knight(self,letter,number):
        letters = ['a','b','c','d','e','f','g','h']
        letter_index = letters.index(letter)
        fields = []
        directions = [
            [letter_index+2,number-1],
            [letter_index+2,number+1],
            [letter_index+1,number+2],
            [letter_index-1,number+2],
            [letter_index-2,number+1],
            [letter_index-2,number-1],
            [letter_index-1,number-2],
            [letter_index+1,number-2]
        ]
        for i in range(len(directions)):
            if directions[i][0] >= 0 and directions[i][0] <= 7 and directions[i][1] > 0 and directions[i][1] <=8:
                fields.append([letters[directions[i][0]], directions[i][1]])
        return fields
    def queen(self,letter,number):
        return self.rook(letter,number)+self.bishop(letter,number)




chess = Chess()
print('pawn: ',chess.pawn('a',3))
print('rook: ',chess.rook('a',1))
print('king: ',chess.king('a',1))
print('bishop: ',chess.bishop('d',4))
print('knight: ',chess.knight('d',4))
print('bishop: ',chess.bishop('d',8))
print('queen: ',chess.queen('d',2))