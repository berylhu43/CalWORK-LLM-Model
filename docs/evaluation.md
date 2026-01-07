# Prompt Test Results

This document evaluates the performance of **Mistral:7B** and **GPT-3.5-Turbo** under identical prompt conditions.

The purpose of these tests is to examine model behavior in a retrieval-augmented policy analysis setting, focusing on:
- Faithfulness to retrieved evidence
- Ability to summarize temporal and subgroup trends
- Clarity and interpretability of generated responses

Rather than optimizing for benchmark scores, this evaluation emphasizes qualitative differences that are relevant for real-world policy analysis workflows.

## Prompt 1: Trend Analysis — Reentry Rate Over Time (Orange County)

**Prompt**  

> Are there any trends in reentry rate over time in Orange County?
---
### Model A: Ollama (Local)
- Embedding model: BAAI/bge-m3
- LLM: Mistral:7B
- Execution time: ~80 seconds

**Summary of Response**

The model identifies an overall increasing trend in the program reentry rate in Orange County, with a peak in Q4 2019 and a notable decline in Q2 2020. It further distinguishes between different reentry definitions (overall reentries vs. reentries after exit with earnings) and highlights that trends may differ across subgroups.

Notably, the model explicitly flags **gender heterogeneity**, pointing out that reentry rates for male participants exhibit a decreasing trend over time, contrasting with the overall county-level pattern.

---

### Model B: OpenAI

- **Embedding model:** text-embedding-3-small  
- **LLM:** GPT-3.5-Turbo  
- **Execution time:** ~28 seconds  

**Summary of response**

The model reports a downward trend in program reentry rates between Q4 2019 and Q3 2020. The response focuses primarily on the aggregate county-level trend and does not further explore subgroup-level variation or multiple reentry definitions.

---

### Comparative Observations

- **Depth of analysis**  
  Mistral:7B provides a more detailed and structured analysis, distinguishing between multiple reentry metrics and identifying subgroup-level differences (e.g., gender-specific trends). GPT-3.5-Turbo offers a concise summary but remains focused on a single aggregate trend.

- **Sensitivity to heterogeneity**  
  Only the local Mistral model explicitly acknowledges that trends may differ across demographic subgroups, which is particularly relevant for policy analysis.

- **Latency trade-off**  
  GPT-3.5-Turbo produces responses significantly faster, while Mistral:7B trades latency for richer contextualization and interpretability.

---

### Takeaway

For exploratory policy analysis where subgroup heterogeneity and nuanced interpretation are important, the local Mistral-based pipeline appears more informative. However, GPT-3.5-Turbo may be preferable in time-sensitive settings where a high-level summary is sufficient.

## Prompt 2: Employment Barriers — Fresno County (Past Three Years)

**Prompt**

> In Fresno County, what are the most frequently cited employment barriers over the last three years?

---

### Model A: Ollama (Local)

- **Embedding model:** BAAI/bge-m3  
- **LLM:** Mistral:7B  
- **Execution time:** ~80 seconds  

**Summary of response**

The model identifies a set of structural and demographic employment barriers in Fresno County that have persisted over the past three years. These barriers are largely driven by labor market composition, gender disparities, and infrastructure constraints.

Key findings include limited income growth opportunities in Fresno’s dominant employment sectors (e.g., agriculture, personal care, fast food), significant public transportation gaps affecting rural residents, and pronounced gender-based wage disparities within the CalWORKs population. The model further highlights challenges in facilitating upward mobility from entry-level positions and encouraging female participants to enter male-dominated fields with higher earning potential.

The analysis also contextualizes these barriers within recent economic shocks, noting a temporary decline in employment rates during the COVID-19 pandemic followed by a rebound that exceeded statewide averages.

---

### Model B: OpenAI

- **Embedding model:** text-embedding-3-small  
- **LLM:** GPT-3.5-Turbo  
- **Execution time:** ~15 seconds  

**Summary of response**

