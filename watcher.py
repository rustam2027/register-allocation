import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    def __init__(self, directory_to_watch, script_to_run):
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.SCRIPT_TO_RUN = script_to_run
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            import subprocess
            subprocess.Popen(['sh', watcher.SCRIPT_TO_RUN])

if __name__ == '__main__':
    directory_to_watch = './src'
    script_to_run = './update.sh'
    watcher = Watcher(directory_to_watch, script_to_run)
    watcher.run()
