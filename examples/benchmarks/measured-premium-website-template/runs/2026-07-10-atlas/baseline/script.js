(() => {
  const menuButton = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#primary-nav');
  menuButton?.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', String(!open));
    nav?.classList.toggle('is-open', !open);
  });
  nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    menuButton?.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open');
  }));
  const copyButton = document.querySelector('#copy-button');
  const status = document.querySelector('#copy-status');
  copyButton?.addEventListener('click', async () => {
    const command = copyButton.dataset.copy;
    try { await navigator.clipboard.writeText(command); }
    catch { const input = document.createElement('textarea'); input.value = command; document.body.append(input); input.select(); document.execCommand('copy'); input.remove(); }
    copyButton.classList.add('copied'); status.textContent = 'Command copied to clipboard.';
    window.setTimeout(() => { copyButton.classList.remove('copied'); status.textContent = ''; }, 2200);
  });
})();
