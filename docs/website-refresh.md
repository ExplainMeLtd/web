# Family launch website preview — 30 October 2026

This is a review candidate, not the deployed explainme.co.uk website. Based on `4a2a04b` in an isolated checkout; the original checkout's unpublished HTML/CSS/assets are preserved. Hosting remains GitHub Pages. No app/API/configuration/model/evaluation change.

## Design and content

- Warm cream, deep teal, a restrained lavender/sage/peach palette, self-hosted DM Sans with Lora italic accents, open spacing and a short mobile headline.
- The family communication benefit leads; genuine App Store screenshots illustrate guardian and teen experiences. No invented reviews, clinical outcomes, endorsements or product interfaces.
- Direct, country-neutral App Store link: `https://apps.apple.com/app/id6760954081`. Browser verification opens ExplainMe Family. No Android, desktop app, sign-up or testing-group offer.
- The opening action works directly on iPhone. The lower download section has Apple's official badge and a larger-screen QR panel, hidden at phone portrait widths. QR is a local PNG encoding the same direct Apple URL, with a four-module quiet zone and no tracking redirect/service. Apple Vision successfully decoded it.
- Native disclosure elements provide keyboard-operable FAQs. Sharing distinguishes standard guardian-visible check-ins from eligible Teen Trust choices. AI is optional and needs guardian plus teen agreement. No blanket confidentiality, clinical or emergency-monitoring promise.
- Support retains the existing contact and response aim, removes the obsolete publishing instruction, and advises against emailing private child content.
- The public privacy and terms **main content is unchanged**. Web PR2 remains separate unpublished legal review work; its `_review` exclusion is preserved in this candidate's Pages configuration. PR3 can be reviewed and published independently using the existing legal wording. PR2's outstanding decisions apply to the later notice update; this redesign does not establish approval of either notice.

## Evidence and validation

- Failing-first visitor tests: four failures on the baseline (download/QR, mode distinctions and obsolete support instruction); six tests pass after implementation.
- Tests verify App Store actions, QR asset/compatibility, internal navigation/assets, qualified sharing/AI copy, support instructions, unchanged legal content and no runtime scripts.
- Browser checks at 320, 390, 768, 1024 and 1440 CSS pixels: horizontal fit, readable progression, phone versus larger-screen QR treatment. Rechecked 768 separately after the browser's asynchronous resize.
- FAQ expanded through its accessible control and collapsed with Return; download action reached the correct live listing. Lazy product images and QR verified loaded after navigation.
- Rendered text contrast checked, low-contrast secondary captions corrected. This is bounded browser QA, not full assistive-technology certification or a physical iPhone Safari test.
- No external fonts, JavaScript, forms, trackers, cookies or QR services are added. Assets are served locally. Social metadata, canonical URL, iOS Smart App Banner and share image included.

## Assets and provenance

- Existing ExplainMe brand mark/favicons reused from the original unpublished website assets; app icon cross-checked against the iOS app's current icon. Original assets are not modified.
- Screenshots are unedited copies of the already public ExplainMe Family App Store screenshots, downloaded 30 October 2026. They show the published example profile, not a new capture of live family data. `guardian-home.webp` is guardian Home, `insights.webp` is weekly insights, `teen-home.webp` is Teen Trust Home, `em-reflection.webp` is the teen reflection/sharing screen. A gallery screenshot is not a routines screen.
- Screenshot source: https://apps.apple.com/gb/app/explainme-family/id6760954081 (Apple-hosted PurpleSource assets). This does not claim those screenshots represent every newer development feature.
- Badge: https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg ; guidance: https://developer.apple.com/app-store/marketing/guidelines/ . Artwork is unmodified, minimum dimensions and clear space retained; one badge is used.
- DM Sans and Lora: Google Fonts, local WOFF2 subsets with OFL licences in `assets/fonts/`. No Google font requests are made by visitors.
- `scripts/social-card.html` is source for the local 1200×630 sharing artwork screenshot, excluded from Pages output. `assets/social-card.jpg` is JPEG, matching its extension.
- QR regeneration is optional build-only tooling: install `requirements-dev.txt`, run `python3 scripts/generate-qr.py`. No dependency installation is required to serve the site.

## Before publication

Review the mobile/desktop design and final copy, including eligibility/privacy phrasing against the released build. PR3 does not depend on merging PR2 or publishing its draft. Merging PR3 to `main` can publish the redesign through the existing GitHub Pages setup; preparing it for review does not merge or publish it. No DNS or hosting-setting changes are required. The iOS compatibility line was checked against the public listing (iOS 27 or later) on 30 October 2026.

## Independent review follow-up — 30 October

- Increased meaningful supporting text: phone FAQ answers 15px, AI/eligibility warning 14px, compatibility 14px and screenshot caption 12px, with accompanying paragraph/caption layout adjustments. Decorative eyebrow text remains smaller.
- The sharing link now targets the answer inside its native disclosure. Browser failing-first evidence showed the old link left the answer closed; the corrected fragment opens its ancestor disclosure without JavaScript, including after a prior collapse.
- Added a larger-screen opening link to the QR download section, hidden on phone portrait layouts. QR still links directly to the app.
- Added failing-first source regressions for the disclosure target and opening QR handoff; eight static tests pass. Phone browser checks also assert the increased important text sizes.
- PR2 is being reconciled separately; publication of a final notice still needs the concrete decisions in its review sheet. No merge is implied by passing design checks. The present public policy remains unchanged.
