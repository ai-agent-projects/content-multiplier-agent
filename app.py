import gradio as gr
import subprocess
import shutil


def repurpose_content(input_text):
    try:
        if not shutil.which("ollama"):
            return "❌ Ollama is not installed or not available in your system PATH."
        
        prompt = f"""
                You are a creative content repurposing assistant.

                Given the following content:
                {input_text}

                Generate the following:
                1. A short summary in 2-3 sentences.
                2. A tweet thread (max 5 tweets).
                3. A LinkedIn post (professional tone).
                4. An Instagram caption (engaging and informal).
                5. An email copy suitable for a newsletter.

                Format the response with clear section titles like:
                ## Summary
                ## Tweet Thread
                ## LinkedIn Post
                ## Instagram Caption
                ## Email Copy
                """
        
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
             return f"❌ Ollama error: {result.stderr.strip()}"

        return result.stdout
    
    except Exception as e:
        print(f"Error: {e}")


# 🖼️ Gradio Interface
def create_ui():
    with gr.Blocks() as demo:
        gr.Markdown("## 🔄 Content Repurposer Agent (Local Ollama)")
        input_text = gr.Textbox(label="📄 Paste Blog/Article/Transcript", lines=10)
        output = gr.Textbox(label="📤 Repurposed Content Output", lines=25)
        submit = gr.Button("⚡ Repurpose Content")
        submit.click(fn=repurpose_content, inputs=[input_text], outputs=output)

    demo.launch(share=True)

# 🚀 Run App
if __name__ == "__main__":
    create_ui()