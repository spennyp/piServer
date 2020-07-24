# A Python Flask server to help with some task automation running on a raspberry Pi on my local network

## Installation
1. Clone this repo
2. Create a virtual envrionment called pyServerEnv
'''
virtualenv -p python3 pyServerEnv
'''
3. Activate the virtual envrionment
'''
source /pyServerEnv/bin/activate
'''
4. Install the requirments
'''
pip3 install -r requirements.txt
'''


## Running the app
1. Make sure to activate the virtual envrionment
'''
source /pyServerEnv/bin/activate
'''
2. Start the server 
'''
python3 app.py
'''
