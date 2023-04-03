class Room:
    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.songs = []

    def check_in_guest(self, guest):
        if len(self.guests) >= self.capacity:
            return f"Sorry, {self.name} is full. Please try {self.suggest_alternative_room()} instead."
        else:
            self.guests.append(guest)
            return f"{guest.name} has been checked into {self.name}."

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)

    def suggest_alternative_room(self):
        return f"Room {int(self.name.split()[-1]) + 1}"
