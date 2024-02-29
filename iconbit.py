from imports import *

#--------------- FOR REMOVE CTK ICONBIT ----------------------#
                                                                   
ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'    
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))    
                                                                   
_, ICON_PATH = tempfile.mkstemp()                                  
with open(ICON_PATH, 'wb') as icon_file:                           
    icon_file.write(ICON)                                              
