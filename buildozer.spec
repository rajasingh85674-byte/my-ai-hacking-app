[app]

# (str) Title of your application
title = Jamui AI App

# (str) Package name
package.name = jamuiai

# (str) Package domain (needed for android packaging)
package.domain = org.jamui

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = Equal)
warn_on_root = 1
