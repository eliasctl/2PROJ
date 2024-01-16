import express from 'express';

const Router = express.Router();

Router.get("/", (req, res) => {
    res.status(200).send("J'ai pas d'idée");
})

export default Router;