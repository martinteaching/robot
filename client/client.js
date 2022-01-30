// Note the new way to import code from elsewhere into our program.
// New ES6 syntax is closer to Python.
const userInput = require('./userInput');
const simplePost = require('./simplePost');

/* All await calls must appear in a function marked with the 'async' keyword.
So, we create a main function, and call it directly, in order to account for this. */
async function main() {
    // Start a user input session, using a method from our pre-supplied class.
    userInput.startInput();
    // The user input we did have in Python has now moved to our Javascript client.
    // We must 'await', as a user entering input is an operation that may take a while, and we don't want to continue until we have the information this operation provides.
    // NB: Python waits for operations with a delay by default (synchronous), whereas Javascript (NodeJS) does not (asynchronous). It is designed like this in order to prioritise speed and scalability, but as a consequence we need to program in a way that takes in to account a variable order in which things might complete.
    const x = await userInput.getInput('Enter target X position: ');
    const y = await userInput.getInput('Enter target Y position: ');
    // Pre-construct body here for neatness, but could place in HTTP call directly.
    // This structure matches the format expected by the server, e.g.: '{"x":3, "y":3}'; we are adhering to the 'contract'.
    // Note that has we had strings as values, they would have required speech marks too.
    const requestBody = '{"x":' + x + ', "y":' + y + '}';
    // We're now done with the input part of our code, so we can stop the input session.
    userInput.endInput();
    // We now have all the information we need to make a request to move the simulated robot, on the server, to the coordinates we have provided.
    // Again, this may take a while, so we should use await.
    // We store the eventual response in a variable.
    let response = await simplePost.httpPostJSON({
        body: requestBody,
        hostname: 'localhost',
        port: 8888
    });
    // Our utility class extracts the body of the response for us (the robot's path), so we can just print directly.
    // Printing is different in Javascript.
    console.log(response);
    
}

// Call our main function when program runs.
main();
