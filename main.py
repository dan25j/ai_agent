import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function


def main():
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")
    client = genai.Client(api_key=api_key)
    messages = [types.Content(
        role="user",
        parts=[types.Part(text=args.user_prompt)])
    ]
    generate_content(client, messages, args.verbose)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = messages,
        config = types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
            # Setting temperature to 0 makes the output more deterministic, which is often desirable for code generation tasks.
            temperature=0
            )
    )

    if not response.usage_metadata:
       raise RuntimeError("Gemini API response appears to be malformed")

    if verbose:
        print(f"User prompt: {verbose}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"Total tokens: {response.usage_metadata.total_token_count}")
    
    function_results = []
    if response.function_calls:
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose)
            if (
                not function_call_result.parts
                or not function_call_result.parts[0].function_response
                or not function_call_result.parts[0].function_response.response
            ):
                raise RuntimeError(f"Empty function response for {function_call.name}")
            function_results.append(function_call_result.parts[0])
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    else:
        print("Response:")
        print(response.text)


if __name__ == "__main__":
    main()
