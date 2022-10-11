from tkinter import * 

class Root:
    def init(size: tuple[int], caption: str):
        # creating a window
        root = Tk(className = caption)
        # setting the size of the screen
        root.minsize(size[0], size[1])
        root.maxsize(size[0], size[1])
        return root