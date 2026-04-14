# Cursor Composer 2 Prompt: Full Audit, Simulation & Benchmark of the Entrepreneur Persona Skill

## Purpose

You are performing a comprehensive end-to-end audit of the `skills/entrepreneur-persona/` Claude skill. This audit has three phases:

1. **Structural Audit** — Verify the skill conforms to Anthropic's skill specification
2. **Simulation Suite** — Run 12 simulated user sessions end-to-end through every workflow
3. **Benchmark Scoring** — Compare skill outputs against patterns from real winning pitches at major competitions, score gaps, and produce a gap-fix report

The output is a complete audit report with pass/fail checks, simulation transcripts, benchmark scorecards, and a prioritized remediation plan.

---

## PHASE 1: Structural Audit

### 1A. Specification Compliance Checks

Read every file in `skills/entrepreneur-persona/` and verify each item. Output a checklist with PASS/FAIL:

| # | Check | Criteria | Status |
|---|-------|----------|--------|
| 1 | Folder naming | Skill folder `skills/entrepreneur-persona/` — inner name kebab-case, no spaces, no underscores, no capitals | |
| 2 | SKILL.md exists | Exact filename `SKILL.md` (case-sensitive) | |
| 3 | YAML frontmatter delimiters | Opens and closes with `---` | |
| 4 | `name` field | kebab-case, matches folder name, no spaces/capitals | |
| 5 | `description` field | Under 1024 characters; includes WHAT + WHEN + trigger phrases | |
| 6 | No XML tags | No `<` or `>` in frontmatter | |
| 7 | No README.md | No README.md inside the skill folder | |
| 8 | No reserved names | Name doesn't contain "claude" or "anthropic" | |
| 9 | Progressive disclosure | SKILL.md links to `references/` and `assets/` files | |
| 10 | SKILL.md word count | Under 5,000 words | |
| 11 | Description character count | Under 1024 characters | |
| 12 | References linked | All files in `references/` are mentioned in SKILL.md | |
| 13 | Assets linked | All files in `assets/` are mentioned in SKILL.md | |
| 14 | Scripts exist | `scripts/validate_proposal.py` is functional Python | |
| 15 | No broken references | Every `references/X.md` and `assets/X.md` mentioned in SKILL.md actually exists | |

### 1B. Content Quality Checks

| # | Check | Criteria | Status |
|---|-------|----------|--------|
| 16 | Persona consistency | Persona is defined with specific principles, not generic "be helpful" | |
| 17 | Workflow completeness | All 5 workflows present: Ideation, Proposal, Presentation, Transcript, Refinement | |
| 18 | Actionability | Instructions use specific verbs and measurable outputs, not vague guidance | |
| 19 | Framework integration | References Lean Startup, Business Model Canvas, JTBD, Mom Test, Crossing the Chasm | |
| 20 | Competition alignment | Proposal template matches Clapp IDEA Competition format (7 sections) | |
| 21 | Financial rigor | Gross profit formula present; assumptions table template exists | |
| 22 | Judge question coverage | 50+ questions across 6+ categories | |
| 23 | Validation hierarchy | Evidence types ranked from strongest (revenue) to weakest (anecdotes) | |
| 24 | Error handling | Guidance for when user provides incomplete info or unrealistic claims | |
| 25 | Negative triggers | Description or SKILL.md clarifies what's out of scope | |

### 1C. Script Validation

Run the validation script against the business proposal template to confirm it works:

```bash
cd skills/entrepreneur-persona
python3 scripts/validate_proposal.py assets/business-proposal-template.md
```

Record the output. Verify it correctly identifies all 7 sections.

---

## PHASE 2: Simulation Suite (12 End-to-End Scenarios)

For each simulation, you act as both the USER and the SKILL (Claude using the entrepreneur-persona skill from `skills/entrepreneur-persona/`). Generate a realistic multi-turn conversation that exercises the workflow. Then score the skill's output.

### Simulation Scoring Rubric (per simulation)

Score each dimension 1-5:

