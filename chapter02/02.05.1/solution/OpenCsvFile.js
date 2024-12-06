// Description: Function to open a CSV file and read it line by line then return an array of the values.

// Import the file system module
const fs = require('fs');
// Import the csv-parser module
const csv = require('csv-parser');

// Open the CSV file

// Create a readable stream
const readableStream = fs.createReadStream('data.csv');
// Pipe the stream to the csv-parser

// Read the CSV file line by line
readableStream.pipe(csv())
  .on('data', (row) => {
    console.log(row);
  })
  .on('end', () => {
    console.log('CSV file successfully processed');
  });
  