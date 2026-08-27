# MultiMind Platform Torture Benchmark v1

## Purpose

This repository is an isolated benchmark for evaluating future presentation
platforms for MultiMind.

It is NOT the production MultiMind repository.

The goal is not to produce a generic dashboard.

The goal is to determine whether a candidate platform can support a highly
art-directed, professional, responsive, material-rich application without
forcing MultiMind back into a fixed framework visual identity.

A candidate is allowed to fail.

`NO_MIGRATION_TARGET_APPROVED` is a valid outcome.

---

# 1. Candidate Platforms

Implement the benchmark independently for:

1. FastHTML
2. Reflex
3. SvelteKit + FastAPI

Each platform must receive the SAME functional requirements and visual benchmark.

Do not reuse implementation code across frameworks in a way that hides the
actual framework cost.

---

# 2. Core Evaluation Principle

The framework must adapt to MultiMind.

MultiMind must NOT be simplified to fit the framework.

The benchmark explicitly rejects:

- generic SaaS templates;
- fixed left-sidebar dashboard morphology;
- "same cards, different colors";
- desktop layouts merely stacked vertically on mobile;
- framework-default visual fingerprints;
- material used only as decorative images inside cards;
- unreadable typography for the sake of visual style;
- full page reloads for presentation changes;
- loss of application/session state during visual switching;
- brittle dependence on undocumented internal DOM selectors;
- excessive framework escape-hatch usage that defeats the reason for choosing
  the framework.

---

# 3. Actual-Web Reference Benchmarks

Use these four real-world web references as capability benchmarks.

Do NOT clone the complete websites.

Create one representative mini vertical-slice proof for each reference.

The goal is to prove that the framework can express the relevant visual and
interaction language.

## Reference A — Arknights Global

Primary test:

- layered visual materials;
- strong art direction;
- non-generic typography;
- interactive loading;
- scroll choreography;
- motion;
- transitions;
- responsive identity.

Reference:
https://www.arknights.global/

## Reference B — Noomo Labs / Agency-style interaction benchmark

Primary test:

- unusual interaction;
- scroll-linked motion;
- 3D or layered motion where appropriate;
- interactive composition;
- mobile-specific choreography;
- non-standard navigation behavior.

## Reference C — Dioriviera-style luxury/material benchmark

Primary test:

- imagery used as composition, not card decoration;
- premium spacing;
- material layering;
- strong typography;
- restrained but highly polished presentation;
- responsive art direction;
- proof that visual sophistication does not require visual clutter.

## Reference D — Viens-là-style typography / navigation benchmark

Primary test:

- typography-led composition;
- unusual navigation;
- horizontal/vertical presentation behavior where appropriate;
- microinteractions;
- cursor/pointer feedback where relevant;
- transitions;
- deliberate editorial layout.

---

# 4. Reference Parity Floor

Reproduction is NOT considered an achievement.

It is the minimum capability floor.

For each mini reference proof:

- preserve the relevant visual language;
- preserve the relevant interaction behavior;
- preserve the relevant material behavior;
- preserve responsive intent;
- preserve readability;
- avoid replacing difficult behavior with generic cards, gradients, or fade-ins.

A proper reproduction receives only:

`REFERENCE_PARITY = MINIMUM_PASS`

If the framework cannot approach the benchmark behavior without major compromise:

`REFERENCE_PARITY = FAIL`

A candidate that repeatedly fails reference parity may be recommended for DROP.

---

# 5. Material-First Requirement

The platform must support materials as first-class presentation elements.

Supported proof should include several of:

- PNG / JPG;
- GIF;
- animated WebP;
- animated AVIF where appropriate;
- SVG;
- SVG animation;
- Lottie;
- Rive;
- WebM / MP4;
- textures;
- patterns;
- masks;
- layered images;
- foreground/background assets;
- overlays;
- clipped or irregular imagery;
- custom fonts / web fonts.

Materials must be usable as:

