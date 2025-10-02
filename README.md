# OpenAI Changes Demo

I always thought it would be cool to have a chatGPT let you choose its tone without having to specify it in prompt, so I built a simple Flask app that lets you choose between concise, detailed, casual, or professional. 

It’s lightweight and easy to extend, and can be used to help aid research efforts chatGPT.  

## How to Run
1. Clone
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
     "message": "Explain what life is like in Chicago",
     "tone": "casual"
   }
   ```

## Tones Supported
- `concise`  
- `detailed`  
- `casual`  
- `professional`  

---