| Dimension | 1 (Fail) | 3 (Adequate) | 5 (Excellent) |
|-----------|----------|--------------|---------------|
| **Persona consistency** | Generic AI assistant tone | Mostly mentoring but occasional drift | Consistently direct, specific mentor voice throughout |
| **Actionability** | Vague advice ("do research") | Some specific guidance mixed with generic | Every recommendation has who/what/where/when/how |
| **Framework application** | No frameworks referenced | Frameworks mentioned but not applied | Frameworks used as tools on the user's specific case |
| **Competition awareness** | No judge perspective | Occasional judge framing | Consistently frames through "what will judges ask?" |
| **Output quality** | Incomplete or wrong structure | Correct structure with gaps | Publication-ready output matching competition requirements |
| **Iterative depth** | Single pass, no follow-up | One round of refinement | Multiple refinement cycles with escalating specificity |

---

### Simulation 1: Cold Start Ideation — Physical Product (Consumer Health)

**Scenario:** A sophomore at IU says: "I have this idea for a phone accessory that holds your daily medication so you never forget it when you leave the house. Like a pop socket but with a pill compartment."

**Exercise:** Full Workflow 1 (Idea Generation). Walk through all 5 steps. The user should give imperfect initial answers that the skill refines.

**Benchmark match:** This mirrors the "Philly Pop" pitch from the Clapp transcript. Compare skill output against what that team presented and what judges pushed back on (distribution strategy, social stigma, unit economics, patent protection).

**Expected outputs:**

- One-sentence solution framing
- Viability check results (4 filters)
- Competitive landscape (PopSocket, pill cases, reminder apps)
- Enrichment with JTBD and Lean Canvas
- 3 specific next actions

---

### Simulation 2: Cold Start Ideation — Service Business (End-of-Life Planning)

**Scenario:** An MBA student says: "When my grandma died, the funeral planning process was terrible. I want to build an online platform where people pre-plan their cremation and memorial service."

**Exercise:** Full Workflow 1. User references personal pain. Skill should probe market (baby boomers, $3.1B funeral industry), competition (Meadow), pricing ($5,500 base), and distribution challenges (funeral homes resistant to change).

**Benchmark match:** Mirrors the "Mora/Ramora" pitch. Compare against their pitch structure, judge questions about B2C vs B2B, trust-building with funeral homes, and conservative financial projections ($150K Y1, $48K profit).

---

### Simulation 3: Cold Start Ideation — Tech/SaaS (GPU Optimization)

**Scenario:** A CS grad student says: "We've built software that optimizes GPU memory allocation for AI training workloads. We can reduce compute costs by 24%. We have 87 companies using our open-source SDK."

**Exercise:** Full Workflow 1, but the user is further along. Skill should recognize traction, probe monetization (freemium to enterprise), competitive moat (vs Google/Microsoft/Nvidia who own the hardware), and defensibility.

**Benchmark match:** Mirrors the "Deep Variants" pitch. Compare against their handling of: open-source-to-paid conversion, data privacy concerns, the "why won't Nvidia just do this?" question.

---

### Simulation 4: Business Proposal Writing — Graduation Travel Package

**Scenario:** User says: "I need to write a 7-page business proposal for the Clapp IDEA Competition. My business is an all-inclusive graduation weekend travel package for parents visiting IU. We've already sold 14 packages and have 180+ on our waitlist for next year."

**Exercise:** Full Workflow 2. Walk through all 7 sections. The user provides raw data; skill structures it.

**Benchmark match:** Mirrors "Go Grad Travel" pitch. Key benchmarks:

