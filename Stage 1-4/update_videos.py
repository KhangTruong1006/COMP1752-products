import tkinter as tk
import tkinter.scrolledtext as tkst
import font_manager as fonts

from settings import Settings
from video_library import VideoLibrary

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateVideos:
    def __init__(self, window):
        self.settings = Settings()
        self.video_lib = VideoLibrary()
        
        window.geometry(self.settings.uv_geometry)
        window.title("Update Videos")
        
        # Row 0 
        list_videos_btn = tk.Button(window, text = "List all video", width = 15, command= self.list_all_clicked)
        list_videos_btn.grid(row=0, column=0, padx=20, pady= 20)
        
        enter_lbl = tk.Label(window, text = "Enter Video Number")
        enter_lbl.grid(row= 0, column= 1, padx= 10, pady= 20)
        
        self.input_txt = tk.Entry(window, width= 5)
        self.input_txt.grid(row= 0, column= 2, padx= 5, pady= 20)
        
        check_video_btn = tk.Button(window, text="Check Video", width= 11, command= self.check_video_clicked)
        check_video_btn.grid(row=0, column= 3, padx= 10, pady=20)
        
        # Row 1
        self.list_txt = tkst.ScrolledText(window, width= self.settings.uv_box_width, height= self.settings.box_height, wrap= "none")
        self.list_txt.grid(row= 1, column= 0, columnspan= 3, sticky= "NW", padx= 35, pady= 10)
        
        self.video_txt = tk.Text(window, width= 30, height=10, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky= "NW", padx= 35, pady=10)
        
        # Row 2
        update_video_number = tk.Label(window, text= "Enter Video Number")
        update_video_number.grid(row= 2, column= 0, padx= 30, pady= 20, sticky= "W")
        
        self.udpate_input = tk.Entry(window, width= self.settings.entry_width)
        self.udpate_input.grid(row= 2, column= 1, padx= 10, pady=20, sticky= "W")
        
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row= 2, column=3, sticky="W", padx= 30, pady=10)
        
        # Row 3
        new_rating_label = tk.Label(window, text= "Enter New Rating")
        new_rating_label.grid(row= 3, column= 0, padx= 30, pady= 10, sticky= "W")
        
        self.new_rating_input = tk.Entry(window, width= self.settings.entry_width)
        self.new_rating_input.grid(row= 3, column= 1, padx= 10, pady=10, sticky= "W")
        
        # Row 4
        update_button = tk.Button(window, text= "Update", command= self.update_rating)
        update_button.grid(row= 4, column= 1,padx= 10, pady= 20, sticky= "W")

        #self.list_all_clicked() # Testing
    
    def check_video_clicked(self):
        key, name = self.get_key_and_name(self.input_txt)
        if name is not None:
            director, rating, play_count = self.get_video_details(key)
            output = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, output)     
        else:
            set_text(self.video_txt, f"Video {key} not found")
            
        self.status_lbl.configure(text="Check video button was clicked!")
    
    def list_all_clicked(self):
        video_list = self.video_lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text= "List all button was clicked!")  
          
    def get_key_and_name(self, entry_box):
        key = entry_box.get()
        name = self.video_lib.get_name(key)
        return (key, name)
    
    def get_video_details(self, key):
        director = self.video_lib.get_director(key)
        rating = self.video_lib.get_rating(key) 
        play_count = self.video_lib.get_play_count(key)
        return (director, rating, play_count)
        
    # Update function
    def update_rating(self):
        key, name = self.get_key_and_name(self.udpate_input)
        new_rating_str = self.new_rating_input.get()
        try:
            new_rating = int(new_rating_str)
            if name is not None:
                if not (new_rating < 1 or new_rating > 5):
                    self.video_lib.set_rating(key, new_rating)
                    video_list = self.video_lib.list_all()
                    director, rating, play_count = self.get_video_details(key)
                    set_text(self.list_txt, video_list)
                    output = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
                    set_text(self.video_txt, output)
                
                elif new_rating < 1 or new_rating > 5:
                    set_text(self.video_txt, self.settings.enter_1_5_msg)
                else:
                    set_text(self.video_txt, f"The number is invalid")
                
            elif name is not None:
                set_text(self.video_txt, f"Video {key} not found")
            else:
                set_text(self.video_txt, self.settings.enter_video_number_msg)
                
            self.status_lbl.configure(text= "Update button was clicked")
        
        except:
            if (name and new_rating_str) is None:
                set_text(self.video_txt, f"Please enter the video number\nPlease enter the rating number")
                
            elif new_rating_str is None:
                set_text(self.video_txt, f"Please enter the new rating number")
                
            else:
                set_text(self.video_txt, self.settings.enter_1_5_msg)
     
if __name__ == '__main__':
    window = tk.Tk()
    fonts.configure()
    UpdateVideos(window)
    window.mainloop()