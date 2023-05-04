from intro import *
from steaks import *
from linkedlist import LinkedList
from playsound import playsound
import speech_recognition as sr
import gtts
r = sr.Recognizer()
# Creates the introduction figure.
begin()


# make request to google to get synthesis
tts = gtts.gTTS("Welcome to A B B Grilling!")

# save the audio file
tts.save("welcome.mp3")

# play the audio file
playsound("welcome.mp3")

time.sleep(1)
# Makes the steak options into a linked list.
def insert_steak_types():
    food_type_list = LinkedList()
    for food_type in steak_type:
        food_type_list.insert_beginning(food_type)
    return food_type_list

# Makes all the beef cut options into a linked list with all their data options.
def insert_steak_data():
    all_data_list = LinkedList()
    for steaks_type in steak_type:
        steak_sublist = LinkedList()
        for steak in steak_data:
            if steak[0] == steaks_type:
                steak_sublist.insert_beginning(steak)
        all_data_list.insert_beginning(steak_sublist)
    return all_data_list

# Initializes the linked lists.
my_beef_list = insert_steak_types()
my_steak_list = insert_steak_data()

# Starts the application.
response = ""

while len(response) == 0:
    print("\nWhat cut of beef would you like to grill? ")
    # make request to google to get synthesis
    tts = gtts.gTTS("What cut of beef would you like to grill?")

    # save the audio file
    tts.save("cut.mp3")

    # play the audio file
    playsound("cut.mp3")
    
    # Makes voice recgonition for the user to say the steak they want.
    with sr.Microphone() as source:
      audio = r.listen(source)
      inh = r.recognize_google(audio)
      inh = inh.lower()
      
    correct_answer = []
    heady = my_beef_list.get_head_node()
    
    while heady is not None:
        if str(heady.get_value()).startswith(inh):
            correct_answer.append(heady.get_value())
            
        heady = heady.get_next_node()
    if correct_answer:
      for cuts in correct_answer:
        print(cuts)
    else:
       print(inh + " is not an option.")
    if len(correct_answer) == 1:
        time.sleep(1)
        print("\nWould you like to use this cut?[yes/no] ")
        tts = gtts.gTTS("Would you like to use this cut? Say yes or no.")

        # save the audio file
        tts.save("use.mp3")

        # play the audio file
        playsound("use.mp3")
        with sr.Microphone() as source:
         audio = r.listen(source)
         inh2 = r.recognize_google(audio)
         inh2 = inh2.lower()
         print(inh2)
        
        if inh2 == "yes":
          #Creates the grilling data display for the user to use.
          steaks = correct_answer[0]
          print("\nSelected Beef Cut: " + steaks)
          heady1 = my_steak_list.get_head_node()
          while heady1.get_next_node() is not None:
              sublist_head = heady1.get_value().get_head_node()
              if sublist_head.get_value()[0] == steaks:
                  while sublist_head.get_next_node() is not None:
                      print("--------------------------")
                      print("Grill Temp: " + sublist_head.get_value()[1])
                      print("Steak Temp: " + sublist_head.get_value()[2])
                      print("Grill Time: " + sublist_head.get_value()[3])
                      print("--------------------------\n")
                      
                      sublist_head = sublist_head.get_next_node()
              heady1 = heady1.get_next_node()

          #Asks the user if the want to look up a different grill option.
          time.sleep(1)
          with sr.Microphone() as source:
            tts = gtts.gTTS("Do you wish to look at another grill option? Say yes or no.")

            # save the audio file
            tts.save("rep.mp3")

            # play the audio file
            playsound("rep.mp3")
            audio = r.listen(source)
            inh3 = r.recognize_google(audio)
            inh3 = inh3.lower()

          if inh3 == 'yes':
            response = ""
            time.sleep(1)
          else:
            break

        else:
          # Asks the user if the want to look up a different grill option.
          time.sleep(1)
          with sr.Microphone() as source:
            print("\nDo you wish to look at another grill option? ")
            tts = gtts.gTTS("Do you wish to look at another grill option? Say yes or no.")

            # save the audio file
            tts.save("rep1.mp3")

            # play the audio file
            playsound("rep1.mp3")
            audio = r.listen(source)
            inh4 = r.recognize_google(audio)
            inh4 = inh4.lower()

          if inh4 == 'yes':
            response = ""
            time.sleep(1)
          else:
            break
  