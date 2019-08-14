
// $(document).ready(function() {

//     $('a.name-tag').attr('target', '_blank');

//     $('.name-tag').popover({ 
//         html: true,
//         trigger: 'hover',
//         placement: 'bottom',
//         content: function () {
//             return '<img src="'+ $(this).attr('href') + '" width=400px/>';
//         }
//     });
// });

const displayBox = document.getElementById("display-box");

const getCharacterDetails = id => getDetailsFor(getNameFromId(id));

const initializeDisplayBox = () => {
	const characters = document.getElementsByClassName("name-tag");
	for (const character of characters) {
		character.onmouseover = (event) => {
			customizeDisplayBox(event.path[0].id);
			showDisplayBox(event);
		};

		character.onmouseout = hideDisplayBox;
	}
}

const getNameFromId = id => id.split('_')[0];

const customizeDisplayBox = id => {
	const character = getCharacterDetails(id);
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

const initializeNameTags = () => {
	const characters = document.getElementsByClassName("name-tag");
	for (const character of characters) {
		character.target = "_blank";
		character.href = getCharacterDetails(character.id).imagePath;
	}
}

initializeDisplayBox();
initializeNameTags();