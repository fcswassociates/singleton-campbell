# Singleton-Campbell Limited

Static company website and StageCom product information, prepared for https://www.singleton-campbell.co.uk.

## Hosting

GitHub Pages deploys the `main` branch through `.github/workflows/pages.yml`. The site uses HTML, CSS, vanilla JavaScript and original SVG artwork. It has no paid hosting dependency or server runtime.

## Editing

Run `python3 build.py` to regenerate all pages. The company page content is in `build.py`; the StageCom template and English copy are in `templates/stagecom.html` and `locales/en-GB.json`. Styling is in `assets/style.css` and `assets/stagecom.css`.

The StageCom gallery contains actual developer-supplied alpha screenshots. Its optional interactive workflow is explicitly labelled as a concept and sends no product messages.

## Contact forms

Contact and StageCom testing enquiries are submitted over HTTPS through FormSubmit to office@singleton-campbell.co.uk. The mailbox owner must activate the form for the published domain when requested. FormSubmit uses its standard CAPTCHA protection. Microsoft 365 can quarantine delivery emails: confirm inbox delivery during launch testing. The thank-you page confirms submission, not final inbox delivery.

## Domain

GitHub Pages must be configured for `www.singleton-campbell.co.uk` in repository Settings → Pages before updating DNS. The `www` CNAME target is `fcswassociates.github.io`. Preserve all Microsoft 365 MX, TXT and mail-related CNAME records. `config/CNAME` contains the intended custom domain; the deployment workflow can copy it when `CUSTOM_DOMAIN_ENABLED=true`, but GitHub Pages' custom-domain setting is authoritative for Actions deployments.

The form return URL resolves from the current website URL and supports both the GitHub Pages project path and the custom domain. Future language translations can reuse the StageCom template and locale structure.

## Company identity

The approved Linked Initials logo pairs a transparent cyan interlocking SC vector mark (`assets/sc-linked.svg`) with the Singleton–Campbell wordmark in the company header and footer. The favicon uses the same monogram. StageCom retains its separate waveform identity. The registered company name and address remain in the centred legal footer.

## Reducing repeated address exposure

The Contact and confirmation pages use the enquiry form rather than repeated direct email links. A clear direct company/privacy contact remains in the Privacy notice. Both forms resolve their action from `config/forms.json`; use the recipient’s public FormSubmit replacement action URL here once available. It is not an API key. CAPTCHA remains enabled and the current working recipient action is retained until that replacement is supplied. The email address is still present in the public source and its history, so the change reduces repetition rather than guaranteeing mailbox secrecy or preventing spam.
