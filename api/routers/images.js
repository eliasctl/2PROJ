import express from 'express';
import mysql from 'mysql2/promise';

const dbConfig = {
    host: 'eliascastel.ddns.net',
    user: 'proj',
    password: 'ne76uWF#8#',
    database: 'proj',
};

const image = express.Router();

image.get('/', async (req, res) => {
    // Connexion à la base de données
    const connection = await mysql.createConnection(dbConfig);

    try {
        // Récupération des données de l'image depuis la base de données
        const [rows] = await connection.execute('SELECT id, name FROM images');

        // Envoi des données en tant que réponse
        res.json(rows);
    } catch (error) {
        // Gestion des erreurs de la base de données
        console.error('Database error:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    } finally {
        // Fermeture de la connexion à la base de données
        await connection.end();
    }
});

image.get('/:id', async (req, res) => {
    const imageId = req.params.id;

    // Connexion à la base de données
    const connection = await mysql.createConnection(dbConfig);

    try {
        // Récupération des données de l'image depuis la base de données
        const [rows] = await connection.execute('SELECT name, image FROM images WHERE id = ?', [imageId]);

        if (rows.length > 0) {
            const image = rows[0].image;
            const imageName = rows[0].name;

            // Envoi de l'image en tant que réponse
            res.setHeader('Content-Type', 'image/png');
            res.setHeader('Content-Disposition', `inline; filename=${imageName}`);
            res.end(image, 'binary');
        } else {
            // Aucune image trouvée pour l'ID spécifié
            res.status(404).json({ error: 'Image not found' });
        }
    } catch (error) {
        // Gestion des erreurs de la base de données
        console.error('Database error:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    } finally {
        // Fermeture de la connexion à la base de données
        await connection.end();
    }
});

export default image;