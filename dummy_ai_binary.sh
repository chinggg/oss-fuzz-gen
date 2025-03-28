#!/bin/bash

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    -prompt)
      PROMPT_FILE="$2"
      shift
      ;;
    -response)
      RESPONSE_FILE="$2"
      shift
      ;;
    *)
      echo "Unknown parameter: $1"
      exit 1
      ;;
  esac
  shift
done

# Check if required arguments are provided
if [ -z "$PROMPT_FILE" ] || [ -z "$RESPONSE_FILE" ]; then
  echo "Usage: $0 -prompt <prompt_file> -response <response_file>"
  exit 1
fi

# Read prompt from file (not used in this dummy implementation)
#prompt=$(cat "$PROMPT_FILE")

# Dummy fuzz target code
fuzz_target_code="// Dummy fuzz target
int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
  int a = 0, b = 0;
  example(a, b);
  return 0;
}"

# Write the dummy code to the response file
echo "$fuzz_target_code" > "$RESPONSE_FILE"

exit 0
