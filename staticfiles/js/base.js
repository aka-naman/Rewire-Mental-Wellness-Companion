// Base JavaScript for Rewire App

document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Initialize Bootstrap popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
    
    // Add animation class to elements with data-animate attribute
    const animatedElements = document.querySelectorAll('[data-animate]');
    animatedElements.forEach(function(element) {
        element.classList.add('fade-in');
    });
    
    // Add form-control class to all form inputs (except buttons, checkboxes, and radios)
    const formInputs = document.querySelectorAll('form input:not([type="button"]):not([type="submit"]):not([type="reset"]):not([type="checkbox"]):not([type="radio"]), form textarea, form select');
    formInputs.forEach(function(input) {
        input.classList.add('form-control');
    });
    
    // Add form-check-input class to checkboxes and radios
    const checkInputs = document.querySelectorAll('form input[type="checkbox"], form input[type="radio"]');
    checkInputs.forEach(function(input) {
        input.classList.add('form-check-input');
    });
    
    // Add form-label class to labels
    const formLabels = document.querySelectorAll('form label');
    formLabels.forEach(function(label) {
        label.classList.add('form-label');
    });
});