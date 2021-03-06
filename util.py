from os import system
import ascii
import sys
is_windows = hasattr(sys, 'getwindowsversion')
MAX_TIME = 999999.99
MAX_SCORE = 99999

winning_hand_log_filename = "winning_hands.log"
losing_hand_log_filename = "losing_hands.log"

def clear_screen():
	if is_windows:
		system('cls')
	else:
		system('clear')

def lives_2_hearts(lives):
	hearts_str = ""
	if is_windows:
		for i in range(lives):
			hearts_str += "♥"
		for i in range(lives):
			hearts_str += " "
	else:
		for i in range(lives):
			hearts_str += "♥"
		for i in range(3 - lives):
			hearts_str += "♡"
	return hearts_str	

def pause(page):
	while True:
		user_input = input("")
		if user_input == 'q':
			clear_screen()
			exit()
		elif user_input == 'r':
			ascii.show_rankings()
		else:
			break
		print(page)

def show_tutorial():
	page1 = open("tutorial_page_1.txt", "r")
	page1_str = page1.read()
	page2 = open("tutorial_page_2.txt", "r")
	page2_str = page2.read()
	clear_screen()
	print(page1_str)
	pause(page1_str)
	clear_screen()
	print(page2_str)
	pause(page2_str)

def show_instructions():
	page1 = open("instructions_page_1.txt", "r")
	page1_str = page1.read()
	page2 = open("instructions_page_2.txt", "r")
	page2_str = page2.read()
	clear_screen()
	print(page1_str)
	pause(page1_str)
	clear_screen()
	print(page2_str)
	pause(page2_str)

def is_tutorial_mode(): 
	answer = 'x'
	while answer != 'y' and answer != 'n':
		print("Would you like to play in tutorial mode? (y/n) q to exit")
		answer = input()
		if answer == "":
			continue
		if answer == "q":
			exit()
	return answer == 'y'

def clear_player_hands(players):
	for player in players:
		player.fold()

def process_continuation_input(state):
	while True:
		user_input = input("")
		if user_input == 'q':
			clear_screen()
			exit()
		elif user_input == 'r':
			ascii.show_rankings()
		elif user_input == 'i':
			show_instructions()
		else:
			break
		print(state)
	
def print_preflop(board_state):
	print(board_state + "\n\n\n\n\n\n\n\nPre-flop")

def clear_logs():
	f = open(winning_hand_log_filename, 'w', encoding='utf-8')
	f.close()
	f = open(losing_hand_log_filename, 'w', encoding='utf-8')
	f.close()

def write_to_file(filename, text):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)

def record_hands(players, winners, game_round):
	for p in players:
		is_winner = False
		for w in winners:
			if w[0].id == p.id:
				is_winner = True
				break
		msg = "R " + str(game_round) + ", "
		if is_winner:
			msg += p.hand_stringify() + "\n"
			write_to_file(winning_hand_log_filename, msg)
		else:
			msg += p.hand_stringify() + "\n"
			write_to_file(losing_hand_log_filename, msg)
			

def get_user_name():
	name = ""
	uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lowercase =	"abcdefghijklmnopqrstuvwxyz" 
	digits = "1234567890"
	allowed_characters = uppercase + lowercase + digits + " " + "_"
	while(True):
		bad_chars = False
		name = input("Your name:")
		if len(name) > 20:
			continue
		if len(name) == 0:
			continue
		for c in name:
			if c not in allowed_characters:
				bad_chars = True
				break
		if not bad_chars:
			break
	return name

def draw_scoreboard(entries):
	clear_screen()
	print()
	print("                 HIGHEST CASH-INS")
	print("######################################################## ")
	print('|    {:<30}{:>6} {:>10}   |'.format("Name", "Made", "In"))
	print("######################################################## ")
	for i, e in enumerate(entries, start=1):
		print('| {:<2} {:<30}{:>6} {:>10}   |'.format(str(i),               \
                                                      e.get("name"),        \
								                      '$' + e.get("score"), \
                                                      e.get("time") + 'm'))
		print("+------------------------------------------------------+ ")

def save_score(user, play_time):
	if play_time > MAX_TIME:
		play_time = MAX_TIME
	if user.score > MAX_SCORE:
		user.score = MAX_SCORE
	entries = []
	with open("score_board.csv", "r") as file:
		for line in file:
			print(line)
			name, score, time = line.split(',')
			time = time[:-1] # get rid of new line
			entries.append({"name": name, "score": score, "time": time})

	draw_scoreboard(entries)
	name = get_user_name()
	entries.append({"name": name,             \
                    "score": str(user.score), \
                    "time": '{:.2f}'.format(play_time)})

	entries.sort(reverse=True, \
                 key=lambda e: (float(e.get('score')), float(e.get('time'))))
	score_board_w = open("score_board.csv", "w")
	for e in entries[:10]:
		score_board_w.write(e.get("name")  + "," +\
                            e.get("score") + "," + \
                            e.get("time")  + "\n")
	draw_scoreboard(entries)
	input()

