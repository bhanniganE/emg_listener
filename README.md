# readme for emg_listener

visit https://developer.equinix.com
 - sign up for an account
 - under 'app dashboard' create a new app with App Type = Production
 - under 'messaging gateway' create a new subscription

when the subscription is ready, click on it and the 'copy YAML' button

copy the .env.template file to .env, then update it with the values from your subscription

review the requirements.txt file, listed are the needed python libraries and deployment instructions 

run command:

	python3 emg_listener.py