The model highlights several core employment barriers in Fresno County, including gender concentration in low-growth occupations, limited opportunities for income advancement, challenges in transitioning from entry-level positions to higher-paying roles, and the lingering impacts of the COVID-19 pandemic. It also notes broader socioeconomic constraints such as high poverty and unemployment rates.

While the response captures the main themes present in the source documents, it presents them in a more condensed form and does not explicitly distinguish between structural barriers and demographic dynamics.

---

### Comparative Observations

- **Analytical depth**  
  Mistral:7B provides a more comprehensive and contextualized analysis, linking employment barriers to sectoral composition, gender wage gaps, transportation access, and post-pandemic recovery trends. GPT-3.5-Turbo offers a succinct thematic summary with less elaboration on causal mechanisms.

- **Policy relevance**  
  The local model explicitly frames employment barriers in ways that align with workforce development and gender equity policy considerations, such as occupational segregation and advancement pathways. The OpenAI model captures these issues but with less emphasis on policy implications.

- **Latency vs. richness**  
  GPT-3.5-Turbo delivers results significantly faster, while Mistral:7B trades speed for richer interpretation and cross-sectional synthesis.

---

### Takeaway

For policy analysis focused on diagnosing structural employment barriers and informing targeted workforce interventions, the Mistral-based local pipeline demonstrates stronger interpretive value. However, GPT-3.5-Turbo may be sufficient for rapid, high-level assessments where detailed contextualization is not required.

## Prompt 3: Cross-County Comparison — Reentry Rates in Humboldt vs. Shasta

**Prompt**

> Compare the reentry rate reported in Humboldt and Shasta counties.

---

### Model A: Ollama (Local)

- **Embedding model:** BAAI/bge-m3  
- **LLM:** Mistral:7B  
- **Execution time:** ~65 seconds  

**Summary of response**

The model provides a detailed comparative analysis of program reentry rates between Humboldt and Shasta counties, highlighting both overall trends and subgroup disparities.

Overall, Shasta County consistently exhibited **lower program reentry rates** than Humboldt County from Q1 2020 through the most recent available data, with the exception of a temporary reversal in Q2 2020 when both counties experienced pandemic-related disruptions. Shasta County also outperformed statewide averages, particularly for reentries after exits with earnings, which the model attributes to early adoption of the CalWORKs 2.0 framework and proactive barrier identification.

In contrast, Humboldt County demonstrated an **upward trend in reentry rates** over the same period. This increase was especially pronounced among males, whose reentry rate rose from approximately 4.3% to 10.2%, while female reentry rates increased more modestly (from 11.8% to 13.1%). Gender disparities were present in both counties but manifested differently: males had lower reentry rates than females in Shasta County, while in Humboldt County females had higher rates in three out of four quarters.

The model also notes data limitations. Race-based disparities could not be assessed for Shasta County due to data de-identification, whereas Humboldt County data indicated rising reentry rates across demographic subgroups.

---

### Model B: OpenAI

- **Embedding model:** text-embedding-3-small  
- **LLM:** GPT-3.5-Turbo  
- **Execution time:** ~13 seconds  

**Summary of response**

The model reports that both Humboldt and Shasta counties generally experienced reentry rates below statewide averages. Humboldt County showed higher reentry rates for females than males in most quarters and an overall increase in reentry rates over time, particularly for males. Shasta County displayed lower average reentry rates but greater short-term fluctuations, which may reflect differences in business practices rather than broader economic conditions.

The response focuses on high-level patterns and does not extensively explore policy explanations or institutional factors behind the observed differences.

---

### Comparative Observations

- **Depth of comparison**  
  Mistral:7B offers a multi-dimensional comparison that integrates temporal trends, gender disparities, policy context, and data limitations. GPT-3.5-Turbo captures the main directional differences but remains largely descriptive.

- **Policy interpretation**  
  The local model explicitly connects Shasta County’s lower reentry rates to programmatic choices (e.g., CalWORKs 2.0 adoption), whereas the OpenAI model does not attribute outcomes to specific institutional factors.

- **Handling of data constraints**  
  Mistral:7B explicitly acknowledges data de-identification issues and their implications for racial subgroup analysis, a nuance absent from the GPT-3.5-Turbo response.

