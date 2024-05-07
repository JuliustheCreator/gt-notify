# GT Notify

This is a class avaliability program I made to check for seat openings (not waitlist seats). Sends you an email when a seat opens in a class. Similar to NotifyGT and Coursicle but can monitor multiple classes for free and updates much more quickly.

## Setup

1. Install Dependencies
   ```
   pip install -r requirements.txt
   ```

2. Fill Out the Script
   - Fill in the `courses` dictionary in the file with class names and URLs
   - Set your Gmail in `user_email` and [app password](https://support.google.com/accounts/answer/185833?hl=en) in `email_password`


## Usage

### macOS

1. Create a Shell Script
   - Make a shell script (monitor.sh) to run your Python script. Include these lines:
  
     ```
     #!/bin/bash
      cd /path/to/your/script/directory
      python script.py
    ```
    
    Replace /path/to/your/script/directory with the actual path

2. Make the Script Executable:
    - Run the following command to make your script executable:
    ```
    chmod +x /path/to/monitor.sh
    ```

3. Set Up Continuous Running:
    - Use `launchd` to keep the script running. Create a plist file (`com.user.monitor.plist`) in ~/Library/LaunchAgents with the following content:
    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.user.monitor</string>
        <key>ProgramArguments</key>
        <array>
            <string>/path/to/monitor.sh</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
        <key>KeepAlive</key>
        <true/>
    </dict>
    </plist>
    ```
    Replace /path/to/monitor.sh with the actual path to your shell script.

4. Load the agent to start the script automatically:
    ```
    launchctl load ~/Library/LaunchAgents/com.user.monitor.plist
    ```

