"""Offline extractive evidence-support baseline; not an LLM hallucination detector."""
import argparse
import json
import re
import urllib.request
from pathlib import Path

URL = 'https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json'

def normalize(text):
    return ' '.join(re.findall(r'\w+', text.lower()))

def supported(answer, context):
    """True if normalized answer is a contiguous phrase in the context."""
    a, c = normalize(answer), normalize(context)
    return bool(a) and a in c

def load_squad(path):
    path = Path(path)
    if not path.exists():
        urllib.request.urlretrieve(URL, path)
    with path.open(encoding='utf-8') as f:
        data = json.load(f)
    for article in data['data']:
        for para in article['paragraphs']:
            for qa in para['qas']:
                if qa['answers']:
                    yield {'id': qa['id'], 'question': qa['question'], 'context': para['context'], 'answer': qa['answers'][0]['text']}

def evaluate(records):
    rows = []
    for item in records:
        ok = supported(item['answer'], item['context'])
        rows.append({'id': item['id'], 'answer': item['answer'], 'supported_by_exact_phrase': ok})
    n = len(rows)
    return {'method': 'normalized_contiguous_phrase_match', 'total': n, 'supported': sum(r['supported_by_exact_phrase'] for r in rows), 'unsupported': sum(not r['supported_by_exact_phrase'] for r in rows), 'support_rate': sum(r['supported_by_exact_phrase'] for r in rows) / n if n else None, 'model_evaluated': False, 'limitations': 'Extractive string matching only. Paraphrases may be falsely flagged; matching does not establish factual truth or detect all hallucinations.', 'results': rows}

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--limit', type=int, default=100)
    p.add_argument('--dataset', default='squad_validation.json')
    p.add_argument('--output', default='evidence_report.json')
    args = p.parse_args()
    if args.limit < 1:
        p.error('--limit must be positive')
    from itertools import islice
    report = evaluate(islice(load_squad(args.dataset), args.limit))
    Path(args.output).write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'results'}, indent=2))
    print(f'Report written to {args.output}')

if __name__ == '__main__':
    main()
