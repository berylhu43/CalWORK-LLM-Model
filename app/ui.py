import gradio as gr
from application import TOP_K_DEFAULT, top_queries, init_engine, ask
from application import current_settings

def handle_click(question, model):
    # force reset
    current_settings["embed_backend"] = None
    current_settings["embed_model"] = None
    current_settings["llm_backend"] = None
    current_settings["llm_model"] = None

    return ask(
        question,
        5,
        "BAAI" if model.startswith("mistral") else "OpenAI Embeddings",
        "BAAI/bge-m3" if model.startswith("mistral") else "text-embedding-3-small",
        "Ollama" if model.startswith("mistral") else "OpenAI",
        model
    )


# Build Gradio UI
def ui():
    with gr.Blocks() as demo:
        gr.HTML("""
        <style>
          body { 
              background-color: #ffffff !important; 
              color: #000000 !important;
          }
          
          h3 {
            margin: 0 !important;
            padding: 0 !important;
        }

          .main-title { 
              font-size: 32px; 
              font-weight: 700; 
              margin-bottom: 10px; 
              color: #333333;
          }

          .section-box {
              background: #ffffff;
              padding: 5px;
              margin-bottom: 5px;
          }

          .answer-box {
              background: #f5f5f5;
              border-radius: 10px;
              padding: 20px;
              font-size: 18px;
              line-height: 1.6;
              border: 1px solid #cccccc;
              min-height: 200px;
              color: #000000;
              white-space: pre-wrap;
          }

          .answer-box em {
              color: #9aa0a6;
          }

          input, textarea, select {
              background-color: #ffffff !important;
              color: #000000 !important;
              border: none !important;
              box-shadow: none !important;
          }

          .gr-block, .gr-box, .gr-group, .gr-panel, .gr-row {
              background: transparent !important;
              border: none !important;
              box-shadow: none !important;
          }

          .gr-button {
              background-color: #e6eaf0 !important;
              color: #ffffff !important;
              border-radius: 8px !important;
              border: none !important;
          }

          .gr-button:hover {
              background-color: #6b7280 !important;
          }

          #answer-btn {
              height: 48px;
              width: 80px;
              margin-left: 10px;
              background-color: #e6eaf0 !important;
              color: black !important;
              border-radius: 6px !important;
              border: none !important;
          }

          #answer-btn:hover {
              background-color: #6b7280 !important;
          }

          .input-with-button {
              width: 100%;
          }

          #question-row {
              position: relative;
          }

          #question-box input {
              padding-right: 10px !important;
              font-size: 18px !important;
          }
        </style>
        """)

        gr.HTML("<div class='main-title'>CalWORKs County QA System</div>")

        gr.HTML("<h3 style='margin:0; padding:0; font-size:22px;'>LLM Model</h3>")
        with gr.Row():
            llm_model = gr.Dropdown(
                ["mistral:7b", "gpt-3.5-turbo"],
                value="mistral:7b",
                label=""
            )
        gr.HTML("<h3 style='margin:0; padding:0; font-size:22px;'>Question</h3>")
        gr.HTML("<div class='input-with-button'>")

        with gr.Row(elem_id="question-row"):
            qbox = gr.Textbox(
                label="",
                placeholder="Type your question here...",
                elem_id="question-box",
                scale=5
            )
            go = gr.Button("Ans", elem_id="answer-btn", scale=1)

        gr.HTML("</div>")

        answer = gr.HTML(
            "<div class='answer-box'><em>Answer will appear here...</em></div>",
            label="Answer"
        )

        go.click(
            handle_click,
            inputs=[qbox, llm_model],
            outputs=answer
        )

        gr.HTML("<h3 style='margin:0; padding:0; font-size:22px;'>Top Queries</h3>")
        gr.Textbox(value=top_queries(), interactive=False, lines=10, label="")


        gr.Image(
            "asset/cdss-logo.png",
            show_label=False,
            width=500,
            height=150
        )

        placeholder = gr.Textbox(visible=False)

        demo.load(
            fn=lambda: init_engine(
                "BAAI",
                "BAAI/bge-m3",
                "Ollama",
                "mistral:7b"
            ),
            inputs=[],
            outputs=[placeholder]
        )
        demo.launch(debug=True, share=True)

    return demo

if __name__ == "__main__":
    # start_ollama()
    ui()