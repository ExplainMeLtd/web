"""Visitor-facing checks; run with python3 -m unittest discover -s tests."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import re
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
STORE = 'https://apps.apple.com/app/id6760954081'


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.elements = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


class WebsiteTests(unittest.TestCase):
    def test_download_actions_reach_the_iphone_app(self):
        page = Page((ROOT / 'index.html').read_text())
        links = [attrs for tag, attrs in page.elements if tag == 'a' and attrs.get('href') == STORE]
        self.assertGreaterEqual(len(links), 2, 'A visitor needs an App Store action in the opening and download sections')
        self.assertTrue(all(attrs.get('aria-label') for attrs in links), 'Download links need accessible names')
        self.assertNotIn('aria-disabled="true"', (ROOT / 'index.html').read_text())

    def test_download_section_has_a_static_accessible_qr_and_compatibility(self):
        source = (ROOT / 'index.html').read_text()
        page = Page(source)
        codes = [attrs for tag, attrs in page.elements if tag == 'img' and 'app-store-qr' in attrs.get('src', '')]
        self.assertEqual(len(codes), 1)
        self.assertIn('App Store', codes[0].get('alt', ''))
        self.assertTrue((ROOT / codes[0]['src'].lstrip('/')).is_file())
        self.assertIn('iOS 27', source)
        self.assertIn('iPhone', source)

    def test_site_navigation_and_assets_resolve(self):
        for path in ROOT.rglob('*.html'):
            if '_review' in path.parts:
                continue
            page = Page(path.read_text())
            ids = {attrs['id'] for _, attrs in page.elements if 'id' in attrs}
            for tag, attrs in page.elements:
                for key in ('src', 'href'):
                    value = attrs.get(key, '')
                    if not value or urlparse(value).scheme or value.startswith('//'):
                        continue
                    url = urlparse(value)
                    if not url.path:
                        self.assertIn(unquote(url.fragment), ids, f'{path}: broken anchor {value}')
                        continue
                    target = (ROOT / unquote(url.path).lstrip('/')) if url.path.startswith('/') else path.parent / unquote(url.path)
                    if target.is_dir():
                        target = target / 'index.html'
                    self.assertTrue(target.is_file(), f'{path}: broken local resource {value}')

    def test_sharing_and_ai_explanations_distinguish_modes(self):
        source = (ROOT / 'index.html').read_text()
        self.assertIn('guardian-visible', source)
        self.assertIn('both the guardian and teen', source)
        self.assertIn('without AI', source)
        self.assertIn('Teen Trust', source)
        for claim in ('Nothing is shared unless', 'completely private', 'stored only on your phone'):
            self.assertNotIn(claim, source)

    def test_support_is_ready_for_public_visitors(self):
        source = (ROOT / 'support/index.html').read_text()
        self.assertNotIn('Before publishing', source)
        self.assertIn('support@explainme.co.uk', source)
        self.assertIn('private', source)

    def test_sharing_link_targets_the_answer_for_native_disclosure_reveal(self):
        page = Page((ROOT / 'index.html').read_text())
        link = next(attrs for tag, attrs in page.elements
                    if tag == 'a' and 'sharing-' in attrs.get('href', ''))
        target = link['href'].removeprefix('#')
        target_tag, attrs = next((tag, attrs) for tag, attrs in page.elements
                                 if attrs.get('id') == target)
        self.assertNotEqual(target_tag, 'details', 'The link must reveal the answer, not a closed question')
        self.assertIn('faq-answer', attrs.get('class', ''))

    def test_computer_visitor_can_find_the_iphone_qr_handoff_from_the_intro(self):
        source = (ROOT / 'index.html').read_text()
        intro = re.search(r'<section class="hero container".*?</section>', source, re.S)[0]
        self.assertIn('href="#download"', intro)

    def test_redesign_does_not_publish_unreviewed_legal_wording_or_track_visitors(self):
        for relative in ('privacy/index.html', 'terms/index.html'):
            original = subprocess.check_output(['git', 'show', f'main:{relative}'], cwd=ROOT, text=True)
            current = (ROOT / relative).read_text()
            main = lambda text: re.search(r'<main\b[^>]*>(.*?)</main>', text, re.S)[1]
            self.assertEqual(main(current), main(original), f'{relative}: legal wording needs a separate review')
        for path in ROOT.rglob('*.html'):
            self.assertNotIn('<script', path.read_text(), 'This site needs no scripts or analytics')


if __name__ == '__main__':
    unittest.main()
