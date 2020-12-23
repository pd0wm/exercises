#!/usr/bin/env python3
from collections import deque


def winner_01(player1, player2):
    if len(player1) == 0:
        return 2
    elif len(player2) == 0:
        return 1
    else:
        return 0

def play_game_01(player1, player2):
    p1, p2 = player1.copy(), player2.copy()

    while not winner_01(p1, p2):
        a, b = p1.popleft(), p2.popleft()

        winner = 1 if a > b else 2

        if winner == 1:
            p1.append(a)
            p1.append(b)
        else:
            p2.append(b)
            p2.append(a)

    return p1, p2, winner_01(p1, p2)


games = {}

def play_game_02(player1, player2, n):
    p1, p2 = player1.copy(), player2.copy()

    seen = set()

    i = 1
    while not winner_01(p1, p2):
        # Before either player deals a card, if there was a previous round in
        # this game that had exactly the same cards in the same order in the
        # same players' decks, the game instantly ends in a win for player 1.
        # Previous rounds from other games are not considered.
        # (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
        h = (tuple(p1), tuple(p2))
        if h in seen:
            return p1, p2, 1

        seen.add(h)

        # Otherwise, this round's cards must be in a new configuration;
        # the players begin the round by each drawing the top card of their deck as normal.
        a, b = p1.popleft(), p2.popleft()

        # If both players have at least as many cards remaining in their deck
        # as the value of the card they just drew, the winner of the round is determined by
        # playing a new game of Recursive Combat (see below).
        if len(p1) >= a and len(p2) >= b:
            # To play a sub-game of Recursive Combat, each player creates a new deck by making
            # a copy of the next cards in their deck (the quantity of cards copied is
            # equal to the number on the card they drew to trigger the sub-game).
            p1_new = deque(list(p1)[:a])
            p2_new = deque(list(p2)[:b])
            _, _, winner = play_game_02(p1_new, p2_new, n + 1)
        # Otherwise, at least one player must not have enough cards left in their deck to recurse;
        # the winner of the round is the player with the higher-value card.
        else:
            winner = 1 if a > b else 2

        if winner == 1:
            p1.append(a)
            p1.append(b)
        else:
            p2.append(b)
            p2.append(a)

        i += 1

    return p1, p2, winner_01(p1, p2)


if __name__ == "__main__":
    player = 0
    player1 = deque()
    player2 = deque()

    with open('input_22') as f:
        for line in f:
            line = line.strip()
            if line.startswith('Player'):
                player += 1
                continue
            if not line:
                continue

            i = int(line)
            if player == 1:
                player1.append(i)
            else:
                player2.append(i)


    # Part 1
    p1, p2, winner = play_game_01(player1, player2)
    winner_hand = p1 if winner == 1 else p2

    solution_01 = 0
    for a, b in zip(list(winner_hand)[::-1], range(1, len(winner_hand)+1)):
        solution_01 += a * b
    print(solution_01)

    # Part 2
    p1, p2, winner = play_game_02(player1, player2, 1)
    winner_hand = p1 if winner == 1 else p2

    solution_02 = 0
    for a, b in zip(list(winner_hand)[::-1], range(1, len(winner_hand)+1)):
        solution_02 += a * b
    print(solution_02)
