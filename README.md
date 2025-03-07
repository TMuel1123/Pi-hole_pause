# PiHole DNS Blocking Pause Script

A simple Python script to temporarily disable DNS blocking on Pi-hole v6 using the API interface.

## Description

This script allows you to pause Pi-hole's DNS blocking functionality for a configurable duration. It uses Pi-hole's API v6 to authenticate and temporarily disable blocking, making it useful when you need to briefly access blocked domains.

## Features

- Temporarily disables Pi-hole DNS blocking
- Configurable pause duration
- Uses Pi-hole API v6
- Config file based setup
- Simple authentication using Pi-hole API token

## Prerequisites

- Python 3.x
- Pi-hole v6 installed and running
- `requests` library (`pip install requests`)
- Valid Pi-hole API token

## Installation

1. Clone this repository:
```bash
git clone https://github.com/TMuel1123/Pi-hole_pause.git
cd Pi-hole_pause
```

2. Create a config.ini file with your Pi-hole settings:
```ini
[PIHOLE]
HOST = 192.168.x.x
API_KEY = your_api_key_here
BLOCK_PAUSE = 300
```
## Usage
Simply run the script:

```bash
python PiHole_PauseBlock.py
```

The script will:

1. Read the configuration from config.ini
2. Authenticate with Pi-hole
3. Disable DNS blocking for the configured duration
4. Display success/error messages

## Configuration
### With ini-file
Edit `config.ini` to customize:

- `piHole`: Your Pi-hole IP address
- `apiKey`: Your Pi-hole API key/password
- `blockPause`: Duration to pause blocking (in seconds)

Further description in the ini-file itself.

### Direct in the script
To avoid having an additional config file, the [PiHole_PauseBlock.py](PiHole_PauseBlock.py) can be edited in the following way:

- Line 7: Comment this line
- Line 10: Comment this line
- Line 13: Replace `config['DEFAULT']['piHole']` with the Pi-hole IP
- Line 14: Replace `config['DEFAULT']['apiKey']` with the Pi-hole API key
- Line 15: Replace `config['DEFAULT']['piHole']` number of seconds to pause blocking (int)

## Error Handling
The script includes basic error handling for:

- Authentication failures
- Connection issues
- Invalid configurations

## License
This project is licensed under **The Unlicense** - see the [LICENSE](LICENSE) file for details.


## Acknowledgments
- Pi-hole team for providing the API
- Python requests library

## Contributing
Feel free to:

1. Fork the project
2. Create a feature branch
3. Submit a Pull Request

## Security Note
Keep your `config.ini` secure as it contains your Pi-hole API key.

