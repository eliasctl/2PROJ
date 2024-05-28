// import * as functions from './functions.js';
import express from 'express';
import swaggerUi from 'swagger-ui-express';
//import swaggerFile from './swagger_output.json' assert { type: 'json' };
import swaggerFile from './swagger_output.json' with { type: "json" };
//const swaggerFile = require('./swagger_output.json');
import game from './routers/game.js';
import image from './routers/image.js';
import player from './routers/player.js';
const app = express()
const port = 3001

app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    if (req.method === 'OPTIONS') {
        res.setHeader('Access-Control-Allow-Methods', 'GET');
        res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
        return res.status(200).json({});
    }
    next();
});

app.use("/game", game);

//app.use("/match", match);

app.use("/image", image);

app.use("/player", player);

app.use('/doc', swaggerUi.serve, swaggerUi.setup(swaggerFile));

app.get('/', (req, res) => {
    res.send('API 2PROJ Paris 1')
})

// app.get('/user', (req, res) => {
//     res.send(functions.user());
// })

// app.get('/redirect', (req, res) => {
//     res.redirect('http://elidev.fr');
// })

app.listen(port, () => {
    console.log(`The app are started on port ${port}`)
})