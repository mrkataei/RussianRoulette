from run import Play


if __name__ == '__main__':
    one = ""
    two = ""
    same_players = False
    while True:
        if not same_players:
            one = input('>Enter player one\n>')
            two = input('>Enter player two\n>')
        game_play = Play(first_player=one, sec_player=two)
        game_play.run()
        again = input('>Do you want play again[Y/n]?\n>')
        if again == 'n':
            break
        else:
            same_players = True if input(f'>Is the name of {one} and {two} players[Y/n]?\n>') != 'n' else False
            continue
