from query_data import query_rag
from langchain_community.llms.ollama import Ollama

EVAL_PROMPT = """
Expected Response: {expected_response}
Actual Response: {actual_response}
---
(Answer with 'true' or 'false') Does the actual response match the expected response? 
"""

def test_monopoly_rules():
    assert query_and_validate(
        question="Who was the eldest Pandava? (Answer with the name only)",
        expected_response="Yudhishthira",
    )
    print("Monopoly Rules Test Passed!")

def test_ticket_to_ride_rules():
    assert query_and_validate(
        question="How many days did the Kurukshetra war last? (Answer with the number only)",
        expected_response="50",
    )
    print("Ticket to Ride Rules Test Passed!")

# def test_monopoly_rules():
#     print("Running Monopoly Rules Test...")
#     assert query_and_validate(
#         question="How much total money does a player start with in Monopoly? (Answer with the number only)",
#         expected_response="$1500",
#     )
#     print("Monopoly Rules Test Passed!")


# def test_ticket_to_ride_rules():
#     print("Running Ticket to Ride Rules Test...")
#     assert query_and_validate(
#         question="How many points does the longest continuous train get in Ticket to Ride? (Answer with the number only)",
#         expected_response="10 points",
#     )
#     print("Ticket to Ride Rules Test Passed!")


def query_and_validate(question: str, expected_response: str):
    response_text = query_rag(question)
    prompt = EVAL_PROMPT.format(
        expected_response=expected_response, actual_response=response_text
    )

    model = Ollama(model="llama3.1:8b")
    evaluation_results_str = model.invoke(prompt)
    evaluation_results_str_cleaned = evaluation_results_str.strip().lower()

    print(prompt)

    if "true" in evaluation_results_str_cleaned:
        # Print response in Green if it is correct.
        print("\033[92m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return True
    elif "false" in evaluation_results_str_cleaned:
        # Print response in Red if it is incorrect.
        print("\033[91m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return False
    else:
        raise ValueError(
            f"Invalid evaluation result. Cannot determine if 'true' or 'false'."
        )


if __name__ == "__main__":
    test_monopoly_rules()
    test_ticket_to_ride_rules()
