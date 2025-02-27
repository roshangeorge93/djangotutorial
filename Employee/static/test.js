function myFunction() {
    alert("Hello from a static file!");
  }

  function changeImageOn() {
    // Get the element
    const lighting = document.getElementById('img1')
    
    // Change the background image
    lighting.src= "https://img.freepik.com/free-vector/realistic-light-bulb-with-electricity_23-2149129410.jpg"
    
    }
    
    function changeImageOff() {
    // Get the element
    const dark = document.getElementById('img1');
    
    
    // Change the background image
    dark.src = "https://media.istockphoto.com/id/185206958/photo/light-bulb.jpg?s=612x612&w=0&k=20&c=uff31Cf5Qy0Rss2OBw7aOysvoDEVKJVk53PrLfzGpBI="
    
    }