# Libraries

import os
import sys
import shutil

# Variables

APP_NAME = "Pokemon-NAH"

# Functions

def get_data_path(filename):
    
    '''
    Get the path of the game data file in parameter.      
    ### PARAMETER
            filename: str
    ### RETURN
            target_file: str
    '''

    # PyInstaller
    if getattr(sys, 'frozen', False):
        base = os.getenv("APPDATA")
        gamedata_dir = os.path.join(base, APP_NAME, "data")
        os.makedirs(gamedata_dir, exist_ok=True)

        target_file = os.path.join(gamedata_dir, filename)

        if not os.path.exists(target_file):
            bundled_file = os.path.join(sys._MEIPASS, "data", filename)
            if os.path.exists(bundled_file):
                shutil.copy(bundled_file, target_file)

        return target_file

    # normal Python
    else:
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..",
            "..",
            "data",
            filename
        )
