# OpenAI Changes Demo

I always thought it would be cool to have a chatbot that could change its tone on the fly — concise, detailed, casual, or professional. So I built a simple Flask app that does exactly that.  

It’s lightweight, easy to extend, and meant as a playground for experimenting with prompt-engineering ideas.  

## How to Run
1. Clone this repo  
2. Install requirements:  
   ```bash
   pip install flask
   ```
3. Start the app:  
   ```bash
   python app.py
   ```
4. Send a POST request to `/chat` with JSON like:  
   ```json
   {
     "message": "Explain AI in simple terms",
     "tone": "casual"
   }
   ```

## Tones Supported
- `concise`  
- `detailed`  
- `casual`  
- `professional`  

---

This is just a starting point — I’ll keep tweaking as I go.  
