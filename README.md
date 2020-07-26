# A Python Flask server to help with some task automation running on a raspberry Pi on my local network

## This is a restful server that is used by some other projects
1. 3D printer automation
* Octoprint running on RPi connected to Monoprice mini V2
* Running VPN server on the Pi to access octoprint from anywhere
* Slack notification intigration on printer status, and errors
* Ability to control LED power, and printer power via the RPI connected to a custom PCB (coming soon)
* Print failure detection via computer vision with openCV, that will send a notification and stop the print

2. Dog monitor (coming soon)
* This is a an app built to monitor a dog when it is left alone
* Send slack notifications when the dog is moving a lot, or being loud
* Stream real time video
* Ability to talk to the dog through a speaker
* Ability to give treats by triggering a servo



## Installation
1. Clone this repo
2. Create a virtual envrionment called pyServerEnv
```
virtualenv -p python3 piServerEnv
```
3. Activate the virtual envrionment
```
source /piServerEnv/bin/activate
```
4. Install the requirments
```
pip3 install -r requirements.txt
```


## Running the app
1. Make sure to activate the virtual envrionment
```
source /piServerEnv/bin/activate
```
2. Start the server 
```
python3 app.py
```

I am running it with Gunicorn and Nginx, which manages starting and restating my server. 


## API documentation
Coming soon

