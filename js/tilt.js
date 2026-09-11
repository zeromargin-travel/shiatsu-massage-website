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

    const MAX_TILT = 15; // Maximum tilt angle in degrees
    const PERSPECTIVE = 1000; // Perspective distance in px

    const cards = document.querySelectorAll('.card, .review-card, .google-live-card, .campaign-card, .calendly-external-wrapper, .compact-pricing-box, .js-tilt');
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
        card.style.willChange = 'transform, box-shadow';
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
        const shadowX = (-clampedX * 15).toFixed(1);
        const shadowY = (-clampedY * 15).toFixed(1);

        card.style.transform = `perspective(${PERSPECTIVE}px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02) translateZ(15px)`;
        card.style.boxShadow = `${shadowX}px ${shadowY}px 30px rgba(0, 0, 0, 0.15)`;
    }

    function resetTilt(card) {
        card.style.transition = 'transform 0.5s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.5s ease-out';
        card.style.transform = `perspective(${PERSPECTIVE}px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1) translateZ(0px)`;
        card.style.boxShadow = '';
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
            card.style.transition = 'transform 0.1s ease-out, box-shadow 0.1s ease-out';
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
                // Gyro response
                const rotX = (-deltaBeta * 0.3).toFixed(2);
                const rotY = (deltaGamma * 0.3).toFixed(2);
                card.style.transition = 'transform 0.2s ease-out';
                card.style.transform = `perspective(${PERSPECTIVE}px) rotateX(${rotX}deg) rotateY(${rotY}deg) translateZ(10px)`;
            });
        });
    }

    // Enable Gyro Sensor if available
    if (window.DeviceOrientationEvent) {
        if (typeof DeviceOrientationEvent.requestPermission === 'function') {
            // iOS 13+ permission support
        } else {
            window.addEventListener('deviceorientation', onDeviceOrientation, { passive: true });
        }
    }
})();
