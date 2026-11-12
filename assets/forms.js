// Resolve the thank-you page from this site's asset URL, including a GitHub
// Pages repository prefix. Delivery remains a native HTTPS POST to FormSubmit.
(() => {
  const script = document.currentScript;
  if (!script?.src) return;
  const nextUrl = new URL('../thanks.html', script.src);
  if (!['https:', 'http:'].includes(nextUrl.protocol)) return;
  document.querySelectorAll('form.integrated-form').forEach(form => {
    const endpoint = new URL(form.action);
    if (endpoint.origin !== 'https://formsubmit.co') return;
    let field = form.querySelector('input[name="_next"]');
    if (!field) {
      field = document.createElement('input');
      field.type = 'hidden';
      field.name = '_next';
      form.appendChild(field);
    }
    field.value = nextUrl.href;
  });
})();
