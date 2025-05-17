# Mass SMS Sender

This Python script allows you to send the same SMS message to multiple recipients using the Karibu Briq SMS API. It reads recipient phone numbers from a CSV file, making it easy to send bulk notifications or announcements.

## Prerequisites

* **Python 3.x** installed on your system.
* An account with [Karibu Briq](https://karibu.briq.tz/) , senderID and a valid API key.
* A CSV file containing the recipient phone numbers.

## Setup

1.  **Clone or download the repository:**
    ```bash
    git clone https://github.com/kefa-steven/Mass-SMS-sender.git
    cd Mass-SMS-sender
    ```

2.  **Install the required library:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Prepare your CSV file:**
    * Use the template cloned from the repository and place the recipient phone numbers.
    * Ensure each phone number is in its own row.
    * The script is configured to skip the first row, assuming it contains a header (e.g., "Phone Number").
    * Phone numbers should be in a format acceptable by the Karibu Briq API (usually international format, e.g., `2557XXXXXXXX`).

4.  **Configure the script:**
    * Open the `Mass_SMS.py` file .
    * **Replace the placeholder API key:**
        ```python
        API_KEY = "<your_api_key>"  # Replace with your actual API key from Karibu
        ```
        with your actual API key from your Karibu Briq account.
    * **Replace the placeholder sender ID: with your registered sender ID from Karibu Briq**
        ```python
        SENDER_ID = "registered-sender-id-name"  # Replace with your registered sender ID from Karibu
        ```
    * **Modify the CSV file path and column index:**
        ```python
        csv_file_path = "phone_numbers_template.csv"  # Update if your CSV file has a different name or path
        ```
    * **(Optional) Modify the default message: Change this default message to your intended message**
        ```python
        message_to_send = "Hello everyone! This is a mass announcement sent via Karibu API."  # Your mass message here
        ```
## Usage

1.  **Navigate to the project directory** in your terminal.
    ```bash
    cd Mass-SMS-sender
    ```
2.  **Run the Python script:**
    ```bash
    python Mass_SMS.py
    ```

    The script will:
    * Load the phone numbers from the specified CSV file.
    * Authenticate with the Karibu Briq API using your API key.
    * Send the defined message to each of the phone numbers.
    * Print status messages indicating success or failure.

## Important Notes

* **API Key Security:** Keep your API key confidential. Do not hardcode it directly in the script if you plan to share it publicly. Consider using environment variables or a separate configuration file for storing sensitive information.
* **Karibu Briq API Limits:** Be aware of any rate limits or other usage restrictions imposed by the Karibu Briq API. Sending a large number of messages too quickly might lead to errors or suspension of your account.
* **Message content:** The message content you intend to send should be less than 160 characters. Try to be brief in your message contents
* **Phone Number Format:** Ensure the phone numbers in your CSV file are in the correct international format expected by the Karibu Briq API. Incorrectly formatted numbers might fail to send.
* **Cost:** Be mindful of the cost associated with sending SMS messages through the Karibu Briq API. Review their pricing before sending large volumes of messages.

## Contributing

Feel free to fork the repository, make changes, and submit a pull request.

---
