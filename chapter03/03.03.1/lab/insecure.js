// Describe: express app that is vulnerable to XSS

const express = require('express');
const app = express();

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
    extended: true
}));

// TODO: Run the following prompt:
// /fix it looks like this code is insecure. Help me understand what the issue is and how to resolve it.
app.get('/', (req, res) => {

    const user = req.param.q

    if (user != ""){
        pool.query('SELECT * FROM users WHERE name = $1', [user], (error) => {
            if (error) {
                throw error
            }
            res.status(200).json(results.rows)
        })
    }
})

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
