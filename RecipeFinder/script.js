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
        
        // Check if the loaded page is the profile page
        if (url === 'profile.html') {
          // Call a function to initialize Facebook login
          initializeFacebookLogin();
        }
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

  // Function to initialize Facebook login
  function initializeFacebookLogin() {
    // Check login status on page load
    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
  }

  // Function to handle Facebook login status change
  function statusChangeCallback(response) {
    if (response.status === 'connected') {
      // User is logged into your app
      console.log('Logged in and authenticated');
      // Additional actions after login if needed
    } else {
      // User is not logged into your app or not authenticated
      console.log('Not authenticated');
    }
  }
});


