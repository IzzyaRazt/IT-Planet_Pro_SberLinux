from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'File modified: {event.src_path}')
        # Здесь можно добавить код для сохранения изменений в git

observer = Observer()
observer.schedule(ChangeHandler(), path='path/to/configs', recursive=False)
observer.start()