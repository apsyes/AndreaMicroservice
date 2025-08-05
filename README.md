3A. How to programmatically request data from the microservice
To programmatically request data from the microservice, create a ZeroMQ REQ socket and connect to tcp://localhost:5000, then send a JSON object containing any of the following fields:

"return_data": set to true if you want the watchlist returned
"include_watched": set to true or false to include or exclude watched movies
"output_filename": a string like "backup.json" to trigger a file-based backup
Example:
socket.send_json({
"return_data": True,
"include_watched": True,
"output_filename": "backup.json"
})
3B. How to programmatically receive data from the microservice
Immediately after sending your request with send_json(), receive the response using:
example:
response = socket.recv_json()
The result will be either:

A list of movies if "return_data" was true, or

A status message like {"status": "Backup complete."} if no data was requested.

3C. UML Sequence Diagram
<img width="388" height="453" alt="Screenshot 2025-08-04 191552" src="https://github.com/user-attachments/assets/21b6965b-b214-4072-bd7a-07460abb97a3" />

4A. For which teammate did you implement Microservice A?
Andrea

4B. What is the current status of the microservice?
The microservice is fully implemented and operational.

4C. If the microservice isn’t done, which parts aren’t done and when will they be done?
N/A
4D. How is your teammate going to access your microservice?
Andrea should clone the code from GitHub, run movie_backup_service.py locally using Python, and interact with it using ZeroMQ request/reply messages as shown in the examples above.

4E. If your teammate cannot access/call your microservice, what should they do?
They should contact me via our class group chat or email. I’m available weekday afternoons and evenings to troubleshoot.

4F. If your teammate cannot access/call your microservice, by when do they need to tell you?
Please notify me by Friday at 5:00 PM so we have time to resolve any issues before the deadline.

4G. Is there anything else your teammate needs to know?
The microservice responds using JSON and stores backup files in the local backups folder. It uses a simulated file called watchlist.json as its data source and does not use a database. If you're running on a different OS or machine, update the IP address or port accordingly.
