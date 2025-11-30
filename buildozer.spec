[app]
title = 振动异议器
package.name = objection
package.domain = craft.soul
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,ogg,mp3
source.include_patterns = bgm/*
version = 1.1.4
fullscreen = 0
orientation = portrait
requirements = python3,kivy==2.2.1,plyer,kivymd,libiconv,libffi,openssl
icon.filename = attorney.png
presplash.filename = objection.png
entrypoint = main.py
android.accept_sdk_license = True
android.allow_api_min = 21
android.api = 33
android.minapi = 21
android.ndk = 25b
exclude_patterns = **/test/*, **/tests/*
android.gradle_download = https://services.gradle.org/distributions/gradle-7.6.4-all.zip
android.gradle_plugin = 7.4.2
android.sdk = 33
android.ndk_api = 21
p4a.gradle_dependencies = gradle:7.6.4
p4a.bootstrap = sdl2
p4a.gradle_options = -Dorg.gradle.java.home=/usr/lib/jvm/java-17-openjdk-amd64
android.permissions = INTERNET

# 强制构建 APK 而不是 AAB
android.aab = False

# 签名配置 - 使用绝对路径
android.keystore = /home/runner/work/Objection/Objection/craft.soul.objection.keystore
android.keystore_storepass = android
android.keystore_keypass = android
android.keystore_alias = craft.soul.objection

[buildozer]
log_level = 2
warn_on_root = 1
