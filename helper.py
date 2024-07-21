class Helper:
    def __init__(self):
        pass
    
    def print_board(self, mapping : dict):
        print("-------------")
        print(f"| {mapping[1]} | {mapping[2]} | {mapping[3]} |")
        print("-------------")
        print(f"| {mapping[4]} | {mapping[5]} | {mapping[6]} |")
        print("-------------")
        print(f"| {mapping[7]} | {mapping[8]} | {mapping[9]} |")
        print("-------------")

    def check_status(self, mapping : dict):
        ##otherwise check for game result
        #check rows
        for i in range(1, 10, 3):
            if mapping[i] == mapping[i+1] == mapping[i+2]:
                return mapping[i]
        #check columns
        for i in range(1, 4):
            if mapping[i] == mapping[i+3] == mapping[i+6]:
                return mapping[i]
        #check diagonals
        if mapping[1] == mapping[5] == mapping[9]:
            return mapping[1]
        if mapping[3] == mapping[5] == mapping[7]:
            return mapping[3]
        
        ##if set of unique values != 2 ==> another move is possible
        if len(set(mapping.values())) != 2:
            return 'Another move is possible'
        
        return 'Draw'
