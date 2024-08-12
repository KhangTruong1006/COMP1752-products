import csv
from v2_library_item import LibraryItemV2

class VideoLibrary:
    def __init__(self):
        self.video_lib ={}
        
        with open('_video_list.csv') as video_list:
            video_details = csv.reader(video_list)
            next(video_details)
            for info in video_details:
                self.video_lib[f'{info[0]}'] = LibraryItemV2(info[1], info[2], int(info[3]), int(info[4]))
    
    # Listing funtion
    def list_all(self):
        output = ""    
        for key in self.video_lib:
            item = self.video_lib[key]
            output += f"{key} - {item.details()}\n"
        return output
    
    def display_playlist_videos(self, playlist):
        output = ""
        for index, key in enumerate(playlist):
            item = self.video_lib[key]
            output += f'{index + 1 :02d} // {key} - {item.details()} //\n'
        return output

    # Video name
    def get_name(self, key):
        try:
            item = self.video_lib[key]
            return item.name 
        except KeyError:
            return None
        
    def set_name(self, key, name):
        try:
            item = self.video_lib[key]
            item.name = name
        except KeyError:
            return None
    
    # Video director
    def get_director(self, key):
        try:
            item = self.video_lib[key]
            return item.director
        except KeyError:
            return None
        
    def set_director(self, key, director):
        try:
            item = self.video_lib[key]
            item.director = director
        except KeyError:
            return None

    # Video rating  
    def get_rating(self, key):
        try:
            item = self.video_lib[key]
            return item.rating
        except KeyError:
            return -1
        
    def set_rating(self, key, rating):
        try:
            item = self.video_lib[key]
            item.rating = rating
        except KeyError:
            return

    # Video playcount   
    def get_playcount(self, key):
        try:
            item = self.video_lib[key]
            return item.playcount
        except KeyError:
            return -1
        
    def increment_playcount(self, key):
        try:
            item = self.video_lib[key]
            item.playcount += 1
        except KeyError:
            return
        
    def update_video_list(self):
        with open('_video_list.csv', 'w', newline= "") as update_file:
            detail_field = ['key', 'name', 'director', 'rating', 'playcount']
            update_details = csv.DictWriter(update_file, fieldnames= detail_field)
            update_details.writeheader()
            for key in self.video_lib:
                name = self.get_name(key)
                director = self.get_director(key)
                rating = self.get_rating(key)
                playcount = self.get_playcount(key)
                update_details.writerow({"key": key, "name": name, "director": director, "rating": rating, "playcount": playcount})
              
if __name__ == '__main__':
   runs= VideoLibrary()
   for key in list(runs.video_lib):
       print(runs.video_lib[key].details())