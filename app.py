import gradio as gr
from scripts.text_analyzer import analyze

with gr.Blocks() as app:
    gr.Markdown(
        "## Приложение для анализа тональности текста\n\n* Шершнев Андрей (РИМ-120907)\n* Кожин Артём (РИМ-120906)\n* Иванов Сергей (РИМ-120906)\n* Чупахин Юрий (РИМ-120908)"
    )
    with gr.Row():
        inp = gr.Textbox(label="Введите текст для анализа")
        out = gr.Textbox(label="Результат")
    btn = gr.Button("Проанализировать")
    btn.click(fn=analyze, inputs=inp, outputs=out)

if __name__ == "__main__":
    app.launch(server_name="0.0.0.0")
