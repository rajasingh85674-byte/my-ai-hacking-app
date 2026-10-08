[app]

# (str) Title of your application
title = Jamui AI App

# (str) Package name
package.name = jamuiai

# (str) Package domain (needed for android packaging)
package.domain = org.jamui

# (str) Source directory where the application resides
source.dir = .

# (str) Application versioning
version = 0.1

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (bool) Enable Android SDK license acceptance
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = Equal)
warn_on_root = 1
