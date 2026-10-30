# ExplainMe Web

A lightweight, mobile-first website for ExplainMe Family, an iPhone app for everyday reflection and family communication.

Public routes: `/`, `/support/`, `/privacy/`, `/terms/`. Static HTML/CSS only, with local assets and native FAQ disclosures. No JavaScript, build framework, forms or analytics.

## Preview and validation

```sh
python3 -m http.server 4173 --bind 127.0.0.1
python3 -m unittest discover -s tests -v
```

Open `http://127.0.0.1:4173/`. Test phone and desktop widths. Optional QR regeneration: install `requirements-dev.txt`, then run `python3 scripts/generate-qr.py`; serving the site needs no third-party packages.

See [the design, asset provenance and verification brief](docs/website-refresh.md). The redesign is a review candidate. Existing public privacy and terms main content is unchanged and needs its separate review; do not infer legal approval from this PR.

## Publication boundaries

GitHub Pages uses `main` / repository root with `CNAME` set to `explainme.co.uk`. Merging a website change can publish it. Review the final candidate before merging. No custom-domain or hosting changes are required.

Unpublished policy review material under `_review/` is excluded from Pages by `_config.yml`, alongside development scripts/tests/docs. Do not remove that exclusion or add `.nojekyll`. Exclusion controls website publication; repository content may still be public. Privacy draft PR2 is separate from this redesign; publish approved legal wording through a separately authorised change.

## App Store links

- App: https://apps.apple.com/app/id6760954081
- Privacy: https://explainme.co.uk/privacy/
- Terms: https://explainme.co.uk/terms/
- Apple standard EULA: https://www.apple.com/legal/internet-services/itunes/dev/stdeula/

The badge and static QR link directly to the same app, without a tracking redirect. Plan/pricing details are shown in the app. Support: `support@explainme.co.uk`.
