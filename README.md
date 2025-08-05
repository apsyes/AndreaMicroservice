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

response = socket.recv_json()

The result will be either:

A list of movies if "return_data" was true, or

A status message like {"status": "Backup complete."} if no data was requested.

3C. UML Sequence Diagram
<img width="388" height="453" alt="Screenshot 2025-08-04 191552" src="https://github.com/user-attachments/assets/21b6965b-b214-4072-bd7a-07460abb97a3" />
