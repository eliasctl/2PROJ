import express from 'express';
import mysql from 'mysql2/promise';
import dbConfig from '../dbConf.js';

const image = express.Router();

image.get('/background', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT * FROM background');

        res.status(200).json(rows);

        await connection.end();
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

export default image;

