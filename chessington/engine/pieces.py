from __future__ import annotations
from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from chessington.engine.board import Board

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player: Player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board: Board) -> List[Square]:
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):

    def __init__(self, player: Player):
        self.player = player
        self.had_first_move = False

    """
    A class representing a chess pawn.
    """
    def get_available_moves(self, board) -> List[Square]:
        available_moves = []

        current_square = board.find_piece(self)
        if self.player == Player.BLACK:
            self.available_moves(available_moves, current_square, -1, -2)
        else:
            self.available_moves(available_moves, current_square, 1, 2)            
        
        return available_moves

    def available_moves(self, available_moves, current_square, sq_in_front : int, sq_two_in_front: int):
        square_in_front = Square.at(current_square.row + sq_in_front, current_square.col)
        available_moves.append(square_in_front)
        if not self.had_first_move:
            available_moves.append(Square.at(current_square.row + sq_two_in_front, current_square.col))
        
    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        self.had_first_move = True
        super().move_to(board, new_square)


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []