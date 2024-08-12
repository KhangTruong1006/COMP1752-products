import csv
import os

from v2_playlist_item import PlaylistItem

class PlaylistLibrary:
    def __init__(self):
        self.playlist_lib = {}
        self.playlist_ids = []
        self.playlist_names = []
        self.open_csv()
        

    def open_csv(self):
        with open('_playlists_list.csv', 'r') as playlists:
            playlist_items = csv.reader(playlists)
            next(playlists)
            for playlist_id, name in playlist_items:
                self.playlist_ids.append(int(playlist_id))
                self.playlist_names.append(name)
                self.playlist_lib[f'{playlist_id}'] = PlaylistItem(playlist_id, name)

    def list_all(self, return_ouput = False):
        name_list =[]
        output= "ID - Name\n"
        for id in sorted(self.playlist_lib, key= int):
            name = self.get_playlist_names(id)
            output += f'{int(id) :02d} - {name}\n' # For Displaying in text
            combobox_output = f'{int(id)} - {name}' # For Display in combobox
            name_list.append(combobox_output)
        if return_ouput:
            return output
        else:
            return tuple(name_list)

    # Get name and keys
    def get_playlist_names(self, playlist_id):
        playlist_name = self.playlist_lib[f'{playlist_id}'].playlist_name
        return playlist_name

    def get_playlist_keys(self, playlist_id):
        keys_list = self.playlist_lib[f'{playlist_id}'].video_keys
        return keys_list
    
    # Update name
    def set_playlist_name(self, playlist_id, name):
        try:
            self.playlist_lib[f'{playlist_id}'].playlist_name = name
            target_index = self.playlist_ids.index(playlist_id)
            self.playlist_names[target_index] = self.playlist_lib[f'{playlist_id}'].playlist_name
            self.update_playlists_list()
        except:
            return

    # Add and delete video
    def add_video_to_playlist(self, playlist_id, input_key):
        self.playlist_lib[f'{playlist_id}'].add_video(input_key)
        
    def delete_video_from_list(self,playlist_id, input_key):
        self.playlist_lib[f'{playlist_id}'].delete_video(input_key)
        
    # Reset, create playlists
    def reset_playlist(self, playlist_id):
        self.playlist_lib[f'{playlist_id}'].reset_playlist()

    def create_playlist(self, name):
        try:
            max_index = len(self.playlist_ids) - 1
            if self.playlist_ids[max_index] == len(self.playlist_ids):
                new_id = self.playlist_ids[max_index] + 1
                if name == "" :
                    name = f'Playlist {new_id}'
                self.create_new_playlist(new_id, name)

            elif self.playlist_ids[max_index] != len(self.playlist_ids):
                for playlist_index in range(self.playlist_ids[max_index]):
                    if playlist_index + 1 == self.playlist_ids[playlist_index]:
                        continue
                    else:
                        new_id = playlist_index + 1
                        self.playlist_ids.insert(playlist_index , new_id)
                        if name == "":
                            name = f'Playlist {new_id}'
                        self.playlist_names.insert(playlist_index, name)
                        self.create_new_playlist(new_id, name, True)
                        break
                            
        except:
            return
        
    def create_new_playlist(self, playlist_id, name, add_missing_id = False):
        with open(f'playlists/{playlist_id}.csv', 'w', newline= "") as new_playlist:
            test_csv = csv.writer(new_playlist)
            headers = ["video_ID","key"]
            test_csv.writerow(headers)
        
        if not add_missing_id:
            self.playlist_ids.append(int(playlist_id))
            self.playlist_names.append(name)
        self.playlist_lib[f'{playlist_id}'] = PlaylistItem(playlist_id, name)
        self.update_playlists_list()
        

    def delete_playlist(self, playlist_id): 
        del self.playlist_lib[f'{playlist_id}']
        os.remove(f'playlists/{playlist_id}.csv')
        for id in range(len(self.playlist_ids)):
            if self.playlist_ids[id] != int(playlist_id):
                continue
            else:
                target_index = self.playlist_ids.index(playlist_id)
                self.playlist_ids.pop(target_index)
                self.playlist_names.pop(target_index)
                break
            
        self.update_playlists_list() 
    
    def update_playlists_list(self):
        with open('_playlists_list.csv', 'w', newline="") as update_list:
            detail_fields = ['playlist_id','name']
            update_details = csv.DictWriter(update_list, fieldnames= detail_fields)
            update_details.writeheader()
            for id, name in zip(self.playlist_ids, self.playlist_names):
                update_details.writerow({'playlist_id': int(id), 'name': name})
        
    
# Testing
if __name__ == '__main__':
    test = PlaylistLibrary()