- Opening with personal story (sister's graduation)
- Market sizing (50,000 people congregate, 45,000 need hotels)
- Channel strategy (Meta ads, Facebook parent groups, student reps)
- Conservative revenue ($13K Y1 from 14 customers → $180K potential from waitlist)
- Zero startup costs positioning
- Scalability to other universities

**Evaluate:** Does the skill-generated proposal match the structure, specificity, and judge-readiness of what GoGrad actually presented?

---

### Simulation 5: Business Proposal Writing — Fitness Equipment (B2B)

**Scenario:** "I'm building a cable machine attachment that allows natural range of motion for back training. I have a prototype, biomechanics professors have validated the science, and personal trainers who tested it report better muscle activation."

**Exercise:** Full Workflow 2.

**Benchmark match:** Mirrors "Shapeshifter Solutions." Key benchmarks:

- Scientific validation as competitive moat
- B2B pricing ($100+ profit per unit to gyms)
- 100,000 gym TAM, 50% capture = $3M opportunity
- Manufacturing challenges (need to find manufacturer, ~$10K for first batch)
- Patent strategy discussion
- Durability/liability concerns judges raised

---

### Simulation 6: Pitch Deck Development — Medication Accessory

**Scenario:** Same user from Sim 1, now ready for slides. "I need a 5-minute pitch deck for the Clapp finals."

**Exercise:** Full Workflow 3. Generate the 11-slide structure with content for each slide.

**Benchmark scoring against winning patterns:**

| Element | Benchmark Standard (from top competitions) | Score 1-5 |
|---------|-------------------------------------------|-----------|
| Hook | Personal story connecting founder to problem (Duarte "what is vs could be") | |
| Problem slide | Specific stat + current alternative failure + frequency | |
| Solution demo | Physical product pass-around or video; mechanism clear in 10 sec | |
| Market funnel | TAM→SAM→SOM with cited sources; beachhead named and justified | |
| Competition | 2x2 matrix or landscape showing positioning beyond price | |
| Traction | Method disclosed (n=35 street survey, 85% take daily meds, 71% signed up) | |
| Business model | Unit economics on one slide (cost $X, sell $Y, margin Z%) | |
| GTM phases | 3-phase growth with clear triggers between phases | |
| Use of funds | $ amounts per category tied to milestones | |
| Team | Founder-problem fit + identified gaps + how filling them | |
| Close | Memorable one-liner + specific ask | |
| Time discipline | Total script under 5:00 with section timings | |

---

### Simulation 7: Pitch Transcript — Funeral Pre-Planning Service

**Scenario:** "Write me a full spoken pitch script for Mora, my funeral pre-planning platform. Target time: 4:30."

**Exercise:** Full Workflow 4. Generate complete script with stage directions.

**Benchmark against real Mora transcript patterns:**

- Did it open with personal story (grandma's death)?
- Did it quantify the market ($3.1B, baby boomers control $78T wealth)?
- Did it address competition (Meadow) honestly?
- Did it handle the B2C positioning rationale?
- Did it include the conservative financial framing?
- Timing: does each section fit within the 5-min structure?

---

### Simulation 8: Q&A Preparation — Stress Test

**Scenario:** "I'm presenting my graduation travel business tomorrow. Drill me with the hardest judge questions and coach me on answers."

**Exercise:** Full Workflow 5 (Refinement Protocol). Run the Judge Gauntlet with 10 questions.

**Benchmark against real Clapp Q&A transcript:**
Compare the questions the skill asks against what judges actually asked GoGrad Travel:

- "Is there a deposit?" (cash flow timing)
- "What about transportation costs?" (operational detail)
- "How do you plan to compete if successful?" (moat)
- "What about hotel capacity limits?" (scalability constraint)
- "How much money do you need to break even?" (unit economics)

Score: How many of the real judge questions did the skill anticipate?

---

### Simulation 9: Idea Refinement — Weak Idea Stress Test

**Scenario:** User says: "I want to build an app that reminds people to drink water. There are lots of people who don't drink enough water."

**Exercise:** Workflow 5. The skill should NOT be encouraging here. It should:

1. Identify the idea is commoditized (100+ water reminder apps exist)
2. Probe for differentiation (there likely is none)
3. Score the idea low on the judge gauntlet
4. Either guide toward a pivot or honestly assess viability

**Benchmark:** This tests the skill's ability to be constructively critical, not just supportive. Top mentors in Y Combinator and Techstars are known for killing bad ideas fast. Score whether the skill does this with specificity and offers a path forward.

---

### Simulation 10: Full Pipeline — Idea Through Final Presentation

**Scenario:** User says: "I want to build a platform that helps international students manage their visa documents and travel requirements. I studied abroad and almost missed my visa deadline."

**Exercise:** Run ALL workflows in sequence:

1. Ideation (Workflow 1) → Lean Canvas output
2. Proposal draft (Workflow 2) → 7-section outline
3. Pitch deck (Workflow 3) → 11-slide structure
4. Script (Workflow 4) → Full spoken text with timing
5. Stress test (Workflow 5) → Judge gauntlet + remediation

**Benchmark match:** Mirrors the travel document management pitch from Clapp transcripts. Evaluate full pipeline coherence — does the story stay consistent from Canvas to final script?

---

### Simulation 11: Edge Case — User Pushback and Unrealistic Claims

**Scenario:** User says: "My app will capture 30% of the market in year one. We don't have any competitors. Everyone will want this."

**Exercise:** Test the skill's ability to:

1. Challenge the 30% claim with math
2. Find the hidden competitors the user is ignoring
3. Reframe "everyone" into a beachhead
4. Do this without being condescending

**Benchmark:** Top competition coaches (per SCORE.org, Y Combinator office hours) redirect grandiose claims in 2-3 pointed questions. Score the skill's coaching technique.

---

### Simulation 12: Edge Case — Technical Founder, No Business Sense

**Scenario:** CS student says: "I built this ML model that detects plant diseases from photos with 94% accuracy. It's really cool technology. I want to enter the Clapp competition but I've never written a business plan."

**Exercise:** The skill should:

1. Acknowledge the tech but immediately pivot to "who pays for this?"
2. Guide through customer discovery (farmers? agricultural companies? governments?)
3. Help frame technology as a business, not a research project
4. Generate a first-pass proposal outline using the template

**Benchmark:** Mirrors how NSF I-Corps coaches technical founders — "Get out of the lab." Score whether the skill bridges technical excitement to business viability.

---

## PHASE 3: Benchmark Scorecards

### 3A. Winning Pitch Pattern Database

Build a reference database of patterns from these real competition winners. For each, document the structural elements, timing, and what made them win:

#### Tier 1: Major Competition Winners (research-backed, verified patterns)

**Y COMBINATOR DEMO DAY** (2:30 pitch format — extreme clarity required)

| Winner | Year | Key Winning Pattern | Structural Takeaway |
|--------|------|---------------------|---------------------|
| **Airbnb** | W2009 | Reframed from "air mattresses" to "$26B short-term accommodation market." Led with market size + unit economics, not product. Showed revenue/booking and organic growth in cities with zero marketing. | Market timing + revenue proof beats clever product description |
| **Dropbox** | W2007 | Drew Houston opened with universal pain: "You email yourself a file, wrong version." Then LIVE DEMO — showed syncing working. 75K waitlist as traction. | Demo > slides. Show the product being absurdly simple. |
| **Stripe** | S2010 | Patrick Collison offered to integrate payments into someone's site in 7 lines of code, live. Problem: integration normally takes weeks. | Contrast current pain (weeks) vs solution (seconds) with live proof |
| **Brex** | W2017 | Opened with founder credibility: "Built a payments company in Brazil processing $1B before age 20." Then: startups can't get corporate credit cards. Front-loaded waitlist + revenue ramp. | Lead with founder credibility when it's extraordinary |

**Common YC Demo Day Structure (extracted from multiple batches):**

1. One-sentence company description (5 sec)
2. Problem with emotional/financial hook (15 sec)
3. Solution — what you built (20 sec)
4. **Traction / proof** (30 sec) — THIS gets the most time
5. Market size (15 sec)
6. Business model (15 sec)
7. Team credibility (10 sec)
8. The ask (5 sec)

*Paul Graham and Michael Seibel emphasize: growth rate is the single most compelling element. 15% week-over-week growth beats a beautiful narrative. "The best Demo Day pitches make investors feel like the train is leaving the station and they need to get on."*

---

**TECHCRUNCH DISRUPT BATTLEFIELD** (6-min pitch + 6-min Q&A — rewards showmanship)

| Winner | Year | Key Winning Pattern |
|--------|------|---------------------|
| **Mint.com** | 2007 | "Americans spend 3 hours/month managing finances and still don't know where money goes." Before/after demo (cluttered Quicken vs clean Mint). Acknowledged Wesabe/Quicken competition honestly. 20K beta users. |
| **Fitbit** | 2008 | Held up tiny device: "This knows more about your health than your doctor." Aspirational framing, not problem framing. Created a category. |
| **Dropbox** | 2008 | Full live demo with humor. Audience audibly reacted. Massive waitlist. |

**Battlefield winning structure:**

1. Bold claim or surprising statistic (15-30 sec)
2. Problem dramatization with story/persona (45 sec)
3. **Live product demo (2-2.5 min)** — this is the core
4. Traction metrics (30 sec)
5. Market + business model (45 sec)
6. Team + vision (30 sec)

---

**MIT $100K** (10-15 min pitch, heavy Q&A — emphasizes technical defensibility)

| Winner | Key Pattern |
|--------|-------------|
| **Akamai Technologies** (1999) | Mathematical proof of solution. Showed *inevitability* of the problem (internet traffic curves). Positioned as only architecturally sound approach. |
| **HubSpot** (2006 ecosystem) | Coined "inbound marketing," defined a category, positioned as category leader. |

**MIT $100K structure:**

1. Team credentials + why uniquely positioned (1-2 min)
2. Problem with quantified market failure (2 min)
3. Technical solution with defensibility explanation (3-4 min)
4. Business model + GTM (2 min)
5. Financial projections with clear assumptions (2 min)
6. Competitive landscape — 2x2 matrix (1 min)
7. Ask + use of funds (1 min)

---

**RICE BUSINESS PLAN COMPETITION** ($1.5M+ in prizes — investment-readiness focus)

Winners present detailed financial models: not just revenue projections but cap table structures, exit scenarios, and comparable transaction analyses. Pattern: "This market spends $X solving this problem badly. Our science reduces cost by Y% with Z switching cost." Winners address top 3 risks proactively.

---

**HULT PRIZE** ($1M — social enterprise, 8-10 min)

| Winner | Key Pattern |
|--------|-------------|
| **Rumi Spice** (2017) | Veterans built saffron supply chain in Afghanistan. "We saw farmers forced to grow opium because they had no market access for legal crops." Emotional narrative inseparable from business case. |
| **Aspire Food Group** (2013) | "2 billion people already eat insects. We're not changing behavior; we're building supply chain for existing demand." Reframed disgust into opportunity. |

Hult judges penalize NGO-sounding pitches. Winners frame social impact as a *market inefficiency they exploit*.

---

**SHARK TANK** (5-15 min pitch + negotiation)

| Winner | Key Pattern |
|--------|-------------|
| **Bombas Socks** | "#1 most requested item in homeless shelters = socks." Then immediately: revenue, growth, margins. One-for-one as *marketing engine*, not charity. |
| **Scrub Daddy** | Live physical demo: changed sponge texture in hot vs cold water. Let product sell itself. Pitch time spent on financials + retail traction. |
| **Ring** (Doorbot) | Personal story (missed delivery). Product demo. Showed retail partnerships already secured. Created FOMO — company would succeed without shark money. |

**Anti-patterns that lose on Shark Tank:**

- Overvaluation without revenue
- Too long on backstory before showing product
- Not knowing your numbers (COGS, CAC, LTV)
- "There's no competition"

---

| Competition | Winner | Year | Key Winning Pattern |
|-------------|--------|------|---------------------|
| **Y Combinator Demo Day** | Airbnb | 2009 | Market timing + revenue proof. Led with $26B market, not product. |
| **Y Combinator Demo Day** | Dropbox | 2007 | Live demo + 75K waitlist. Made complex tech feel like solving everyday annoyance. |
| **Y Combinator Demo Day** | Stripe | 2010 | "7 lines of code." Contrast: weeks of integration vs. instant. |
| **TechCrunch Disrupt** | Mint.com | 2007 | Before/after demo. Honest competitive landscape. 20K beta users. |
| **MIT $100K** | Akamai | 1999 | Mathematical proof of inevitability. Only sound architecture. |
| **Hult Prize** | Aspire Food Group | 2013 | Reframed disgust into demand. "2B people already eat insects." |
| **Shark Tank** | Scrub Daddy | 2012 | Physical demo that wows. Crystal clear unit economics ($1 cost, $4 wholesale). |
| **Shark Tank** | Ring | 2013 | Personal story + retail partnerships. Created investor FOMO. |
| **Rice Business Plan** | Various | Annual | Financial rigor dominates. CAC/LTV in Q&A. Conservative > optimistic. |

#### Tier 2: University Competition Patterns (synthesized)

| Pattern Cluster | What Winners Do | What Losers Do |
|-----------------|-----------------|----------------|
| **Opening** | Personal story (2-3 sentences) connecting founder to pain | Generic market stat with no personal stake |
| **Problem** | Specific person, specific moment, measurable cost | Abstract problem affecting "everyone" |
| **Market** | Bottom-up sizing from known data + beachhead | "If we capture just 1% of a $X billion market" |
| **Competition** | Honest landscape with clear wedge | "We have no competitors" |
| **Traction** | Method + n + result + next test | "People love it" (no method, no n) |
| **Financials** | Assumptions stated, conservative base case | Hockey stick with no driver logic |
| **Team** | Relevant experience + identified gaps + plan to fill | "We're passionate" |
| **Q&A** | Direct answers, admits unknowns, redirects to strength | Defensive, contradictory, or evasive |
| **Close** | Specific ask tied to milestones | Vague "we need funding" |
| **Time** | Under limit with poise | Rushed/overtime, reading slides |

#### Tier 3: Investor Pitch Structure Benchmarks

| Framework | Structure | Time Split |
|-----------|-----------|------------|
| **Sequoia Capital Template** | Problem → Solution → Why Now → Market Size → Product → Team → Financials → Ask | Even across all, heavy on Why Now |
| **Guy Kawasaki 10/20/30** | 10 slides, 20 min, 30pt font. Title → Problem → Solution → Business Model → Go-to-Market → Competitive Analysis → Team → Projections → Status → Timeline | 2 min/slide |
| **Dave McClure (500 Startups)** | Elevator → Problem → Solution → Market → Revenue Model → Traction → Team → Financials → Competition → Ask | Emphasis on traction and revenue |
| **Peter Thiel Framework** | What secret do you know? → Monopoly theory → Why now? → Why you? | Emphasis on insight/secret |
| **First Round Capital** | 1 sentence each: Problem, Insight, Solution, Traction, Why Now, Team, Ask | Extreme brevity |

---

### 3B. Benchmark Scoring Matrix

For each simulation (1-12), score the skill output against benchmarks:

```
BENCHMARK SCORECARD — Simulation [N]: [Name]
═══════════════════════════════════════════════════

STRUCTURAL ALIGNMENT (vs Clapp Competition Requirements)
├── All 7 sections present and within page limits    [__/5]
├── Financial formula correctly applied               [__/5]
├── Challenges + mitigation in every section          [__/5]
└── Competition format compliance                     [__/5]
                                          Subtotal:   [__/20]

PITCH QUALITY (vs Winning Pitch Patterns)
├── Personal hook strength (Duarte standard)          [__/5]
├── Problem specificity (who/when/cost/frequency)     [__/5]
├── TAM/SAM/SOM rigor (sourced, bottom-up check)      [__/5]
├── Competitive honesty (no "no competitors")          [__/5]
├── Validation evidence quality (hierarchy position)   [__/5]
├── Conservative financial framing                     [__/5]
├── Growth phase logic (beachhead → expand → scale)    [__/5]
└── Use of funds specificity ($ + milestone)           [__/5]
                                          Subtotal:   [__/40]

MENTORING QUALITY (vs Top Accelerator Coaching)
├── Socratic questioning depth                         [__/5]
├── Framework application (not lecturing)              [__/5]
├── Constructive criticism when needed                 [__/5]
├── Specificity of next-action prescriptions           [__/5]
├── Judge empathy / Q&A preparation                    [__/5]
└── Iteration coaching (return-and-improve loop)       [__/5]
                                          Subtotal:   [__/30]

PERSONA FIDELITY
├── Consistent mentor voice throughout                 [__/5]
├── Never generic / always specific to their case      [__/5]
                                          Subtotal:   [__/10]

═══════════════════════════════════════════════════
TOTAL:                                                [__/100]

GRADE: [A/B/C/D/F based on: 90+=A, 80+=B, 70+=C, 60+=D, <60=F]
```

---

### 3C. Cross-Simulation Gap Analysis

After scoring all 12 simulations, produce a gap analysis table:

| Dimension | Avg Score | Weakest Simulation | Root Cause | Fix Priority |
|-----------|-----------|-------------------|------------|--------------|
| Structural alignment | /20 | Sim # | [Why] | P1/P2/P3 |
| Pitch quality | /40 | Sim # | [Why] | P1/P2/P3 |
| Mentoring quality | /30 | Sim # | [Why] | P1/P2/P3 |
| Persona fidelity | /10 | Sim # | [Why] | P1/P2/P3 |

---

## PHASE 4: Remediation Plan

Based on the audit, simulations, and benchmarks, produce:

### 4A. Critical Fixes (P1 — blocks competition readiness)

For each P1 issue:

- **File to edit:** exact path
- **Current state:** what's wrong (quote the text)
- **Target state:** what it should say
- **Benchmark justification:** which winning pitch pattern this aligns with

### 4B. Enhancement Opportunities (P2 — improves quality)

For each P2:

- What to add/change
- Which simulation exposed the gap
- Expected score improvement

### 4C. Nice-to-Haves (P3 — polish)

Quick wins for completeness.

---

## PHASE 5: Regression Test Suite

After fixes, produce a minimal test suite of 5 prompts that should be re-run to confirm:

```yaml
tests:
  - name: "Trigger on obvious"
    input: "Help me pitch my startup idea for a meditation app"
    expect: "Skill loads; asks about problem, not solution first"
    
  - name: "Trigger on paraphrase"
    input: "I'm entering a business plan competition at my university"
    expect: "Skill loads; asks about the competition format and idea"
    
  - name: "No trigger on unrelated"
    input: "Write a Python function to sort a list"
    expect: "Skill does NOT load"
    
  - name: "Financial rigor"
    input: "My product costs $5 to make and I'll sell it for $25"
    expect: "Skill applies Units*(Price-COGS) formula; asks for unit assumptions and Y1/Y2 projections"
    
  - name: "Constructive challenge"
    input: "We have no competitors and will capture 50% of the market"
    expect: "Skill challenges both claims with specific questions; reframes toward beachhead"
```

---

## Execution Instructions for Cursor Composer 2

1. **Read all files** in `skills/entrepreneur-persona/` (SKILL.md, all references, all assets, scripts)
2. **Run Phase 1** — output the full structural checklist
3. **Run Phase 2** — simulate all 12 conversations, scoring each
4. **Run Phase 3** — compile benchmark scorecards and gap analysis
5. **Run Phase 4** — write the remediation plan with exact file edits
6. **Run Phase 5** — output the regression test suite
7. **Write the final report** to `skills/entrepreneur-persona/AUDIT_REPORT.md` (this file is for development use, not part of the distributed skill runtime)

### Output Format

The final `AUDIT_REPORT.md` should contain:

- Executive summary (5 lines: overall grade, top 3 strengths, top 3 gaps)
- Phase 1 checklist (table)
- Phase 2 simulation scores (12 scorecards)
- Phase 3 benchmark comparison (cross-sim gap analysis)
- Phase 4 remediation plan (prioritized)
- Phase 5 regression tests (YAML block)
- Appendix: winning pitch pattern database for future reference
