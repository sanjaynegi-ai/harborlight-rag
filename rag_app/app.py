from __future__ import annotations

import gradio as gr

from config import settings
from rag_app.answer import answer_question


def _context_markdown(documents: list) -> str:
    if not documents:
        return "No context retrieved."
    lines = []
    for index, document in enumerate(documents, start=1):
        metadata = document.metadata
        source = metadata.get("source", "unknown")
        category = metadata.get("category", "unknown")
        text = document.page_content[:900]
        lines.append(f"### Chunk {index}: `{source}`\nCategory: `{category}`\n\n{text}")
    return "\n\n".join(lines)


def respond(message: str, history: list, retrieval_k: int, show_context: bool):
    answer, documents = answer_question(message, history=history, k=int(retrieval_k))
    context = _context_markdown(documents) if show_context else "Context hidden."
    return answer, context


def build_app() -> gr.Blocks:
    with gr.Blocks(title="HarborLight RAG Assistant") as demo:
        gr.Markdown("# HarborLight Internal RAG Assistant")
        gr.Markdown("Ask questions about approved HarborLight documents. The assistant cites retrieved source filenames.")
        with gr.Row():
            retrieval_k = gr.Slider(1, 10, value=settings.RETRIEVAL_K, step=1, label="Retrieval k")
            show_context = gr.Checkbox(value=True, label="Show retrieved context")
        chatbot = gr.ChatInterface(
            fn=respond,
            additional_inputs=[retrieval_k, show_context],
            additional_outputs=[gr.Markdown(label="Retrieved context")],
        )
        del chatbot
    return demo


def main() -> None:
    build_app().launch(server_name=settings.APP_HOST, server_port=settings.RAG_APP_PORT)


if __name__ == "__main__":
    main()