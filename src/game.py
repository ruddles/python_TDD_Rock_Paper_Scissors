from src.hand import Hand
from src.game_result import GameResult
import random


def check(player_1_hand: Hand, player_2_hand: Hand) -> GameResult:
    _result_map = {Hand.Rock: Hand.Scissors, Hand.Scissors: Hand.Paper}

    if player_1_hand == player_2_hand:
        return GameResult.Draw

    if _result_map[player_1_hand] == player_2_hand:
        return GameResult.Player1Win

    return GameResult.Player2Win


def get_random_hand() -> Hand:
    seed = random.randint(0, 2)
    return Hand(seed)
