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

<!-- PORTFOLIO-OVERVIEW-START -->

## Project overview

Evaluate extractive evidence matching against SQuAD references for grounded-answer checks.

### Technologies and concepts

 - python
 - hallucination detection
 - nlp
 - ai testing
 - squad

### Repository information

- **Category:** AI Quality Engineering / Software Testing
- **Evaluation type:** Offline and/or synthetic fixtures, as documented in this repository
- **Source code:** [GitHub repository](https://github.com/gireeshvuyyuru501-design/hallucination-hunter.git)
- **License:** MIT (subject to repository license file)

### AI Quality Engineering portfolio

This project is part of an 11-project portfolio covering evaluation datasets, structured-output validation, offline scoring, prompt regression, retrieval benchmarking, adversarial testing, agent tool calls, and quality monitoring.

[Explore the integrated AI Quality Engineering Platform](https://github.com/gireeshvuyyuru501-design/ai-quality-engineering-platform)

<!-- PORTFOLIO-OVERVIEW-END -->
