function addToCalendar(groupId) {
    // Send AJAX request to add group to user's calendar
    fetch(`/join_group/${groupId}/`)
        .then(response => {
            if (response.ok) {
                alert('Group event added to calendar successfully!');
            } else {
                alert('Failed to add group event to calendar.');
            }
        })
        .catch(error => {
            console.error('Error adding group event to calendar:', error);
            alert('An error occurred while adding group event to calendar.');
        });
}