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
        console.log(error);
    }
});

player.post('/', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [result] = await connection.execute('INSERT INTO player (name) VALUES (?)', [req.query.name]);

        res.status(201).json({ id: result.insertId });

        await connection.end();
    } catch (error) {
        //res.status(400).json({ error: 'Bad request' });
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

player.delete('/', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        await connection.execute('DELETE FROM player WHERE id = ?', [req.query.id]);
        res.status(200).json({ message: 'Player deleted' });
    } catch (error) {
        res.status(400).json({ error: 'Bad request' });
    }
});

export default player;