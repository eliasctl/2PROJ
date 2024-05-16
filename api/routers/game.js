import express from 'express';
import mysql from 'mysql2/promise';
import dbConfig from '../dbConf.js';

const game = express.Router();

game.get('/', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT * FROM game');

        res.status(200).json(rows);

        await connection.end();
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

game.post('/', async (req, res) => {
    // quand on met ?entity=value dans l'url
    console.log(req.query);
    res.status(200).json({ message: 'POST request to the homepage' });
});

game.get('/background', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT * FROM background');

        res.status(200).json(rows);

        await connection.end();
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

game.get('/camps', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT * FROM camps');

        res.status(200).json(rows);

        await connection.end();
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

game.get('/civilization', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT * FROM civilization');

        res.status(200).json(rows);

        await connection.end();
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

game.get('/specialCapacity', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT * FROM specialCapacity');

        res.status(200).json(rows);

        await connection.end();
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

game.get('/troops', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT * FROM troops');

        res.status(200).json(rows);

        await connection.end();
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

game.get('/turrets', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT * FROM turrets');

        res.status(200).json(rows);

        await connection.end();
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

export default game;