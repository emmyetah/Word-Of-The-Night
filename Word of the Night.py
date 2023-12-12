#Word of the Night programme

#I want ot improve my vocabulary so I made a programme that sends me a word, its definition and it used in a sentence every night before I go to sleep.
#I call it the word of the night. I am more likely to check my emails and take the word in properly as im going to sleep.
#I made an email list so that a couple of my friends can receieve the email too if they are looking to learn new words
#To automate this code I used windows task manager 

#Because the time class from the date time module has the same name as the time module I have to rename one of the modules.
from datetime import datetime, time as dt_time
import time
#imported the random module to choose a random word from the dictionaries
import random
#For sending the email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#A list of emails that want to receieve the word of the night
Emails = ["emsetah10@gmail.com", "onibaboriufuoma@gmail.com", "nyokorosa@yahoo.com", "jltchiesso@gmail.com","thenoirtheory@gmail.com", "muniazoqueeny@gmail.com"]

#A list of the words 
words = ["Satiate", "Moniker", "Bespoke", "Obfuscate", "Perspicacious", "Ineffable",
         "Ephemeral","Egregious","Mellifluous", "Esoteric", "Plenipotentiary", "Paragon" ]

#A dictionary with the word and the definition.
Definitions = {"Satiate": "The term 'Satiate' means to satisfy fully, or to fill or supply to the point of being satisfied",
               "Moniker": "The term 'Moniker' refers to a name or nickname",
               "Bespoke": "'Bespoke' refers to something that was made to order, custom-made or to an individuals specific requirements.",
               "Obfuscate": "This term refers to the action of deliberately making somehting unclear or unintelligible.",
               "Perspicacious": "Having a keen insight, a sharp understanding or clear-sightedness.",
               "Ineffable": "Refers to something too great or extreme to be described in words",
               "Ephemeral": "Refers to something that lasts for a ver short time",
               "Egregious": "Something outstandingly bad or shocking. You could even go as far as saying offensive.",
               "Mellifluous": "A sound pleasingly smooth and musical.",
               "Esoteric": "Used to describe something very unusual and understood/liked by only a small numbe rof people",
               "Plenipotentiary": "A person such as a diplomat, invested with the full power to transact business on behalf of their government or another person",
               "Paragon": "A person or thing regarded as the perfect example of a particular quality."
               }

#A dictionary with sentences including the word. 
Sentences = {"Satiate": "The novel was so fascinating that it contiued to satiate the reader until the very last page",
             "Moniker": "Although the moniker 'Emmy' may be unfamiliar to you, it's still a beautiful name.",
             "Bespoke": "Emmy bought a bespoke dress for the ball. She wanted the evening to be perfect.",
             "Obfuscate": "The lawyer attempted to obfuscate the details of Emmy's prenuptial agreement",
             "Perspicacious": "Emmy's perspicacious observations analysis of the show Greys Anatomy left her friends and family in awe of her taste in Tv shows.",
             "Ineffable": "Emmy's beauty was ineffable, her friends and family were in awe of her undeniably breathtaking looks.",
             "Ephemeral": "Emmy's joy was ephemeral as she discovered she was eating chicken flavoured Indomie and not onion-chicken.",
             "Egregious": "The taste of ginger was egregious to Emmy",
             "Mellifluous": "Emmy's mellifluous voice shocked all of her friends and family when she sang let it go from Frozen.",
             "Esoteric": "Assembly code is an esoteric language but if you learn it you can increase your career prospects",
             "Plenipotentiary": "Emmy was appointed as a plenipotentiary to negotiate contracts on behalf of the company.",
             "Paragon": "Emmy's exceptional leadership skills and dedication to her work made her a paragon of excellence in the company.",
             }

#I then state the time right now and the time I want the email to be released. 
#The arguments for the time object is hour, minute, second. SO to specify the release time as 10pm I enetered 22,0,0 below:
now_time = datetime.now().time()
release_time = dt_time(22,0,0)

def send_email(receiver_email, body):
    """This function sends the email"""
    #I set my variables and login to the email using an app-specific password generated in my google account
    sender_email = "Wordofthenight22@gmail.com"
    sender_password = "sfnwwnzegfdryctv"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Word Of The Night"
    message.attach(MIMEText(body, "plain"))
    #this with function establishes a connection to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        #this line starts the server
        server.starttls()
        #Then I login to gemail using the username and password variables created above
        server.login(sender_email, sender_password)
        #I then combine everything used to send the email using the sendmail fucntion
        server.sendmail(sender_email, receiver_email, message.as_string())

#random function selects a random word form the list of words
word = random.choice(words)
#I then created variables specifying the word definition and th eword sentence
word_definition = Definitions[word]
word_sentence = Sentences[word]
#created the body of the email
email_body = "Good Evening,\n\nWelcome to todays Word Of The Night.\n\nToday your word is: {}.\nDefinition: {}.\n{} used in a sentence: {}.\n\nHave a great night, I hope you learnt something new today!\n\nKind regards,\nEmmy Natasha Etah \n\n\nTo unsubscribe, email emsetah10@gmail.com 'STOP'".format(word,word_definition,word,word_sentence)
#finally I created a for loop that sends an email to every email in the emails list.
for emails in Emails:
    receiver_email = emails
    send_email(receiver_email, email_body)



