import gradio as gr
from google import genai
import os


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


def random_response(message, history, prev_id):
    ai_response, prev_interaction_id = aiBot(user_input_str=message, prev_id=prev_id, ai_client=client,
                                             llm_model=llmModel)
    return ai_response, prev_interaction_id


if __name__ == "__main__":
    client = genai.Client()
    llmModel = "gemini-3.1-flash-lite"
    state = gr.State(None)

    gr.ChatInterface(
        fn=random_response,
        additional_inputs=[state],
        additional_outputs=[state]
    ).launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", "7860")))
