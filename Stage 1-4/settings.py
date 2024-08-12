class Settings:
    def __init__(self): 
        """ Stage 1-4 """
        """ Window size settings"""
        # Update_videos.py (uv)
        self.uv_width = 935
        self.uv_height = 500
        self.uv_geometry = f"{self.uv_width}x{self.uv_height}"
        
        # Create_video_list.py (cvl)
        self.cvl_width = 1100
        self.cvl_height = 610
        self.cvl_geometry = f"{self.cvl_width}x{self.cvl_height}"
          
        # Playing video box (pvb) settings
        self.pvb_column = 3
        self.pvb_columnspan = 3

        # Box sizes 
        self.uv_box_width = 55
        self.cvl_box_width = 50
        self.box_height = 10
        
        # Entry size
        self.entry_width = 8
        
        # Playlist default/start id
        self.playlist_id = 0
        
        # Playlist id increment
        self.playlist_id_increment = 1
        
        # messages
        self.no_videos_msg = f"There are no videos\nPlease add a video to the playlist"
        self.enter_1_5_msg = f"Please enter the valid\nnumber between 1-5"
        self.enter_video_number_msg = f"Please enter the video number"
