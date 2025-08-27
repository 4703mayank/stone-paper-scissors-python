
import random
from enum import Enum, auto


class Move(Enum):
    STONE = auto()
    PAPER = auto()
    SCISSORS = auto()

    @staticmethod
    def from_string(s: str):
        s = s.strip().lower()
        if s in ("stone", "rock", "r", "s"):
            return Move.STONE
        if s in ("paper", "p"):
            return Move.PAPER
        if s in ("scissors", "scissor", "x", "c"):
            return Move.SCISSORS
        raise ValueError(f"Invalid move: {s}")

    def beats(self, other: "Move") -> bool:
        return (
            (self is Move.STONE and other is Move.SCISSORS) or
            (self is Move.PAPER and other is Move.STONE) or
            (self is Move.SCISSORS and other is Move.PAPER)
        )


RESULT_DRAW = "draw"
RESULT_PLAYER = "player"
RESULT_COMPUTER = "computer"


def play_round(player_move: Move, computer_move: Move | None = None):
    """Compute one round. If computer_move not given, choose randomly."""
    if computer_move is None:
        computer_move = random.choice(list(Move))

    if player_move == computer_move:
        return RESULT_DRAW, player_move, computer_move

    if player_move.beats(computer_move):
        return RESULT_PLAYER, player_move, computer_move

    return RESULT_COMPUTER, player_move, computer_move


def move_to_emoji(move: Move) -> str:
    return {
        Move.STONE: "🪨",
        Move.PAPER: "📄",
        Move.SCISSORS: "✂️",
    }[move]
