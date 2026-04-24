# Entrepreneur Persona Skill - Test Results

**Date:** 2026-04-13  
**Tester:** Claude (automated workflow trace + script validation)  
**Method:** Traced each SKILL.md workflow against simulated student inputs, verified reference file linkage, and ran `validate_proposal.py` on a generated proposal.

---

## Test Summary

| Test | Workflow | Result | Issues Found |
|------|----------|--------|--------------|
| 1 | Idea Generation | PASS | 1 minor gap |
| 2 | Business Proposal Writing | PASS | 0 |
| 3 | Pitch Deck/Presentation | PASS | 1 minor gap |
| 4 | Pitch Script | PASS | 0 |
| 5 | Idea Refinement/Stress-Test | PASS | 1 minor gap |
| 6 | Validation Script | PASS | 0 |

**Overall: 6/6 PASS - skill is functional and well-structured.**

---

## Test 1: Idea Generation

**Simulated input:** "I want to start a business selling healthy snacks to college students."

**Trace through SKILL.md (lines 49–92):**

| Step | Expected behavior | Present in SKILL.md? | Reference linked? |
|------|-------------------|----------------------|-------------------|
| Problem discovery | Ask who hurts, how often, what they do today | YES (line 53-55) | - |
| Reject vagueness | Demand demographics, behaviors, frequency | YES (line 55) | - |
| Solution framing | One-sentence template | YES (lines 60-62) | - |
| Viability check | 4 criteria (v1 in 90 days, first 10 customers, way to charge, founder connection) | YES (lines 66-69) | - |
| Stop/pivot triggers | 4 kill conditions | YES (lines 71-76) | - |
| Competitive scan | 3-5 alternatives | YES (lines 78-80) | - |
| Enrichment | Cross-check with frameworks | YES (lines 82-92) | `references/idea-validation-frameworks.md` ✓ |

**Verdict: PASS**

**Minor gap:** Step 1 says "Ask the user to describe a frustration" but doesn't explicitly instruct the mentor to *refuse to discuss solutions* until the problem is clear. The persona principles (Principle 1) cover this ("ask who hurts before solutions") but the workflow step could reinforce it more explicitly.

---

## Test 2: Business Proposal Writing

**Simulated input:** "Help me write a business proposal for SnackBox."

**Trace through SKILL.md (lines 97–148):**

| Check | Expected | Present? |
|-------|----------|----------|
| Points to template | `assets/business-proposal-template.md` | YES (line 97) |
| All 7 Clapp sections defined | S1-S4, I1-I4, M1-M5, O1-O3, F1-F5, T1-T2, P1-P3 | YES (lines 99-146) |
| Financial formula enforced | `Units × (Price − COGS) = Gross Profit` | YES (line 133) |
| Page limit enforced | 7-page max, flag filler | YES (line 147) |
| Validation script offered | `scripts/validate_proposal.py` | YES (line 147) |
| Section sub-codes match template | S1-S4, I1-I4, M1A-M5, etc. | YES - exact match |

**Template completeness check (business-proposal-template.md):**

- All 7 sections present with bracketed placeholders ✓
- F4 shows `Units × (Price − COGS) = Gross Profit` formula ✓
- Market sizing has TAM/SAM/SOM with source fields ✓
- Validation evidence field asks for method and n= ✓

**Verdict: PASS - no gaps.**

---

## Test 3: Pitch Deck/Presentation

**Simulated input:** "I need to build a 5-minute pitch deck for the Clapp competition."

**Trace through SKILL.md (lines 150–176):**

| Check | Expected | Present? |
|-------|----------|----------|
| 11-slide structure | Hook through Ask+Close | YES (lines 157-168) |
| Time allocations | Specific seconds per slide, totals ~5:00 | YES |
| Coaching rules | Time it, "so what?" test, 6 lines max, speak to judges, prep Q&A | YES (lines 172-175) |
| References linked | `pitch-patterns.md`, `competition-rubrics.md` | YES (line 152) |
| Q&A prep linked | `judge-question-bank.md` | YES (line 175) |

**Cross-check: pitch-patterns.md alignment:**

- Personal Hook pattern → maps to Slide 1 (Hook) ✓
- Problem-Solution Bridge → maps to Slides 2-3 ✓
- TAM/SAM/SOM Funnel → maps to Slide 4 ✓
- Validation Evidence Hierarchy → maps to Slide 6 ✓
- Use of Funds Specificity → maps to Slide 9 ✓
- Conservative Credibility → maps to Slide 7 (Business Model) ✓

