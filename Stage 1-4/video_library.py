from library_item import LibraryItem

class VideoLibrary:
    def __init__(self):
        self.library = {}
        self.library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
        self.library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5)
        self.library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2)
        self.library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1)
        self.library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3)


    def list_all(self):
        output = ""
        for key in self.library:
            item = self.library[key]
            output += f"{key} - {item.info()}\n"
        return output

    def list_video(self, playlist):
        output = ""
        for index, key in enumerate(playlist):
            item = self.library[key]
            output+= f"{index + 1 :02d}  // {key} - {item.info()} //\n"
        return output

    def get_name(self, key):
        try:
            item = self.library[key]
            return item.name
        except KeyError:
            return None


    def get_director(self, key):
        try:
            item = self.library[key]
            return item.director
        except KeyError:
            return None


    def get_rating(self, key):
        try:
            item = self.library[key]
            return item.rating
        except KeyError:
            return -1


    def set_rating(self, key, rating):
        try:
            item = self.library[key]
            item.rating = rating
        except KeyError:
            return


    def get_play_count(self, key):
        try:
            item = self.library[key]
            return item.play_count
        except KeyError:
            return -1


    def increment_play_count(self, key):
        try:
            item = self.library[key]
            item.play_count += 1
        except KeyError:
            return
        
    def reset_play_count(self):
        try:
            for key in self.library:
                item = self.library[key]
                item.play_count = 0
        except KeyError:
            return