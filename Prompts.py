'''
Patient Scheduling
An AI Receptionist (AIR) calls a patient for scheduling the appointment which is due next month
The patient and the AIR communicate through natural language (over phone - use Twilio number to call) and the AIR also has all the information from the patient history about the upcoming follow up visit.
The AIR confirms the date and time from the patient and hangs up
This conversation triggers the appointment scheduling RPA bot which either uses EMR API or UI to schedule an appointment in the system
Once done the AIR sends a text message to the patient confirming the appointment
Patient Vitals Upload
An AIR calls a patient to inquire about the heart rate (or any other health parameter) for the previous day.
The patient tells his 5 readings for the previous day(s)
The AIR then acknowledges and inputs all readings into the EMR.
And AIR acknowledges the reading uploads to the patient and the doctor through a text message
'''
# ----------------------------------------------------------

# For getting the name out of the text.
# ----------------------------------------------------------
Name_extract_prompt = '''Get the name that can be found in the following text. 
Do not include any extra text just return the name found.
Do not even mention the name found in the text.
If no name is found then simply return 'None'.

'''


# For extracting the EMR ID out of the text.
# ----------------------------------------------------------
EMR_id_extract_prompt = '''Get the EMR ID that can be found in the following text.
Do not include any extra text just return the ID found.
Do not even mention the EMR ID found in the text.
If no ID is found, then simply return 'None'.

'''

# For reading the appointment date.
# ----------------------------------------------------------
Date_extract_prompt = '''Get the date that can be found in the following text.
The date should be returned in DD-MM-YYYY format.
If no year is mentioned, then consider the current ongoing year.
Do not include any extra words just return the date.

'''


# For reading the blood pressure readings
# ----------------------------------------------------------
heart_rate_extract_prompt = '''Get the list of heart rate readings from the text.
The list should be in comma separated text format.
Just return the list, do not include any extra words.
For example, "72, 60, 85, 105, 75".
'''

# For getting other health parameters
# ----------------------------------------------------------
other_health_parameters_extract_prompt = '''Extract the list of health issues from the text.
The output list should be in comma seperated format.
Do not include any text other than the name of health diseases.
'''