- **Latency vs. analytical richness**  
  GPT-3.5-Turbo provides results substantially faster, while Mistral:7B trades speed for deeper cross-county synthesis and interpretability.

---

### Takeaway

For comparative policy analysis across counties, the Mistral-based local pipeline demonstrates superior analytical depth and contextual awareness, particularly in explaining *why* differences in reentry rates may exist. GPT-3.5-Turbo remains useful for rapid comparative summaries but is less effective for nuanced policy evaluation.

## Prompt 4: Thematic Analysis — Transportation as a Barrier to Employment

**Prompt**

> Which counties mention transportation as a barrier to employment, and how is it described?

---

### Model A: Ollama (Local)

- **Embedding model:** BAAI/bge-m3  
- **LLM:** Mistral:7B  
- **Execution time:** ~65 seconds  

**Summary of response**

The model identifies transportation as a recurring employment barrier across multiple predominantly rural counties, including **Lassen, Mariposa, Colusa, Tuolumne, and Modoc**. In these counties, transportation challenges are consistently described as structural rather than individual-level issues.

Common themes include **limited or nonexistent public transportation systems**, large geographic service areas, and lack of access to private vehicles. These constraints hinder residents’ ability to commute to work, attend job interviews, access childcare, and participate in required CalWORKs activities. The barrier is particularly acute in remote or rural regions where only one or two transit routes serve the entire county, or where no formal transit system exists at all.

Several counties also link transportation barriers to **broader labor market constraints**. In Mariposa and Lassen Counties, seasonal employment—particularly in tourism or public-sector-dominated economies—exacerbates transportation challenges by creating unstable job availability. In Colusa County, inadequate transportation infrastructure compounds a **skill mismatch problem**, limiting workers’ ability to reach the few available non-agricultural jobs. Tuolumne County explicitly identifies lack of transportation as the *primary* barrier to sustaining employment, even when job readiness and subsidized employment programs are available.

The model also notes proposed mitigation strategies discussed in county reports, such as transportation reimbursements or gas cards, but emphasizes that many transportation challenges fall outside county control due to geographic and infrastructure limitations.

---

### Model B: OpenAI

- **Embedding model:** text-embedding-3-small  
- **LLM:** GPT-3.5-Turbo  
- **Execution time:** ~10 seconds  

**Summary of response**

The model reports that transportation is cited as a barrier to employment in **Sierra, Tuolumne, Colusa, and Lassen Counties**. The primary issue identified is the lack of reliable transportation in remote or rural areas, which limits individuals’ ability to access and maintain employment. The response highlights recommendations such as providing gas cards or transportation assistance but offers less detail on how transportation barriers interact with local labor markets or demographic factors.

---

### Comparative Observations

- **Breadth of coverage**  
  Mistral:7B identifies a broader set of counties and captures transportation barriers across multiple report sections, including community needs assessments, partner feedback, and service delivery evaluations. GPT-3.5-Turbo identifies fewer counties and focuses primarily on partner-reported barriers.

- **Thematic depth**  
  The local model synthesizes transportation barriers as part of a larger structural pattern affecting rural employment, linking transportation limitations to seasonal labor markets, skill mismatches, and childcare access. The OpenAI model provides a concise but less integrated thematic summary.

- **Policy relevance**  
  Mistral:7B more clearly distinguishes between barriers that counties can mitigate (e.g., reimbursements) and those rooted in infrastructure and geography, which has direct implications for policy design and expectations.

- **Latency vs. analytical richness**  
  GPT-3.5-Turbo delivers results rapidly, while Mistral:7B prioritizes interpretive depth and cross-county synthesis at the cost of longer execution time.

---

### Takeaway

For thematic policy questions that require identifying recurring structural barriers across jurisdictions, the Mistral-based local pipeline demonstrates stronger performance in synthesizing context, explaining mechanisms, and surfacing policy-relevant patterns. GPT-3.5-Turbo remains effective for quick thematic identification but provides less insight into how and why transportation functions as a persistent employment barrier across counties.

