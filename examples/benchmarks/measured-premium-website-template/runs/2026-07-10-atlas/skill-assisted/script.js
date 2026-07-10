(() => {
  "use strict";

  const menuToggle = document.querySelector("[data-menu-toggle]");
  const navigation = document.querySelector("[data-nav]");
  const copyButton = document.querySelector("[data-copy-button]");
  const copyLabel = document.querySelector("[data-copy-label]");
  const copyStatus = document.querySelector("[data-copy-status]");

  const setMenuState = (isOpen) => {
    if (!menuToggle || !navigation) return;

    menuToggle.setAttribute("aria-expanded", String(isOpen));
    menuToggle.setAttribute("aria-label", isOpen ? "Close navigation" : "Open navigation");
    navigation.dataset.open = String(isOpen);
  };

  menuToggle?.addEventListener("click", () => {
    const isOpen = menuToggle.getAttribute("aria-expanded") === "true";
    setMenuState(!isOpen);
  });

  navigation?.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => setMenuState(false));
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") setMenuState(false);
  });

  const fallbackCopy = (text) => {
    const textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.setAttribute("readonly", "");
    textarea.style.position = "fixed";
    textarea.style.opacity = "0";
    document.body.appendChild(textarea);
    textarea.select();
    const copied = document.execCommand("copy");
    textarea.remove();
    return copied;
  };

  copyButton?.addEventListener("click", async () => {
    const command = copyButton.dataset.copyText;
    if (!command) return;

    let copied = false;
    try {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(command);
        copied = true;
      } else {
        copied = fallbackCopy(command);
      }
    } catch (error) {
      copied = fallbackCopy(command);
    }

    if (!copied) {
      if (copyStatus) copyStatus.textContent = "Copy unavailable — select the command above.";
      return;
    }

    copyButton.dataset.state = "copied";
    if (copyLabel) copyLabel.textContent = "Copied";
    if (copyStatus) copyStatus.textContent = "Command copied. Then run atlas map in the root of your repository.";

    window.setTimeout(() => {
      delete copyButton.dataset.state;
      if (copyLabel) copyLabel.textContent = "Copy command";
      if (copyStatus) copyStatus.textContent = "Then run atlas map in the root of your repository.";
    }, 2400);
  });
})();
