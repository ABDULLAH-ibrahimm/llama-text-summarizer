from fastapi import FastAPI, Form
import requests

app = FastAPI()

@app.post("/summarize/")
def summarize(text: str = Form(...)):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama2",
                "prompt": f"Summarize this:\n\n{text}",
                "stream": False
            }
        )
        response.raise_for_status()
        result = response.json()
        return {"summary": result.get("response", "No summary returned.")}
    except requests.exceptions.RequestException as e:
        return {"summary": f"Error contacting Ollama: {str(e)}"}
    except ValueError:
        return {"summary": f"Invalid JSON from Ollama: {response.text}"}
