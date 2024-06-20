const fs = require('fs');
const csv = require('csv-parser');

// Description: Open a CSV file and read it line by line.
// You can use the csv-parser package to read a CSV file line by line. This package is useful for parsing large CSV files.
// First, install the csv-parser package using npm:
// npm install csv-parser
// Then, use the following code snippet to read a CSV file line by line:
const filePath = '/path/to/your/csv/file.csv';

fs.createReadStream(filePath)
    .pipe(csv())
    .on('data', (row) => {
        // Process each row of the CSV file here
        console.log(row);
    })
    .on('end', () => {
        console.log('CSV file successfully processed');
    });