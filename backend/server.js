const express = require('express');

const app = express();
const PORT = 5000;

// Home Route
app.get('/', (req, res) => {
    res.send('VitalAI Backend Running');
});

// API Route
app.get('/api/telemetry', (req, res) => {

    const data = {
        heart_rate: (65 + Math.random() * 45).toFixed(1),
        spo2: (92 + Math.random() * 8).toFixed(1),
        temp: (36.5 + Math.random() * 3).toFixed(1),
        systolic: Math.floor(110 + Math.random() * 35),
        diastolic: Math.floor(70 + Math.random() * 25),
        glucose: (80 + Math.random() * 80).toFixed(1),
        sweat_ph: (4.5 + Math.random() * 2.5).toFixed(1)
    };

    let alerts = [];

    if (data.heart_rate > 100) {
        alerts.push("High Heart Rate");
    }

    if (data.spo2 < 95) {
        alerts.push("Low Oxygen Level");
    }

    if (data.temp > 38) {
        alerts.push("Fever Detected");
    }

    let stress = "Low";

    if (data.heart_rate > 90 && data.sweat_ph < 5.0) {
        stress = "High";
    }

    let prediction = "Normal";

    if (alerts.length > 0) {
        prediction = alerts.join(" / ");
    }

    res.json({
        telemetry: data,
        prediction: prediction,
        stress_level: stress
    });
});

// Start Server
app.listen(PORT, () => {
    console.log(`Server running on http://127.0.0.1:${PORT}`);
});