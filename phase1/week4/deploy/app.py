import gradio as gr
from google import genai
import os


def random_response(message, history, prev_id):
    new_id = prev_id
    acc = ""

    try:
        if prev_id is None:
            stream = client.interactions.create(
                model=llmModel,
                input=message,
                stream=True
            )
        else:
            stream = client.interactions.create(
                model=llmModel,
                input=message,
                previous_interaction_id=prev_id,
                stream=True
            )

        for event in stream:
            if event.event_type == "interaction.created":
                new_id = event.interaction.id
            elif event.event_type == "step.delta" and event.delta.type == "text":
                acc += event.delta.text
                yield acc, new_id

    except Exception as e:
        print("(debug)", e, flush=True)
        yield "Hit a rate limit / error — wait a sec and try again", prev_id


if __name__ == "__main__":
    client = genai.Client()
    llmModel = "gemini-3.1-flash-lite"
    state = gr.State(None)

    gr.ChatInterface(
        fn=random_response,
        additional_inputs=[state],
        additional_outputs=[state]
    ).launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", "7860")))
