let searchHistory = [];

function search(event) {
    const searchInput = event.target.value.trim();
    if (event.key === 'Enter' && searchInput !== '') {
        searchHistory.push(searchInput);
        updateSearchHistory();
        document.getElementById('search-box').value = '';
    }
}

function deleteItem(index) {
    searchHistory.splice(index, 1);
    updateSearchHistory();
}

function updateSearchHistory() {
    const searchHistoryList = document.getElementById('search-history-list');
    searchHistoryList.innerHTML = ''; // Clear previous list

    // Add each search item to the list
    searchHistory.forEach((item, index) => {
        const searchItem = document.createElement('div');
        searchItem.classList.add('search-item');
        searchItem.textContent = item;

        const deleteButton = document.createElement('span');
        deleteButton.classList.add('delete-button');
        deleteButton.textContent = '❌';
        deleteButton.addEventListener('click', () => deleteItem(index));

        searchItem.appendChild(deleteButton);

        searchItem.classList.add('search-item-border');
        searchHistoryList.appendChild(searchItem);
    });
}

function handleBodyPartClick(event) {
    // Get the part name from the clicked element's data attribute
    const partName = event.target.getAttribute('data-part');
    // Add the body part name with the status of "hurts" to the search history
    const bodyPartStatus = partName + " hurts";
    searchHistory.push(bodyPartStatus);
    updateSearchHistory();
}

// Other JavaScript code

document.getElementById('get-results-button').addEventListener('click', () => {
    const bodyPartMessageContainer = document.getElementById('body-part-message-container');
    const bodyPartMessage = document.getElementById('body-part-message');
    bodyPartMessage.value = ''; // Clear previous message

    // Loop through search history to find hurting body parts
    searchHistory.forEach(item => {
        if (item.includes("hurts")) {
            // Extract the body part name
            const bodyPart = item.split(' ')[0];
            // Display different message based on the body part
            switch (bodyPart) {
                case "Head":
                    bodyPartMessage.value += "Protect your head from trauma by wearing appropriate safety gear during sports activities and using seatbelts while driving. Seek medical attention for any head injuries, including concussions, and follow the recommended recovery protocols.\n\n";
                    break;
                case "Shoulders":
                    bodyPartMessage.value += "Maintain proper ergonomics and avoid repetitive overhead movements to prevent shoulder impingement and rotator cuff injuries. If you experience persistent shoulder pain or limited range of motion, consult a healthcare professional for assessment and treatment.\n\n";
                    break;
                case "Right_Chest":
                    bodyPartMessage.value += "Any discomfort or palpitations in the right chest area should be evaluated by a healthcare provider promptly, as it could indicate conditions such as angina, inflammation of the chest wall, or cardiac issues.\n\n";
                    break;
                case "Left_Chest":
                    bodyPartMessage.value += "Left-sided chest pain may be a symptom of heart-related problems such as angina or myocardial infarction (heart attack). Seek immediate medical attention if you experience chest pain, especially if it radiates to your left arm, jaw, or back.\n\n";
                    break;
                case "Stomach":
                    bodyPartMessage.value += "Maintain a healthy diet rich in fruits, vegetables, lean proteins, and whole grains to support gastrointestinal health. If you experience persistent abdominal pain, bloating, or changes in bowel habits, consult a gastroenterologist for evaluation.\n\n";
                    break;
                case "Waist":
                    bodyPartMessage.value += "Maintain a healthy weight and waist circumference to reduce the risk of metabolic syndrome, diabetes, and cardiovascular disease. Engage in regular physical activity and consume a balanced diet to support overall health and well-being.\n\n";
                    break;
                case "Right_Arm":
                case "Left_Arm":
                    bodyPartMessage.value += "To prevent overuse injuries and strains, warm up properly before engaging in physical activities and gradually increase intensity. If you experience persistent arm pain, weakness, or numbness, consult an orthopedic specialist for evaluation and treatment.\n\n";
                    break;
                case "Right_Leg":
                case "Left_Leg":
                    bodyPartMessage.value += "Prevent leg cramps and venous insufficiency by staying hydrated, maintaining electrolyte balance, and avoiding prolonged sitting or standing. If you develop leg swelling, pain, or discoloration, seek medical attention to rule out deep vein thrombosis (DVT) or other vascular conditions.\n\n";
                    break;
                case "Right_Foot":
                case "Left_Foot":
                    bodyPartMessage.value += "Practice good foot hygiene and inspect your feet regularly for signs of cuts, blisters, or infections, especially if you have diabetes or peripheral artery disease. Wear properly fitting shoes with adequate arch support to prevent foot pain and deformities.\n\n";
                    break;
                case "Lower_Back":
                    bodyPartMessage.value += "Manage lower back pain with a combination of gentle stretching, strengthening exercises, and ergonomic adjustments to your work environment. If back pain persists or worsens, consult a spine specialist for a comprehensive evaluation and personalized treatment plan.\n\n";
                    break;
                default:
                    break;
            }
        }
    });

    // Show the message container
    bodyPartMessageContainer.style.display = 'block';
});
