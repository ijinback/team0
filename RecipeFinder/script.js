document.addEventListener('DOMContentLoaded', function() {
  const recipesLink = document.querySelector('a[href="#recipes"]');
  const profileLink = document.querySelector('a[href="#profile"]');
  const mainContent = document.querySelector('main');

  // Function to fetch and display content based on the clicked link
  function loadContent(url) {
    fetch(url)
      .then(response => response.text())
      .then(html => {
        mainContent.innerHTML = html;
      })
      .catch(error => {
        console.error('Error fetching content:', error);
      });
  }

  // Event listeners for navigation links
  recipesLink.addEventListener('click', function(event) {
    event.preventDefault();
    loadContent('recipes.html');
  });

  profileLink.addEventListener('click', function(event) {
    event.preventDefault();
    loadContent('profile.html');
  });

  // Initially load the Recipes page on website load
  loadContent('recipes.html');
});