- full-bleed background;
- foreground visual element;
- overlay;
- mask;
- texture;
- pattern;
- navigation treatment;
- responsive material;
- animated ambient layer;
- loading material;
- section transition material.

Do not merely place images inside generic cards.

---

# 6. Material-over-Code Efficiency

Prefer a reusable visual asset over unnecessary custom animation logic when the
result is equivalent.

Example:

GOOD:

animated WebP
+ positioning
+ opacity
+ responsive crop

BAD:

custom particle engine
+ large JavaScript loop
+ unnecessary state
+ hundreds of lines of animation code

Use code when interaction or state genuinely requires code.

Report where material assets reduce implementation complexity.

---

# 7. MultiMind Final Improvisation

After the four reference parity proofs, create ONE final MultiMind application
surface.

This is the main benchmark.

Do NOT copy the layout of any reference website.

Extract the visual and interaction principles and apply them to MultiMind's
actual product needs.

The final surface must include:

- one mock user;
- one mock session;
- a realistic long conversation;
- multi-agent / debate state;
- agent progress / waiting state;
- navigation;
- theme / presentation switching;
- desktop presentation;
- mobile presentation.

No real AI provider calls are required.

Mock data is sufficient.

---

# 8. Professional Product Requirement

The final MultiMind surface must look like a deliberately designed professional
product.

Automatic failure patterns include:

- generic purple gradient SaaS UI;
- default framework cards;
- default admin dashboard layout;
- obvious component-library visual identity;
- "template with MultiMind logo";
- random visual effects without coherent art direction.

The viewer should not be able to identify the framework merely from the
screenshot.

---

# 9. Panel / Component Morphology

Do not only reposition the same component.

The visual construction itself must be able to change.

For example, one presentation may use:

- borderless organic groupings;
- large negative space;
- quiet typography.

Another may use:

- hard segmented surfaces;
- dense status strips;
- compressed typography;
- poster-like geometry.

Another may use:

- editorial rules;
- asymmetry;
- decorative material intersections.

The semantic function may remain the same.

The visual morphology does not need to remain the same.

---

# 10. Typography Requirement

Typography is part of the architecture.

The implementation must be able to alter:

- font family;
- display font;
- scale;
- weight;
- tracking;
- line height;
- hierarchy;
- alignment;
- density;
- heading/body relationship;
- responsive typography;
- placement.

However:

READABILITY OVERRIDES VISUAL STYLE.

A visually impressive implementation that becomes tiring or difficult to read
during a long conversation is a FAIL.

---

# 11. Mobile Recomposition — HARD GATE

Mobile must NOT be a desktop layout with columns stacked vertically.

The mobile version may change:

- navigation system;
- component hierarchy;
- visual emphasis;
- material placement;
- controls;
- typography scale;
- density;
- interaction pattern;
- status presentation.

Example:

Desktop may use a top status rail plus secondary tools.

Mobile may use:

- full-screen conversation;
- compact status header;
- floating action;
- bottom command/navigation surface.

The mobile composition must preserve identity and remain intentionally designed.

`DESKTOP_STACKED_VERTICALLY = FAIL`

---

# 12. Live Presentation Mutation — HARD GATE

The application must support changing presentation while the current session is
still active.

Required proof:

1. Open conversation.
2. Maintain current mock session/data.
3. Change presentation/theme.
4. Transition to a meaningfully different visual morphology.
5. Preserve conversation.
6. Preserve application state.
7. Handle scroll position deliberately.
8. Do NOT perform a full page refresh.

Transitions are allowed and encouraged.

The transition may include:

- layout movement;
- crossfade;
- material transition;
- typography transition;
- component replacement;
- enter/exit animation.

`FULL_PAGE_REFRESH_REQUIRED = FAIL`

---

# 13. Interactive Waiting / Loading State

Do NOT use only a default spinner.

Create a branded MultiMind waiting state.

Example semantic state:

Research Agent       RUNNING
Critic Agent         WAITING
Synthesis Agent      PENDING

