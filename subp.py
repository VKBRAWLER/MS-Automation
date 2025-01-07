import subprocess
import time
mainapp = 'c:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe --profile-directory="Default"'
# Replace 'your_application_path' with the actual path to the application you want to open 
application_path = 'c:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe --profile-directory="Profile "' 

profile = ["Default", "Profile 1", "Profile 2", "Profile 3", "Profile 5", "Profile 6"]
subprocess.Popen(mainapp)