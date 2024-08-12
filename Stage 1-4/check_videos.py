import tkinter as tk
import tkinter.scrolledtext as tkst


import video_library as lib
import font_manager as fonts


def set_text(text_area, content):   #insert contents into specific text area
    text_area.delete("1.0", tk.END) # delete the first existed content
    text_area.insert(1.0, content)  # insert the new content to the area


class CheckVideos():    # Create a class
    def __init__(self, window): # Create a initial object for the class
        window.geometry("750x350")  # Create a window with the size of 750x350
        window.title("Check Videos")    # Name the window
        self.video_lib = lib.VideoLibrary()
        
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)   # Create a button with a text, when it's clicked, it will run the command
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10) # Position the button and how much space between it and the x and y axises

        enter_lbl = tk.Label(window, text="Enter Video Number") # Create a label with text
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)   # Position the button and how much space between the label and the previous button and the y axises

        self.input_txt = tk.Entry(window, width=3)  # Create a text entry for user to insert video id 
        self.input_txt.grid(row=0, column=2, padx=10, pady=10) # Position the entry and how much space between the entry and the label

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)   # Create a button with a text, when it's clicked, it will run the command
        check_video_btn.grid(row=0, column=3, padx=10, pady=10) # Position the button and how much space between the button and the entry

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none") # Create a scroll text box with specific size
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10) # Position the box, how much column is used and how much space between the box and the x axis and the row 1

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")   # Create a text field for showing video info with specific size
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10) # Position the field and how much space between it and the list box and the check button

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) # Create a label for checking the button if it's clicked
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)   # Position the label

        self.list_videos_clicked()  # Print the video list automatically when the program run
                                    # Mainly , it is used for testing

    def check_video_clicked(self):  # Create a function for check video button
        key = self.input_txt.get()  # Get key input by the user
        name = self.video_lib.get_name(key)    # Get name by using the key to call the function from video_library.py
        if name is not None:    # Check if the name is available in the library
            director = self.video_lib.get_director(key) # Get director by using the key to call the function from video_library.py
            rating = self.video_lib.get_rating(key)    # Get rating by using the key to call the function from video_library.py
            play_count = self.video_lib.get_play_count(key)    # Get play count by using the key to call the function from video_library.py
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}" # Create a string format variable
            set_text(self.video_txt, video_details) # Display the variable in set area
        else: # Check if the name is unavailable in the library
            set_text(self.video_txt, f"Video {key} not found") # Display text in set area
        self.status_lbl.configure(text="Check Video button was clicked!")   #Set status if button is clicked

    def list_videos_clicked(self):  # Create a list all function
        video_list = self.video_lib.list_all() # List all video details
        set_text(self.list_txt, video_list) # Display each video details in list box
        self.status_lbl.configure(text="List Videos button was clicked!")   #Set status if button is clicked

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
