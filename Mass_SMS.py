import requests # Import the 'requests' library for making HTTP requests to the SMS API.
import json     # Import the 'json' library for working with JSON data (which the API likely uses).
import csv      # Import the 'csv' library for reading data from CSV files (like your phone number list for our case).

# --- API Configuration (SMS Provider: karibu.briq.tz) ---
SEND_SMS_URL = "https://karibu.briq.tz/v1/message/send-instant"
API_KEY = "<your_api_key>"  # Replace with your actual API key from Karibu
SENDER_ID = "registered-sender-id-name"  # Replace with your registered sender ID from karibu. 
CAMPAIGN_ID = None  # Optional: If you are running a specific campaign, you might set its ID here. Otherwise, leave it as None.


# --- Function to Load Phone Numbers from CSV ---
def load_phone_numbers_from_csv(file_path, phone_number_column=0, skip_header=True):
    """Loads phone numbers from a CSV file.

    Args:
        file_path (str): The path to the CSV file.
        phone_number_column (int): The index of the column containing phone numbers (default is 0 - the first column).
        skip_header : Skips the first row from the CSV file if its set to TRUE
    Returns:
        list: A list of phone numbers.
    """
    #an empty array intitated to store numbers from the csv file
    phone_numbers = []
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
             # Open the CSV file in read mode ('r').
            # 'newline=''' ensures proper handling of line endings across different operating systems.
            # 'encoding='utf-8'' sets the character encoding to UTF-8, which supports a wide range of characters.
            reader = csv.reader(csvfile) # Creating a CSV reader object to iterate over rows in the file.
            if skip_header: #checks the state of the skip_header variable, if true
                next(reader, None)  # Advance the reader to the next line, effectively skipping the first row (header).
            for row in reader: # Iterate over each row in the CSV file (after the header, if skipped).
                if row:  # Ensure the row is not empty
                    phone_number = row[phone_number_column].strip() # Access the phone number from the specified column index,and remove any leading or trailing whitespace.
                    phone_numbers.append(phone_number) # Add the extracted and cleaned phone number to the list.
    except FileNotFoundError:
        print(f"Error: CSV file not found at '{file_path}'")
        return []  # If the specified CSV file is not found, print an error and return an empty list.
    except IndexError:
        print(f"Error: Phone number column index '{phone_number_column}' is out of bounds in the CSV file.")
        return []  # If a row doesn't have the expected number of columns, print a warning and move to the next row.
    return phone_numbers  # Return the list of extracted phone numbers.

# --- Function to Send Mass SMS ---
def send_mass_sms(recipients, message):
    """Sends the same SMS message to multiple recipients.
        Args:
        recipients (list): A list of phone numbers (strings) to send the SMS to.
        message (str): The text content of the SMS message to be sent.

    Returns:
        bool: True if the mass SMS was sent successfully (based on the API response), False otherwise.
    """
    
    headers = {
        "Content-Type": "application/json", # Set the Content-Type header to 'application/json' as the API expects JSON data.
        "X-API-Key": API_KEY # Includes the API key in the 'X-API-Key' header for authentication.
    }
    payload = {
        "content": message, # The content of the SMS message.
        "recipients": recipients,  # A list of recipient phone numbers.
        "sender_id": SENDER_ID  # The registered sender ID for the SMS.
    }
    if CAMPAIGN_ID:
        payload["campaign_id"] = CAMPAIGN_ID # Includes the campaign ID in the payload if it's set.

    try:
         
        response = requests.post(SEND_SMS_URL, headers=headers, json=payload) # Send a POST request to the Karibu Briq SMS sending URL with the specified headers and JSON payload.
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx status codes).
        data = response.json() # Parse the JSON response from the API.
        print("Mass SMS sent successfully!") 
        print(f"Response: {data}") # Print the API response for debugging or informational purposes.
        return True # Return True to indicate successful sending.
    except requests.exceptions.RequestException as e:
        print(f"Error sending mass SMS: {e}") # Print a general error message if a request exception occurs
        if response is not None:
            print(f"Response status code: {response.status_code}")  # Print the HTTP status code of the response.
            try:
                print(f"Response body: {response.json()}") # Try to print the JSON response body for more specific error details.
            except json.JSONDecodeError:
                print(f"Response body (non-JSON): {response.text}")  # If the response is not valid JSON, print the raw text.
        return False  # Return False to indicate failure.
    except json.JSONDecodeError:
        print("Error decoding JSON response.") # Print an error if there's an issue decoding the API's JSON response.
        return False # Return False to indicate failure.

# --- Main Execution ---
if __name__ == "__main__":
    csv_file_path = "phone_numbers_template.csv"  # Replace with the actual path to your CSV file
    phone_number_column_index = 0  # Assuming phone numbers are in the first column (index 0)
    skip_header_row = True  # Set to True if your CSV file has a header row that you want to skip.

    recipient_numbers = load_phone_numbers_from_csv(csv_file_path, phone_number_column_index)   # Call the function to load phone numbers from the CSV file.

    if recipient_numbers: # Check if any phone numbers were successfully loaded.
        message_to_send = "Hello, this is a test message sent via Karibu API to recipients from CSV."  # Your mass message here
        print(f"Loaded {len(recipient_numbers)} phone numbers from '{csv_file_path}'.") 
        send_mass_sms(recipient_numbers, message_to_send)  # Call the function to send the SMS to the loaded recipients
        print("Mass SMS sending process initiated.") # Indicate that the sending process has started. Once all the process are successfull
    else:
        print("No recipient phone numbers loaded. Please check the CSV file.")  # If no numbers were loaded, inform the user.