The presentation may visualize:

- progress;
- activity;
- material motion;
- agent-state transitions;
- subtle animation;
- structured feedback.

Loading should feel like part of the product.

It must not become distracting during normal use.

---

# 14. Scroll / Motion Torture Test

At least one benchmark surface must demonstrate intentional scroll-driven
presentation behavior.

Examples:

- scroll-linked transform;
- material movement;
- opacity/reveal;
- sticky scene;
- parallax;
- layered section transition;
- controlled horizontal/vertical interaction.

Motion must remain usable.

Do not add motion purely for spectacle.

Include reduced-motion behavior where the platform makes it reasonably possible.

---

# 15. Long-Use Usability Test

The final MultiMind surface must remain usable with a long conversation.

Test with enough mock messages to expose:

- readability problems;
- layout instability;
- excessive animation;
- spacing problems;
- scroll problems;
- sticky-navigation problems;
- performance issues.

A portfolio-like UI that only looks impressive for 30 seconds but becomes
unusable during a 1–2 hour session is a FAIL.

---

# 16. Framework Fingerprint Test

Evaluate whether the result visibly exposes the framework's default identity.

Examples of undesirable fingerprint:

- obvious Material / Flutter look;
- obvious Quasar look;
- obvious dashboard template;
- obvious framework-default buttons/cards/forms.

A framework with many applications but very low visual diversity is NOT
considered flexible.

Visual diversity matters more than showcase quantity.

---

# 17. Visual Entropy Principle

Evidence quality is evaluated as:

10 radically different professional applications

is stronger evidence than:

100 applications built from essentially one template.

The framework should behave like a medium, not like a visual style.

---

# 18. Abstraction Survival Rate

Report how much of the implementation remains within the intended framework
idiom.

Examples:

FastHTML:
HTML / HTMX / CSS / browser JS are considered native to its philosophy.

Reflex:
heavy dependence on custom React wrappers / custom hooks / raw browser JS must
be reported.

SvelteKit:
Svelte / CSS / JS / browser APIs are native, but FastAPI integration and
frontend/backend contract cost must be reported.

Provide an estimated:

`ABSTRACTION_SURVIVAL_PERCENT`

Do not hide escape-hatch usage.

---

# 19. Reference Parity Cost

For every platform report:

- source lines of code, approximately;
- significant dependencies;
- custom components;
- custom wrappers;
- JavaScript usage;
- framework escape-hatch usage;
- build complexity;
- test complexity;
- obvious maintenance risks.

A framework that can technically achieve parity only by defeating its own
abstraction should receive a major penalty.

---

# 20. Free / Open Requirement

The benchmark must not rely on:

- mandatory paid framework licenses;
- mandatory paid UI component packs;
- mandatory proprietary deployment;
- paid-only visual capability.

Open-source/free framework functionality must be sufficient.

Deployment is NOT part of this benchmark yet.

Run locally.

---

# 21. Local Execution Only

Do NOT deploy these PoCs to production hosting.

Local execution is sufficient.

Each implementation must provide:

- startup instructions;
- dependency installation instructions;
- local URL;
- deterministic evidence capture instructions.

---

# 22. Evidence Requirements

For each platform provide:

## Reference proofs

For each of the 4 benchmarks:

- desktop screenshot;
- mobile screenshot;
- short explanation of the capability demonstrated.

## Final MultiMind proof

Provide:

- desktop screenshot;
- mobile screenshot;
- presentation A screenshot;
- presentation B screenshot;
- evidence of live mutation;
- loading / debate-state proof;
- long-conversation proof.

Where practical, capture a short video/GIF showing:

- scroll choreography;
- live presentation switch;
- loading interaction;
- mobile behavior.

Do not use screenshot-only evidence for dynamic behavior when better evidence can
be captured.

---

# 23. Testing

Add focused automated tests where reasonably applicable.

At minimum validate:

