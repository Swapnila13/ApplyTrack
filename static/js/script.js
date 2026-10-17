document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.delete-form').forEach((form) => {
    form.addEventListener('submit', (event) => {
      const company = form.dataset.company || 'this application';
      if (!window.confirm(`Delete the application for ${company}? This cannot be undone.`)) {
        event.preventDefault();
      }
    });
  });
});
