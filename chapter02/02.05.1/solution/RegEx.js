// Description: Regular Expression function to parse an URL.

/*
function parseURL(url) {
  var pattern = /(\w+):\/\/([\w.]+)\/(\S*)/;
  var result = pattern.exec(url);
  var keys = ['url', 'protocol', 'host', 'path'];
  var obj = {};
  for (var i = 0; i < keys.length; i++) {
    obj[keys[i]] = result[i];
  }
  return obj;
}*/

function parseURL(url) {
  const pattern = /(\w+):\/\/([\w.]+)\/(\S*)/;
  const result = pattern.exec(url);

  // Check if the URL matches the pattern
  if (!result) {
    throw new Error('Invalid URL format');
  }

  const [ , protocol, host, path ] = result;
  return {
    url,
    protocol,
    host,
    path
  };
}

// export the function
module.exports = parseURL;
