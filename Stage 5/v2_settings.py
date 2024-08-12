class Settings:
    def __init__(self):
        """" Stage 5"""
        """ Video player V2"""
        # Playlist increment
        self.video_id_increment = 1
        
        # Messages
        self.choose_a_list_msg = "Please choose a playlist"
        self.enter_valid_id_msg = "Please enter VALID video ID"
        self.enter_valid_rating_msg = "Please enter VALID rating number between 1 - 5"
        self.enter_other_id_msg = "Please enter another video ID"
        self.empty_entry_msg = "Entry fields must not be empty"
        self.last_playlist_msg = "Cannot remove the last playlist"
        self.new_playlist_created_msg = "New playlist created"
        self.no_videos_msg = "There are no videos"
        self.rename_playlist_successfully = "Playlist renamed successfully"
        
        # New video player (vp) window size
        self.vp_width = 1080
        self.vp_height = 380
        self.vp_geometry = f"{self.vp_width}x{self.vp_height}"
        
        # Frame (Use for all tabs)
        self.f1_width = 960
        self.f1_height = 320
        self.f1_borderwidth = 10
        
        # Set sizes of boxes
        self.list_box_width = 65
        self.list_box_height = 15
        
        self.video_details_txt_width = 30
        self.video_details_txt_height = 10

        self.playing_video_width = 35
        self.playing_video_height = 7

        self.playing_status_width = 35
        self.playing_status_height = 1

        self.media_btn_width = 7
        self.edit_playlist_btn = 13