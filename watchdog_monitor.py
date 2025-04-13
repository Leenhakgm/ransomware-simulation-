from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

class RansomwareDetectionHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"⚠️ File modified: {event.src_path}")

    def on_created(self, event):
        if event.is_directory:
            return
        print(f"🆕 File created: {event.src_path}")

    def on_deleted(self, event):
        if event.is_directory:
            return
        print(f"❌ File deleted: {event.src_path}")

def monitor_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ Error: Folder '{folder_path}' not found.")
        return

    event_handler = RansomwareDetectionHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    print(f"👀 Monitoring started for folder: {folder_path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Start monitoring the ransomware_test folder
monitor_folder("ransomware_test")
