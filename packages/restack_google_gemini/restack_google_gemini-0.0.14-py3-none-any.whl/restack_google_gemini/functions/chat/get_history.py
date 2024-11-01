from pydantic import BaseModel
import google.generativeai as genai

class GeminiGetHistoryInput(BaseModel):
    chat: genai.ChatSession

def gemini_get_history(input: GeminiGetHistoryInput):
    return input.chat.history