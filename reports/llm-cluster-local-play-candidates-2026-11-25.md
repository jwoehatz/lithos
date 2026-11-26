# LLM / knowledge-engine cluster: local-play candidates — skeptic verdict

Worker: ds-skeptic@1 (deepseek, skeptic lens). Task: local-play-candidates. Date: 2026-11-25.

## Verdict table

| Candidate | For the local play? | One-line reason | Fetch-verified source |
|---|---|---|---|
| K2 (davendw49/k2) | **No** | Runnable (7B, Apache-2.0, ungated) but a 2023-era LLaMA-7B; a modern general open LLM has better instruction-following and tool-calling | github.com/davendw49/k2; huggingface.co/daven3/k2-v1 |
| GeoMinLM (wangcug/GeoMinLM) | **No** | Chinese Baichuan-2 base trained on Yunnan Province data; weights on Google Drive, no license field; useless for Connecticut geology | github.com/wangcug/GeoMinLM; doi.org/10.1016/j.oregeorev.2025.106638 |
| JiuZhou (THU-ESIS/JiuZhou) | **No** | Runnable (7B, Apache-2.0, ungated) but Chinese-centric (Chinese-Mistral base, expanded Chinese vocab); English tool-calling orchestration is not its strength | github.com/THU-ESIS/JiuZhou; huggingface.co/itpossible/JiuZhou-Instruct-v0.2 |
| MetalGPT-1 (nn-tech/MetalGPT-1) | **No** | Triple kill: 32B (~69 GB fp16), Russian-only (base t-tech/T-pro-it-2.0, `language: ru`), cc-by-nc-sa-4.0 non-commercial | huggingface.co/nn-tech/MetalGPT-1; huggingface.co/t-tech/T-pro-it-2.0 |
| NRCan geoscience_language_models | **No** | Not an LLM — GloVe/BERT embeddings + training code; no orchestrator capability | github.com/NRCan/geoscience_language_models |
| GeoVec (spadarian/GeoVec) | **No** | Research artifact: 2019 word-level GloVe, dead repo (2020), no license assertion; not a knowledge engine | github.com/spadarian/GeoVec; soil.copernicus.org/articles/5/177/2019/ |

**All six killed.** The honest answer to Q1 is: a general-purpose modern open LLM beats every domain candidate here for the orchestrator role.

## Obtainability

| Candidate | Weights open? | Size | License | Last activity |
|---|---|---|---|---|
| K2 | Yes — full model `daven3/k2-v1` (3 safetensors shards, ~14.8 GB fp16; shard1 = 4.94 GB), delta `k2_fp_delta`, LoRA adapter `k2_it_adapter`; all ungated | 7B | Apache-2.0 | repo pushed 2024-06-05; HF last modified 2024-06-02; demo k2.acemap.info returns **404 (dead)** |
| GeoMinLM | Yes but informal — Google Drive tarball (drive link returns 200) | Baichuan-2 (7B-class, Chinese) | README claims MIT; GitHub license field **null** | repo pushed 2024-12-19; 5 stars, 2 forks |
| JiuZhou | Yes — `JiuZhou-Instruct-v0.2` (4 shards, ~15.6 GB fp16; shard1 = 3.90 GB), `JiuZhou-base`, `Chinese-Mistral`; all ungated | 7B (Mistral-7B-v0.1 base, vocab expanded 32000→63872) | Apache-2.0 | repo pushed 2025-06-19; HF last modified 2025-06-22 |
| MetalGPT-1 | Yes — 14 shards, ungated | **32B** (Qwen3-32B base; shard1 = 4.93 GB → ~69 GB fp16) | **cc-by-nc-sa-4.0** (non-commercial, share-alike) | HF last modified 2026-02-17; 312 downloads, 45 likes |
| NRCan | Partial — repo ships training code + `Geoscience_GloVe_Embedding_Minerals.csv` (5.7 MB); full BERT weights not in repo | GloVe 300d / BERT (not an LLM) | MIT | repo pushed 2024-01-24 |
| GeoVec | Yes — OSF `geovec_300d_v1.h5`, **468 MB**, download URL osf.io/download/kt6eu returns 200 | GloVe 300d, ~280k docs | **NOASSERTION** (no license) | repo pushed 2020-07-30 (dead ~6 yr); 14 stars, 2 forks |

Hobbyist-runnable as an orchestrator: **K2 and JiuZhou only** (7B, ~15 GB fp16, or ~8 GB 4-bit quantized — fits 16 GB RAM / 8 GB VRAM). MetalGPT-1 needs ~70 GB fp16 (or ~35 GB quantized) — beyond consumer hardware. GeoMinLM is downloadable but Chinese/Yunnan-specific. NRCan and GeoVec are not LLMs.

## GeoVec gradient claim

**Verified from the primary source** (Padarian & Fuentes, SOIL 5, 177–2019, §6.5 and Fig. 7b):

