function calculateDaysBetweenDates(begin, end) {
    const millisecondsPerDay = 1000 * 60 * 60 * 24;
    const millisBetween = end.getTime() - begin.getTime();
    const days = millisBetween / millisecondsPerDay;
    return Math.floor(days);

        
}

// find all images without alternate text
// and give them a red border
function process() {
    const images = document.getElementsByTagName('img');
    for (let i = 0; i < images.length; i++) {
        const image = images[i];
        if (image.alt === '') {
            image.classList.add('image');
        }
    }

}
// Express server on port 3000
const express = require('express');
const app = express();
app.listen(3000, () => console.log('listening on port 3000'));
app.get('/', (req, res) => res.send('Hello World'));

