// Description: Open a CSV file and read it line by line.
// Run: node OpenCsvFile.js

const fs = require('fs');
const readline = require('readline');

const readInterface = readline.createInterface({
    input: fs.createReadStream('data.csv'),
    output: process.stdout,
    console: false
    });
