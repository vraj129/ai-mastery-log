from google import genai


def aiBot(user_input_str, prev_id=None, ai_client=None, llm_model=None):
    try:
        if prev_id is None:
            interaction = ai_client.interactions.create(
                model=llm_model,
                input=user_input_str,
            )
        else:
            interaction = ai_client.interactions.create(
                model=llm_model,
                input=user_input_str,
                previous_interaction_id=prev_id,
            )
        prev_id = interaction.id
        return interaction.output_text, prev_id
    except Exception as e:
        print("(debug)", e)
        return "Hit a rate limit / error — wait a sec and try again", prev_id


if __name__ == "__main__":
    client = genai.Client()
    llmModel = "gemini-3.1-flash-lite"

    input_str = input("Start Chatting : ")
    prev_interaction_id = None

    while input_str != "exit":
        ai_response, prev_interaction_id = aiBot(input_str, prev_interaction_id, client, llmModel)
        print("Ai:", ai_response)
        input_str = input("Your Input: ")
