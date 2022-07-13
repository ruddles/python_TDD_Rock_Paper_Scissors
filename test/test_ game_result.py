from src.game_result import GameResult
from assertpy import assert_that


def test_game_result_has_player1win_player2win_draw():
    assert_that(GameResult).contains(GameResult.Player1Win)
    assert_that(GameResult).contains(GameResult.Player2Win)
    assert_that(GameResult).contains(GameResult.Draw)
