# Import necessary modules and libraries
from SpeechMethods import *
from Prompts import *
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
import semantic_kernel.connectors.ai.open_ai as sk_oai
from semantic_kernel.prompt_template.input_variable import InputVariable
import asyncio

# Initialize semantic kernel
kernel = sk.Kernel()

# Get OpenAI API key
api_key, _ = sk.openai_settings_from_dot_env()

# Add OpenAI ChatCompletion service to the kernel
kernel.add_service(OpenAIChatCompletion(ai_model_id="gpt-3.5-turbo", api_key=api_key))

# Define prompt template for semantic kernel
prompt = """{{$input}}
"""

# Configure execution settings for OpenAI ChatPrompt
execution_settings = sk_oai.OpenAIChatPromptExecutionSettings(
    ai_model_id="gpt-3.5-turbo",
    max_tokens=1000,
    temperature=0.7,
)

# Configure prompt template
prompt_template_config = sk.PromptTemplateConfig(
    template=prompt,
    name="ner",
    template_format="semantic-kernel",
    input_variables=[
        InputVariable(name="input", description="The user input", is_required=True),
    ],
    execution_settings=execution_settings,
)

# Create function for health parameters extraction using the prompt template
health_parameters_extract = kernel.create_function_from_prompt(
    function_name="healthFunc",
    plugin_name="chatPlugin",
    prompt_template_config=prompt_template_config,
)


# Function to get user's name using speech input
def get_name():
    i = 5
    while i > 0:
        try:
            # Prompt user to confirm their name
            TextToSpeech('Kindly, confirm your name?')
            user_input = SpeechToText()
            # Extract name using semantic kernel function
            name = str(asyncio.run(kernel.invoke(health_parameters_extract, sk.KernelArguments(input=Name_extract_prompt + '\n\n' + user_input))))
            Validate_Output(name)
            print(name)
            return name
        except Exception as e:
            print(e)
            TextToSpeech("Couldn't recognize! ")
            i -= 1
    TextToSpeech("Sorry! Your voice cannot be heard at the current moment. We'll call you later.")


# Function to get yesterday's heart rate readings using speech input
def get_heart_rates() -> str:
    i = 5
    while i > 0:
        try:
            # Prompt user to provide yesterday's heart rate readings
            TextToSpeech("Can you please help me note down your yesterday's Heart Rate reading to monitor you health.")
            user_input = SpeechToText()
            # Extract heart rate readings using semantic kernel function
            heart_readings = str(asyncio.run(kernel.invoke(health_parameters_extract, sk.KernelArguments(input=heart_rate_extract_prompt + '\n\n' + user_input))))
            Validate_Output(heart_readings)
            print(heart_readings)
            return heart_readings
        except Exception as e:
            print(e)
            TextToSpeech("Couldn't recognize! ")
            i -= 1
    TextToSpeech("Sorry! Your voice cannot be heard at the current moment. We'll call you later.")


# Function to get any additional health details from the user using speech input
def get_extra_details() -> str:
    i = 5
    while i > 0:
        try:
            # Prompt user if they want to provide any other health details
            TextToSpeech("Would you like to provide any other details to monitor your health?")
            user_input = SpeechToText()
            # Extract other health parameters using semantic kernel function
            other_parameters = str(asyncio.run(kernel.invoke(health_parameters_extract, sk.KernelArguments(input=other_health_parameters_extract_prompt + '\n\n' + user_input))))
            print(other_parameters)
            return other_parameters
        except Exception as e:
            print(e)
            TextToSpeech("Couldn't recognize! ")
            i -= 1
    TextToSpeech("Sorry! Your voice cannot be heard at the current moment. We'll call you later.")


# Main function to interact with the user
def main():
    name, readings, other_parameters = '', '', ''
    wishme()

    # Initiate the conversation to follow up on the user's health
    TextToSpeech('This is a follow-up call to know about your health. ')
    # Get user's name
    name = get_name()
    # Confirm user's name and provide EMR ID
    TextToSpeech(f'Thanks {name}! For confirming your name. Your EMR ID is xxxxx.')
    # Get yesterday's heart rate readings
    readings = get_heart_rates()
    # Thank user for cooperation
    TextToSpeech("Thankyou for your co-operation. ")
    # Get any additional health details from the user
    other_parameters = get_extra_details()
    # Conclude the conversation
    TextToSpeech("Thank you! Stay healthy and have a nice day! ")
    

# Run the main function
if __name__ == "__main__":
   main()
