import express from 'express';
import mysql from 'mysql2/promise';
import dbConfig from '../dbConf.js';

const player = express.Router();

player.get('/', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT * FROM player');

        res.status(200).json(rows);

        await connection.end();
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

player.post('/', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [result] = await connection.execute('INSERT INTO player (name) VALUES (?)', [req.body.name]);

        res.status(201).json({ id: result.insertId });

        await connection.end();
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

export default player;