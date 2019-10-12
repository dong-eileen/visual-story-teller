const displayBox = document.getElementById("display-box");

const getCharacterDetails = name => getDetailsFor(getNameFromId(name));
const getNameFromId = name => name.slice(0, -1).toLowerCase();

const initializeDisplayBox = () => {
	const characters = document.getElementsByClassName("name-tag");
	for (const character of characters) {
		character.onmouseover = (event) => {
			customizeDisplayBox(event.composedPath()[0].innerText);
			showDisplayBox(event);
		};

		character.onmouseout = hideDisplayBox;
	}
}

const initializeNameTags = () => {
	const characters = document.getElementsByClassName("name-tag");
	for (const character of characters) {
		character.target = "_blank";
		character.href = getCharacterDetails(character.innerText).imagePath;
	}
}

const customizeDisplayBox = name => {
	const character = getCharacterDetails(name);
	document.getElementById("portrait").src = character.imagePath;
}

const hideDisplayBox = _ => {
	displayBox.style.display = "none";
}

const showDisplayBox = event => {
	displayBox.style.top = event.pageY + 20;
	displayBox.style.left = event.pageX + 20;
	displayBox.style.display = "block";
}

initializeDisplayBox();
initializeNameTags();