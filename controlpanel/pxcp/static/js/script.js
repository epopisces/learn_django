document.getElementById('search-input').addEventListener('input', function() {
  const query = this.value;
  fetch(`/search/?q=${query}`)
      .then(response => response.json())
      .then(data => {
          const resultsContainer = document.getElementById('search-results');
          resultsContainer.innerHTML = '';
          data.forEach(item => {
              const li = document.createElement('li');
              li.textContent = item.name;
              li.addEventListener('click', () => {
                  window.location.href = item.link;
              });
              resultsContainer.appendChild(li);
          });
      });
});