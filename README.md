# ExplainMe Web

Minimal static site for `explainme.co.uk` with:

- homepage: `/`
- support page: `/support/`
- privacy policy: `/privacy/`
- terms of use: `/terms/`

This repo is designed for GitHub Pages with a custom domain.

## Before publishing

Update these items:

- support email address in `/support/index.html`
- support email address in `/privacy/index.html`
- any privacy-policy or terms wording you want legal review on

## App Review legal links

The iOS app can use these public GitHub Pages URLs for subscription compliance:

- Privacy Policy: `https://explainme.co.uk/privacy/`
- Terms of Use: `https://explainme.co.uk/terms/`

Recommended App Store Connect setup:

- Privacy Policy field: `https://explainme.co.uk/privacy/`
- Terms of Use in metadata: Apple standard EULA link
  - `https://www.apple.com/legal/internet-services/itunes/dev/stdeula/`

The app itself can still link to `https://explainme.co.uk/terms/` as its user-facing terms page.

## Suggested GitHub Pages setup

- repository visibility: public
- branch: `main`
- folder: `/root`
- custom domain: `explainme.co.uk`

## Unpublished review material

Policy drafts and supporting review notes live in [`_review/`](_review/), excluded from GitHub Pages output by `_config.yml`. They remain visible in the GitHub repository; they are not confidential. The served policy remains `/privacy/index.html`. Publish approved wording only through a separately authorised publication PR after the review decisions are recorded. Do not bypass the exclusion with `.nojekyll` or site navigation links to draft artifacts.
