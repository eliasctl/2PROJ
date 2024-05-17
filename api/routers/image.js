import express from 'express';
import mysql from 'mysql2/promise';
import dbConfig from '../dbConf.js';

const image = express.Router();

image.get('/', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT id, name FROM images');

        res.status(200).json(rows);

        await connection.end();
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

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

image.get('/:id', async (req, res) => {
    const imageId = req.params.id;

    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT image FROM images WHERE id = ?', [imageId]);

        if (rows.length > 0) {
            res.status(200).send("<img src='data:image/png;base64," + rows[0].image + "' />")

        } else {
            res.status(404).json({ error: 'Image not found' });
        }

        await connection.end();
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

export default image;

