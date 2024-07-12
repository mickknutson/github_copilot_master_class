// Description: Regular Expression function to parse an URL.

function parseURL(url) {
    const regex = /^(https?):\/\/([^:/?]+)(?::(\d+))?(\/[^?#]*)?(?:\?([^#]*))?(?:#(.*))?$/;
    const match = url.match(regex);
    
    if (match) {
        const [, protocol, host, port, path, query, fragment] = match;
        return {
            protocol,
            host,
            port,
            path,
            query,
            fragment
        };
    } else {
        return null;
    }
}

const url = "https://www.example.com:8080/path/to/resource?param1=value1&param2=value2#fragment";
const parsedURL = parseURL(url);
console.log(parsedURL);
