import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Summer Holiday", "Cliff Richard")
        self.guest1 = Guest("Steve", 50 , self.song1)
        self.guest2 = Guest("Lena", 40, self.song1)
        self.guest3 = Guest("Paul", 30, self.song1)
        self.room1 = Room("Room 1", 2, 10)

    def test_guest_has_name(self):
        self.assertEqual("Steve", self.guest1.name)

    def test_guest_has_fav_song(self):
        self.assertEqual(self.song1, self.guest1.fav_song)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest1.wallet)

    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room1.name)

    def test_check_in_guest_success(self):
        self.assertEqual(f"{self.guest1.name} has been checked into {self.room1.name}.",self.room1.check_in_guest(self.guest1))

    def test_check_in_guest_failure(self):
        self.room1.check_in_guest(self.guest1)
        result = self.room1.check_in_guest(self.guest2)
        expected = f"Sorry, {self.room1.name} is full. Please try {self.room1.suggest_alternative_room()} instead."
        self.assertEqual(expected, result)

    def test_check_in_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guests))

    def test_check_out_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_out_guest(self.guest1)
        self.assertEqual(0, len(self.room1.guests))

    def test_add_song(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, len(self.room1.songs))