class Settings:
    """handles variable speeds, expire penalties, etc)
    
    Stereotype:
        Information Holder
    Attributes:
        
        
    """
    def __init__(self, screen_width=1280, screen_height=960, radius=150):
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.SCREEN_TITLE = "Welcome to Speed"
        self.RADIUS = radius