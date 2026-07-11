import gradio as gr
from google import genai

from phase1.week4.day24 import aiBot


def random_response(message, history, prev_id):
    ai_response, prev_interaction_id = aiBot(user_input_str=message, prev_id=prev_id, ai_client=client,
                                             llm_model=llmModel)
    return ai_response,prev_interaction_id


if __name__ == "__main__":
    client = genai.Client()
    llmModel = "gemini-3.1-flash-lite"
    state = gr.State(None)

    gr.ChatInterface(
        fn=random_response,
        additional_inputs=[state],
        additional_outputs=[state]
    ).launch()
