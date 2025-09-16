async function fetchSignals() {
    try {
        const res = await fetch('http://127.0.0.1:5000/get_signals');
        const data = await res.json();
        const container = document.getElementById('signals-container');
        container.innerHTML = '';

        data.forEach(signal => {
            const card = document.createElement('div');
            card.className = 'signal-card ' + signal.type.toLowerCase();
            card.innerHTML = `
                <img src="images/${signal.coin.toLowerCase()}.png" class="coin-icon">
                <h3>${signal.coin} - ${signal.type}</h3>
                <p>Time: ${signal.time}</p>
                <p>Price: ${signal.price} | Target: ${signal.target} | Stop-loss: ${signal.stoploss}</p>
            `;
            container.appendChild(card);
        });
    } catch(err) {
        console.error('Error fetching signals:', err);
    }
}

setInterval(fetchSignals, 120000); 
fetchSignals();
