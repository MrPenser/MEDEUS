# MEDEUS V3.9.4 — lilac color for the internally lit large sphere

Date: 2026-10-13
Authority: user requested "Сделай шар лиловым", then directly authorized "Сама".
Recall decision: EXTEND the accepted V3.9.3 layout and V3.9 inner-light shader with COLOR-ONLY modification of the large sphere. Do not change microphone, original V3 art, mobile layout, title, breathing or hover/click behavior.
Status: SOURCE_QA=PASS / CI=PASS / LOVABLE_SYNC=PASS / USER_COLOR_VISUAL_SIGNOFF=PENDING / STAGE_COMPLETE=FALSE.

## Exact source changes
Repository: `MrPenser/medeus-master-asset`, `main`.
- `src/lib/medeus/orb-field.ts`, commit `0dec3483971bb9ba499d6e89983275a18949db7f`, palette of only the `pearlSphereColor` default orb material:
  - ivory tint `(.94,.88,1.)`; lilac `(.72,.55,.96)`; deepLilac `(.48,.33,.76)`.
  - stronger lilac blend `pearl=mix(ivory,lilac,.31+.19*grain)`; volume `mix(deepLilac,pearl,.45+.40*scatter)`.
  - internal light now `innerWhite=(.94,.86,1.)`, `innerLilac=(.78,.59,1.)`; transmitted limb `(.75,.59,.99)`. No change to emitter strength, thickness, water normal, alpha silhouette, ripples, time or shape.
  - No rotation, external mirrors, dark central iris or new image generated.
- `src/lib/medeus/core-flow.test.ts` commit `77a0dac79569f3677210c3b0593cf1380e898970`: updates source-palette assertions while retaining volume/light/mic/click invariant tests.
- `.github/workflows/medeus-liquid-orb-qa.yml` commit `8d8dec4b0f0f542e7f13a42784d45993c86c872a`: source gate updated to new palette; all prior shader, mic and immutable image tests retained.
- Final website main HEAD `8d8dec4b0f0f542e7f13a42784d45993c86c872a`.

## Verified evidence
- GitHub Actions run `38424331561`: **success**, both shader GLSL ES100 validation and Bun/Vite production build passed, 58/58 tests passed across 10 suites.
- Lovable project ID `76dd8168-469d-4edb-88f6-f313be1c1de8` independently read as `ready` with `latest_commit_sha=8d8dec4b0f0f542e7f13a42784d45993c86c872a`.
- Preview https://id-preview--76dd8168-469d-4edb-88f6-f313be1c1de8.lovable.app/
- Immutable original V3 master PNG SHA256 `9aac52baeac03d61a35ea9809d3580128952de1ae14d77f43c97a5fb7585c50d` not modified. All 10 FSM states, separate microphone and lower mobile location, single mobile title/cosmic layer, soft breath, outward click and hover retained.
- Browser acceptance remains `PENDING`; source QA and screenshot-independent tests do not prove that the user likes the exact shade or that actual Android/iOS GPU matches desktop. `STAGE_COMPLETE=FALSE` until approval.
