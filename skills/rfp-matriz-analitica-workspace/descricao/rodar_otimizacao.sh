#!/bin/zsh
# Loop de otimização da descrição da skill rfp-matriz-analitica (skill-creator / run_loop)
S="/private/tmp/claude-501/-Users-tfgcaixeta-Library-Application-Support-Claude-scratch-workspaces-3d6c3529-b878-4c64-a5d2-9aebd2f46221-e9920352-825f-4023-a292-91ef7c26e07d-scratch-2026-10-17-46e619/a169dcfb-5479-433a-86a0-f61944b34bb4/scratchpad"
D="/Users/tfgcaixeta/Library/Application Support/Claude/scratch-workspaces/3d6c3529-b878-4c64-a5d2-9aebd2f46221/e9920352-825f-4023-a292-91ef7c26e07d/scratch-2026-10-17-46e619/skills/rfp-matriz-analitica-workspace/descricao"
SKILL="/Users/tfgcaixeta/Library/Application Support/Claude/scratch-workspaces/3d6c3529-b878-4c64-a5d2-9aebd2f46221/e9920352-825f-4023-a292-91ef7c26e07d/scratch-2026-10-17-46e619/skills/rfp-matriz-analitica"
export PATH="$S/bin:$PATH"
export PYTHONPATH="$S/sc"
unset CLAUDECODE
cd "$S/trigger-proj" || exit 1
echo "== Verificando login do CLI"
claude -p "Responda apenas: ok" --output-format text || { echo "Falha no teste do CLI"; exit 1; }
echo "== Iniciando loop (pode levar bastante tempo)"
"$S/venv/bin/python" -m scripts.run_loop \
  --eval-set "$D/trigger_eval.json" \
  --skill-path "$SKILL" \
  --model claude-opus-5-5 \
  --description "$(cat "$D/descricao_iteracao2.txt")" \
  --max-iterations 4 \
  --num-workers 5 \
  --timeout 60 \
  --results-dir "$D/resultados" \
  --verbose > "$D/resultado_loop.json" 2> >(tee -a "$D/log_loop.txt" >&2)
echo "== Fim. Código de saída: $?"
