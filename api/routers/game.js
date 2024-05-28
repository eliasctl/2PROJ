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

game.get('/get/:id', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT * FROM game WHERE id = ?', [req.params.id]);

        if (rows.length > 0) {
            res.status(200).json(rows[0]);
        } else {
            res.status(404).json({ error: 'Game not found' });
        }

        await connection.end();
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

game.post('/', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT * FROM player WHERE id = ?', [req.query.player]);
        if (rows.length > 0) {
            const [game] = await connection.execute('INSERT INTO game (player1Id, player1Civilization, player2Civilization, player1HPCamp, player2HPCamp) VALUES (?, 1, 1, 5000, 5000)', [req.query.player]);
            res.status(201).json({ id: game.insertId });
        }
        else {
            res.status(404).json({ error: 'User not found' });
        }
    } catch (error) {
        res.status(400).json({ error: 'Bad request' });
    }
});

game.put('/joinGame', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        const [rows] = await connection.execute('SELECT * FROM player WHERE id = ?', [req.query.player]);
        if (rows.length > 0) {
            const [game] = await connection.execute('SELECT * FROM game WHERE player2Id IS NULL AND id = ?', [req.query.game]);
            if (game.length > 0) {
                await connection.execute('UPDATE game SET player2Id = ? WHERE id = ?', [req.query.player, req.query.game]);
                res.status(200).json({ id: req.query.game });
            }
            else {
                res.status(404).json({ error: 'Game not found or already full or ended' });
            }
        }
        else {
            res.status(404).json({ error: 'User not found' });
        }
    } catch (error) {
        res.status(400).json({ error: 'Bad request' });
    }
});

game.put('/data', async (req, res) => {
    try {
        const connection = await mysql.createConnection(dbConfig);
        await connection.execute('UPDATE game SET player1Civilization = ?, player2Civilization = ?, player1HPCamp = ?, player2HPCamp = ?, field = ?, player1SpecialCapacity = ?, player2SpecialCapacity = ?, player1Turrets1 = ?, player1Turrets2 = ?, player1Turrets3 = ?, player2Turrets1 = ?, player2Turrets2 = ?, player2Turrets3 = ? WHERE id = ?', [req.query.player1Civilization, req.query.player2Civilization, req.query.player1HPCamp, req.query.player2HPCamp, req.query.field, req.query.player1SpecialCapacity, req.query.player2SpecialCapacity, req.query.player1Turrets1, req.query.player1Turrets2, req.query.player1Turrets3, req.query.player2Turrets1, req.query.player2Turrets2, req.query.player2Turrets3, req.query.game]);
        res.status(200).json({ message: 'Data updated' });
    } catch (error) {
        res.status(400).json({ error: 'Bad request' });
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