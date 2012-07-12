import sublime_plugin
import urllib2
# import sublime
# import subprocess
# import os


class TitaniumBuildCommand(sublime_plugin.WindowCommand):
    def run(self):
        urllib2.urlopen('http://localhost:9090/run')
        # builder = "/Users/shikajiro/Library/Application Support/Titanium/mobilesdk/osx/2.0.2.GA/iphone/builder.py"
        # folder = sublime.packages_path()
        # command = builder + " run " + folder
        # sublime.error_message(command)
        # subprocess.call(command, shell=True)
