from src.hand import Hand
from assertpy import assert_that


def test_hand_has_rock_paper_scissors():
    assert_that(Hand).contains(Hand.Rock)
    assert_that(Hand).contains(Hand.Paper)
    assert_that(Hand).contains(Hand.Scissors)