**Cross-check: benchmark-vignettes.md coverage:**

- YC, TechCrunch, MIT $100K, Shark Tank, Hult, Rice patterns all present ✓
- Patterns are structural ("pattern, not copy-paste") ✓

**Verdict: PASS**

**Minor gap:** The slide structure doesn't explicitly mention "demo or physical product" as its own beat, though line 159 says "(demo line if product in hand)" in parentheses. For Shark Tank-style and TechCrunch Disrupt-style pitches where live demos dominate, the skill could provide an alternate slide order. Low priority - the current structure handles 5-minute competition pitches well.

---

## Test 4: Pitch Script

**Simulated input:** "Help me write my spoken pitch script."

**Trace through SKILL.md (lines 179–198):**

| Check | Expected | Present? |
|-------|----------|----------|
| Points to template | `assets/pitch-script-template.md` | YES (line 181) |
| 6-step script process | Draft, read aloud, mark emphasis, transitions, open with story, close with one-liner | YES (lines 185-190) |
| Time target | ~4:30 to leave buffer | YES (line 186) |
| Delivery coaching | Practice Q&A more, know "how do you know" for every claim | YES (lines 194-198) |
| Drill questions listed | Validation, CAC, competitor copies, IP, scaling, unit economics, team | YES (line 197) |

**Template completeness (pitch-script-template.md):**

- All 11 sections match SKILL.md slide structure ✓
- Time allocations per section ✓
- Transition phrases provided ✓
- Q&A reminder at bottom links to judge-question-bank.md ✓
- Marking notation explained (pause, bold = emphasis) ✓

**Verdict: PASS - no gaps.**

---

## Test 5: Idea Refinement / Stress-Test

**Simulated input:** "I have my SnackBox idea pretty developed. Can you stress-test it?"

**Trace through SKILL.md (lines 200–218):**

| Check | Expected | Present? |
|-------|----------|----------|
| Points to canvas | `assets/idea-refinement-canvas.md` | YES (line 202) |
| 5-step refinement protocol | Restate, Judge gauntlet, Weakest link, Prescribe actions, Iterate | YES (lines 206-218) |
| Judge gauntlet uses question bank | "10 hardest from judge-question-bank.md" | YES (line 207) |
| Score answers 1-5 | Explicit scoring | YES (line 207) |
| Domain-specific question routing | Travel/events/hospitality → special category | YES (lines 207-208) |
| Weakest link categories | 7 categories listed | YES (lines 209-216) |
| Prescribe concrete actions | Specific example given | YES (line 217) |
| Iteration loop | Re-run gauntlet on improved areas | YES (line 218) |

**Cross-check: judge-question-bank.md has 50+ questions across 6 categories:**

- Validation & Market (10) ✓
- Business Model & Finance (10) ✓
- Competition & Moat (8) ✓
- Distribution & Scale (7) ✓
- Operations & Risk (7) ✓
- Team (10) ✓

**Verdict: PASS**

**Minor gap:** The refinement protocol says to pick "10 hardest" questions but doesn't specify the distribution across categories. A mentor might pull 8 from Validation and 2 from Team, leaving financials untested. Consider adding: "at least 1 question from each of the 6 categories."

---

## Test 6: Validation Script

**Command (from repo root):** `python3 skills/entrepreneur-persona/scripts/validate_proposal.py test-proposal.md` (or `cd skills/entrepreneur-persona` and run `python3 scripts/validate_proposal.py ../../test-proposal.md`).

**Results:**

```
Business proposal validation checklist
=====================================
  Section 1: OK  (162 words)
  Section 2: OK  (168 words)
  Section 3: OK  (182 words)
  Section 4: OK  (85 words)
  Section 5: OK  (164 words)
  Section 6: OK  (95 words)
  Section 7: OK  (90 words)

Total words (file): 974

Length: no section exceeds the word threshold.

Financial section (Section 5) signals:
  Keyword hits (16): $, assumption, cogs, f1, f2, f3, f4, f5, gross profit, price, projection, revenue, unit, y1, y2, year 2
  OK: Gross-profit style language or formula pattern detected.
```

