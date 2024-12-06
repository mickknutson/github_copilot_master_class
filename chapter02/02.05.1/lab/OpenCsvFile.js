// Description: A Function to open a CSV file and read it line by line printing the content of each line.

const fs = require('fs');

function openCsvFile(filePath) {
    const readStream = fs.createReadStream(filePath, 'utf8');
    readStream.on('data', (chunk) => {
        const lines = chunk.split('\n');
        lines.forEach(line => {
            console.log(line);
        });
    });

    readStream.on('error', (err) => {
        console.error('Error reading the file:', err);
    });

    readStream.on('end', () => {
        console.log('Finished reading the file.');
    });
}

// Example usage
openCsvFile('path/to/your/file.csv');