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

prompt = """{{$input}}
"""

execution_settings = sk_oai.OpenAIChatPromptExecutionSettings(
    ai_model_id="gpt-3.5-turbo",
    max_tokens=1000,
    temperature=0.7,
)
prompt_template_config = sk.PromptTemplateConfig(
    template=prompt,
    name="ner",
    template_format="semantic-kernel",
    input_variables=[
        InputVariable(name="input", description="The user input", is_required=True),
    ],
    execution_settings=execution_settings,
)
health_parameters_extract = kernel.create_function_from_prompt(
    function_name="healthFunc",
    plugin_name="chatPlugin",
    prompt_template_config=prompt_template_config,
)


def get_name():
    i = 5
    while i > 0:
        try:
            TextToSpeech('Kindly, confirm your name?')
            user_input = SpeechToText()
            name = str(asyncio.run(kernel.invoke(health_parameters_extract, sk.KernelArguments(input=Name_extract_prompt + '\n\n' + user_input))))
            Validate_Output(name)
            print(name)
            return name
        except Exception as e:
            print(e)
            TextToSpeech("Couldn't recognize! ")
            i -= 1
    TextToSpeech("Sorry! Your voice cannot be heard at the current moment. We'll call you later.")


def get_heart_rates() -> str:
    i = 5
    while i > 0:
        try:
            TextToSpeech("Can you please help me note down your yesterday's Heart Rate reading to monitor you health.")
            user_input = SpeechToText()
            heart_readings = str(asyncio.run(kernel.invoke(health_parameters_extract, sk.KernelArguments(input=heart_rate_extract_prompt + '\n\n' + user_input))))
            Validate_Output(heart_readings)
            print(heart_readings)
            return heart_readings
        except Exception as e:
            print(e)
            TextToSpeech("Couldn't recognize! ")
            i -= 1
    TextToSpeech("Sorry! Your voice cannot be heard at the current moment. We'll call you later.")


def get_extra_details() -> str:
    i = 5
    while i > 0:
        try:
            TextToSpeech("Would you like to provide any other details to monitor your health?")
            user_input = SpeechToText()
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

    TextToSpeech('This is a follow-up call to know about your health. ')
    name = get_name()
    TextToSpeech(f'Thanks {name}! For confirming your name. Your EMR ID is xxxxx.')
    readings = get_heart_rates()
    TextToSpeech("Thankyou for your co-operation. ")
    other_parameters = get_extra_details()
    TextToSpeech("Thank you! Stay healthy and have a nice day! ")
    
    

# Run the main function
if __name__ == "__main__":
   main()
