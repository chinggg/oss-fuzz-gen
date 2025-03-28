#!/usr/bin/env python3

import argparse
import os
import openai

def main():
    parser = argparse.ArgumentParser(
        description="Call Google AI Studio's OpenAI-compatible API."
    )
    parser.add_argument(
        "-prompt", type=str, required=True, help="Path to the prompt file."
    )
    parser.add_argument(
        "-response", type=str, required=True, help="Path to the response directory."
    )
    parser.add_argument(
        "-max-tokens", type=int, default=2000, help="Maximum number of tokens in the response."
    )
    parser.add_argument(
        "-expected-samples", type=int, default=1, help="Number of samples to generate."
    )
    parser.add_argument(
        "-temperature", type=float, default=0.4, help="Sampling temperature."
    )
    parser.add_argument(
        "-model", type=str, default="gemini-2.0-flash", help="Model name."
    )

    args = parser.parse_args()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable is required.")

    client = openai.OpenAI(
        api_key=api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    with open(args.prompt, "r") as f:
        prompt = f.read()

    completion = client.chat.completions.create(
        model=args.model,
        messages=[{"role": "user", "content": prompt}],
        n=args.expected_samples,
        max_tokens=args.max_tokens,
        temperature=args.temperature,
    )

    for index, choice in enumerate(completion.choices):
        content = choice.message.content
        output_path = os.path.join(args.response, f"{index + 1:02}.rawoutput")
        with open(output_path, "w") as output_file:
            output_file.write(content)


if __name__ == "__main__":
    main()
