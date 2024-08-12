import csv

class PlaylistItem:
    def __init__(self, playlist_id, playlist_name):
        self.playlist_id = playlist_id
        self.playlist_name = playlist_name

        self.id_order = []
        self.video_keys = []
        self.get_id_order_and_keys()

    def get_id_order_and_keys(self):
        with open(f'playlists/{self.playlist_id}.csv', 'r') as playlist:
            playlist_info = csv.reader(playlist)
            next(playlist_info)
            for id, key in playlist_info:
                self.id_order.append(int(id))
                self.video_keys.append(key)
                
    def update_playlist(self, delete_video = False):
        with open(f'playlists/{self.playlist_id}.csv', 'w', newline= "") as update_playlist:
            detail_fields = ['video_ID', 'key']
            update_details = csv.DictWriter(update_playlist, fieldnames= detail_fields)
            update_details.writeheader()
            if delete_video:
                self.id_order.pop()
            for id in self.id_order:
                key = self.video_keys[id - 1]
                update_details.writerow({'video_ID': id, 'key': key})
                        
    def add_video(self, input_key):
        self.video_keys.append(input_key)
        self.id_order.append(self.video_keys.index(f'{input_key}') + 1)
        self.update_playlist()
          
    def delete_video(self, video_key):
        remove_key_index = self.video_keys.index(video_key)
        self.video_keys.remove(video_key)
        self.id_order.remove(remove_key_index + 1)
        for i in range(len(self.id_order)):
            self.id_order[i] = i + 1
        self.update_playlist()

    def reset_playlist(self):
        self.id_order.clear()
        self.video_keys.clear()
        with open(f'playlists/{self.playlist_id}.csv', 'w', newline= "") as update_playlist:
            detail_fields = ['video_ID', 'key']
            update_details = csv.DictWriter(update_playlist, fieldnames= detail_fields)
            update_details.writeheader()

# Testing
if __name__ == '__main__':
    #test = PlaylistItem()
    #print(test.id_order)
    a = 0