import zmq
import json
import os
from datetime import datetime

WATCHLIST_FILE = 'watchlist.json'  # Movie watchlist file
BACKUP_FOLDER = 'backups'          # Folder to store backup files
os.makedirs(BACKUP_FOLDER, exist_ok=True)

def load_watchlist():
    # movie list (would normally load from store)
    if not os.path.exists(WATCHLIST_FILE):
        sample = [
            {"title": "Inception", "watched": True},
            {"title": "Matrix", "watched": False},
            {"title": "Godfather", "watched": True}
        ]
        with open(WATCHLIST_FILE, 'w') as f:
            json.dump(sample, f, indent=2)
    with open(WATCHLIST_FILE, 'r') as f:
        return json.load(f)

def save_backup(data, filename):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = os.path.join(BACKUP_FOLDER, f"{timestamp}-{filename}")
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    return path

def microservice():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5001")

    print("Microservice A listening on port 5001...")

    while True:
        request = socket.recv_json()
        print(f"Received request: {request}")

        if "watchlist_data" in request:
            watchlist = request["watchlist_data"]
        else:
            watchlist = load_watchlist()

        # Filter watched if requested
        include_watched = request.get("include_watched", True)
        if not include_watched:
            watchlist = [movie for movie in watchlist if not movie.get("watched")]

        # Save backup if requested
        if "output_filename" in request:
            filename = request["output_filename"]
            save_path = save_backup(watchlist, filename)
            print(f"Backup saved to {save_path}")

        # Return data if requested
        if request.get("return_data"):
            socket.send_json(watchlist)
        else:
            socket.send_json({"status": "Backup complete."})

if __name__ == "__main__":
    microservice()

