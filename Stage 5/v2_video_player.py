import tkinter as tk 
import tkinter.scrolledtext as tkst
from tkinter import ttk

from v2_settings import Settings
from v2_video_library import VideoLibrary
from v2_playlist_library import PlaylistLibrary

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class VideoPlayerV2:
    def __init__(self, window):
        self.settings = Settings()
        self.video_library = VideoLibrary()
        self.playlist_library = PlaylistLibrary()
                
        window.geometry(self.settings.vp_geometry)
        window.title("Video Player V2")
        #window.configure(bg='black')

        # StringVar
        self.name_strVar = tk.StringVar(value= "")
        self.director_strVar = tk.StringVar(value= "")
        self.rating_strVar = tk.StringVar(value= "")
        self.t3_playlist_strVar = tk.StringVar(value= "")
        self.t4_playlist_strVar = tk.StringVar(value= "")

        self.video_id_position = 0

        """Tabs"""
        tabs = ttk.Notebook(window)
        
        # Tab 1 - check_video
        check_video_tab = ttk.Frame(tabs, width = self.settings.f1_width, 
                                height= self.settings.f1_height, borderwidth= self.settings.f1_borderwidth, relief= tk.GROOVE)
        
        self.t1_video_list = tkst.ScrolledText(check_video_tab, width= self.settings.list_box_width, height= self.settings.list_box_height, wrap= "none")
        self.t1_video_list.grid(row= 0, column= 0,rowspan= 3, padx = 10, pady= 10)
        
        self.video_details_txt = tk.Text(check_video_tab, width= self.settings.video_details_txt_width, height= self.settings.video_details_txt_height, wrap= "none")
        self.video_details_txt.grid(row= 0, column= 1,rowspan= 2, columnspan= 3, padx= 10, pady= 10)
        
        entry_label = tk.Label(check_video_tab, text="Enter video number")
        entry_label.grid(row=2, column= 1)
        
        self.t1_entry_input = tk.Entry(check_video_tab, width= 5)
        self.t1_entry_input.grid(row= 2, column= 2)
        
        check_button = tk.Button(check_video_tab, text= "Check Video", command= self.check_button_click)
        check_button.grid(row= 2, column = 3)
        
        list_all_btn = tk.Button(check_video_tab, text='List all video', command= self.list_all_clicked)
        list_all_btn.grid(row=3, column=0)
        
        # Tab 2 - update_video
        update_video_tab = ttk.Frame(tabs, width = self.settings.f1_width, 
                                height= self.settings.f1_height, borderwidth= self.settings.f1_borderwidth, relief= tk.GROOVE)
        
        self.t2_video_list = tkst.ScrolledText(update_video_tab,  width= self.settings.list_box_width, height= self.settings.list_box_height, wrap= "none")
        self.t2_video_list.grid(row= 0, column= 0, rowspan= 5, padx = 10, pady= 10)
        
        entry_label = tk.Label(update_video_tab, text= "Enter video ID")
        entry_label.grid(row= 0, column= 1, pady= 10)
        
        self.t2_entry_input = tk.Entry(update_video_tab, width= 5)
        self.t2_entry_input.grid(row= 0, column= 2, padx= 15)
        
        edit_button = tk.Button(update_video_tab, text= "Edit Video", command= self.edit_button_clicked)
        edit_button.grid(row= 0, column= 3)
        
        name_label = tk.Label(update_video_tab, text= "Name / Title")
        name_label.grid(row = 1, column = 1)
        
        self.name_entry = tk.Entry(update_video_tab, width= 20, textvariable= self.name_strVar, state="readonly")
        self.name_entry.grid(row= 1, column= 2, columnspan= 2)
        
        director_label = tk.Label(update_video_tab, text= "Director")
        director_label.grid(row = 2, column = 1)
        
        self.director_entry = tk.Entry(update_video_tab, width= 20, textvariable= self.director_strVar, state="readonly")
        self.director_entry.grid(row= 2, column= 2, columnspan= 2)
        
        rating_label = tk.Label(update_video_tab, text= "Rating")
        rating_label.grid(row = 3, column = 1)
        
        self.rating_entry = tk.Entry(update_video_tab, width= 20, textvariable= self.rating_strVar, state="readonly")
        self.rating_entry.grid(row= 3, column= 2, columnspan= 2)

        update_button = tk.Button(update_video_tab, text="Update", width= 8, command= self.update_button_clicked)
        update_button.grid(row= 4, column= 2)
        
        list_all_btn = tk.Button(update_video_tab, text='List all video', command= self.list_all_clicked)
        list_all_btn.grid(row= 5, column=0)
        
        # Tab 3 - video_playlist
        video_playlist_tab = ttk.Frame(tabs, width = self.settings.f1_width, 
                                height= self.settings.f1_height, borderwidth= self.settings.f1_borderwidth, relief= tk.GROOVE)
        
        self.t3_playlist = tkst.ScrolledText(video_playlist_tab, width= self.settings.list_box_width, 
                                            height= self.settings.list_box_height, wrap= "none")
        self.t3_playlist.grid(row= 0, column= 0, rowspan= 6, padx = 10, pady= 10)

        self.t3_video_details = tkst.ScrolledText(video_playlist_tab, width= self.settings.playing_video_width,
                                               height = self.settings.playing_video_height, wrap= 'none')
        self.t3_video_details.grid(row= 0, column= 1, rowspan= 2, columnspan= 4, sticky= 'N', padx= 10, pady= 10)

        self.t3_display_video = tk.Text(video_playlist_tab, width= self.settings.playing_status_width,
                                      height= self.settings.playing_status_height, wrap= "none", state= 'disabled')
        self.t3_display_video.grid(row= 2, column= 1, columnspan= 4, sticky= 'N')

        choose_playlist_lable = tk.Label(video_playlist_tab, text= "Choose playlist", width= 20)
        choose_playlist_lable.grid(row= 3, column= 2, columnspan= 2)

        self.t3_playlist_selection = ttk.Combobox(video_playlist_tab, textvariable= self.t3_playlist_strVar)
        self.t3_playlist_selection['values'] = self.playlist_library.list_all()
        self.t3_playlist_selection.grid(row= 4, column= 2, columnspan= 2, pady= 10)
        self.t3_playlist_selection.bind('<<ComboboxSelected>>', lambda event: self.playlist_clicked(self.t3_playlist, self.t3_playlist_strVar))
        
        
        previous_btn = tk.Button(video_playlist_tab, text = "⏮", width= self.settings.media_btn_width, command= self.previous_button_clicked)
        previous_btn.grid(row= 5, column= 1)

        play_btn = tk.Button(video_playlist_tab, text="⏵", width= self.settings.media_btn_width, command= self.play_button_clicked)
        play_btn.grid(row= 5, column= 2, padx= 5)

        pause_btn = tk.Button(video_playlist_tab, text="⏸", width= self.settings.media_btn_width, command= self.pause_button_clicked)
        pause_btn.grid(row= 5, column= 3)

        next_btn = tk.Button(video_playlist_tab, text="⏭", width= self.settings.media_btn_width, command= self.next_button_clicked)
        next_btn.grid(row= 5, column= 4, padx= 5)
        
        # Tab 4 - edit_playist
        edit_playlist_tab = ttk.Frame(tabs, width = self.settings.f1_width, 
                                height= self.settings.f1_height, borderwidth= self.settings.f1_borderwidth, relief= tk.GROOVE)
        
        self.t4_playlist = tkst.ScrolledText(edit_playlist_tab,  width= self.settings.list_box_width, height= self.settings.list_box_height, wrap= "none")
        self.t4_playlist.grid(row= 0, column= 0, rowspan= 5, columnspan= 4, padx = 10, pady= 10)

        self.t4_notification = tkst.ScrolledText(edit_playlist_tab, width= self.settings.playing_video_width,
                                               height = self.settings.playing_video_height, wrap= 'none')
        self.t4_notification.grid(row= 0, column= 6, columnspan= 3, sticky= 'N', padx= 10, pady= 10)

        self.t4_display_video = tk.Text(edit_playlist_tab, width= self.settings.playing_status_width,
                                      height= self.settings.playing_status_height, wrap= "none", state='disabled')
        self.t4_display_video.grid(row= 1, column= 6, columnspan= 3, padx= 10, sticky= 'N')
        
        self.t4_playlist_selection = ttk.Combobox(edit_playlist_tab,textvariable= self.t4_playlist_strVar, width= 15)
        self.t4_playlist_selection['values'] = self.playlist_library.list_all()
        self.t4_playlist_selection.grid(row=2 , column= 7, pady= 5)
        self.t4_playlist_selection.bind('<<ComboboxSelected>>', lambda event: self.playlist_clicked(self.t4_playlist, self.t4_playlist_strVar, True))
        
        reset_playlist_button = tk.Button(edit_playlist_tab, text="Reset playlist", width= self.settings.edit_playlist_btn, command=self.reset_button_clicked)
        reset_playlist_button.grid(row= 2, column= 8)
        
        remove_list_button = tk.Button(edit_playlist_tab, text= "Remove playlist", width= self.settings.edit_playlist_btn, command= self.delete_playlist_clicked)
        remove_list_button.grid(row= 2, column= 9)
            
        ## Add and delete video
        video_entry_label = tk.Label(edit_playlist_tab, text="Enter Video ID")
        video_entry_label.grid(row= 3, column= 6, sticky= 'W')
        
        self.t4_entry_input = tk.Entry(edit_playlist_tab, width= 10, state='readonly')
        self.t4_entry_input.grid(row= 3, column= 7)

        add_video_button = tk.Button(edit_playlist_tab, text= "Add video", width= self.settings.edit_playlist_btn, command= self.add_button_clicked)
        add_video_button.grid(row= 3, column= 8, padx= 10)

        delete_video_button = tk.Button(edit_playlist_tab, text="Delete video", width= self.settings.edit_playlist_btn, command= self.delete_button_clicked)
        delete_video_button.grid(row= 3, column= 9)

        ## Create and rename playlist
        playlist_name_label = tk.Label(edit_playlist_tab, text= "Enter name")
        playlist_name_label.grid(row= 4, column= 6, pady= 10, sticky= "W")

        self.playlist_name_entry = tk.Entry(edit_playlist_tab, width= 10)
        self.playlist_name_entry.grid(row=4, column= 7, pady= 10)

        create_playlist_button = tk.Button(edit_playlist_tab, text="Create playlist", width= self.settings.edit_playlist_btn, command= self.create_playlist_clicked)
        create_playlist_button.grid(row= 4, column= 8, pady= 10)

        rename_playlist_button = tk.Button(edit_playlist_tab, text= "Rename playlist", width= self.settings.edit_playlist_btn, command= self.rename_playlist_clicked)
        rename_playlist_button.grid(row= 4, column= 9, pady= 10)

        ## Buttons
        t4_list_all_btn = tk.Button(edit_playlist_tab, text= 'List all video', command= self.list_all_clicked)
        t4_list_all_btn.grid(row= 5, column= 1)

        list_all_playlist_btn = tk.Button(edit_playlist_tab, text= 'List all playlist', command= self.list_all_playlist)
        list_all_playlist_btn.grid(row= 5, column= 2)

        # Displaying tab
        tabs.add(check_video_tab, text= "Check Video")
        tabs.add(update_video_tab, text= "Update Video")
        tabs.add(video_playlist_tab, text= "Playlist")
        tabs.add(edit_playlist_tab, text= "Edit Playlist")
        tabs.pack()
        
        # Status label
        status_label = tk.Label(window, text="© Khang Truong")
        status_label.pack(side='left')

    """Functions"""
    # Unviersal functions
    def list_all_clicked(self):
        video_list = self.video_library.list_all()
        self.list_in_all_tabs(video_list)

    def get_key_and_name(self, input_method):
        key = input_method
        name = self.video_library.get_name(key)
        return (key, name)
        
    def get_details(self, key):
        director = self.video_library.get_director(key)
        rating = self.video_library.get_rating(key)
        playcount = self.video_library.get_playcount(key)
        return (director, rating, playcount)
    
    def list_in_all_tabs(self, content):
        set_text(self.t1_video_list, content)
        set_text(self.t2_video_list, content)
        set_text(self.t4_playlist, content)
        
    def playlist_clicked(self, text_area, strVar, add_video_permit = False):
        if add_video_permit:
            self.t4_entry_input.configure(state='normal')
        self.video_id_position = 0
        keys = self.get_keys_from_playlist(strVar)
        content = self.video_library.display_playlist_videos(keys)
        set_text(text_area, content)
    
    def get_keys_from_playlist(self,strVar, get_playlist_id = False):
        playlist_id = strVar.get().split()[0]
        if playlist_id in list(self.playlist_library.playlist_lib):
            keys = self.playlist_library.get_playlist_keys(playlist_id)
            if get_playlist_id:
                return(playlist_id, keys)
            else:
                return keys         
    
    # Tab 1 functions
    def check_button_click(self):
        key, name = self.get_key_and_name(self.t1_entry_input.get())
        if name is not None:
            director, rating, playcount = self.get_details(key)
            output = f"{name}\n{director}\nRating: {rating}\nPlay count: {playcount}"
            set_text(self.video_details_txt, output)
        
        else:
            set_text(self.video_details_txt, self.settings.enter_valid_id_msg)
        

    # Tab 2 functions
    def edit_button_clicked(self):
        key, name = self.get_key_and_name(self.t2_entry_input.get())
        if name is not None:
            director, rating, playcount = self.get_details(key)
            self.set_edit_permit(True, name, director, rating)
        else:
            self.set_edit_permit(False)
            set_text(self.t2_video_list, self.settings.enter_valid_id_msg)

    def configure_entry(self, type_entry, input_strVar, type_detail = "", state = "readonly"):
        type_entry.configure(textvariable = input_strVar.set(f'{type_detail}'))
        type_entry.configure(state= state)

    def set_edit_permit(self, allow_edit = False, name= None, director = None, rating = None):
        if allow_edit:
            self.configure_entry(self.name_entry, self.name_strVar, name, "normal")
            self.configure_entry(self.director_entry, self.director_strVar, director, "normal")
            self.configure_entry(self.rating_entry, self.rating_strVar, rating, "normal")

        else:
            self.configure_entry(self.name_entry, self.name_strVar)
            self.configure_entry(self.director_entry, self.director_strVar)
            self.configure_entry(self.rating_entry, self.rating_strVar)
        
    def update_button_clicked(self):
        try:
            key, name = self.get_key_and_name(self.t2_entry_input.get())
            new_name = self.name_entry.get()
            new_director = self.director_entry.get()
            new_rating_str = self.rating_entry.get()
            new_rating = int(new_rating_str)
 
            if new_name:
                self.video_library.set_name(key, new_name)
            
            if new_director:
                self.video_library.set_director(key, new_director)
            self.video_library.update_video_list()

            if name is not None:
                if not (new_rating < 1 or new_rating > 5): 
                    self.video_library.set_rating(key, new_rating)
                    self.video_library.update_video_list()
                    self.list_in_all_tabs(f"Video {key} was updated")
                    self.set_edit_permit(False)
                    set_text(self.video_details_txt, "")
                else:
                    set_text(self.t2_video_list, self.settings.enter_valid_rating_msg)
            else:
                set_text(self.t2_video_list, self.settings.enter_valid_id_msg)
        except:
                set_text(self.t2_video_list, self.settings.enter_valid_rating_msg)
    
    # Tab 3 functions
    def play_button_clicked(self):
        try:
            keys = self.get_keys_from_playlist(self.t3_playlist_strVar)
            if len(keys) != 0:
                key, name = self.get_key_and_name(keys[self.video_id_position])
                self.video_library.increment_playcount(key)
                self.video_library.update_video_list()
                director, rating, playcount = self.get_details(key)
                output = f"{name}\n{director}\nRating: {rating}\nPlay count: {playcount}"
                self.display_playing_video(name)
                set_text(self.t3_video_details, output)

            else:
                set_text(self.t3_video_details, self.settings.no_videos_msg)
        except:
            set_text(self.t3_video_details, self.settings.choose_a_list_msg)

    def display_playing_video(self, name):
        self.t3_display_video.configure(state='normal')
        content = f'Now playing "{name}"'
        set_text(self.t3_display_video, content)
        self.t3_display_video.configure(state= 'disabled')

    def pause_button_clicked(self):
        try:
            playlist_id = self.t3_playlist_strVar.get()[0]
            if playlist_id in list(self.playlist_library.playlist_lib):
                    self.t3_display_video.configure(state='normal')
                    set_text(self.t3_display_video, "Paused")
                    self.t3_display_video.configure(state= 'disabled')
        except:
            set_text(self.t3_video_details, "There are no video playing")

    def adjust_video_id_position(self, keys, increment):
        if len(keys) == 0:
            set_text(self.t3_video_details, self.settings.no_videos_msg)
        else:
            self.video_id_position += increment
            self.check_playlist_limit(keys)

    def check_playlist_limit(self, keys):
        if self.video_id_position < 0:
            self.video_id_position = 0
        elif self.video_id_position > len(keys) - 1:
            self.video_id_position = len(keys) - 1

    def change_video_details(self, increment):
        try:
            keys = self.get_keys_from_playlist(self.t3_playlist_strVar)
            self.adjust_video_id_position(keys, increment)
            key, name = self.get_key_and_name(keys[self.video_id_position])
            director, rating, playcount = self.get_details(key)
            output = f"{name}\n{director}\nRating: {rating}\nPlay count: {playcount}"
            set_text(self.t3_video_details, output)
        
        except:
            set_text(self.t3_video_details, self.settings.no_videos_msg)

    def previous_button_clicked(self):
        self.change_video_details(-self.settings.video_id_increment)

    def next_button_clicked(self):
        self.change_video_details(+self.settings.video_id_increment)

    # Tab 4 functions
    def list_all_playlist(self):
        output = self.playlist_library.list_all(True)
        set_text(self.t4_playlist, output)

    ## Create and delete video buttons
    def add_button_clicked(self):
        try:
            input_key, name = self.get_key_and_name(self.t4_entry_input.get())
            playlist_id, keys = self.get_keys_from_playlist(self.t4_playlist_strVar, True)
            if name is not None:
                if input_key not in keys:
                    self.playlist_library.add_video_to_playlist(playlist_id, input_key)
                    set_text(self.t4_notification, f"Video {input_key} added")
                else:
                    set_text(self.t4_notification, self.settings.enter_other_id_msg)
            else:
                set_text(self.t4_notification, self.settings.enter_valid_id_msg)     
        except:
            set_text(self.t4_notification, self.settings.choose_a_list_msg)
            
    def delete_button_clicked(self):
        try:
            input_key, name = self.get_key_and_name(self.t4_entry_input.get())
            playlist_id, keys = self.get_keys_from_playlist(self.t4_playlist_strVar, True)
            if name is not None:
                if input_key in keys:
                    self.playlist_library.delete_video_from_list(playlist_id, input_key)
                    set_text(self.t4_notification, f"Video {input_key} deleted")
                    self.playlist_clicked(self.t4_playlist, self.t4_playlist_strVar)
                else:
                    set_text(self.t4_notification, f"Video {input_key} was deleted")
            else:
                set_text(self.t4_notification, self.settings.enter_valid_id_msg) 
        except:
            set_text(self.t4_notification, self.settings.choose_a_list_msg)
    
    ## Playlist selection
    def reset_button_clicked(self):
        try:
            playlist_id, keys = self.get_keys_from_playlist(self.t4_playlist_strVar, True)
            self.playlist_library.reset_playlist(playlist_id)
            self.list_all_playlist()
            set_text(self.t4_notification, f"Playlist {playlist_id} is cleared")
            set_text(self.t4_playlist, "")
            
        except:
            set_text(self.t4_notification, self.settings.choose_a_list_msg)

    ## Create and rename playlist buttons
    def rename_playlist_clicked(self):
        if self.t4_playlist_strVar.get() != "":
            name = self.playlist_name_entry.get()
            if len(name) != 0:
                playlist_id, keys = self.get_keys_from_playlist(self.t4_playlist_strVar,True)
                self.playlist_library.set_playlist_name(int(playlist_id), name)
                self.update_combobox()
                self.list_all_playlist()
                set_text(self.t4_notification, self.settings.rename_playlist_successfully)
            else:
                set_text(self.t4_notification, self.settings.empty_entry_msg)
        else:
            set_text(self.t4_notification, self.settings.choose_a_list_msg)

    def create_playlist_clicked(self):
        name_input = self.playlist_name_entry.get()
        self.playlist_library.create_playlist(name_input)
        self.update_combobox()
        self.list_all_playlist()
        set_text(self.t4_notification, self.settings.new_playlist_created_msg)
    
    def delete_playlist_clicked(self):
        try:
            if len(self.playlist_library.playlist_lib) <= 1:
                set_text(self.t4_notification, self.settings.last_playlist_msg)
                self.update_combobox()
        
            else:
                playlist_id , keys = self.get_keys_from_playlist(self.t4_playlist_strVar, True)
                self.playlist_library.delete_playlist(int(playlist_id))
                
                set_text(self.t4_notification, f'Playlist {playlist_id} removed')
            self.update_combobox()
            self.list_all_playlist()
        except:
            set_text(self.t4_notification, self.settings.choose_a_list_msg)
            self.update_combobox()

    def update_combobox(self):
        self.t4_playlist_strVar.set(value="")
        self.t4_playlist_selection['values'] = self.playlist_library.list_all()
        self.t3_playlist_strVar.set(value="")
        self.t3_playlist_selection['values'] = self.playlist_library.list_all()
        
if __name__ == '__main__':
    window = tk.Tk()
    VideoPlayerV2(window)
    window.mainloop()