let characters = {

        alice: {
            name: "Alice",
            imagePath: "./images/alice.png"
        },
        bob: {
            name: "Bob",
            imagePath: "./images/bob.png"
        },
};

const getDetailsFor = name => characters[name];
