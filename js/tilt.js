/**
 * Ultra-Lightweight 3D Card Tilt & Parallax Effect
 * Supports: PC Mouse, Touch Devices, Gyro / DeviceOrientation
 * Performance: 60fps via requestAnimationFrame, { passive: true } event listeners, IntersectionObserver
 */
(function () {
    'use strict';

    // Respect reduced motion settings
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        return;
    }

    const MAX_TILT = 10; // Maximum tilt angle in degrees
    const PERSPECTIVE = 1000; // Perspective distance in px

    const cards = document.querySelectorAll('.card, .review-card, .google-live-card, .campaign-card, .js-tilt');
    if (!cards.length) return;

    // Track active cards visible in viewport using IntersectionObserver
    const visibleCards = new Set();
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                visibleCards.add(entry.target);
            } else {
                visibleCards.delete(entry.target);
                resetTilt(entry.target);
            }
        });
    }, { threshold: 0.1 });

    cards.forEach(card => {
        // Apply performance styles
        card.style.transformStyle = 'preserve-3d';
        card.style.willChange = 'transform';
        card.style.transition = 'transform 0.15s ease-out, box-shadow 0.15s ease-out';
        observer.observe(card);

        // Bind Mouse events (PC)
        card.addEventListener('mousemove', onMouseMove);
        card.addEventListener('mouseleave', onMouseLeave);

        // Bind Touch events (Mobile)
        card.addEventListener('touchstart', onTouchStart, { passive: true });
        card.addEventListener('touchmove', onTouchMove, { passive: true });
        card.addEventListener('touchend', onTouchEnd, { passive: true });
        card.addEventListener('touchcancel', onTouchEnd, { passive: true });
    });

    let rAFId = null;

    function applyTilt(card, mouseX, mouseY) {
        const rect = card.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;

        const percentX = (mouseX - centerX) / (rect.width / 2);
        const percentY = (mouseY - centerY) / (rect.height / 2);

        // Clamp between -1 and 1
        const clampedX = Math.max(-1, Math.min(1, percentX));
        const clampedY = Math.max(-1, Math.min(1, percentY));

        const rotateX = (-clampedY * MAX_TILT).toFixed(2);
        const rotateY = (clampedX * MAX_TILT).toFixed(2);

        card.style.transform = `perspective(${PERSPECTIVE}px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(10px)`;
    }

    function resetTilt(card) {
        card.style.transition = 'transform 0.5s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.5s ease-out';
        card.style.transform = `perspective(${PERSPECTIVE}px) rotateX(0deg) rotateY(0deg) translateZ(0px)`;
    }

    function onMouseMove(e) {
        const card = e.currentTarget;
        card.style.transition = 'transform 0.1s ease-out, box-shadow 0.1s ease-out';
        if (rAFId) cancelAnimationFrame(rAFId);
        rAFId = requestAnimationFrame(() => applyTilt(card, e.clientX, e.clientY));
    }

    function onMouseLeave(e) {
        resetTilt(e.currentTarget);
    }

    function onTouchStart(e) {
        if (e.touches.length === 1) {
            const card = e.currentTarget;
            card.style.transition = 'transform 0.1s ease-out';
            const touch = e.touches[0];
            applyTilt(card, touch.clientX, touch.clientY);
        }
    }

    function onTouchMove(e) {
        if (e.touches.length === 1) {
            const card = e.currentTarget;
            const touch = e.touches[0];
            if (rAFId) cancelAnimationFrame(rAFId);
            rAFId = requestAnimationFrame(() => applyTilt(card, touch.clientX, touch.clientY));
        }
    }

    function onTouchEnd(e) {
        resetTilt(e.currentTarget);
    }

    // DeviceOrientation API for Mobile Gyro tilt
    let gyroRAF = null;
    let initialGamma = null;
    let initialBeta = null;

    function onDeviceOrientation(e) {
        if (e.gamma === null || e.beta === null) return;

        if (initialGamma === null) {
            initialGamma = e.gamma;
            initialBeta = e.beta;
        }

        const deltaGamma = Math.max(-25, Math.min(25, e.gamma - initialGamma));
        const deltaBeta = Math.max(-25, Math.min(25, e.beta - initialBeta));

        if (gyroRAF) cancelAnimationFrame(gyroRAF);
        gyroRAF = requestAnimationFrame(() => {
            visibleCards.forEach(card => {
                // Subtle gyro response (max 6deg)
                const rotX = (-deltaBeta * 0.25).toFixed(2);
                const rotY = (deltaGamma * 0.25).toFixed(2);
                card.style.transition = 'transform 0.2s ease-out';
                card.style.transform = `perspective(${PERSPECTIVE}px) rotateX(${rotX}deg) rotateY(${rotY}deg) translateZ(5px)`;
            });
        });
    }

    // Enable Gyro Sensor if available
    if (window.DeviceOrientationEvent) {
        if (typeof DeviceOrientationEvent.requestPermission === 'function') {
            // iOS 13+ requires user permission, handled gracefully
        } else {
            window.addEventListener('deviceorientation', onDeviceOrientation, { passive: true });
        }
    }
})();
