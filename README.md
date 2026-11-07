# Hallucination Hunter — Extractive Evidence Baseline

An offline, reproducible Python quality-assurance project that checks whether a candidate answer appears as a normalized contiguous phrase in its supplied source context. **This is not a semantic hallucination detector or an LLM evaluation.**

## Public dataset

[SQuAD v1.1 validation set](https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json), Stanford Question Answering Dataset. Downloaded automatically at runtime; not committed to Git.

## Run

Python 3.10+; no third-party dependencies.

```bash
python -m unittest discover -s tests -v
python hunter.py --limit 100
```

Produces `evidence_report.json` containing per-example evidence matching results. The CLI reports the actual sample results; no predetermined scores are claimed.

## Limitations

- Exact normalized phrase matching only; paraphrases and synonyms can be wrongly marked unsupported.
- A matched phrase is not proof of factual correctness.
- The SQuAD answers are human-annotated references, not generated model responses.
- A high support rate on this extractive dataset does not establish hallucination-detection performance.

## Roadmap

Add a configurable input JSONL of actual model outputs, semantic entailment evaluation, evidence span attribution, human-labeled error sets, FastAPI endpoints, and optional Gemini evaluation after API access is verified.