## Prompt 5: Irrelevant / Out-of-Scope Question Handling

**Prompt**

> What's the best-selling product in McDonald's?

---

### Model A: Ollama (Local)

- **Embedding model:** BAAI/bge-m3  
- **LLM:** Mistral:7B  
- **Execution time:** ~65 seconds  

**Model behavior**

The model correctly identifies that the question is **out of scope** relative to the provided document corpus. It explicitly states that the retrieved context does not contain any information related to McDonald’s sales data or best-selling products and therefore declines to generate a substantive answer.

Instead of hallucinating an answer, the model grounds its response in the absence of relevant evidence, referencing unrelated county-level Cal-CSA excerpts to demonstrate that no supporting material exists within the retrieved documents.

This behavior indicates successful **context-bound reasoning** and effective hallucination avoidance.

---

### Model B: OpenAI

- **Embedding model:** text-embedding-3-small  
- **LLM:** GPT-3.5-Turbo  
- **Execution time:** ~10 seconds  

**Model behavior**

The model similarly refuses to answer the question, noting that the provided context does not include information about McDonald’s products or sales. The response is concise and clearly communicates that the question cannot be answered based on the available documents.

---

### Comparative Observations

- **Hallucination avoidance**  
  Both models successfully avoid fabricating answers when the query is unrelated to the document corpus, demonstrating robust grounding behavior.

- **Transparency of reasoning**  
  Mistral:7B provides a more explicit explanation by referencing retrieved but irrelevant excerpts, making the absence of relevant evidence visible to the user. GPT-3.5-Turbo offers a shorter refusal without contextual elaboration.

- **Policy relevance**  
  For government and policy-oriented applications, the ability to decline irrelevant questions is critical to preventing misinformation. Both systems demonstrate acceptable behavior, with the local model offering stronger traceability.

- **Latency trade-off**  
  GPT-3.5-Turbo responds significantly faster, while the local pipeline prioritizes interpretability over speed.

---

### Takeaway

This test demonstrates that both the local and cloud-based systems are capable of **recognizing and safely handling irrelevant or out-of-domain questions**. Such behavior is essential in policy analysis settings, where hallucinated responses could lead to incorrect conclusions or misuse of data. The local Mistral-based system provides additional transparency at the cost of increased response time.

## Prompt 6: Non-existent / Out-of-Scope Entity (Geographic Mismatch)

**Prompt**

> Why has the employment status decreased in Chicago in recent years?

---

### Model A: Ollama (Local)

- **Embedding model:** BAAI/bge-m3  
- **LLM:** Mistral:7B  
- **Execution time:** ~65 seconds  

**Model behavior**

The model correctly recognizes that **Chicago is not part of the California county–level Cal-CSA / Cal-OAR corpus**. It explicitly states that the provided context does not contain information about Chicago and therefore cannot directly answer the question.

Instead of hallucinating Chicago-specific explanations, the model:
- Clearly flags the **geographic mismatch**
- Avoids fabricating city-level facts
- Provides **general employment decline mechanisms** (e.g., seasonal employment, COVID-19 unemployment benefits, resource constraints) while labeling them as contextual insights rather than direct answers

This demonstrates **partial answer restraint**: the model distinguishes between *explaining general patterns* and *answering the specific query*, while keeping the boundary explicit.

---

### Model B: OpenAI

- **Embedding model:** text-embedding-3-small  
- **LLM:** GPT-3.5-Turbo  
- **Execution time:** ~7 seconds  

**Model behavior**

The model immediately rejects the question, stating that Chicago is not mentioned in the provided context. The response is concise and avoids extrapolation or indirect reasoning based on unrelated counties.

---

### Comparative Observations

- **Entity grounding**
  Both models correctly identify that Chicago is outside the document scope, preventing geographic hallucination.

- **Response strategy**
  - *Mistral:7B* provides a cautious, explanatory fallback by discussing general factors observed in California counties, while clearly stating the limitation.
  - *GPT-3.5-Turbo* provides a stricter refusal without additional contextual interpretation.

