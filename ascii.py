# 30 chars per line.

def flop_string(cards):
	custom_string  = "+-------+ +-------+ +-------+\n"
	custom_string += "|       | |       | |       |\n"
	custom_string += "|       | |       | |       |\n"
	custom_string += "|       | |       | |       |\n"
	custom_string += "|       | |       | |       |\n"
	custom_string += "|       | |       | |       |\n"
	custom_string += "+-------+ +-------+ +-------+\n"
	
	card1 = cards[0]
	card2 = cards[1]
	card3 = cards[2]
	card1_suit = str(card1)[-1]
	card2_suit = str(card2)[-1]
	card3_suit = str(card3)[-1]
	len_card1 = len(str(card1))
	len_card2 = len(str(card2))
	len_card3 = len(str(card3))
	
	top_left_first_card  = 31
	top_left_second_card = top_left_first_card + 10
	top_left_third_card  = top_left_second_card + 10
	
	center_first_card  = 94
	center_second_card = center_first_card + 10
	center_third_card  = center_second_card + 10
	
	bottom_right_first_card  = 158
	bottom_right_second_card = bottom_right_first_card + 10
	bottom_right_third_card  = bottom_right_second_card + 10
	
	custom_string = custom_string[:top_left_first_card]                \
					+ str(card1)                                       \
	                + custom_string[top_left_first_card + len_card1:]
	
	custom_string = custom_string[:center_first_card]         \
					+ card1_suit                              \
	                + custom_string[center_first_card + 1:]
	
	custom_string = custom_string[:bottom_right_first_card - len_card1]   \
					+ str(card1)                                           \
	                + custom_string[bottom_right_first_card:]
	
	custom_string = custom_string[:top_left_second_card]       \
					+ str(card2)                               \
	                + custom_string[top_left_second_card + len_card2:]
	
	custom_string = custom_string[:center_second_card]         \
					+ card2_suit                               \
	                + custom_string[center_second_card + 1:]
	
	custom_string = custom_string[:bottom_right_second_card - len_card2]    \
					+ str(card2)                                             \
	                + custom_string[bottom_right_second_card:]
	
	custom_string = custom_string[:top_left_third_card]       \
					+ str(card3)                              \
	                + custom_string[top_left_third_card + len_card3:]
	
	custom_string = custom_string[:center_third_card]         \
					+ card3_suit                              \
	                + custom_string[center_third_card + 1:]
	
	custom_string = custom_string[:bottom_right_third_card - len_card3]  \
					+ str(card3)                                         \
	                + custom_string[bottom_right_third_card:]
	return custom_string

def flop_turn_string(cards):
	custom_string  = "+-------+ +-------+ +-------+ +-------+\n"
	custom_string += "|       | |       | |       | |       |\n"
	custom_string += "|       | |       | |       | |       |\n"
	custom_string += "|       | |       | |       | |       |\n"
	custom_string += "|       | |       | |       | |       |\n"
	custom_string += "|       | |       | |       | |       |\n"
	custom_string += "+-------+ +-------+ +-------+ +-------+\n"
	
	card1 = cards[0]
	card2 = cards[1]
	card3 = cards[2]
	card4 = cards[3]
	card1_suit = str(card1)[-1]
	card2_suit = str(card2)[-1]
	card3_suit = str(card3)[-1]
	card4_suit = str(card4)[-1]
	len_card1 = len(str(card1))
	len_card2 = len(str(card2))
	len_card3 = len(str(card3))
	len_card4 = len(str(card4))
	
	top_left_first_card  = 41
	top_left_second_card = top_left_first_card + 10
	top_left_third_card  = top_left_second_card + 10
	top_left_fourth_card  = top_left_third_card + 10
	
	center_first_card  = 124
	center_second_card = center_first_card + 10
	center_third_card  = center_second_card + 10
	center_fourth_card  = center_third_card + 10
	
	bottom_right_first_card  = 208
	bottom_right_second_card = bottom_right_first_card + 10
	bottom_right_third_card  = bottom_right_second_card + 10
	bottom_right_fourth_card  = bottom_right_third_card + 10
	
	custom_string = custom_string[:top_left_first_card]                \
					+ str(card1)                                       \
	                + custom_string[top_left_first_card + len_card1:]
	
	custom_string = custom_string[:center_first_card]         \
					+ card1_suit                              \
	                + custom_string[center_first_card + 1:]
	
	custom_string = custom_string[:bottom_right_first_card - len_card1]   \
					+ str(card1)                                           \
	                + custom_string[bottom_right_first_card:]
	
	custom_string = custom_string[:top_left_second_card]       \
					+ str(card2)                               \
	                + custom_string[top_left_second_card + len_card2:]
	
	custom_string = custom_string[:center_second_card]         \
					+ card2_suit                               \
	                + custom_string[center_second_card + 1:]
	
	custom_string = custom_string[:bottom_right_second_card - len_card2]    \
					+ str(card2)                                             \
	                + custom_string[bottom_right_second_card:]
	
	custom_string = custom_string[:top_left_third_card]       \
					+ str(card3)                              \
	                + custom_string[top_left_third_card + len_card3:]
	
	custom_string = custom_string[:center_third_card]         \
					+ card3_suit                              \
	                + custom_string[center_third_card + 1:]
	
	custom_string = custom_string[:bottom_right_third_card - len_card3]  \
					+ str(card3)                                         \
	                + custom_string[bottom_right_third_card:]

	custom_string = custom_string[:top_left_fourth_card]       \
					+ str(card4)                              \
	                + custom_string[top_left_fourth_card + len_card4:]
	
	custom_string = custom_string[:center_fourth_card]         \
					+ card4_suit                              \
	                + custom_string[center_fourth_card + 1:]
	
	custom_string = custom_string[:bottom_right_fourth_card - len_card4]  \
					+ str(card4)                                         \
	                + custom_string[bottom_right_fourth_card:]
	return custom_string

