# Upstream provenance — skill-creator

## Anthropic lifecycle source

Repository: `anthropics/skills`
Path: `skills/skill-creator`
Pinned ref: `8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4`
License: Apache-2.0.

Lifecycle: capture intent → draft → eval prompts → with-skill + baseline/old-skill → assertions/grading → benchmark → human review → revise → repeat → expand.

Exact command forms observed in the upstream skill:

~~~bash
cp -r <skill-path> <workspace>/skill-snapshot/

python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>

nohup python <skill-creator-path>/eval-viewer/generate_review.py \
  <workspace>/iteration-N \
  --skill-name "my-skill" \
  --benchmark <workspace>/iteration-N/benchmark.json \
  > /dev/null 2>&1 &
VIEWER_PID=$!

kill $VIEWER_PID 2>/dev/null

python -m scripts.run_loop \
  --eval-set <path-to-trigger-eval.json> \
  --skill-path <path-to-skill> \
  --model <model-id-powering-this-session> \
  --max-iterations 5 \
  --verbose

python -m scripts.package_skill <path/to/skill-folder>
~~~

Script CLI inventory from argparse/source:
- `aggregate_benchmark.py <benchmark_dir> [--skill-name NAME] [--skill-path PATH] [-o OUTPUT]`
- `generate_report.py <input> [-o OUTPUT] [--skill-name NAME]`
- `package_skill.py <skill-folder> [output-directory]`
- `quick_validate.py <skill-directory>`
- `generate_review.py <workspace> [-p PORT] [-n NAME] [--previous-workspace PATH] [--benchmark PATH] [-s STATIC]`
- `run_eval.py --eval-set PATH --skill-path PATH [--description TEXT] [--num-workers N] [--timeout S] [--runs-per-query N] [--trigger-threshold F] [--model ID] [--verbose]`
- `improve_description.py --eval-results PATH --skill-path PATH [--history PATH] --model ID [--verbose]`
- `run_loop.py --eval-set PATH --skill-path PATH [--description TEXT] [--num-workers N] [--timeout S] [--max-iterations N] [--runs-per-query N] [--trigger-threshold F] [--holdout F] --model ID [--verbose] [--report PATH|auto|none] [--results-dir PATH]`

`run_eval.py`, `improve_description.py`, and `run_loop.py` invoke `claude -p` directly. MIDNIGHT classifies them `UPSTREAM_CLAUDE_ONLY` and does not vendor them as Codex executables.

## OpenAI/Codex compatibility source

Repository: `openai/skills`
Path: `skills/.system/skill-creator`
Pinned ref: `49f948faa9258a0c61caceaf225e179651397431`
License: Apache-2.0.

Exact Codex utility CLIs brought into MIDNIGHT:

~~~bash
python scripts/init_skill.py <skill-name> --path <path> [--resources scripts,references,assets] [--examples] [--interface key=value]
python scripts/generate_openai_yaml.py <skill_dir> [--name <skill_name>] [--interface key=value]
python scripts/quick_validate.py <skill_directory>
~~~

OpenAI guidance preserved: concise SKILL.md, progressive disclosure, appropriate degrees of freedom, agents/openai.yaml, deterministic scripts for fragile/repeated work.
