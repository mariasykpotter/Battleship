import sea_battle
class Player:
    '''This class represents player'''
    def __init__(self, name):
        '''
        Initialises player
        (Player,str)->None
        '''
        self.name = name

    def read_position(self):
        '''
        Coverts a position into numbers
        (Player)->tuple
        '''
        position = ""
        print(self.name)
        while not ((len(position) == 2) and ('a' <= position[0] <= 'j') and ("0" <= position[1] <= "9")):
            position = input("{}, enter your position please".format(self.name))
        print((ord(position[0]) - ord("a"), int(position[1])-1))
        return (ord(position[0]) - ord("a"), int(position[1]) - 1)


class Game:
    '''Class represents game'''
    def __init__(self, fields, players, current_player):
        '''
        Initialises game
        (Game,list,list,Player)->None
        '''
        self.fields = fields
        self.players = players
        self.current_player = current_player

    def shoot_at(self, index, tuple,filename):
        '''Shoots at tuple position
        (Game,int,tuple,str)->tuple'''
        ''''''
        return self.fields[index].shoot_at(tuple,filename)

    def field_with_ships(self, index,tuple,filename):
        '''Prints field with ships
                (Game,int,tuple,str)->None'''
        print(self.fields[index].field_with_ships(self.shoot_at(index, tuple,filename)[0],
                                                     self.shoot_at(index, tuple,filename)[1],filename))

    def field_without_ships(self, index,tuple,filename):
        '''Prints field without ships
            (Game,int,tuple,str)->None'''

        print(self.fields[index].field_without_ships(self.shoot_at(index, tuple,filename)[0], self.shoot_at(index, tuple,filename)[1],filename))

    def change_player(self):
        '''Changes player.
                   (Game)->Player'''
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]
        return self.current_player.name
class Ship:
    '''Represents class ship'''
    def __init__(self, bow, length, horizontal):
        '''
        Initialises class ship
        (Ship,tuple,int,bool)->None
        '''
        self.bow = bow
        self._length = length
        self.hit = 0
        self.fields = []
        self.horizontal = horizontal
        if self.horizontal:
            for i in range(self._length):
                self.fields.append([self.bow[0] + i, self.bow[1], False])
        elif not self.horizontal:
            for i in range(self._length):
                self.fields.append([self.bow[0], self.bow[1] + i, False])

        # print(self.fields)

    def shoot_at(self, tup):
        '''Shoots at ship
        (Ship,tuple)->list
        '''
        self.hit += 1
        # print(self.hit)
        fields_final = []
        # print(self.fields)
        for field in self.fields:
            if field[0] == tup[0] and field[1] == tup[1]:
                field.remove(False)
                field.append(True)
            fields_final.append(field)
        self.__fields = fields_final
        return self.__fields

    def killed(self):
        '''Represents killed ship
        (Ship)->bool
        '''
        if self.length == self.hit:
            return True
        else:
            return False


class Field:
    '''Represents class field.'''

    def __init__(self,fields,shot,ships):
        '''Initialises class field
        (Field,list,list,list)->None'''
        self.__fields = fields
        self.shot = shot
        self.__ships =ships
    def shoot_at(self, tuple):
        '''Shoots at ship on the field.
        (Field,tuple)->tuple
        ('''
        shot = []
        lost = []
        try:
            if sea_battle.has_ship(self.__fields, tuple):
                if tuple not in self.shot:
                    for ship in self.__ships:
                        coords = ship.shoot_at(tuple)
                        # print(coords)
                        for coord in coords:
                            # print(coord)
                            shoot = coord.pop()
                            if shoot:
                                if coord[0] == tuple[0] and coord[1] == tuple[1]:
                                    shot.append(tuple)
                self.shot = shot
            else:
                lost.append(tuple)
        except IndexError:
            print("Marianna won!")
        return self.shot, lost

    def field_without_ships(self, shot, lost):
        '''Shows field without ships
        (Field,list,list)->str'''
        # item = input("Enter a character for a without_ships board:")
        item = " "
        field = self.__fields
        if shot:
            for el in shot:
                x = el[0]
                y = el[1]
                print(field[y])
                field[y][x] = "shot"
        elif lost:
            for el in lost:
                x = el[0]
                y = el[1]
                # print(field[y])
                field[y][x] = None
        else:
            print('''The field is invalid.
                                  Check please he number of ships and their length''')

        return sea_battle.field_to_str(field, item)

    def matrix(self):
        '''Shows matrix.
        (Field)->None
        '''
        for el in self.__fields:
            print(el)

    def killed_all_ships(self):
        '''Checks if all the ships are dead.
        (Field)->bool
        '''
        for el in self.__fields:
            for e in el:
                if e == 0:
                    return False
                    break
        return True

    def field_with_ships(self, shot, lost):
        '''Shows field without ships
        (Field,list,list)->str'''
        # item = input("Enter for a with_ships board ")
        item = " "
        # if sea_battle.is_valid(sea_battle.read_field(filename)):
        #     field = sea_battle.read_field(filename)
        field = self.fields
        if shot:
            for el in shot:
                x = el[0]
                y = el[1]
                # print(field[y])
                field[y][x] = "shot"
        elif lost:
            for el in lost:
                x = el[0]
                y = el[1]
                # print(field[y])
                field[y][x] = None
        else:
            print('''The field is invalid.
                           Check please he number of ships and their length''')
        return sea_battle.field_to_str_with_ships(field, item)



ship1 = Ship((2, 4), 4, True)
ship2 = Ship((5, 4), 4, True)
ships1 = [ship1]
ships2 = [ship1]
player1 = Player("Marianna")
player2 = Player("Minion")
print()
players = [player1, player2]
field111 = sea_battle.read_field("sea.txt")
field222 = sea_battle.read_field("sea.txt")
field1 = Field(field111, [], ships1)
field2 = Field(field222, [], ships2)
fieldss = [field111, field222]
game1 = Game(fieldss, players, player1)
while True:
    tup1 = player1.read_position()
    # print(field2.matrix)
    print(field2.field_without_ships(field2.shoot_at(tup1)[0], field2.shoot_at(tup1)[1]))
    print(field2.matrix())
    if field2.killed_all_ships():
        print("{} won!!!".format(player1.name))
        break
    else:
        game1.change_player()
        tup2 = player2.read_position()
        # print(field1.matrix())
        print(field1.field_without_ships(field1.shoot_at(tup2)[0], field1.shoot_at(tup2)[1]))
        print(field1.matrix())
        if field1.killed_all_ships():
            print("{} won!!!".format(player2.name))
            break
        game1.change_player()

