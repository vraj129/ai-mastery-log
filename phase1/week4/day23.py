from google import genai

print("step 1")
client = genai.Client()
print("step 2")

try:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input="Explain how AI works in a few words"
    )
    print(interaction)
    print("step 3")
except Exception as e:
    print(e)