| Check | Result |
|-------|--------|
| All 7 sections detected | ✓ |
| Word counts reasonable | ✓ (85-182 words per section) |
| No sections over 250-word threshold | ✓ |
| Financial keywords detected (16/17) | ✓ |
| Gross profit formula detected | ✓ |
| Exit code 0 (success) | ✓ |

**Verdict: PASS - script works correctly on skill-compliant proposals.**

---

## Cross-Cutting Checks

### Persona Fidelity (7 Principles)

| Principle | Where enforced in SKILL.md | Reference support |
|-----------|---------------------------|-------------------|
| 1. Problem-first | Lines 34-35, 53-55 | idea-validation-frameworks.md §1, §2 |
| 2. Validation over assumption | Lines 37-38, 207 | idea-validation-frameworks.md §2 (Mom Test) |
| 3. Specificity breeds credibility | Lines 40-41, 55 | pitch-patterns.md §TAM/SAM/SOM |
| 4. Story-problem-solution-traction | Lines 43-44, 157-168 | pitch-patterns.md §Personal Hook, §Problem-Solution Bridge |
| 5. Conservative financial honesty | Lines 46-48, 129-136 | financial-modeling-guide.md §1, §7 |
| 6. Judge empathy | Lines 50-51, 172-175, 207 | competition-rubrics.md, judge-question-bank.md |
| 7. Iterative refinement | Lines 53, 217-218 | idea-refinement-canvas.md |

**All 7 principles have both SKILL.md enforcement AND reference file backing. ✓**

### Progressive Disclosure

| Reference | Linked from SKILL.md? | Content quality |
|-----------|----------------------|-----------------|
| pitch-patterns.md | ✓ (line 14) | 7 patterns + framework citations |
| idea-validation-frameworks.md | ✓ (line 15) | 8 frameworks with templates |
| competition-rubrics.md | ✓ (line 16) | 10-category rubric, 1-5 scale |
| judge-question-bank.md | ✓ (line 17) | 52 questions, 6 categories |
| financial-modeling-guide.md | ✓ (line 18) | 7 sections, formulas + traps |
| benchmark-vignettes.md | ✓ (line 19) | 6 competition archetypes |
| business-proposal-template.md | ✓ (line 20) | 7-section fill-in template |
| pitch-script-template.md | ✓ (line 20) | 11-section with times |
| idea-refinement-canvas.md | ✓ (line 20) | 6-block single-page canvas |

**All 9 files linked and populated. ✓**

### Quality Bar (lines 222-234)

| Quality rule | Testable? | Enforced where? |
|--------------|-----------|-----------------|
| Respectful directness | Persona instruction | Lines 223 |
| Actionable specificity | Persona instruction | Lines 224, 217 |
| Pattern-based examples | Reference linkage | Lines 225 |
| Honest about what's missing | Persona instruction | Lines 226 |
| Treat uncited metrics as hypotheses | Explicit instruction | Lines 230-234 |
| Don't endorse hockey sticks | Explicit instruction | Line 231 |
| Demand provenance | Explicit instruction | Line 232 |

**All quality rules present and actionable. ✓**

---

## Issues Found (3 minor, 0 blocking)

| # | Severity | Workflow | Issue | Suggested Fix |
|---|----------|----------|-------|---------------|
| 1 | Minor | Idea Generation | Step 1 doesn't explicitly say "refuse to discuss solutions until problem is validated" - relies on Principle 1 | Add one line to Step 1: "Do not move to Step 2 until the user has articulated a specific problem with who/frequency/severity." |
| 2 | Minor | Pitch Deck | No alternate slide order for demo-heavy pitches (physical product, live software) | Add a 2-sentence note after slide structure: "For physical products or live demos, expand Slide 3 to 60s and compress Slides 4-5. Demo is the pitch." |
| 3 | Minor | Idea Refinement | Judge gauntlet says "10 hardest" but no category distribution guidance | Add: "Draw at least 1 question from each of the 6 categories; weight remaining 4 toward the venture's weakest areas." |

---

## Conclusion

The skill is **production-ready**. All 5 workflows trace correctly through SKILL.md to their reference files. The validation script works. The 7 persona principles are consistently enforced. The 3 minor gaps are improvements, not bugs - the skill will function correctly without them.

**Recommended next step:** Apply the 3 minor fixes to SKILL.md, then run the full audit prompt (`AUDIT_BENCHMARK_PROMPT.md`) in Cursor Composer for simulation-level testing.
