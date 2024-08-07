// 03.03.1 Describe: express app that is vulnerable to XSS

const express = require('express');
const app = express();

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
    extended: true
}));

// TODO: Run the following prompt:
// /fix it looks like this code is insecure. Help me understand what the issue is and how to resolve it.

// app.get('/', (req, res) => {

//     const user = req.param.q

//     if (user != ""){
//         pool.query('SELECT * FROM users WHERE name = $1', [user], (error) => {
//             if (error) {
//                 throw error
//             }
//             res.status(200).json(results.rows)
//         })
//     }
// })

app.get('/', (req, res) => {
    const user = req.query.q;

    if (user && typeof user === 'string') {
        const sanitizedUser = sanitizeInput(user); // Sanitize the user input
        pool.query('SELECT * FROM users WHERE name = $1', [sanitizedUser], (error, results) => {
            if (error) {
                console.error(error);
                res.status(500).json({ error: 'Internal server error' });
            } else {
                res.status(200).json(results.rows);
            }
        });
    } else {
        res.status(400).json({ error: 'Invalid user input' });
    }
});


app.listen(3000, () => {
  console.log('Server started on port 3000');
});




/*
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const pool = require('./db'); // Assuming you have a db.js that exports a pool
const sanitizer = require('sanitizer'); // You can use a sanitizer library

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    const user = req.query.q;

    if (user && typeof user === 'string') {
        const sanitizedUser = sanitizer.escape(user); // Sanitize the user input
        pool.query('SELECT * FROM users WHERE name = $1', [sanitizedUser], (error, results) => {
            if (error) {
                console.error(error);
                res.status(500).json({ error: 'Internal server error' });
            } else {
                res.status(200).json(results.rows);
            }
        });
    } else {
        res.status(400).json({ error: 'Invalid user input' });
    }
});

app.listen(3000, () => {
    console.log('Server started on port 3000');
});
*/
