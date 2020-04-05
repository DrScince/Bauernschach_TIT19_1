# pylint: disable=C
import unittest
import sys
try:
    from chess_logik.pawn import Pawn
    from chess_logik.position import Position
    from chess_logik import consts
except ImportError as err:
    print("ImportError"+str(err))
    sys.exit()

class PawnTest(unittest.TestCase):

    def test_get_pos(self):
        pos = Position("A", 2)
        f = Pawn(consts.COLOR_BLACK, pos)
        self.assertEqual(f.get_position(), pos)

    def test_wrong_argument_types(self):
        pos = Position("A", 2)
        pawn = Pawn(consts.COLOR_WHITE, pos)
        with self.assertRaises(Exception):
            pawn.get_possible_moves("not a list")
        with self.assertRaises(Exception):
            pawn.get_possible_moves((0, 3, 5)) #liste vom falschen typ
        with self.assertRaises(Exception):
            pawn.do_move("not a Position")

    def test_moves(self):
        # make a custom field to quickly test all moves
        field = []
        field.append(Pawn(consts.COLOR_WHITE, Position("A", 2)))
        field.append(Pawn(consts.COLOR_WHITE, Position("B", 2)))
        field.append(Pawn(consts.COLOR_WHITE, Position("C", 2)))
        field.append(Pawn(consts.COLOR_BLACK, Position("A", 6)))
        field.append(Pawn(consts.COLOR_BLACK, Position("B", 6)))
        field.append(Pawn(consts.COLOR_BLACK, Position("C", 6)))
        #double move white
        pos_moves = field[0].get_possible_moves(field)
        self.assertIsInstance(pos_moves, list)
        self.assertEqual(field[0].do_move(Position("A", 4)), consts.ERROR_CODES["Success"])
        #single move white
        pos_moves = field[1].get_possible_moves(field)
        self.assertIsInstance(pos_moves, list)
        self.assertEqual(field[1].do_move(Position("B", 3)), consts.ERROR_CODES["Success"])
        #double move black
        pos_moves = field[4].get_possible_moves(field)
        self.assertIsInstance(pos_moves, list)
        self.assertEqual(field[4].do_move(Position("B", 4)), consts.ERROR_CODES["Success"])
        #single move black
        pos_moves = field[5].get_possible_moves(field)
        self.assertIsInstance(pos_moves, list)
        self.assertEqual(field[5].do_move(Position("C", 5)), consts.ERROR_CODES["Success"])
        #test en passant possible
        pos_moves = field[0].get_possible_moves(field)
        self.assertIsInstance(pos_moves, list)
        self.assertEqual(field[0].do_move(Position("B", 5)), consts.ERROR_CODES["Success"])
        #test hit possible
        pos_moves = field[0].get_possible_moves(field)
        self.assertIsInstance(pos_moves, list)
        self.assertEqual(field[0].do_move(Position("A", 6)), consts.ERROR_CODES["Success"])
        #single moves black to stay in front
        pos_moves = field[5].get_possible_moves(field)
        self.assertIsInstance(pos_moves, list)
        self.assertEqual(field[5].do_move(Position("C", 4)), consts.ERROR_CODES["Success"])
        pos_moves = field[5].get_possible_moves(field)
        self.assertIsInstance(pos_moves, list)
        self.assertEqual(field[5].do_move(Position("C", 3)), consts.ERROR_CODES["Success"])
        pos_moves = field[5].get_possible_moves(field)
        self.assertIsInstance(pos_moves, list)
        self.assertEqual(len(pos_moves), 0)
        #get error code no pos move
        self.assertEqual(field[5].do_move(Position("A", 2)), consts.ERROR_CODES["NoPosMove"])

