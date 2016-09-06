import json
import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException , NoSuchElementException
from selenium.webdriver.common.keys import Keys

# OPEN WHATSAPP WEB AND ASK USER TO SCAN QR-CODE TO LOGIN.
# AFTER SUCCESSFUL LOGIN USER SHOULD PRESS ANY KEY.
# IT IS THE RESPONSIBLITY OF USER TO LOGIN SUCCESSFULLY.
# TO EXIT PRESS Ctrl+C.

s1="  WELCOME TO WHATSAPP CHAT BOT  "
s2=""" 
	Enter number of spam messages and Press 'enter' key. 
	A browser window will open where you will have to scan the
	QR code for whatsapp web login. After successful login, open
	the contact you want to spam and press 'enter' key.Press Ctrl+C to exit. 
	Once setup is complete the bot will spam the chat by last message 
	present in the conversation (Make sure you have atleast one message 
	in the conversation).
	"""	
s3=" REVENGE TAKEN "

print "\n\n%s" %(s1.center(80,'*'))
print "\n\n%s" %(s2.center(60,' '))
total = int(raw_input("\n\nENTER NUMBER OF SPAM MESSAGES "))

try:
	browser = webdriver.Chrome()
	browser.implicitly_wait(60) # TIMEOUT SET TO 60s
	browser.get("https://web.whatsapp.com")
	raw_input() # USER IS READY TO AUTOMATE THE CHAT
	chat_text = browser.find_element_by_xpath("(//span[@class='emojitext selectable-text'])[last()]")
	message_field = browser.find_element_by_xpath("//div[@dir='auto']")
	for count in range(total+1):
		print "sent message %d times" %(count+1)
		message_field.send_keys(str(chat_text.text))
		message_field.send_keys(Keys.ENTER)
	print "\n%s" %(s3.center(80,'*'))
	browser.quit()

except (KeyboardInterrupt, EOFError):
	print "\n\n%s\n\n" %("  EXITING NOW  ").center(80,'*')
	exit(0)

except TimeoutException as exc:
	print "\n%s" %(" TIMEOUT EXCEPTION OCCURRED ").center(80,' ')
	print "\n\n%s\n\n" %("  EXITING NOW  ").center(80,'*')
	exit(0)

except NoSuchElementException as exc:
	error_message = """
		NO SUCH ELEMENT EXCEPTION OCCURRED. 
		PLEASE READ THE INSTRUCTIONS CAREFULLY AND
		DO THE SETUP CORRECTLY! EXCEPTION MESSAGE IS :-
		%s
		""" %(exc)
	print "\n%s" %error_message.center(80,' ')
	print "\n\n%s\n\n" %("  EXITING NOW  ").center(80,'*')
	exit(0)