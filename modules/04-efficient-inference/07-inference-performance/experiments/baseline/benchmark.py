import argparse, csv, time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--model', default='Qwen/Qwen2.5-0.5B')
    p.add_argument('--revision', default='main')
    p.add_argument('--output', default='metrics.csv')
    p.add_argument('--trials', type=int, default=5)
    p.add_argument('--tokens', type=int, default=32)
    a = p.parse_args()
    if not torch.cuda.is_available():
        raise RuntimeError('CUDA-enabled PyTorch and GPU required')
    if min(a.trials, a.tokens) < 1:
        p.error('trials and tokens must be positive')
    tok = AutoTokenizer.from_pretrained(a.model, revision=a.revision)
    model = AutoModelForCausalLM.from_pretrained(a.model, revision=a.revision, torch_dtype=torch.float16).to('cuda').eval()
    inputs = tok('Explain the difference between latency and throughput.', return_tensors='pt').to('cuda')
    n = inputs['input_ids'].shape[1]
    rows, reference = [], None
    with torch.inference_mode():
        for cache in (True, False):
            kwargs = dict(max_new_tokens=a.tokens, min_new_tokens=a.tokens, do_sample=False, use_cache=cache, pad_token_id=tok.eos_token_id)
            model.generate(**inputs, **kwargs)
            torch.cuda.synchronize()
            for trial in range(a.trials):
                torch.cuda.reset_peak_memory_stats()
                t = time.perf_counter()
                out = model.generate(**inputs, **kwargs)
                torch.cuda.synchronize()
                elapsed = time.perf_counter() - t
                peak = torch.cuda.max_memory_allocated()
                ids = out[0, n:].tolist()
                if reference is None:
                    reference = ids
                rows.append(dict(model=a.model, revision=a.revision, cache=cache, trial=trial, input_tokens=n, output_tokens=len(ids), elapsed_s=elapsed, output_tokens_per_s=len(ids)/elapsed, peak_allocated_bytes=peak, matches_reference=ids==reference))
    with open(a.output, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

if __name__ == '__main__':
    main()