- **Policy analysis implications**
  In policy and government settings, extrapolating county-level evidence to unrelated cities can be misleading. Both systems demonstrate safe behavior, with the local model offering more interpretability and educational context.

- **Latency**
  The cloud model responds significantly faster, while the local model trades speed for richer explanation.

---

### Takeaway

This test highlights the system’s ability to **detect non-existent or incompatible entities** and avoid drawing unsupported conclusions. Robust geographic scope validation is critical in policy analysis tools, where misapplied evidence could result in incorrect policy insights. Both implementations demonstrate acceptable safeguards, with different trade-offs between brevity and transparency.

## Overall Evaluation Summary

This evaluation compares a **local RAG pipeline based on Mistral:7B (via Ollama)** with a **cloud-based GPT-3.5-Turbo pipeline**, focusing on qualitative behaviors that are critical for real-world policy analysis rather than benchmark accuracy alone.

Across six prompt categories—trend analysis, barrier identification, cross-county comparison, thematic synthesis, irrelevant question handling, and non-existent entity detection—the two systems exhibit clear and consistent differences in analytical style, depth, and safeguards.

### Key Findings

1. **Analytical Depth and Interpretability**  
   The Mistral-based local pipeline consistently produces richer, more structured analyses. It distinguishes between multiple metric definitions, acknowledges subgroup heterogeneity, integrates institutional or programmatic context, and explicitly discusses data limitations (e.g., de-identification constraints). These behaviors are especially valuable in policy settings where *why* a pattern exists is often as important as *what* the pattern is.


2. **Faithfulness to Retrieved Evidence**  
   Both systems generally remain grounded in retrieved documents. However, the local pipeline more frequently makes the reasoning process explicit by referencing the absence, scope, or limitations of available evidence. This transparency improves trust and auditability in government and policy workflows.


3. **Handling of Out-of-Scope and Invalid Queries**  
   Both models successfully avoid hallucination when faced with irrelevant questions or non-existent entities. Notably:
   - GPT-3.5-Turbo tends toward **strict refusal**, clearly declining to answer when information is missing.
   - Mistral:7B demonstrates **partial answer restraint**, sometimes offering general contextual explanations while clearly flagging that the specific query cannot be answered from the corpus.

   In policy analysis contexts, this softer fallback behavior may be pedagogically useful but must be carefully governed to avoid misinterpretation.


4. **Thematic and Cross-Document Synthesis**  
   For prompts requiring synthesis across multiple counties or reports (e.g., transportation as an employment barrier), the local model demonstrates stronger ability to surface recurring structural themes, link barriers to geography and labor market composition, and distinguish between mitigable and non-mitigable constraints. The cloud model captures high-level themes efficiently but with less integration across documents.


5. **Latency and Practical Trade-offs**  
   GPT-3.5-Turbo consistently responds an order of magnitude faster than the local pipeline. This makes it well-suited for rapid, high-level summaries or interactive use cases. In contrast, the Mistral-based pipeline prioritizes interpretive richness and transparency at the cost of longer execution times.

### Implications for Policy Analysis Workflows

The results suggest a clear trade-off:

- **Local Mistral-based RAG systems** are better suited for exploratory analysis, diagnostic work, and settings where interpretability, subgroup sensitivity, and evidence traceability are paramount.
- **Cloud-based GPT-3.5-Turbo systems** perform well for fast, surface-level assessments and scenarios where concise summaries are sufficient.

Rather than viewing these systems as substitutes, they may be most effective when used **complementarily**—for example, leveraging cloud models for rapid triage and local models for in-depth policy investigation and validation.

### Conclusion

Overall, this evaluation demonstrates that qualitative behaviors—such as scope awareness, evidence grounding, heterogeneity sensitivity, and hallucination avoidance—are as critical as raw performance in policy-oriented RAG applications. The Mistral-based local pipeline shows strong alignment with the interpretive and accountability needs of policy analysis, while GPT-3.5-Turbo offers substantial advantages in speed and simplicity. Future system design should explicitly account for these trade-offs based on the intended decision-making context.