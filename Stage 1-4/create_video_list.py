import tkinter as tk 
import tkinter.scrolledtext as tkst 

from settings import Settings
from video_library import VideoLibrary
import font_manager as fonts 

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)
    
class CreateVideoList():
    def __init__(self, window):
        self.video_lib = VideoLibrary()
        self.settings = Settings()

        window.geometry(self.settings.cvl_geometry)
        window.title("Create Video List")
        
        self.playlist = []
        self.playlist_id = self.settings.playlist_id
        
        # Row 0
        list_videos_btn = tk.Button(window, text = "List all video", width = 15, command= self.list_all_clicked)
        list_videos_btn.grid(row=0, column=0, padx=20, pady= 20)
        
        enter_lbl = tk.Label(window, text = "Enter Video Number")
        enter_lbl.grid(row= 0, column= 1, padx= 10, pady= 20)
        
        self.input_txt = tk.Entry(window, width= 5)
        self.input_txt.grid(row= 0, column= 2, padx= 5, pady= 20)

        check_video_btn = tk.Button(window, text="Check Video", width= 11, command= self.check_video_clicked)
        check_video_btn.grid(row=0, column= 3, padx= 10, pady=20)
        
        add_video_btn = tk.Button(window, text= "Add to playlist", width= 13, command= self.add_to_playlist)
        add_video_btn.grid(row= 0, column= 4, sticky="NW", padx= 5, pady= 20)
        
        reset_btn = tk.Button(window, text = "Reset playlist", width= 11, command= self.reset_playlist)
        reset_btn.grid(row= 0, column = 5, sticky= "NW", padx= 30, pady= 20)
        
        # Row 1
        self.list_txt = tkst.ScrolledText(window, width= self.settings.cvl_box_width, height= self.settings.box_height, wrap= "none")
        self.list_txt.grid(row= 1, column= 0, columnspan= 3, sticky= "NW", padx= 35, pady= 10)
        
        self.video_txt = tk.Text(window, width= 53, height=10, wrap="none")
        self.video_txt.grid(row=1, column=3, columnspan= 3,sticky= "NW", padx= 35, pady=10)

        # Row 2
        previous_btn = tk.Button(window, text = "< Previous", width= 10, command= self.previous_video)
        previous_btn.grid(row=2, column= 3, padx= 35, pady= 10, sticky="NE")
        
        play_btn = tk.Button(window, text= "Play", width= 13, command= self.play_the_playlist)
        play_btn.grid(row= 2, column= 4,padx= 10)
        
        next_btn = tk.Button(window, text = "Next >", width= 10, command= self.next_video)
        next_btn.grid(row= 2, column= 5, padx= 10)
        
        playlist_lbl = tk.Label(window, text= "Playlist")
        playlist_lbl.grid(row= 2, column= 0,rowspan= 2,padx= 35, pady= 5, sticky="NW")
        # Row 3
        self.playlist_txt = tkst.ScrolledText(window, width= self.settings.cvl_box_width, height= self.settings.box_height, wrap= "none")
        self.playlist_txt.grid(row= 3, column= 0, columnspan= 3, sticky="NW", padx= 35, pady= 10)
        
        # Row 4
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row= 4, column=0, columnspan=4, sticky="W", padx= 35, pady=10)
        
        #self.list_all_clicked() #use for testing
        
    def check_video_clicked(self):
        key, name = self.get_key_and_name()
        if name is not None:
            self.print_video_info(key, name, self.video_txt)
            self.video_lib.get_play_count(key)
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")
        
    def list_all_clicked(self):
        video_list = self.video_lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")
        
    def print_video_info(self, key, name, text_area):
        director, rating, play_count = self.get_video_info(key)
        video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
        set_text(text_area, video_details)
    
    def get_video_info(self, key):
        director = self.video_lib.get_director(key)
        rating = self.video_lib.get_rating(key)
        play_count = self.video_lib.get_play_count(key)
        return (director, rating, play_count)
    
    def get_key_and_name(self):
        key = self.input_txt.get()
        name = self.video_lib.get_name(key)
        return (key, name)
    
    def add_to_playlist(self):
        key, name = self.get_key_and_name()
        if name is not None:
            if key not in self.playlist:
                self.playlist.append(key)           
                set_text(self.video_txt, f"Video {key} added")
            else:
                set_text(self.video_txt, f"Video {key} was added\nPlease add another video")
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.show_playlist()
        
        self.status_lbl.configure(text="Add video button was clicked!")

    def show_playlist(self):
        playlist_video = self.video_lib.list_video(self.playlist)
        set_text(self.playlist_txt, playlist_video)
        
    # Reset playlist
    def reset_playlist(self):
        self.playlist.clear()
        self.video_lib.reset_play_count()
        set_text(self.video_txt, f"Playlist cleared")
        self.show_playlist()
        self.status_lbl.configure(text= "Reset button was clicked!")
 
    # Buttons
    def play_the_playlist(self):
        if len(self.playlist) != 0:
            key = self.playlist[self.playlist_id]
            self.video_lib.increment_play_count(key)
            name = self.video_lib.get_name(key)
            self.print_video_info(key, name, self.video_txt)

        else:
            set_text(self.video_txt, self.settings.no_videos_msg)
            
        self.status_lbl.configure(text="Play button was clicked!")

    # Functions for "Previous" and "Next" buttons
    def adjust_playlist_id(self, increment):
        if len(self.playlist) == 0:
            set_text(self.video_txt, self.settings.no_videos_msg)
        else:
            self.playlist_id += increment
            self.check_playlist_limit()
                
    def check_playlist_limit(self):
        if self.playlist_id < 0:
            self.playlist_id = 0
        elif self.playlist_id > len(self.playlist) - 1:
            self.playlist_id = len(self.playlist) - 1
           
    def change_video(self, increment):
        try:
            self.adjust_playlist_id(increment)
            key = self.playlist[self.playlist_id]
            name = self.video_lib.get_name(key)
            self.print_video_info(key, name, self.video_txt)
        except:
            set_text(self.video_txt, self.settings.no_videos_msg)
   
    # "Previous" and "Next" buttons
    def previous_video(self):
        self.change_video(-self.settings.playlist_id_increment)
        self.status_lbl.configure(text="Previous button was clicked!")
        
    def next_video(self):
        self.change_video(+self.settings.playlist_id_increment)
        self.status_lbl.configure(text="Next button was clicked!")

if __name__ == '__main__':
    window = tk.Tk()
    fonts.configure()
    CreateVideoList(window)
    window.mainloop()