def flop_turn_river_string(cards):
	custom_string  = "+-------+ +-------+ +-------+ +-------+ +-------+\n"
	custom_string += "|       | |       | |       | |       | |       |\n"
	custom_string += "|       | |       | |       | |       | |       |\n"
	custom_string += "|       | |       | |       | |       | |       |\n"
	custom_string += "|       | |       | |       | |       | |       |\n"
	custom_string += "|       | |       | |       | |       | |       |\n"
	custom_string += "+-------+ +-------+ +-------+ +-------+ +-------+\n"
	
	card1 = cards[0]
	card2 = cards[1]
	card3 = cards[2]
	card4 = cards[3]
	card5 = cards[4]
	card1_suit = str(card1)[-1]
	card2_suit = str(card2)[-1]
	card3_suit = str(card3)[-1]
	card4_suit = str(card4)[-1]
	card5_suit = str(card5)[-1]
	len_card1 = len(str(card1))
	len_card2 = len(str(card2))
	len_card3 = len(str(card3))
	len_card4 = len(str(card4))
	len_card5 = len(str(card5))
	
	top_left_first_card  = 51
	top_left_second_card = top_left_first_card + 10
	top_left_third_card  = top_left_second_card + 10
	top_left_fourth_card  = top_left_third_card + 10
	top_left_fifth_card  = top_left_fourth_card + 10
	
	center_first_card  = 154
	center_second_card = center_first_card + 10
	center_third_card  = center_second_card + 10
	center_fourth_card  = center_third_card + 10
	center_fifth_card  = center_fourth_card + 10
	
	bottom_right_first_card  = 258
	bottom_right_second_card = bottom_right_first_card + 10
	bottom_right_third_card  = bottom_right_second_card + 10
	bottom_right_fourth_card  = bottom_right_third_card + 10
	bottom_right_fifth_card  = bottom_right_fourth_card + 10
	
	custom_string = custom_string[:top_left_first_card]                \
					+ str(card1)                                       \
	                + custom_string[top_left_first_card + len_card1:]
	
	custom_string = custom_string[:center_first_card]         \
					+ card1_suit                              \
	                + custom_string[center_first_card + 1:]
	
	custom_string = custom_string[:bottom_right_first_card - len_card1]   \
					+ str(card1)                                           \
	                + custom_string[bottom_right_first_card:]
	
	custom_string = custom_string[:top_left_second_card]       \
					+ str(card2)                               \
	                + custom_string[top_left_second_card + len_card2:]
	
	custom_string = custom_string[:center_second_card]         \
					+ card2_suit                               \
	                + custom_string[center_second_card + 1:]
	
	custom_string = custom_string[:bottom_right_second_card - len_card2]    \
					+ str(card2)                                             \
	                + custom_string[bottom_right_second_card:]
	
	custom_string = custom_string[:top_left_third_card]       \
					+ str(card3)                              \
	                + custom_string[top_left_third_card + len_card3:]
	
	custom_string = custom_string[:center_third_card]         \
					+ card3_suit                              \
	                + custom_string[center_third_card + 1:]
	
	custom_string = custom_string[:bottom_right_third_card - len_card3]  \
					+ str(card3)                                         \
	                + custom_string[bottom_right_third_card:]

	custom_string = custom_string[:top_left_fourth_card]       \
					+ str(card4)                              \
	                + custom_string[top_left_fourth_card + len_card4:]
	
	custom_string = custom_string[:center_fourth_card]         \
					+ card4_suit                              \
	                + custom_string[center_fourth_card + 1:]
	
	custom_string = custom_string[:bottom_right_fourth_card - len_card4]  \
					+ str(card4)                                         \
	                + custom_string[bottom_right_fourth_card:]

	custom_string = custom_string[:top_left_fifth_card]       \
					+ str(card5)                              \
	                + custom_string[top_left_fifth_card + len_card5:]
	
	custom_string = custom_string[:center_fifth_card]         \
					+ card5_suit                              \
	                + custom_string[center_fifth_card + 1:]
	
	custom_string = custom_string[:bottom_right_fifth_card - len_card5]  \
					+ str(card5)                                         \
	                + custom_string[bottom_right_fifth_card:]
	return custom_string
