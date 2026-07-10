(() => {
  "use strict";

  const root = document.documentElement;
  const body = document.body;
  const select = (selector, scope = document) => scope.querySelector(selector);
  const selectAll = (selector, scope = document) => Array.from(scope.querySelectorAll(selector));
  const clamp = (value, min, max) => Math.min(Math.max(value, min), max);

  root.classList.replace("no-js", "js");

  const menuToggle = select("[data-menu-toggle]");
  const primaryNav = select("#primary-nav");

  const setMenu = (open) => {
    if (!menuToggle || !primaryNav) return;
    primaryNav.classList.toggle("is-open", open);
    menuToggle.setAttribute("aria-expanded", String(open));
    menuToggle.setAttribute("aria-label", open ? "Close navigation menu" : "Open navigation menu");
  };

  menuToggle?.addEventListener("click", () => {
    setMenu(menuToggle.getAttribute("aria-expanded") !== "true");
  });

  selectAll(".site-nav a").forEach((link) => {
    link.addEventListener("click", () => setMenu(false));
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") setMenu(false);
  });

  const motionToggle = select("[data-motion-toggle]");
  const motionStatus = select("[data-motion-status]");
  const prefersReducedQuery = window.matchMedia?.("(prefers-reduced-motion: reduce)");
  let prefersReduced = Boolean(prefersReducedQuery?.matches);
  let motionPaused = prefersReduced;

  const updateMotionUI = () => {
    if (!motionToggle) return;
    motionToggle.setAttribute("aria-pressed", String(motionPaused));
    motionToggle.setAttribute(
      "aria-label",
      motionPaused ? "Motion is paused. Activate to resume motion." : "Motion is active. Activate to pause motion."
    );
    body.classList.toggle("motion-paused", motionPaused);
    if (motionStatus) {
      motionStatus.textContent = motionPaused ? "Motion is paused." : "Motion is active.";
    }
  };

  motionToggle?.addEventListener("click", () => {
    motionPaused = !motionPaused;
    updateMotionUI();
    if (motionPaused) stopFieldLoop();
    else startFieldLoop();
  });

  prefersReducedQuery?.addEventListener?.("change", (event) => {
    prefersReduced = event.matches;
    motionPaused = prefersReduced;
    updateMotionUI();
    if (motionPaused) stopFieldLoop();
    else startFieldLoop();
  });

  const fieldStage = select("[data-field-stage]");
  const canvas = select("#field-canvas");
  const context = canvas?.getContext("2d");
  const playField = select("[data-play-field]");
  const playLabel = select("[data-play-label]");
  const fieldState = select("[data-field-state]");
  const fieldLiveStatus = select("[data-field-live-status]");
  const rows = selectAll("[data-project]");
  const progress = select("[data-scroll-progress]");
  const sectionState = select("[data-section-state]");
  const methodIndex = select("[data-method-index]");
  const methodState = select("[data-method-state]");

  const field = {
    width: 0,
    height: 0,
    dpr: 1,
    pointerX: 0.52,
    pointerY: 0.48,
    targetX: 0.52,
    targetY: 0.48,
    scroll: 0,
    mode: "default",
    playing: false,
  };

  let fieldFrame = 0;

  const modes = {
    default: { sources: [[0.31, 0.54], [0.68, 0.46]], rotation: -0.16, stretch: 1.28, rings: 10 },
    tidal: { sources: [[0.17, 0.61], [0.74, 0.39]], rotation: -0.32, stretch: 1.55, rings: 12 },
    room: { sources: [[0.49, 0.5], [0.51, 0.5]], rotation: 0, stretch: 1.02, rings: 11 },
    afterimage: { sources: [[0.35, 0.45], [0.64, 0.55]], rotation: 0.23, stretch: 1.2, rings: 9 },
    fault: { sources: [[0.19, 0.73], [0.77, 0.27]], rotation: -0.6, stretch: 1.1, rings: 10 },
  };

  const drawGrid = (width, height) => {
    context.lineWidth = 0.5;
    context.strokeStyle = "rgba(158, 184, 185, 0.17)";
    for (let x = 0; x <= 8; x += 1) {
      const position = (width / 8) * x;
      context.beginPath();
      context.moveTo(position, 0);
      context.lineTo(position, height);
      context.stroke();
    }
    for (let y = 0; y <= 5; y += 1) {
      const position = (height / 5) * y;
      context.beginPath();
      context.moveTo(0, position);
      context.lineTo(width, position);
      context.stroke();
    }
  };

  const drawContour = (sourceX, sourceY, radius, settings, ring, phase, width, height) => {
    const points = 112;
    const horizontal = settings.stretch * (1 + (field.pointerX - 0.5) * 0.08);
    const vertical = 0.65 + (field.pointerY - 0.5) * 0.08;
    const radiusPulse = field.playing && !motionPaused && !prefersReduced ? Math.sin(phase * 1.4 + ring * 0.48) * 6 : 0;
    const opacity = Math.max(0.12, 0.44 - ring * 0.026);
    const isCoral = ring % 3 === 0;

    context.beginPath();
    for (let index = 0; index <= points; index += 1) {
      const angle = (index / points) * Math.PI * 2;
      const interference = Math.sin(angle * 3 + phase * 0.65 + ring * 0.84) * (2.5 + ring * 0.28);
      const radiusWithSignal = radius + radiusPulse + interference;
      const rotatedAngle = angle + settings.rotation;
      const x = sourceX + Math.cos(rotatedAngle) * radiusWithSignal * horizontal;
      const y = sourceY + Math.sin(rotatedAngle) * radiusWithSignal * vertical;
      if (index === 0) context.moveTo(x, y);
      else context.lineTo(x, y);
    }
    context.strokeStyle = isCoral ? `rgba(239, 112, 85, ${opacity})` : `rgba(158, 184, 185, ${opacity * 0.9})`;
    context.lineWidth = ring % 4 === 0 ? 1.15 : 0.68;
    context.stroke();
  };

  const drawFaultTrace = (width, height, phase) => {
    context.save();
    context.translate(width * 0.5, height * 0.5);
    context.rotate(-0.55);
    context.setLineDash([2, 8]);
    context.lineWidth = 1;
    context.strokeStyle = "rgba(239, 112, 85, 0.45)";
    for (let index = -4; index < 5; index += 1) {
      const offset = index * 26 + (field.playing ? Math.sin(phase + index) * 4 : 0);
      context.beginPath();
      context.moveTo(-width * 0.7 + offset, -height * 0.75);
      context.lineTo(width * 0.68 + offset, height * 0.75);
      context.stroke();
    }
    context.restore();
    context.setLineDash([]);
  };

  const drawField = (time = 0) => {
    if (!context || !field.width || !field.height) return;
    const width = field.width;
    const height = field.height;
    const phase = time * 0.001 + field.scroll * 2.4;
    const settings = modes[field.mode] || modes.default;

    if (field.playing && !motionPaused && !prefersReduced) {
      field.pointerX += (field.targetX - field.pointerX) * 0.075;
      field.pointerY += (field.targetY - field.pointerY) * 0.075;
    } else {
      field.pointerX = field.targetX;
      field.pointerY = field.targetY;
    }

    context.clearRect(0, 0, width, height);
    drawGrid(width, height);

    settings.sources.forEach(([x, y], sourceIndex) => {
      const sourceX = width * (x + (field.pointerX - 0.5) * (sourceIndex ? 0.03 : -0.02));
      const sourceY = height * (y + (field.pointerY - 0.5) * (sourceIndex ? -0.025 : 0.025));
      const maxRadius = Math.min(width, height) * (sourceIndex ? 0.64 : 0.57);

      for (let ring = 0; ring < settings.rings; ring += 1) {
        drawContour(sourceX, sourceY, 13 + ring * (maxRadius / settings.rings), settings, ring + sourceIndex, phase, width, height);
      }
    });

    if (field.mode === "fault") drawFaultTrace(width, height, phase);

    const markerX = width * (0.5 + (field.pointerX - 0.5) * 0.55);
    const markerY = height * (0.5 + (field.pointerY - 0.5) * 0.55);
    context.fillStyle = "rgba(239, 112, 85, 0.9)";
    context.fillRect(markerX - 2, markerY - 2, 4, 4);
    context.strokeStyle = "rgba(239, 112, 85, 0.35)";
    context.lineWidth = 0.7;
    context.beginPath();
    context.moveTo(markerX - 13, markerY);
    context.lineTo(markerX + 13, markerY);
    context.moveTo(markerX, markerY - 13);
    context.lineTo(markerX, markerY + 13);
    context.stroke();
  };

  const stopFieldLoop = () => {
    if (fieldFrame) cancelAnimationFrame(fieldFrame);
    fieldFrame = 0;
    drawField(0);
  };

  const animateField = (time) => {
    drawField(time);
    if (field.playing && !motionPaused && !prefersReduced) fieldFrame = requestAnimationFrame(animateField);
    else fieldFrame = 0;
  };

  function startFieldLoop() {
    if (!fieldFrame && field.playing && !motionPaused && !prefersReduced) {
      fieldFrame = requestAnimationFrame(animateField);
    } else {
      drawField(0);
    }
  }

  const resizeField = () => {
    if (!fieldStage || !canvas || !context) return;
    const bounds = fieldStage.getBoundingClientRect();
    field.dpr = Math.min(window.devicePixelRatio || 1, 2);
    field.width = Math.max(1, bounds.width);
    field.height = Math.max(1, bounds.height);
    canvas.width = Math.floor(field.width * field.dpr);
    canvas.height = Math.floor(field.height * field.dpr);
    context.setTransform(field.dpr, 0, 0, field.dpr, 0, 0);
    drawField(0);
  };

  const updateFieldUI = () => {
    const active = field.playing;
    if (playField) {
      playField.setAttribute("aria-pressed", String(active));
      playField.setAttribute("aria-label", active ? "Pause the field" : "Play the field");
    }
    if (playLabel) playLabel.textContent = active ? "Pause the field" : "Play the field";
    if (fieldState) fieldState.textContent = active ? (motionPaused || prefersReduced ? "Reduced" : "Live") : "Standby";
    if (fieldLiveStatus) {
      fieldLiveStatus.textContent = active
        ? motionPaused || prefersReduced
          ? "The field is active with continuous motion reduced."
          : "The field is live."
        : "The field is on standby.";
    }
  };

  playField?.addEventListener("click", () => {
    field.playing = !field.playing;
    updateFieldUI();
    if (field.playing) startFieldLoop();
    else stopFieldLoop();
  });

  fieldStage?.addEventListener("pointermove", (event) => {
    const bounds = fieldStage.getBoundingClientRect();
    field.targetX = clamp((event.clientX - bounds.left) / bounds.width, 0, 1);
    field.targetY = clamp((event.clientY - bounds.top) / bounds.height, 0, 1);
    if (!fieldFrame) drawField(performance.now());
  });

  fieldStage?.addEventListener("pointerleave", () => {
    field.targetX = 0.52;
    field.targetY = 0.48;
    if (!fieldFrame) drawField(performance.now());
  });

  const setFieldMode = (mode) => {
    field.mode = mode || "default";
    fieldStage?.setAttribute("data-mode", field.mode);
    if (!fieldFrame) drawField(performance.now());
  };

  rows.forEach((row) => {
    const activate = () => setFieldMode(row.dataset.project);
    const reset = () => {
      if (!row.matches(":hover") && document.activeElement !== row) setFieldMode("default");
    };
    row.addEventListener("pointerenter", activate);
    row.addEventListener("focus", activate);
    row.addEventListener("pointerleave", reset);
    row.addEventListener("blur", reset);
  });

  const updateProgress = () => {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const amount = scrollable > 0 ? clamp(window.scrollY / scrollable, 0, 1) : 0;
    if (progress) progress.style.transform = `scaleY(${Math.max(0.02, amount)})`;
    field.scroll = clamp(window.scrollY / Math.max(window.innerHeight, 1), 0, 3);
    if (!fieldFrame) drawField(performance.now());
  };

  window.addEventListener("scroll", updateProgress, { passive: true });

  const sections = selectAll("main > section[id]");
  const sectionNames = { top: "Field", work: "Index", method: "Method", contact: "Contact" };
  if ("IntersectionObserver" in window) {
    const sectionObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting && sectionState) sectionState.textContent = sectionNames[entry.target.id] || "Field";
      });
    }, { rootMargin: "-42% 0px -48% 0px", threshold: 0 });
    sections.forEach((section) => sectionObserver.observe(section));
  }

  const methodSteps = selectAll("[data-method-step]");
  if ("IntersectionObserver" in window && methodSteps.length) {
    const methodObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        methodSteps.forEach((step) => step.classList.toggle("is-active", step === entry.target));
        const index = entry.target.dataset.methodStep;
        if (methodIndex) methodIndex.textContent = index;
        if (methodState) {
          const labels = { "01": "Listening now", "02": "Mapping now", "03": "Materializing now" };
          methodState.textContent = labels[index] || "In process";
        }
      });
    }, { rootMargin: "-35% 0px -45% 0px", threshold: 0 });
    methodSteps.forEach((step) => methodObserver.observe(step));
  }

  if (window.ResizeObserver && fieldStage) {
    const sizeObserver = new ResizeObserver(resizeField);
    sizeObserver.observe(fieldStage);
  } else {
    window.addEventListener("resize", resizeField);
  }

  updateMotionUI();
  updateFieldUI();
  resizeField();
  updateProgress();
  requestAnimationFrame(() => body.classList.add("is-ready"));
})();
