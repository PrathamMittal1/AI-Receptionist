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
named_entity_extract = kernel.create_function_from_prompt(
    function_name="nerFunc",
    plugin_name="chatPlugin",
    prompt_template_config=prompt_template_config,
)



def get_name():
    i = 5
    while i > 0:
        try:
            TextToSpeech('Kindly, confirm your name?')
            user_input = SpeechToText()
            name = str(asyncio.run(kernel.invoke(named_entity_extract, sk.KernelArguments(input=Name_extract_prompt + '\n\n' + user_input))))
            Validate_Output(name)
            print(name)
            return name
        except Exception as e:
            print(e)
            TextToSpeech("Couldn't recognize! ")
            i -= 1
    TextToSpeech("Sorry! Your appointment could not be booked this time. Try again later.")


def get_emr_id():
    i = 5
    while i > 0:
        try:
            TextToSpeech('Now, please speak up your EMR ID!')
            user_input = SpeechToText()
            EMR_id = str(asyncio.run(kernel.invoke(named_entity_extract, sk.KernelArguments(input=EMR_id_extract_prompt + '\n\n' + user_input))))
            Validate_Output(EMR_id)
            print(EMR_id)
            return EMR_id
        except:
            TextToSpeech("Couldn't recognize! ")
            i -= 1
    TextToSpeech("Sorry! Your appointment could not be booked this time. Try again later.")
            


def get_date():
    i = 5
    while i > 0:
        try:
            TextToSpeech('When you are available for your next appointment?')
            user_input = SpeechToText()
            date = str(asyncio.run(kernel.invoke(named_entity_extract, sk.KernelArguments(input=Date_extract_prompt + '\n\n' + user_input))))
            Validate_Output(date)
            print(date)
            return date
        except:
            TextToSpeech("Couldn't recognize! ")
            i -= 1
    TextToSpeech("Sorry! Your appointment could not be booked this time. Try again later.")


# Main function to interact with the user
def main():
    name, EMR_id, date = '', '', ''
    wishme()

    TextToSpeech('I am calling you to book your next visit to the hospital ward.')
    name = get_name()
    EMR_id = get_emr_id()
    date = get_date()
    TextToSpeech(f'Alright! So I\'m booking your appointment for {date} with EMR ID {EMR_id}')
    print('++++++++++++++++++++++')
    print('Name: ', name)
    print('EMR ID: ', EMR_id)
    print('Appointment Date: ', date)
    

# Run the main function
if __name__ == "__main__":
   main()