> "The interpolation between the rocks 'slate' and 'migmatite' yields a gradient of rocks with different grades of metamorphism as follows: slate < phyllite < schist < gneiss < migmatite."

Mechanism (from §6.5): linear interpolation `v_int = α·v_a + (1−α)·v_b` with α ∈ [0,1], then cosine-similarity nearest word in the corpus. The claim **survives scrutiny as stated** — it is a real, documented result, and the paper is open access so it is checkable.

But three caveats that matter for the local play:
1. **It is a qualitative illustration, not a continuous physical gradient.** The "gradient" is a chain of nearest-neighbor words in a 2D PCA projection (the paper itself notes the first two PCs account for only 28.8% of variance).
2. **Word-level, not document-level.** GeoVec embeds words, not papers. You cannot query it for "skarn literature" — only for nearest words to "skarn". The paper's own application examples are soil-related (it was published in *SOIL*).
3. **Stale and unlicensed.** 2019 GloVe, repo dead since 2020, no license assertion (NOASSERTION). The corpus predates most modern skarn/amphibolite literature.

Could it add anything? Only as a curiosity — e.g., nearest-neighbor probes for "scheelite"/"skarn"/"amphibolite" to see what 2019 geoscience text associates with them. That is a demo, not a knowledge engine, and a modern embedding model (e.g., any current sentence-transformer) would do the same job better on current text.

## Final ruling

**None of the six. Use a general-purpose modern open instruction-tuned LLM (7–13B) as the orchestrator** — exactly what the prior design report already suggested, and this cluster confirms it.

Reasons:
1. **The two runnable domain LLMs (K2, JiuZhou) are 2023-era 7B models with Chinese-centric training** (JiuZhou) or LLaMA-7B-era instruction-following (K2). The tool-calling pattern (ChemCrow mold) demands reliable function-calling and instruction-following — the exact capability where modern general models (Llama-3.1-8B, Qwen2.5-7B, etc.) dominate 2023 domain models. The domain knowledge these models add is geoscience trivia, not the mineralogy numbers — and the binding ruling says PhaseCast's posterior is the *only* source of mineralogy numbers anyway.
2. **The domain value-add is redundant with the stack.** The orchestrator's job is to narrate, call tools, and ground output in PhaseCast's posterior. That is a general capability. The geoscience-specific knowledge in K2/JiuZhou would be nice-to-have but is not load-bearing, and it comes at the cost of weaker tool-calling.
3. **The rest are dead on arrival**: MetalGPT-1 (32B, Russian, non-commercial), GeoMinLM (Chinese, Yunnan-specific, Google Drive weights, no license), NRCan (not an LLM), GeoVec (research artifact).

**One caveat worth keeping**: if a future stage wants a geoscience-flavored *narrator* voice, K2 is the only English-language, Apache-2.0, hobbyist-runnable option — but it should be treated as a flavor layer, never as the tool-calling brain.

## Sources (fetch-verified URLs)

GitHub API (all 200):
- https://api.github.com/repos/davendw49/k2 — 217 stars, 19 forks, Apache-2.0, pushed 2024-06-05
- https://api.github.com/repos/wangcug/GeoMinLM — 5 stars, 2 forks, no license, pushed 2024-12-19
- https://api.github.com/repos/THU-ESIS/JiuZhou — 15 stars, 5 forks, Apache-2.0, pushed 2025-06-19
- https://api.github.com/repos/NRCan/geoscience_language_models — 34 stars, 6 forks, MIT, pushed 2024-01-24
- https://api.github.com/repos/spadarian/GeoVec — 14 stars, 2 forks, NOASSERTION, pushed 2020-07-30
- https://api.github.com/repos/wangcug/GeoMinLM/contents/ — repo is 4 files (README, cli_demo.py, requirement.txt, triple qa.py)
- https://api.github.com/repos/NRCan/geoscience_language_models/contents/ — ships Geoscience_GloVe_Embedding_Minerals.csv (5.7 MB) + project_tools
- https://api.github.com/repos/NRCan/geoscience_language_models/contents/project_tools — training code, no BERT weights

Raw READMEs (all 200):
- https://raw.githubusercontent.com/davendw49/k2/main/README.md — K2 = LLaMA-7B further-pretrained on 5.5B tokens geoscience text; delta + adapter release
- https://raw.githubusercontent.com/wangcug/GeoMinLM/main/README.md — Google Drive download link; MIT claim
- https://raw.githubusercontent.com/THU-ESIS/JiuZhou/main/README.md — Mistral-7B-v0.1 base, PreparedLLM framework
- https://raw.githubusercontent.com/NRCan/geoscience_language_models/main/README.md — GloVe + BERT on GEOSCAN (27,081 docs)
- https://raw.githubusercontent.com/spadarian/GeoVec/master/README.md — GloVe on ~280k docs; OSF vectors link
- https://raw.githubusercontent.com/NRCan/geoscience_language_models/main/LICENSE.md — MIT

