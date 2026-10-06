# Compatibility map

| Component | Source | MIDNIGHT |
|---|---|---|
| creation/eval lifecycle | Anthropic | PORTED |
| init_skill.py | OpenAI | PORTED EXACT SOURCE |
| generate_openai_yaml.py | OpenAI | PORTED EXACT SOURCE |
| quick_validate.py | OpenAI | PORTED EXACT SOURCE |
| package/benchmark/viewer | Anthropic | STAGE_2 |
| run_eval.py | Anthropic | UPSTREAM_CLAUDE_ONLY |
| improve_description.py | Anthropic | UPSTREAM_CLAUDE_ONLY |
| run_loop.py | Anthropic | UPSTREAM_CLAUDE_ONLY |
| independent subagents | environment-dependent | CONDITIONAL; never fabricate independence |
