# Write your solution here
def who_won(game_board: list):
    player_one = 0
    player_two = 0

    for line in game_board:
        for column in line:
            if column == 1:
                player_one +=1
            elif column == 2:
                player_two +=1
    
    if player_one > player_two:
        return 1
    elif player_two > player_one:
        return 2
    else:
        return 0

if __name__=="__main__":
    result = [[0,1,1],[2,2,2],[1,2,2]]
    print(who_won(result))