// main.js - Enhance UX
document.addEventListener('DOMContentLoaded', function () {
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Smooth scroll for anchor links (optional)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
// Mobile menu toggle functionality
const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

menuBtn.addEventListener('click', () => {
  mobileMenu.classList.toggle('hidden');
});

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Lucide icons
  lucide.createIcons();

  // DOM Elements
  const togglePassword = document.getElementById('togglePassword');
  const passwordField = document.getElementById('password');
  const confirmField = document.getElementById('confirm_password');
  const matchText = document.getElementById('password-match');
  const form = document.getElementById('registerForm');

  // Toggle Password Visibility
  togglePassword.addEventListener('click', () => {
    const type = passwordField.type === 'password' ? 'text' : 'password';
    passwordField.type = type;
    confirmField.type = type;

    // Update icon
    togglePassword.setAttribute('data-lucide', type === 'password' ? 'eye' : 'eye-off');
    lucide.createIcons();
  });

  // Validate Password Match on Submit
  form.addEventListener('submit', (e) => {
    if (passwordField.value !== confirmField.value) {
      e.preventDefault();
      matchText.classList.remove('hidden');
    } else {
      matchText.classList.add('hidden');
      // Optional: Submit via fetch
      // submitForm(e);
    }
  });

  // Optional: AJAX Submit
  // function submitForm(e) {
  //   e.preventDefault();
  //   const formData = new FormData(form);
  //   const data = Object.fromEntries(formData);
  //
  //   fetch('/api/register', {
  //     method: 'POST',
  //     headers: { 'Content-Type': 'application/json' },
  //     body: JSON.stringify(data)
  //   })
  //   .then(res => res.json())
  //   .then(result => {
  //     if (result.success) {
  //       window.location.href = '/dashboard';
  //     } else {
  //       alert(result.message);
  //     }
  //   });
  // }
});