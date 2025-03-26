fetch('restart-time.json').then(res => res.json()).then(data => {
  document.getElementById('overlay').innerHTML = `
    <h1>Server Restarting In: ${data.seconds_left}s</h1>
    <p>👥 ${data.player_count} players online</p>
    <p>${data.admin_message || ''}</p>
  `;
});