const gamedig = require('gamedig');
const axios = require('axios');

const DISCORD_WEBHOOK_URL = 'YOUR WEBHOOKE HERE';

gamedig.query({
    type: 'valheim',
    host: 'your hostname here',
    port: 2456 // replace with your server's port number
}).then((state) => {
    if (true) {
        // if players are online, send message with player info
        const players = state.players.map((player) => player.name).join(', ');
        const message = `The server is up and running with ${state.players.length} players: ${players}`;
        axios.post(DISCORD_WEBHOOK_URL, { content: message })
            .then(() => console.log('Discord message sent successfully!'))
            .catch((error) => console.error('Error sending Discord message:', error));
    }
}).catch((error) => {
    console.error('Error querying server status:', error);
    const message = `The server is down`;
    axios.post(DISCORD_WEBHOOK_URL, { content: message })
        .then(() => console.log('Discord message sent successfully!'))
        .catch((error) => console.error('Error sending Discord message:', error));

});


