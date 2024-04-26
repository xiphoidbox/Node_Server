const express = require('express');
const helmet = require('helmet');
const morgan = require('morgan');
const fs = require('fs');
const path = require('path');
const dotenv = require('dotenv');
const cors = require('cors');
const { createProxyMiddleware } = require('http-proxy-middleware');

dotenv.config();
const app = express();
const PORT = 3000;

app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      imgSrc: ["'self'", "data:", "https://www.google.com"],
      scriptSrc: ["'self'", "https://maps.googleapis.com"],
    },
  },
}));

const accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), { flags: 'a' });
app.use(morgan('combined', { stream: accessLogStream }));
app.use(morgan('combined'));

app.use(cors({
    origin: 'https://proxy.alejandrobermea.com',
    credentials: true,
    methods: ['GET', 'POST', 'OPTIONS'],
    allowedHeaders: ['Content-Type', 'Authorization']
}));

app.use('/mask-detection', createProxyMiddleware({
    target: 'http://localhost:5000',
    changeOrigin: true,
    pathRewrite: {'^/mask-detection': ''},
    logLevel: 'debug',
}));

app.use('/spam-detector', createProxyMiddleware({
    target: 'http://localhost:5001',
    changeOrigin: true,
    pathRewrite: {'^/spam-detector': ''},
    logLevel: 'debug',
}));

app.get('/load-google-maps', (req, res) => {
    res.redirect(`https://maps.googleapis.com/maps/api/js?key=${process.env.GOOGLE_API_KEY}&callback=initMap`);
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
