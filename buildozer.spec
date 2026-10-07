[app]

title = Jamui AI App
package.name = jamuiapp
package.domain = org.jamui

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt

requirements = python3,kivy,requests,certifi,urllib3,charset-normalizer,idna,pip

orientation = portrait
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

version = 0.1
