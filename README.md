# readme for emg_listener

visit https://developer.equinix.com
 - sign up for an account
 - under 'app dashboard' create a new app with App Type = Production
 - under 'messaging gateway' create a new subscription

when the subscription is ready, click on it and the 'copy YAML' button

copy the .env.template file to .env, then update it with the values from your subscription

update your python libraries to include the packages listed in the requirements.txt file 
