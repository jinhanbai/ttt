from helper import Helper

Helper = Helper()   

class Game:
    def __init__(self) -> None:
        # player earns 3 points when won, 1 point when draw and 0 when lost
        self.player_info = {'O': {'First Name': None, 'Last Name': None, 'points': 0},
                            'X': {'First Name': None, 'Last Name': None, 'points': 0}}
        self.mapping = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
        self.winner = None 
    
    def play(self):
        self.get_player_info()
        self.start_game()
        self.process_result()
    
    def get_player_info(self):
        for key in self.player_info.keys():
            self.player_info[key]['First Name'] = input(f"Player {str(key)} First Name: ")
            self.player_info[key]['Last Name'] = input(f"Player {str(key)} Last Name: ")

    def start_game(self):
        #print initial board state
        Helper.print_board(self.mapping)

        turn = 0
        turn_map = ['O', 'X']
        while True:
            player = turn_map[turn]
            user_input = input(f"Player {player} choice (1-9): ")
            self.mapping[int(user_input)] = 'O' if turn % 2 == 0 else 'X'
            Helper.print_board(self.mapping)
            status = Helper.check_status(self.mapping)
            if status == 'Another move is possible':
                print(status) 
            else:
                self.winner = status
                break
            turn = (turn + 1) % 2

    def process_result(self):
        print("_________________________Game Over_________________________")
        if self.winner == 'Draw':
            print("It's a draw!")
            for key in self.player_info.keys():
                self.player_info[key]['points'] += 1
                print(f"{self.player_info[key]['First Name']} {self.player_info[key]['Last Name']} earned {self.player_info[key]['points']} points")
        else:
            print(f"Player {self.winner} wins!")
            self.player_info[self.winner]['points'] += 3
            print(f"{self.player_info[self.winner]['First Name']} {self.player_info[self.winner]['Last Name']} earned {self.player_info[self.winner]['points']} points")