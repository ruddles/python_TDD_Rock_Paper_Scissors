from src.game import check, get_random_hand
from src.hand import Hand
from assertpy import assert_that
from src.game_result import GameResult
from unittest.mock import patch


def test_check_returns_draw_for_2_rocks():
    # arrange / given
    player_1_hand = Hand.Rock
    player_2_hand = Hand.Rock

    # act / when
    result = check(player_1_hand, player_2_hand)

    # assert / then
    assert_that(result).is_equal_to(GameResult.Draw)


def test_check_returns_player_1_win_when_rock_vs_scissors():
    # arrange / given
    player_1_hand = Hand.Rock
    player_2_hand = Hand.Scissors

    # act / when
    result = check(player_1_hand, player_2_hand)

    # assert / then
    assert_that(result).is_equal_to(GameResult.Player1Win)


def test_check_returns_player_2_win_when_rock_vs_paper():
    # arrange / given
    player_1_hand = Hand.Rock
    player_2_hand = Hand.Paper

    # act / when
    result = check(player_1_hand, player_2_hand)

    # assert / then
    assert_that(result).is_equal_to(GameResult.Player2Win)


def test_check_returns_player_1_win_when_scissors_vs_paper():
    # arrange / given
    player_1_hand = Hand.Scissors
    player_2_hand = Hand.Paper

    # act / when
    result = check(player_1_hand, player_2_hand)

    # assert / then
    assert_that(result).is_equal_to(GameResult.Player1Win)


def test_check_returns_player_1_win_when_scissors_vs_rock():
    # arrange / given
    player_1_hand = Hand.Scissors
    player_2_hand = Hand.Rock

    # act / when
    result = check(player_1_hand, player_2_hand)

    # assert / then
    assert_that(result).is_equal_to(GameResult.Player2Win)


def test_check_returns_dar_when_scissors_vs_scissors():
    # arrange / given
    player_1_hand = Hand.Scissors
    player_2_hand = Hand.Scissors

    # act / when
    result = check(player_1_hand, player_2_hand)

    # assert / then
    assert_that(result).is_equal_to(GameResult.Draw)


@patch("random.randint")
def test_get_random_hand_returns_rock_for_0(random_mock):
    random_mock.return_value = 0

    result = get_random_hand()

    assert_that(result).is_equal_to(Hand.Rock)


@patch("random.randint")
def test_get_random_hand_returns_paper_for_1(random_mock):
    random_mock.return_value = 1

    result = get_random_hand()

    assert_that(result).is_equal_to(Hand.Paper)


@patch("random.randint")
def test_get_random_hand_returns_scissors_for_2(random_mock):
    random_mock.return_value = 2

    result = get_random_hand()

    assert_that(result).is_equal_to(Hand.Scissors)
