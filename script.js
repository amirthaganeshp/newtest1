document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('kaleidoscopeCanvas');
    const ctx = canvas.getContext('2d');

    // Canvas dimensions
    const CANVAS_WIDTH = 800;
    const CANVAS_HEIGHT = 600;
    canvas.width = CANVAS_WIDTH;
    canvas.height = CANVAS_HEIGHT;

    // Kaleidoscope settings
    const NUM_SEGMENTS = 6;
    let clickedPoints = [];

    const centerX = CANVAS_WIDTH / 2;
    const centerY = CANVAS_HEIGHT / 2;

    function rotatePoint(point, currentCenterX, currentCenterY, angleRad) { // Renamed params for clarity
        const translatedX = point.x - currentCenterX;
        const translatedY = point.y - currentCenterY;
        const rotatedX = translatedX * Math.cos(angleRad) - translatedY * Math.sin(angleRad);
        const rotatedY = translatedX * Math.sin(angleRad) + translatedY * Math.cos(angleRad);
        return {
            x: rotatedX + currentCenterX,
            y: rotatedY + currentCenterY
        };
    }

    function clearCanvas() {
        ctx.fillStyle = 'black';
        ctx.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
    }

    function draw() {
        clearCanvas();

        // 1. Draw the original user-drawn shape (polyline)
        if (clickedPoints.length > 1) {
            ctx.beginPath();
            ctx.moveTo(clickedPoints[0].x, clickedPoints[0].y);
            for (let k = 1; k < clickedPoints.length; k++) {
                ctx.lineTo(clickedPoints[k].x, clickedPoints[k].y);
            }
            ctx.strokeStyle = 'grey';
            ctx.lineWidth = 1;
            ctx.stroke();
        }

        // 2. Draw the kaleidoscope pattern
        if (clickedPoints.length > 1) {
            // Draw lines
            for (let j = 0; j < clickedPoints.length - 1; j++) {
                const p1_orig = clickedPoints[j];
                const p2_orig = clickedPoints[j + 1];

                for (let i = 0; i < NUM_SEGMENTS; i++) {
                    const angleRad = i * (2 * Math.PI / NUM_SEGMENTS);

                    const finalP1 = rotatePoint(p1_orig, centerX, centerY, angleRad);
                    const finalP2 = rotatePoint(p2_orig, centerX, centerY, angleRad);

                    ctx.beginPath();
                    ctx.moveTo(finalP1.x, finalP1.y);
                    ctx.lineTo(finalP2.x, finalP2.y);
                    ctx.strokeStyle = 'white';
                    ctx.lineWidth = 1; // Line thickness for kaleidoscope
                    ctx.stroke();
                }
            }
        } else if (clickedPoints.length === 1) {
            // Draw single point reflections
            const point = clickedPoints[0];
            ctx.fillStyle = 'white'; // Ensure fillStyle for circles
            for (let i = 0; i < NUM_SEGMENTS; i++) {
                const angleRad = i * (2 * Math.PI / NUM_SEGMENTS);
                const finalPoint = rotatePoint(point, centerX, centerY, angleRad);

                ctx.beginPath();
                ctx.arc(finalPoint.x, finalPoint.y, 3, 0, 2 * Math.PI); // Radius 3 for points
                ctx.fill();
            }
        }
    }

    clearCanvas();
    console.log('Kaleidoscope script initialized (line drawing version).');

    canvas.addEventListener('mousedown', (event) => {
        const rect = canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        clickedPoints.push({ x: x, y: y });
        draw();
    });

    const clearButton = document.getElementById('clearButton');

    clearButton.addEventListener('click', () => {
        clickedPoints = []; // Clear the points
        draw();             // Redraw the empty canvas
        console.log("Pattern cleared.");
    });
});
