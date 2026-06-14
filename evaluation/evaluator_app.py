from __future__ import annotations

import gradio as gr

from config import settings
from evaluation.eval_answers import evaluate_answers
from evaluation.eval_retrieval import evaluate_retrieval


def configuration_display() -> str:
    return (
        f"Chroma: {settings.CHROMA_HOST}:{settings.CHROMA_PORT}\n\n"
        f"Collection: {settings.CHROMA_COLLECTION}\n\n"
        f"Chat model: {settings.CHAT_MODEL}\n\n"
        f"Embedding model: {settings.EMBEDDING_MODEL}\n\n"
        f"Chunk size/overlap: {settings.CHUNK_SIZE}/{settings.CHUNK_OVERLAP}\n\n"
        f"Default retrieval k: {settings.RETRIEVAL_K}"
    )


def run_retrieval(k: int):
    detail, by_category, weak_cases = evaluate_retrieval(k=int(k))
    return detail, by_category, weak_cases


def run_answer_eval(k: int, limit: int):
    detail, by_category = evaluate_answers(limit=int(limit) or None, k=int(k))
    return detail, by_category


def build_app() -> gr.Blocks:
    with gr.Blocks(title="HarborLight Evaluation Dashboard") as demo:
        gr.Markdown("# HarborLight RAG Evaluation Dashboard")
        with gr.Tab("1. Configuration Display"):
            gr.Markdown(configuration_display())
        with gr.Tab("2. Retrieval Evaluation"):
            k_retrieval = gr.Slider(1, 10, value=settings.RETRIEVAL_K, step=1, label="Retrieval k")
            retrieval_button = gr.Button("Run retrieval evaluation")
            retrieval_detail = gr.Dataframe(label="Retrieval cases")
            retrieval_category = gr.Dataframe(label="Category metrics")
            weak_cases = gr.JSON(label="Weak/failing cases")
            retrieval_button.click(run_retrieval, inputs=[k_retrieval], outputs=[retrieval_detail, retrieval_category, weak_cases])
        with gr.Tab("3. Answer Evaluation"):
            k_answer = gr.Slider(1, 10, value=settings.RETRIEVAL_K, step=1, label="Retrieval k")
            answer_limit = gr.Number(value=5, precision=0, label="Answer judge limit")
            answer_button = gr.Button("Run answer evaluation")
            answer_detail = gr.Dataframe(label="Answer cases")
            answer_category = gr.Dataframe(label="Category-level answer metrics")
            answer_button.click(run_answer_eval, inputs=[k_answer, answer_limit], outputs=[answer_detail, answer_category])
        with gr.Tab("4. Experiment Notes"):
            gr.Textbox(
                lines=12,
                label="Experiment notes",
                placeholder="Record chunk size, overlap, k, model, prompt version, results, and next tuning decision.",
            )
            gr.Markdown(
                "Suggested changes: compare chunk sizes 300/700/1000, overlap 50/120/200, k 3/6/10, strict vs relaxed citation prompts, and insufficient-context wording."
            )
    return demo


def main() -> None:
    build_app().launch(server_name=settings.APP_HOST, server_port=settings.EVALUATOR_PORT)


if __name__ == "__main__":
    main()
