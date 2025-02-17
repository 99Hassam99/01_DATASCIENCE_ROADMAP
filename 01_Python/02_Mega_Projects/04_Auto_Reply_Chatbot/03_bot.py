import pyautogui
import time
import pyperclip  # To handle clipboard copy
from transformers import pipeline
from openai import OpenAI


client = OpenAI(
  api_key="<Your Key Here>",
)

def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True
    return False
# A small delay to give you time to switch to the required screen
time.sleep(2)
# Step 1: Click on chrome icon at this coordinate (511,746)
pyautogui.click(511, 746)
time.sleep(0.5)  # Add a slight delay of 0.5-1 seconds
pyautogui.click(297, 30)
time.sleep(0.5)  # Add a slight delay

while True:
    time.sleep(5)
# Step 2: Click at (303,9)

# Step 3: Drag from (500,154) to (1289,690)
    pyautogui.moveTo(532, 168)  # Move to the start position
    pyautogui.dragTo(829, 652, duration=1, button="left")  # Drag to select text

# Step 4: Copy selected text (Ctrl + C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(524, 160)

    chat_history = pyperclip.paste()


    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a person named Naruto who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
                {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Rohan Das: "},
                {"role": "user", "content": chat_history}
            ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        pyautogui.click(1808, 1328)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed
