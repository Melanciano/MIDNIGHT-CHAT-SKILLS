# MIDNIGHT CHAT SKILLS — Catálogo central

> Fonte de verdade: `skills/index.yaml`. Consulte `GPT_CHAT_LOADER.md` antes de executar qualquer skill.
> Release estável: `skills-2026.10.05.1`.

## Estrutura

Cada skill reside em `skills/<nome>/`, com instruções em `SKILL.md` e procedência em `PROVENANCE.yaml`. Arquivos auxiliares em `references/`, `scripts/` e `agents/` pertencem à respectiva skill e não devem ser movidos isoladamente.

| Skill | Instruções | Estado registrado | Finalidade |
|---|---|---|---|
| find-skills | [SKILL.md](skills/find-skills/SKILL.md) | SHADOW_QUALIFIED | Descoberta e avaliação de skills |
| grill-me | [SKILL.md](skills/grill-me/SKILL.md) | SHADOW_QUALIFIED | Revisão crítica com dependência de grilling |
| grilling | [SKILL.md](skills/grilling/SKILL.md) | DEPENDENCY_QUALIFIED_WITH_GRILL_ME | Procedimentos auxiliares de grilling |
| impeccable | [SKILL.md](skills/impeccable/SKILL.md) | SHADOW_QUALIFIED_SAFE_CORE | Qualidade e acabamento de interfaces, restrito ao núcleo qualificado |
| skill-creator | [SKILL.md](skills/skill-creator/SKILL.md) | SHADOW_QUALIFIED | Criação, revisão e validação de skills |
| midnight-auto-advance | [SKILL.md](skills/midnight-auto-advance/SKILL.md) | SHADOW_QUALIFIED | Ciclos iterativos com verificações e limites operacionais |

## Carregamento

1. Leia [GPT_CHAT_LOADER.md](GPT_CHAT_LOADER.md) e [skills/index.yaml](skills/index.yaml).
2. Escolha somente as skills pertinentes à solicitação atual.
3. Leia `SKILL.md` e `PROVENANCE.yaml` de cada skill escolhida.
4. Carregue dependências indicadas no índice; para `grill-me`, carregue também `grilling`.
5. Para `midnight-auto-advance`, leia [PUBLIC_PROFILE.md](skills/midnight-auto-advance/PUBLIC_PROFILE.md) e use PUBLIC_CHAT_MODE, salvo verificação independente das condições descritas no loader.
6. Execute apenas operações suportadas pelas ferramentas disponíveis e pela autorização vigente. Verifique os resultados antes de reportar conclusão.

## Limites e integridade

- Este catálogo **não instala skills nativamente**, não ativa recursos automaticamente em outras conversas e não habilita execução em segundo plano.
- Qualificação shadow não equivale a autorização irrestrita para produção, escrita em outros repositórios ou uso de contas externas.
- Preserve avisos de licença, proveniência e os arquivos auxiliares de cada skill.
- O índice YAML é autoritativo para estados, hashes, dependências e versões; em caso de divergência, reconcilie este catálogo com o índice.
- Humanizer, Fact Checker, Prompt Master e MCP Builder **não integram esta distribuição estável**, conforme o README, até conclusão da qualificação.

## Manutenção

Ao adicionar ou alterar uma skill: mantenha seu diretório `skills/<nome>/`, valide as instruções e procedência, atualize `skills/index.yaml` conforme o processo de qualificação e sincronize este catálogo. Não altere estados de qualificação sem evidência.
