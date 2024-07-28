async function submitImageForm(image) {
  const formData = new FormData();

  if (typeof image === 'string') {
    // If image is a URL
    formData.append('image_url', image);
  } else {
    // If image is a file
    formData.append('image', image);
  }

  try {
    const response = await fetch('/image', {
      method: 'POST',
      body: formData
    });

    document.body.innerHTML = await response.text();

    // Update the URL
    history.pushState(null, 'Image Upload', '/image');
  } catch (error) {
    console.error('Error:', error);
  }
}

function handleUploadFormSubmit(event) {
  event.preventDefault();
  const fileInput = document.getElementById('fileInput');
  if (fileInput.files.length > 0) {
    submitImageForm(fileInput.files[0]);
  }
}