HuggingFace API (all 200):
- https://huggingface.co/api/models/daven3/k2-v1 — ungated, 3 safetensors shards, 21 downloads
- https://huggingface.co/api/models/daven3/k2_fp_delta — ungated, Apache-2.0, 2 pytorch bins
- https://huggingface.co/api/models/daven3/k2_it_adapter — ungated, Apache-2.0, LoRA adapter
- https://huggingface.co/api/models/itpossible/JiuZhou-Instruct-v0.2 — ungated, 4 shards, 117 downloads
- https://huggingface.co/api/models/itpossible/Chinese-Mistral-7B-v0.1 — ungated, 200 downloads
- https://huggingface.co/api/models/itpossible/Prepared-Llama — ungated, 115 downloads
- https://huggingface.co/api/models/nn-tech/MetalGPT-1 — ungated, **cc-by-nc-sa-4.0**, 14 shards, 312 downloads, 45 likes
- https://huggingface.co/api/models/t-tech/T-pro-it-2.0 — MetalGPT-1 base, **language: ru**, Apache-2.0

HuggingFace model cards / configs (all 200):
- https://huggingface.co/nn-tech/MetalGPT-1/raw/main/README.md — `language: ru`, Qwen3-32B base, Russian example output
- https://huggingface.co/nn-tech/MetalGPT-1/raw/main/config.json — qwen3, hidden 5120, 64 layers (32B-class)
- https://huggingface.co/itpossible/JiuZhou-Instruct-v0.2/raw/main/config.json — mistral, vocab 63872 (expanded)
- https://huggingface.co/itpossible/JiuZhou-base/raw/main/config.json — mistral, vocab 63872
- https://huggingface.co/daven3/k2-v1/raw/main/config.json — llama, hidden 4096, 32 layers (7B)
- https://huggingface.co/daven3/k2-v1/resolve/main/model-00001-of-00003.safetensors — HEAD 200, content-length 4,938,985,248 (~4.9 GB/shard)
- https://huggingface.co/itpossible/JiuZhou-Instruct-v0.2/resolve/main/model-00001-of-00004.safetensors — HEAD 200, content-length 3,895,582,632
- https://huggingface.co/nn-tech/MetalGPT-1/resolve/main/model-00001-of-00014.safetensors — HEAD 200, content-length 4,929,778,304

Papers / abstracts (all 200):
- https://soil.copernicus.org/articles/5/177/2019/ — GeoVec paper, §6.5 + Fig. 7b: slate < phyllite < schist < gneiss < migmatite; 2 PCs = 28.8% variance
- https://api.openalex.org/works/doi:10.1016/j.oregeorev.2025.106638 — GeoMinLM, Ore Geology Reviews 2025, Baichuan-2 base, Yunnan 5.16M-word dataset
- https://api.openalex.org/works/doi:10.1080/17538947.2025.2449708 — JiuZhou, IJDE 2025, 13 citations
- https://api.openalex.org/works/doi:10.48550/arXiv.2306.05064 — K2, WSDM 2024, 233 citations, LLaMA-7B on 5.5B tokens

OSF / Google Drive:
- https://api.osf.io/v2/nodes/4uyeq/files/osfstorage/ — geovec_300d_v1.h5, 468,366,258 bytes
- https://osf.io/download/kt6eu/ — HEAD 200 (vectors downloadable)
- https://drive.google.com/file/d/11NIE0VwzlWrPN_PXyBUlZiAblw69tKY8/view — 200 (GeoMinLM weights link live)

Dead endpoints (verified):
- https://k2.acemap.info — **404** (K2 demo dead)
- https://www.tandfonline.com/doi/full/10.1080/17538947.2025.2449708 — 403 (publisher bot-blocking; abstract verified via OpenAlex instead)

## Predictions

1. Zero of the six domain candidates will be recommended as the orchestrator; a general open LLM wins. (K2 and JiuZhou are runnable but not recommended.)
2. GeoVec's metamorphic-gradient claim survives scrutiny as stated (real, documented, open-access) but is a qualitative nearest-neighbor chain in a 2D projection, not a continuous physical gradient.
3. MetalGPT-1 is killed on three independent grounds — size (32B), language (Russian-only), and license (cc-by-nc-sa-4.0) — any one of which alone would disqualify it.

## Check result

**PASS.** ≥5 distinct fetch-verified URLs: 40+ distinct URLs fetched, all 200 except two verified dead endpoints (k2.acemap.info 404, tandfonline 403 bot-block confirmed via OpenAlex fallback). Every candidate in the cluster (K2, GeoMinLM, JiuZhou, MetalGPT-1, NRCan, GeoVec) has an explicit verdict line in the Verdict table. No retries needed.
