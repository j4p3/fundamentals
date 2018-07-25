'use strict';
exports.handler = (event, context, callback) => {
    
    // Extract request from the CloudFront event that is sent to Lambda@Edge 
    var request = event.Records[0].cf.request;

    // Match any '/' that occurs at the end of a URI.
    // Replace it with /index.html.
    if (request.uri.match(/^((?!\.(css|js|html|xml|txt|ico|jpg|png|gif|json|pdf)$).)*$/)) {
        request.uri = request.uri.replace(/\/?$/, '/index.html');
    }
    
    // Return request with modified URI to CloudFront
    return callback(null, request);
};

function uriSwap(request) {
    console.log(`inbound: ${request.uri}`);

    // Match any '/' that occurs at the end of a URI.
    // Replace it with /index.html.
    if (request.uri.match(/^((?!\.(css|js|html|xml|txt|ico|jpg|png|gif|json|pdf)$).)*$/)) {
        request.uri = request.uri.replace(/\/?$/, '/index.html');
    }
    console.log(`passing: ${request.uri}`);
    
    // Return request with modified URI to CloudFront
    return request;
}

console.log(uriSwap({ uri: '/work/'}));