- application starts;
- key routes/surfaces render;
- mock session data is preserved;
- presentation switching works;
- no mandatory full-page navigation is used for presentation mutation;
- mobile-specific presentation path exists.

Use browser testing where practical.

---

# 24. Kill Conditions

A candidate should be recommended for DROP if one or more systemic failures
appear:

- cannot reach actual-reference parity;
- generic framework template dominates;
- mobile is only stacked desktop;
- materials cannot be used compositionally;
- typography cannot be controlled sufficiently;
- readability is sacrificed;
- live presentation switch requires reload;
- application state is lost during visual mutation;
- framework fingerprint remains dominant;
- major undocumented DOM hacking is required;
- extreme escape-hatch usage removes the advantage of the framework;
- professional results require paid components;
- implementation cost approaches proper full-stack while retaining a lower
  visual ceiling.

Do not preserve a candidate merely to keep a Top 3.

---

# 25. Scoring

Score each platform from 0–10 for:

- Reference Parity
- Visual Entropy
- Material Freedom
- Material-over-Code Efficiency
- Panel / Component Morphology
- Typography Control
- Readability
- Mobile Recomposition
- Live Mutation
- Scroll / Motion Capability
- Interactive Loading
- Professional / Non-template Quality
- Framework Fingerprint
- Abstraction Survival
- Engineering Burden
- Maintainability
- Python/Core Integration
- Agent Implementability

Do not allow high convenience scores to compensate for a failed visual hard gate.

---

# 26. Final Verdict Vocabulary

Use exactly one:

`MAGNUM_OPUS`

The implementation can reproduce demanding references, improvise beyond them
without losing aesthetic quality, remains professional/readable, and achieves
the result at an acceptable engineering cost.

`EXCELLENT`

Strong reference parity and strong MultiMind improvisation with manageable
limitations.

`GOOD`

Meets the minimum platform requirements but has meaningful limitations.

`MINIMUM_PASS`

Can reproduce required behavior but does not demonstrate sufficient
improvisational or engineering advantage.

`DROP`

Not suitable for the MultiMind migration target.

`NO_MIGRATION_TARGET_APPROVED`

Use if none of the candidates deserve migration approval.

---

# 27. Agent Evaluation

This benchmark also evaluates the implementer.

Report:

- planning quality;
- design translation quality;
- scope discipline;
- code quality;
- testing quality;
- number of major correction loops;
- number of Governor interventions;
- unnecessary complexity introduced;
- quality of improvisation beyond reproduction.

Do not optimize the implementation merely to make the agent look successful.

---

# 28. Final Delivery Format

For each framework report:

FRAMEWORK:
STATUS:
REFERENCE_PARITY:
MULTIMIND_IMPROVISATION:
MOBILE_RECOMPOSITION:
LIVE_MUTATION:
MATERIAL_FREEDOM:
MATERIAL_OVER_CODE:
SCROLL_MOTION:
INTERACTIVE_LOADING:
READABILITY:
FRAMEWORK_FINGERPRINT:
ABSTRACTION_SURVIVAL_PERCENT:
APPROX_IMPLEMENTATION_COST:
TEST_RESULT:
FINAL_VERDICT:

Then provide an overall ranking.

If no candidate deserves migration:

OVERALL_VERDICT: NO_MIGRATION_TARGET_APPROVED

---

# 29. Scope Discipline

Do NOT access or modify the production MultiMind repository.

Do NOT implement real authentication.

Do NOT implement real provider/API calls.

Do NOT migrate the real MultiMind application.

Do NOT select a migration winner before completing evidence.

Do NOT optimize one candidate using knowledge from another candidate's final
implementation.

This is a platform torture benchmark only.

---

# 30. Final Principle

The benchmark is successful even if every candidate fails.

The objective is not to force a migration.

The objective is to discover whether a platform is genuinely capable of
carrying MultiMind's intended UI/UX without repeating the limitations already
observed in Streamlit.

A candidate must earn MultiMind.

MultiMind must not be reduced to fit a candidate.