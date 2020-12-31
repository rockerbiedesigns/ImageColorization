import requests
import json
import os
import wget
from requests.auth import HTTPBasicAuth

folderpath = "photos//"
convertpath = "colour//"

#Startup
print("---------------------------------------------------")
print("Please make an account at DeepAI.org")
print(" ")
print("Note your API key listed in your account infomation")
print("This is needed to access service")
print(" ")
print("---------------------------------------------------")
print("API Credit: Image Colorization API")
print("https://deepai.org/machine-learning-model/colorizer")
print("---------------------------------------------------")
print(" ")
print(">> PLEASE PUT PHOTOS IN %s FOLDER" % folderpath)
print(">> LOCATED IN Colourizer FOLDER")
print(" ")
print("---------------------------------------------------")
print(" ")


#Function validates key. If key error, exception raised
def validate_request(key):	
	r = requests.post(
		#Send request to DeepAI with key
		"https://api.deepai.org/api/colorizer",
		headers={'api-key': key}
		)

	if r.status_code == 401:
		#401 error/key not recognized by API
		raise Exception("Invalid API Key. Reenter correct key.")

	else:
		print("Loading from key: %s" % key)

def run_request(key):
	for root, dirs, files in os.walk(folderpath):
		for filename in files:
			r = requests.post(
				"https://api.deepai.org/api/colorizer",
				files={
				'image': open(folderpath + filename, 'rb'),
				},
				headers={'api-key': key}
				)
				
			#Load file URL source
			k = r.json()
			response = requests.get(k["output_url"])
				
			#Download from URL
			wget.download(k["output_url"], convertpath + filename + '.png')
					
			#Display URL name/uncomment to see the uploaded image URL
			#print(k["output_url"])
	
while True:
	try:
		#Input API key
		key = input("Enter Your API Key: ")
		validate_request(key)
		
	except:
		#Exception raised
		print("Invalid API Key - Enter valid key")
		
	else:
		#Key passed validation
		print(" ")
		print("Success!")
		print("Starting conversion")
		run_request(key)

	#finally:
		print(" ")
		print("---------------------------------------------------")
		print(" ")
		print("Done! Photos sent to %s folder" % convertpath)
		print(" ")
		print("--------------------------------------------------")
		input("Press enter to continue...")
		break
					
