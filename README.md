# Anthony-Brooks---WOL-Project-Summer-2023-
This is a simple project the uses the ESP8266 MCU interfaced with a switch and LED to turn on my PC from my home network. I wanted to play around with using the MCU's network capabilities. 


#How To Use
Interface a positive logic switch to GPIO 5 and a positive logic LED to GPIO 4

#Setup
Replace the commented values with your own personal details (SSID, Password, MAC Address of Adapter, and Broadcast IP) 

#LED Indicator
On startup the LED should turn off and turn back on whenever the MCU has successfully connected to your network

When pressing the button to WOL the LED will flash 4 times indicating that the WOL packet has been sent. After the LED goes back to the steady state another packet is ready to be sent
